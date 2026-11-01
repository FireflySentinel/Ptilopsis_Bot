"""Wiki 客户端:登录、批量读取、csrf token 缓存、badtoken 重试与限速,全部离线。"""

import json
import re
import time
from datetime import UTC, datetime, timedelta
from email.parser import BytesParser
from email.policy import HTTP
from email.utils import format_datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from urllib.parse import parse_qs

import anyio
import httpx2
import pytest

from ptilopsis.utils import ratelimit
from ptilopsis.utils import wiki as wiki_module
from ptilopsis.utils.ratelimit import RateLimit, Throttle
from ptilopsis.utils.wiki import (
    MAX_RETRY_AFTER,
    READ_CHUNK,
    PageRevision,
    Wiki,
    WikiError,
)

pytestmark = pytest.mark.anyio

API = "https://wiki.example/api.php"
REDIRECT = re.compile(r"#REDIRECT \[\[(.+?)\]\]")


def post_params(request: httpx2.Request) -> dict[str, str]:
    """解析 POST 表单,multipart 与 urlencoded 都认。"""
    content_type = request.headers.get("content-type", "")
    if not content_type.startswith("multipart/form-data"):
        return {k: v[0] for k, v in parse_qs(request.content.decode()).items()}
    message = BytesParser(policy=HTTP).parsebytes(
        f"Content-Type: {content_type}\r\n\r\n".encode() + request.content
    )
    return {
        part.get_param("name", header="content-disposition"): part.get_payload(
            decode=True
        ).decode()
        for part in message.iter_parts()
        if part.get_filename() is None
    }


def multipart_names(request: httpx2.Request) -> list[str]:
    """multipart 请求体里各字段(含文件)按发送顺序的名字。"""
    content_type = request.headers["content-type"]
    message = BytesParser(policy=HTTP).parsebytes(
        f"Content-Type: {content_type}\r\n\r\n".encode() + request.content
    )
    return [
        part.get_param("name", header="content-disposition")
        for part in message.iter_parts()
    ]


class FakeMediaWiki:
    """能应付登录、tokens、titles 查询、edit 与 protect 的最小 MediaWiki。"""

    def __init__(self, pages: dict[str, str]) -> None:
        self.pages = pages
        self.requests: list[dict[str, str]] = []
        self.token_serial = 0
        self.edits: list[dict[str, str]] = []
        self.protects: list[dict[str, str]] = []
        self.reject_tokens: set[str] = set()
        self.error: dict[str, str] | None = None
        """设置后所有 edit 都返回这个错误。"""
        self.ratelimits: dict[str, Any] = {}
        """userinfo 查询返回的 ratelimits;默认为空(noratelimit 账号)。"""
        self.fail_userinfo = False
        """设置后 userinfo 查询直接抛异常,模拟配额查询失败。"""
        self.ratelimit_quota = 0
        """接下来这么多个 edit 请求返回 ratelimited 错误。"""
        self.throttle = 0
        """接下来的这些请求返回 429,等待秒数取 ``retry_after``。"""
        self.retry_after: str | None = "0"
        """429 响应的 Retry-After 头;None 表示不带这个头。"""

    def __call__(self, request: httpx2.Request) -> httpx2.Response:
        params = {k: v[0] for k, v in parse_qs(request.url.query.decode()).items()}
        if request.method == "POST":
            params |= post_params(request)
        self.requests.append(params)
        if self.throttle > 0:
            self.throttle -= 1
            headers = (
                {} if self.retry_after is None else {"retry-after": self.retry_after}
            )
            return httpx2.Response(429, headers=headers)
        return httpx2.Response(200, content=json.dumps(self.handle(params)).encode())

    def handle(self, p: dict[str, str]) -> Any:
        action = p["action"]
        if action == "query" and p.get("meta") == "tokens":
            if p.get("type") == "login":
                return {"query": {"tokens": {"logintoken": "LOGIN"}}}
            self.token_serial += 1
            return {"query": {"tokens": {"csrftoken": f"CSRF{self.token_serial}"}}}
        if action == "query" and p.get("meta") == "userinfo":
            if self.fail_userinfo:
                raise KeyError("userinfo exploded")
            return {
                "query": {
                    "userinfo": {"id": 1, "name": "bot", "ratelimits": self.ratelimits}
                }
            }
        if action == "login":
            ok = p["lgpassword"] == "secret" and p["lgtoken"] == "LOGIN"
            return {
                "login": {"result": "Success"}
                if ok
                else {"result": "Failed", "reason": "Incorrect password"}
            }
        if action == "query" and "titles" in p:
            return self.query_pages(p["titles"].split("|"), "redirects" in p)
        if action == "edit":
            if self.error is not None:
                return {"error": self.error}
            # 和 ApiMain 一样先校验 token,再轮到编辑模块里的限速
            if p["token"] in self.reject_tokens:
                return {"error": {"code": "badtoken", "info": "Invalid CSRF token."}}
            if self.ratelimit_quota > 0:
                self.ratelimit_quota -= 1
                return {
                    "error": {"code": "ratelimited", "info": "Rate limit exceeded."}
                }
            self.edits.append(p)
            return {"edit": {"result": "Success", "title": p["title"]}}
        if action == "protect":
            self.protects.append(p)
            return {"protect": {"title": p["title"]}}
        raise AssertionError(p)

    def query_pages(self, titles: list[str], follow: bool = False) -> Any:
        pages: dict[str, Any] = {}
        normalized = []
        redirects = []
        for i, title in enumerate(titles):
            canonical = title.replace("_", " ")
            if canonical != title:
                normalized.append({"from": title, "to": canonical})
            # redirects=1:像 MediaWiki 一样一路解析,只列出最终页面
            while follow and (m := REDIRECT.match(self.pages.get(canonical) or "")):
                redirects.append({"from": canonical, "to": m[1]})
                canonical = m[1]
            if canonical not in self.pages:
                pages[str(-(i + 1))] = {"title": canonical, "missing": ""}
                continue
            text = self.pages[canonical]
            page: dict[str, Any] = {
                "pageid": i + 1,
                "title": canonical,
                "contentmodel": "wikitext",
            }
            if text is not None and text.startswith("#REDIRECT"):
                page["redirect"] = ""
            # 用 None 模拟超出结果大小上限、内容被截掉的页面(只在批量请求里发生)
            if text is not None or len(titles) == 1:
                page["revisions"] = [
                    {
                        "revid": 100 + i,
                        "timestamp": f"2026-01-01T00:00:{i:02d}Z",
                        "*": text or "single",
                    }
                ]
            pages[str(i + 1)] = page
        return {
            "curtimestamp": "2026-01-02T00:00:00Z",
            "query": {
                "normalized": normalized,
                "redirects": redirects,
                "pages": pages,
            },
        }


def make_wiki(pages: dict[str, Any], mode: str = "product") -> tuple[Wiki, Any]:
    server = FakeMediaWiki(pages)
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    return Wiki(API, mode, client=http), server


async def test_login_success_and_failure() -> None:
    server = FakeMediaWiki({})
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    wiki = await Wiki.login(API, "bot", "secret", client=http)
    assert isinstance(wiki, Wiki)
    # 登录成功后还会查一次 ratelimits
    assert [r["action"] for r in server.requests] == ["query", "login", "query"]
    assert server.requests[-1]["uiprop"] == "ratelimits"

    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    with pytest.raises(RuntimeError, match="Incorrect password"):
        await Wiki.login(API, "bot", "wrong", client=http)


async def test_read_single_page_and_missing() -> None:
    wiki, _ = make_wiki({"阿米娅": "text"})
    assert await wiki.read("阿米娅") == "text"
    with pytest.raises(KeyError):
        await wiki.read("不存在")


async def test_read_many_batches_titles_and_maps_normalized_names() -> None:
    pages = {f"干员{i}": f"text{i}" for i in range(READ_CHUNK + 5)}
    pages["Some Page"] = "spaced"
    wiki, server = make_wiki(pages)

    titles = [*pages, "Some_Page", "缺失的页面"]
    got = await wiki.read_many(titles)

    assert got == {**pages, "Some_Page": "spaced"}
    # 55 + 2 个标题分两批;缺失页面被省略,不再单独请求
    assert len(server.requests) == 2
    assert len(server.requests[0]["titles"].split("|")) == READ_CHUNK


async def test_read_many_refetches_truncated_pages_individually() -> None:
    wiki, server = make_wiki({"a": "A", "b": None, "c": "C"})
    got = await wiki.read_many(["a", "b", "c"])
    assert got == {"a": "A", "b": "single", "c": "C"}
    assert [r["titles"] for r in server.requests] == ["a|b|c", "b"]


async def test_read_revisions_returns_ids_timestamps_and_redirects() -> None:
    pages: dict[str, Any] = {f"藏品{i}": f"text{i}" for i in range(READ_CHUNK + 1)}
    pages["Some Page"] = "#REDIRECT [[藏品0]]"
    pages["截断"] = None
    wiki, server = make_wiki(pages)

    got = await wiki.read_revisions([*pages, "Some_Page", "缺失的页面"])

    assert set(got) == {*pages, "Some_Page"}
    assert got["藏品1"] == PageRevision(
        title="藏品1",
        text="text1",
        revid=101,
        timestamp="2026-01-01T00:00:01Z",
        starttimestamp="2026-01-02T00:00:00Z",
        redirect=False,
        contentmodel="wikitext",
    )
    assert got["Some_Page"] is got["Some Page"] and got["Some Page"].redirect
    # 内容被截掉的页面单独再读一次
    assert got["截断"].text == "single"
    assert [len(r["titles"].split("|")) for r in server.requests] == [
        READ_CHUNK,
        5,
        1,
    ]
    assert server.requests[0]["rvprop"] == "ids|timestamp|content"


async def test_resolve_follows_redirects_and_drops_missing() -> None:
    pages: dict[str, Any] = {f"关卡{i}": "text" for i in range(READ_CHUNK)}
    pages |= {
        "St 06-02": "#REDIRECT [[6-13]]",
        "6-13": "#REDIRECT [[6-13 没有火，没有光]]",
        "6-13 没有火，没有光": "stage",
        "断链": "#REDIRECT [[已删除的页面]]",
    }
    wiki, server = make_wiki(pages)

    got = await wiki.resolve(["St_06-02", "断链", "缺失的页面", *pages])

    # 双重重定向解析到底;规范化前的标题映射回去;指向不存在页面的重定向算不存在
    assert got["St_06-02"] == "6-13 没有火，没有光"
    assert got["6-13"] == "6-13 没有火，没有光"
    assert got["关卡0"] == "关卡0"
    assert "断链" not in got and "缺失的页面" not in got
    assert len(server.requests) == 2
    assert server.requests[0]["redirects"] == "1"


async def test_edit_passes_conflict_detection_timestamps() -> None:
    wiki, server = make_wiki({})
    await wiki.edit(
        title="页面",
        text="1",
        nocreate=True,
        basetimestamp="2026-01-01T00:00:00Z",
        starttimestamp="2026-01-02T00:00:00Z",
    )
    edit = server.edits[0]
    assert edit["nocreate"] == "1"
    assert edit["basetimestamp"] == "2026-01-01T00:00:00Z"
    assert edit["starttimestamp"] == "2026-01-02T00:00:00Z"


async def test_post_is_multipart_so_large_edits_survive() -> None:
    # 站点会丢掉超过约 50KB 的 urlencoded 请求体(api.php 转而返回 HTML 帮助页),
    # 写请求必须走 multipart
    sent: list[httpx2.Request] = []

    def handle(request: httpx2.Request) -> httpx2.Response:
        sent.append(request)
        return httpx2.Response(200, json={"edit": {"result": "Success"}})

    text = "干员" * 50000
    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handle)) as http:
        wiki = Wiki(API, client=http)
        wiki._csrf_token = "CSRF"
        await wiki.edit(title="页面", text=text)

    assert sent[0].headers["content-type"].startswith("multipart/form-data")
    assert post_params(sent[0]) == {
        "format": "json",
        "action": "edit",
        "token": "CSRF",
        "title": "页面",
        "text": text,
        "bot": "1",
    }


async def test_token_is_sent_after_text_and_summary() -> None:
    # 请求体中途断开时服务器会处理收到的前半截:token 在正文前面就会存下半截页面,
    # 所以 token 必须是最后一个字段
    sent: list[httpx2.Request] = []

    def handle(request: httpx2.Request) -> httpx2.Response:
        sent.append(request)
        return httpx2.Response(200, json={"edit": {"result": "Success"}})

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handle)) as http:
        wiki = Wiki(API, client=http)
        wiki._csrf_token = "CSRF"
        await wiki.edit(title="页面", text="正文", summary="update", minor=True)

    names = multipart_names(sent[0])
    assert names[-1] == "token"
    assert names.index("text") < names.index("summary") < names.index("token")
    assert post_params(sent[0])["token"] == "CSRF"


async def test_upload_sends_token_after_file(tmp_path: Path) -> None:
    sent: list[httpx2.Request] = []

    def handle(request: httpx2.Request) -> httpx2.Response:
        sent.append(request)
        return httpx2.Response(200, json={"upload": {"result": "Success"}})

    image = tmp_path / "a.png"
    image.write_bytes(b"\x89PNG" + b"\0" * 64)
    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handle)) as http:
        wiki = Wiki(API, client=http)
        wiki._csrf_token = "CSRF"
        await wiki.upload(str(image), "头像 a.png", comment="c")

    names = multipart_names(sent[0])
    assert names[-2:] == ["file", "token"]
    assert post_params(sent[0]) == {
        "format": "json",
        "action": "upload",
        "filename": "头像 a.png",
        "ignorewarnings": "1",
        "comment": "c",
        "token": "CSRF",
    }


async def test_edit_caches_csrf_token_and_retries_on_badtoken() -> None:
    wiki, server = make_wiki({})
    await wiki.edit(title="页面", text="1", summary="s", minor=True, bot=None)
    await wiki.edit(title="页面", text="2", summary="s", createonly="1")
    # 两次编辑只取一次 token
    assert sum(1 for r in server.requests if r.get("meta") == "tokens") == 1
    assert server.edits[0]["token"] == "CSRF1"
    assert server.edits[0]["minor"] == "1" and "bot" not in server.edits[0]
    assert server.edits[1]["bot"] == "1" and server.edits[1]["createonly"] == "1"

    # token 失效:刷新后重试一次成功
    server.reject_tokens.add("CSRF1")
    await wiki.edit(title="页面", text="3")
    assert server.edits[-1]["token"] == "CSRF2"

    # 其它错误直接抛出
    server.error = {"code": "protectedpage", "info": "This page is protected."}
    with pytest.raises(WikiError, match="protectedpage"):
        await wiki.edit(title="页面", text="4")


async def test_createonly_on_existing_page_is_not_an_error() -> None:
    wiki, server = make_wiki({})
    server.error = {
        "code": "articleexists",
        "info": "The article you tried to create has been created already.",
    }
    assert await wiki.edit(title="页面", text="1", createonly="1") is None
    assert await wiki.edit(title="页面", text="1", createonly=True) is None
    # 不带 createonly 时同一个错误照常抛出
    with pytest.raises(WikiError, match="articleexists"):
        await wiki.edit(title="页面", text="1")


async def test_create_protects_the_page_it_created() -> None:
    wiki, server = make_wiki({})
    created = await wiki.create(
        title="页面",
        text="1",
        summary="init",
        contentmodel="json",
        protections="edit=autoconfirmed|move=sysop",
    )
    assert created is True
    assert server.edits[0]["createonly"] == "1"
    assert server.edits[0]["contentmodel"] == "json"
    assert server.protects[0]["title"] == "页面"
    assert server.protects[0]["protections"] == "edit=autoconfirmed|move=sysop"
    assert server.protects[0]["expiry"] == "infinite"
    # 不给 protections 就只建页
    assert await wiki.create(title="页面2", text="1") is True
    assert len(server.protects) == 1


async def test_create_leaves_existing_page_unprotected() -> None:
    # 占了名字的重定向等已有页面不能被顺手保护
    wiki, server = make_wiki({})
    server.error = {
        "code": "articleexists",
        "info": "The article you tried to create has been created already.",
    }
    created = await wiki.create(title="页面", text="1", protections="edit=sysop")
    assert created is False
    assert server.protects == []
    assert not any(r["action"] == "protect" for r in server.requests)


async def test_create_in_dev_mode_previews_protection() -> None:
    wiki, server = make_wiki({}, mode="dev")
    assert await wiki.create(title="页面", text="1", protections="edit=sysop")
    assert server.requests == []


async def test_dev_mode_does_not_write() -> None:
    wiki, server = make_wiki({}, mode="dev")
    assert await wiki.edit(title="页面", text="1") is None
    assert await wiki.protect(title="页面", protections="edit=sysop") is None
    assert server.requests == []


async def test_login_builds_limiters_from_discovered_limits() -> None:
    server = FakeMediaWiki({})
    server.ratelimits = {
        "edit": {"user": {"hits": 90, "seconds": 60}},
        "upload": {
            "user": {"hits": 90, "seconds": 60},
            "ip": {"hits": 8, "seconds": 10},
            "newbie": {"hits": 100, "seconds": 600},
        },
    }
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    wiki = await Wiki.login(API, "bot", "secret", client=http)

    def windows(action: str) -> list[tuple[int, float]]:
        return [(w.max_hits, w.period) for w in wiki._limiters[action].windows]

    # safety 0.8 -> 任意 60s 内至多 72 次
    assert windows("edit") == [(72, 60.0)]
    # newbie 与 ip 是两个独立计数器,两个窗口都要守
    assert windows("upload") == [(6, 10.0), (80, 600.0)]


async def test_edit_cools_down_and_retries_on_ratelimited() -> None:
    # 窗口取小值,让冷却只睡 0.05s
    server = FakeMediaWiki({})
    server.ratelimits = {"edit": {"user": {"hits": 100, "seconds": 0.05}}}
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    wiki = await Wiki.login(API, "bot", "secret", client=http)

    server.ratelimit_quota = 1
    await wiki.edit(title="页面", text="1")
    assert len(server.edits) == 1  # 第一次被拒,冷却后重试成功
    # 撞限重试不该重新取 token(只有 badtoken 才失效)
    csrf_queries = [
        r for r in server.requests if r.get("meta") == "tokens" and "type" not in r
    ]
    assert len(csrf_queries) == 1

    # 连续撞限:三次尝试全被拒后照常抛出
    server.ratelimit_quota = 3
    with pytest.raises(WikiError, match="ratelimited"):
        await wiki.edit(title="页面", text="2")
    assert len(server.edits) == 1


async def test_write_refreshes_token_only_once_and_only_on_badtoken() -> None:
    wiki, server = make_wiki({})
    wiki._limiters["edit"] = Throttle([RateLimit(100, 0.05)])  # 冷却只睡 0.05s
    await wiki.edit(title="页面", text="1")  # 缓存 CSRF1

    # badtoken 换过 token 后又撞限:冷却重试沿用新 token,不再重取
    server.reject_tokens.add("CSRF1")
    server.ratelimit_quota = 1
    await wiki.edit(title="页面", text="2")
    assert server.edits[-1]["token"] == "CSRF2"
    assert server.token_serial == 2

    # 换过一次 token 仍被拒:照常抛出,不反复刷新
    server.reject_tokens |= {"CSRF2", "CSRF3"}
    with pytest.raises(WikiError, match="badtoken"):
        await wiki.edit(title="页面", text="3")
    assert server.token_serial == 3


async def test_write_min_interval_spaces_writes() -> None:
    server = FakeMediaWiki({})
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    wiki = Wiki(API, "product", client=http, write_min_interval=0.2)
    start = time.monotonic()
    await wiki.edit(title="页面", text="1")
    await wiki.edit(title="页面", text="2")
    # 第二次写要补足与上一次写请求的间隔
    assert time.monotonic() - start >= 0.2
    assert len(server.edits) == 2


async def test_min_interval_is_waited_before_taking_window_slot(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # 先等最小间隔再占窗口名额:占完再睡的话,第一次 edit 在 100s 就记账、
    # 102s 才发出,第三次会在 110s 发出,10 秒内发了三次
    now = 100.0
    sent: list[tuple[str, float]] = []

    async def advance(seconds: float) -> None:
        nonlocal now
        now += seconds

    clock = SimpleNamespace(monotonic=lambda: now)
    monkeypatch.setattr(wiki_module, "time", clock)
    monkeypatch.setattr(ratelimit, "time", clock)
    monkeypatch.setattr(anyio, "sleep", advance)

    def handle(request: httpx2.Request) -> httpx2.Response:
        action = post_params(request)["action"]
        sent.append((action, now))
        return httpx2.Response(200, json={action: {"result": "Success"}})

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handle)) as http:
        wiki = Wiki(API, client=http, rate_safety=1, write_min_interval=2)
        wiki._csrf_token = "CSRF"
        wiki._limiters["edit"] = Throttle([RateLimit(2, 10)])
        await wiki.protect(title="a", protections="edit=sysop")
        for title in "bcd":
            await wiki.edit(title=title, text="X")

    assert sent == [("protect", 100), ("edit", 102), ("edit", 104), ("edit", 112)]


@pytest.mark.parametrize("failure", [429, 503, "transport"])
@pytest.mark.parametrize("pacing", ["interval", "window"])
async def test_http_retries_and_following_write_are_paced(
    monkeypatch: pytest.MonkeyPatch, failure: int | str, pacing: str
) -> None:
    now = 100.0
    sent: list[float] = []

    async def advance(seconds: float) -> None:
        nonlocal now
        now += seconds

    clock = SimpleNamespace(monotonic=lambda: now)
    monkeypatch.setattr(wiki_module, "time", clock)
    monkeypatch.setattr(ratelimit, "time", clock)
    monkeypatch.setattr(anyio, "sleep", advance)
    monkeypatch.setattr(Wiki, "_post", Wiki._post.retry_with(sleep=advance))

    def handle(request: httpx2.Request) -> httpx2.Response:
        sent.append(now)
        if len(sent) == 1:
            if isinstance(failure, str):
                raise httpx2.ConnectError("offline", request=request)
            return httpx2.Response(failure, headers={"Retry-After": "0"})
        return httpx2.Response(200, json={"edit": {"result": "Success"}})

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handle)) as http:
        wiki = Wiki(
            API, client=http, write_min_interval=2 if pacing == "interval" else 0
        )
        wiki._csrf_token = "CSRF"
        if pacing == "window":
            wiki._limiters["edit"] = Throttle([RateLimit(1, 2)])
        await wiki.edit(title="a", text="A")
        await wiki.edit(title="b", text="B")

    assert sent == [100.0, 102.0, 104.0]


async def test_login_survives_rate_limit_query_failure() -> None:
    server = FakeMediaWiki({})
    server.ratelimits = {"edit": {"user": {"hits": 90, "seconds": 60}}}
    server.fail_userinfo = True
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    wiki = await Wiki.login(API, "bot", "secret", client=http)
    # 配额查询失败只是放弃限速,登录照常成功
    assert wiki._limiters == {}


async def test_get_retries_after_429() -> None:
    wiki, server = make_wiki({"a": "A"})
    server.throttle = 1  # Retry-After: 0,立即重试
    assert await wiki.read("a") == "A"
    assert server.requests[-1]["titles"] == "a"


async def test_client_errors_are_not_retried() -> None:
    sent = 0

    def handle(request: httpx2.Request) -> httpx2.Response:
        nonlocal sent
        sent += 1
        return httpx2.Response(404)

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handle)) as http:
        wiki = Wiki(API, client=http)
        with pytest.raises(httpx2.HTTPStatusError):
            await wiki.read("a")
    # 404 再发也是 404,不走重试
    assert sent == 1


def _throttled(
    monkeypatch: pytest.MonkeyPatch, retry_after: str | None, throttle: int = 1
) -> tuple[Wiki, FakeMediaWiki, list[float]]:
    """让接下来 ``throttle`` 个请求返回 429,并拦截重试前的等待秒数。"""
    slept: list[float] = []

    async def record_sleep(seconds: float) -> None:
        slept.append(seconds)

    monkeypatch.setattr(Wiki, "_get", Wiki._get.retry_with(sleep=record_sleep))
    wiki, server = make_wiki({"a": "A"})
    server.throttle = throttle
    server.retry_after = retry_after
    return wiki, server, slept


async def test_429_sleeps_retry_after_header(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    wiki, _, slept = _throttled(monkeypatch, "7")
    assert await wiki.read("a") == "A"
    assert slept == [7.0]


async def test_429_caps_retry_after(monkeypatch: pytest.MonkeyPatch) -> None:
    wiki, _, slept = _throttled(monkeypatch, "86400")
    assert await wiki.read("a") == "A"
    assert slept == [float(MAX_RETRY_AFTER)]


async def test_429_without_header_uses_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    wiki, _, slept = _throttled(monkeypatch, None)
    assert await wiki.read("a") == "A"
    assert slept == [60.0]


async def test_429_does_not_wait_after_last_attempt(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    wiki, server, slept = _throttled(monkeypatch, "7", throttle=3)
    with pytest.raises(httpx2.HTTPStatusError):
        await wiki.read("a")
    # 三次都 429:只在两次重试之前等,最后一次直接抛出
    assert slept == [7.0, 7.0]
    assert len(server.requests) == 3


def test_retry_after_accepts_http_date() -> None:
    def parse(value: str) -> float | None:
        resp = httpx2.Response(429, headers={"Retry-After": value})
        return wiki_module._retry_after(resp)

    soon = format_datetime(datetime.now(UTC) + timedelta(seconds=30), usegmt=True)
    assert (delay := parse(soon)) is not None and 28 <= delay <= 30
    assert parse("Wed, 21 Oct 2015 07:28:00 GMT") == 0  # 已经过去的时刻
    assert parse("-5") == 0
    assert parse("soon") is None

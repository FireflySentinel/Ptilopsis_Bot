"""torappu 客户端:URL 编码、版本挑选、404 处理与目录遍历,全部离线。"""

import asyncio
import json
from typing import Any

import httpx2
import pytest
from tenacity import wait_none

from ptilopsis.utils.torappu import (
    READY_MARKER,
    ChallengePageError,
    TorappuClient,
    TorappuVersion,
)

pytestmark = pytest.mark.anyio

BASE = "https://torappu.example"
V = "26-09-03-04-06-00_ed95a2"


class FakeServer:
    """按完整 URL(不含 query)路由的 MockTransport,记录所有请求。"""

    def __init__(self, routes: dict[str, Any]) -> None:
        self.routes = routes
        self.calls: list[tuple[str, str]] = []

    def __call__(self, request: httpx2.Request) -> httpx2.Response:
        url = str(request.url.copy_with(query=None))
        self.calls.append((request.method, url))
        body = self.routes.get(url)
        if body is None:
            return httpx2.Response(404)
        if isinstance(body, httpx2.Response):
            return body
        if isinstance(body, bytes):
            return httpx2.Response(200, content=body)
        return httpx2.Response(200, content=json.dumps(body).encode("utf-8"))


def make_client(routes: dict[str, Any]) -> tuple[TorappuClient, FakeServer]:
    server = FakeServer(routes)
    http = httpx2.AsyncClient(transport=httpx2.MockTransport(server))
    return TorappuClient(BASE, client=http), server


def version(id_: int, res: str, ready: bool = True) -> dict[str, Any]:
    return {
        "id": id_,
        "clientVersion": "2.7.71",
        "resVersion": res,
        "isReady": ready,
        "assetMappingStatus": "ready",
    }


def test_gamedata_url_encodes_brackets_but_keeps_slashes() -> None:
    client, _ = make_client({})
    url = client.gamedata_url(V, "story/[uc]info/obt/memory/story_demkni_1_1.txt")
    assert url == (
        f"{BASE}/gamedata/{V}/story/%5Buc%5Dinfo/obt/memory/story_demkni_1_1.txt"
    )


def test_files_url_encodes_whole_path_as_one_segment() -> None:
    client, _ = make_client({})
    url = client.files_url(f"gamedata/{V}/story/[uc]info")
    assert url == f"{BASE}/api/v1/files/gamedata%2F{V}%2Fstory%2F%5Buc%5Dinfo"


async def test_fetch_returns_bytes_and_404_becomes_file_not_found() -> None:
    client, server = make_client(
        {f"{BASE}/gamedata/{V}/excel/item_table.json": b'{"items": {}}'}
    )
    assert await client.fetch(V, "excel/item_table.json") == b'{"items": {}}'
    with pytest.raises(FileNotFoundError):
        await client.fetch(V, "excel/nope.json")
    # 404 不重试
    assert server.calls.count(("GET", f"{BASE}/gamedata/{V}/excel/nope.json")) == 1


CHALLENGE = b"<html><script>document.location.reload();</script></html>"


def challenge_page() -> httpx2.Response:
    """CDN CC 防护的 JS 挑战页:200 + HTML + 下发 cookie。"""
    return httpx2.Response(
        200,
        headers={"content-type": "text/html", "set-cookie": "acw_sc__v2=ok; path=/"},
        content=CHALLENGE,
    )


@pytest.fixture
def no_retry_wait(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TorappuClient.fetch.retry, "wait", wait_none())


async def test_challenge_page_is_retried_with_its_cookie(no_retry_wait: None) -> None:
    sent: list[httpx2.Request] = []

    def handle(request: httpx2.Request) -> httpx2.Response:
        sent.append(request)
        if "acw_sc__v2=ok" not in request.headers.get("cookie", ""):
            return challenge_page()
        return httpx2.Response(
            200, headers={"content-type": "text/plain"}, content=b"story"
        )

    http = httpx2.AsyncClient(transport=httpx2.MockTransport(handle))
    client = TorappuClient(BASE, client=http)
    assert await client.fetch(V, "story/a.txt") == b"story"
    assert len(sent) == 2


async def test_persistent_challenge_page_is_never_returned_as_content(
    no_retry_wait: None,
) -> None:
    client, server = make_client({f"{BASE}/gamedata/{V}/story/a.txt": challenge_page()})
    with pytest.raises(ChallengePageError):
        await client.fetch(V, "story/a.txt")
    assert len(server.calls) == 3

    # 没带 content-type 的也认得出来
    bare, _ = make_client({f"{BASE}/gamedata/{V}/story/b.txt": CHALLENGE})
    with pytest.raises(ChallengePageError):
        await bare.fetch(V, "story/b.txt")


async def test_non_http_errors_are_not_retried() -> None:
    # 返回的不是 JSON:数据错误重试也没用
    client, server = make_client({f"{BASE}/api/v1/version": b"<html>"})
    with pytest.raises(ValueError):
        await client.list_versions()
    assert len(server.calls) == 1


async def test_cancellation_is_not_retried() -> None:
    calls = 0
    started = asyncio.Event()

    async def hang(request: httpx2.Request) -> httpx2.Response:
        nonlocal calls
        calls += 1
        started.set()
        await asyncio.sleep(10)
        return httpx2.Response(200, content=b"late")

    http = httpx2.AsyncClient(transport=httpx2.MockTransport(hang))
    client = TorappuClient(BASE, client=http)
    # 与 asyncio.run 收到 SIGINT 时一样,直接 cancel 任务
    task = asyncio.get_running_loop().create_task(client.fetch(V, "excel/a.json"))
    await started.wait()
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert calls == 1


async def test_list_versions_sorted_by_id() -> None:
    client, _ = make_client(
        {f"{BASE}/api/v1/version": [version(3, "c"), version(1, "a"), version(2, "b")]}
    )
    assert [v.res_version for v in await client.list_versions()] == ["a", "b", "c"]
    assert isinstance((await client.list_versions())[0], TorappuVersion)


async def test_latest_version_skips_versions_without_ready_marker() -> None:
    client, server = make_client(
        {
            f"{BASE}/api/v1/version": [
                version(1, "old"),
                version(2, "ready"),
                version(3, "extracting"),
                version(4, "bundles-pending", ready=False),
            ],
            # 只有 ready 这一版有标记
            f"{BASE}/gamedata/ready/{READY_MARKER}": {"schema_version": 1},
        }
    )
    latest = await client.latest_version()
    assert latest.res_version == "ready"
    assert ("GET", f"{BASE}/gamedata/bundles-pending/{READY_MARKER}") in server.calls


async def test_latest_version_accepts_ready_gamedata_with_bundles_pending() -> None:
    client, server = make_client(
        {
            f"{BASE}/api/v1/version": [
                version(1, "old"),
                version(2, "bundles-pending", ready=False),
            ],
            f"{BASE}/gamedata/bundles-pending/{READY_MARKER}": {
                "schema_version": 1,
                "completed_at": "2026-10-16T08:03:26Z",
            },
        }
    )
    latest = await client.latest_version()
    assert latest.res_version == "bundles-pending"
    assert server.calls == [
        ("GET", f"{BASE}/api/v1/version"),
        ("GET", f"{BASE}/gamedata/bundles-pending/{READY_MARKER}"),
    ]


async def test_latest_version_raises_when_nothing_ready() -> None:
    client, _ = make_client({f"{BASE}/api/v1/version": [version(1, "a")]})
    with pytest.raises(RuntimeError, match="no version with ready gamedata"):
        await client.latest_version()


def _listing(path: str, children: list[tuple[str, bool]]) -> dict[str, Any]:
    return {
        "dir": {"name": path.rsplit("/", 1)[-1], "path": path, "is_dir": True},
        "children": [
            {
                "name": name,
                "path": f"{path}/{name}",
                "size": 0 if is_dir else 10,
                "is_dir": is_dir,
            }
            for name, is_dir in children
        ],
    }


def _files_route(path: str) -> str:
    return f"{BASE}/api/v1/files/" + f"gamedata/{V}/{path}".replace("/", "%2F")


async def _walk(client: TorappuClient, path: str) -> list[str]:
    return [file async for file in client.walk(V, path)]


async def test_walk_recurses_into_directories() -> None:
    root = f"gamedata/{V}"
    client, _ = make_client(
        {
            _files_route("levels"): _listing(
                f"{root}/levels", [("obt", True), ("levels_meta.json", False)]
            ),
            _files_route("levels/obt"): _listing(
                f"{root}/levels/obt", [("main", True)]
            ),
            _files_route("levels/obt/main"): _listing(
                f"{root}/levels/obt/main", [("level_main_01-01.json", False)]
            ),
        }
    )
    assert sorted(await _walk(client, "levels")) == [
        "levels/levels_meta.json",
        "levels/obt/main/level_main_01-01.json",
    ]


async def test_walk_on_a_file_yields_itself() -> None:
    path = "levels/obt/main/level_main_01-01.json"
    client, _ = make_client(
        {
            # 目录接口对文件报 500
            _files_route(path): httpx2.Response(500, json={"detail": "not a dir"}),
            f"{BASE}/gamedata/{V}/{path}": b"{}",
        }
    )
    assert await _walk(client, path) == [path]


async def test_walk_missing_directory_raises() -> None:
    client, _ = make_client({})
    with pytest.raises(FileNotFoundError):
        await _walk(client, "levels/nope")

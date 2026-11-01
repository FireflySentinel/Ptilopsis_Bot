"""MediaWiki API 客户端(async,httpx2 + HTTP/2)。

用 :meth:`Wiki.login` 构造;所有请求走同一个连接池。读取用
:meth:`Wiki.read`,一次要读很多页面时用 :meth:`Wiki.read_many`,它把标题按
50 个一批合并成一个 ``action=query``;要在读到的版本上改写页面时用
:meth:`Wiki.read_revisions`,它额外带回版本号与时间戳供编辑冲突检测。
csrf token 按会话缓存,只在服务器报 ``badtoken`` 时重新取。编辑类操作用锁
串行,避免并发写页面;登录后还会查询账号适用的写配额并本地限速,撞限时
冷却重试(见 :mod:`ptilopsis.utils.ratelimit`)。
"""

import time
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import quote

import anyio
import httpx2
from tenacity import RetryCallState, retry, retry_if_exception, stop_after_attempt

from ptilopsis.log import logger
from ptilopsis.utils.http import log_retry, make_client
from ptilopsis.utils.ratelimit import DEFAULT_COOLDOWN, Throttle, parse_ratelimits

__all__ = ["PAGE_PROTECTIONS", "PageRevision", "Wiki", "WikiError"]

PAGE_PROTECTIONS = "edit=autoconfirmed|move=sysop|delete=sysop"
"""bot 新建的干员页、敌人页(含 /spine)的保护等级,配合 :meth:`Wiki.create` 使用。"""

READ_CHUNK = 50
"""一次 ``action=query`` 里带的标题数;普通用户上限 50,bot 有 apihighlimits 才是 500。"""

MAX_RATELIMIT_RETRIES = 2
"""写操作撞 ``ratelimited`` 后冷却重试的次数上限。"""


class WikiError(RuntimeError):
    """API 返回了 ``error`` 字段。"""

    def __init__(self, code: str, info: str) -> None:
        super().__init__(f"{code}: {info}")
        self.code = code
        self.info = info


@dataclass(frozen=True)
class PageRevision:
    """页面最新版本的快照,:meth:`Wiki.read_revisions` 的结果。"""

    title: str
    """服务器规范化后的标题。"""
    text: str
    revid: int
    timestamp: str
    """该版本的保存时间,改写页面时作为 ``basetimestamp``。"""
    starttimestamp: str
    """读取时的服务器时间,改写页面时作为 ``starttimestamp``。"""
    redirect: bool
    contentmodel: str


MAX_RETRY_AFTER = 300
"""按 ``Retry-After`` 等待的上限(秒):等更久说明问题不在节奏,直接失败更好。"""


def _retry_after(resp: httpx2.Response) -> float | None:
    """解析 ``Retry-After``(秒数或 HTTP 日期),截到 :data:`MAX_RETRY_AFTER`。

    没有这个头或看不懂时返回 None。
    """
    value = resp.headers.get("retry-after")
    if value is None:
        return None
    try:
        delay = float(int(value))
    except ValueError:
        try:
            when = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        if when.tzinfo is None:
            when = when.replace(tzinfo=UTC)
        delay = (when - datetime.now(UTC)).total_seconds()
    return min(max(delay, 0.0), MAX_RETRY_AFTER)


def _wait(state: RetryCallState) -> float:
    """tenacity 的 ``wait``:决定重试后再算等多久,最后一次失败直接抛出不白等。

    服务器给了 ``Retry-After``(CDN / 反代层的 429、503,和 MediaWiki 自己的
    配额无关)就照办;429 没给按默认冷却;其余错误固定等 1 秒。
    """
    exc = state.outcome.exception() if state.outcome else None
    if isinstance(exc, httpx2.HTTPStatusError):
        delay = _retry_after(exc.response)
        if delay is not None:
            return delay
        if exc.response.status_code == 429:
            return DEFAULT_COOLDOWN
    return 1.0


def _worth_retrying(exc: BaseException) -> bool:
    """网络错误、5xx 与 429 值得重试;其余 4xx 再发一次也是同样的结果。"""
    if isinstance(exc, httpx2.HTTPStatusError):
        status = exc.response.status_code
        return status == 429 or status >= 500
    return isinstance(exc, httpx2.HTTPError)


def _transient(name: str) -> Any:
    return retry(
        stop=stop_after_attempt(3),
        wait=_wait,
        retry=retry_if_exception(_worth_retrying),
        before_sleep=log_retry(name),
        reraise=True,
    )


class Wiki:
    def __init__(
        self,
        api_url: str,
        mode: str = "product",
        client: httpx2.AsyncClient | None = None,
        rate_safety: float = 0.8,
        write_min_interval: float = 0.0,
    ) -> None:
        self.api_url = api_url
        self.mode = mode
        self.client = client or make_client()
        self._csrf_token: str | None = None
        self._write_lock = anyio.Lock()
        self._rate_safety = rate_safety
        self._write_min_interval = write_min_interval
        self._limiters: dict[str, Throttle] = {}
        """登录后发现配额后,每个写动作一个限速器;查不到时全是 passthrough。"""
        self._unlimited = Throttle()
        self._last_write = 0.0

    @classmethod
    async def login(
        cls,
        api_url: str,
        username: str,
        password: str,
        mode: str = "product",
        client: httpx2.AsyncClient | None = None,
        rate_safety: float = 0.8,
        write_min_interval: float = 0.0,
    ) -> "Wiki":
        """登录并返回客户端;登录失败抛 RuntimeError。"""
        wiki = cls(api_url, mode, client, rate_safety, write_min_interval)
        token = await wiki._query({"meta": "tokens", "type": "login"})
        res = await wiki._post(
            {
                "action": "login",
                "lgname": username,
                "lgpassword": password,
                "lgtoken": token["query"]["tokens"]["logintoken"],
            }
        )
        if res["login"]["result"] != "Success":
            raise RuntimeError(res["login"]["reason"])
        await wiki._discover_rate_limits()
        return wiki

    async def aclose(self) -> None:
        await self.client.aclose()

    # ----- 底层请求 -----

    @_transient("wiki.get")
    async def _get(self, params: dict[str, Any]) -> dict[str, Any]:
        resp = await self.client.get(self.api_url, params={"format": "json", **params})
        resp.raise_for_status()
        return resp.json()

    @_transient("wiki.post")
    async def _post(
        self,
        data: dict[str, Any],
        *,
        write_action: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        if write_action is not None:
            # 放在 HTTP 重试内部,每次实际写请求都占限速名额并更新发送时刻。
            await self._pace_write(write_action)
            self._last_write = time.monotonic()
        form = {"format": "json", **data}
        # 站点会整个丢掉超过约 50KB 的 urlencoded 请求体,api.php 收不到参数
        # 就返回 200 的 HTML 帮助页;multipart 不受这个限制,统一走 multipart
        token = form.pop("token", None)
        parts: dict[str, Any] = {k: (None, str(v)) for k, v in form.items()}
        parts |= kwargs.pop("files", {})
        if token is not None:
            # token 必须排在正文和文件之后(MediaWiki 文档的要求):请求体中途断开时
            # 服务器会把收到的前半截当成完整请求处理,token 在前就会存下半截页面
            # (摘要也丢了);放在最后,截断的请求缺 token,直接被拒
            parts["token"] = (None, str(token))
        resp = await self.client.post(self.api_url, files=parts, **kwargs)
        resp.raise_for_status()
        return resp.json()

    async def _discover_rate_limits(self) -> None:
        """登录后查一次当前账号适用的写配额并建限速器;查不到就保持不限速。"""
        try:
            res = await self._query({"meta": "userinfo", "uiprop": "ratelimits"})
            limits = parse_ratelimits(res["query"]["userinfo"].get("ratelimits") or {})
        except Exception:
            # 配额只是护栏,查询失败不该挡住任务;真撞了还有 ratelimited 重试兜底
            logger.opt(exception=True).warning(
                "Rate limit discovery failed; writes stay unpaced"
            )
            return
        self._limiters = {
            action: Throttle(rls, safety=self._rate_safety)
            for action, rls in limits.items()
        }
        detail = (
            ", ".join(
                f"{a} " + " + ".join(f"{rl.limit}/{rl.period:g}s" for rl in rls)
                for a, rls in sorted(limits.items())
            )
            or "none (noratelimit?)"
        )
        logger.info(f"Rate limits for this account: {detail}")

    async def _query(self, params: dict[str, Any]) -> dict[str, Any]:
        return await self._get({"action": "query", **params})

    async def csrf_token(self, refresh: bool = False) -> str:
        token = None if refresh else self._csrf_token
        if token is None:
            res = await self._query({"meta": "tokens"})
            token = self._csrf_token = res["query"]["tokens"]["csrftoken"]
        return token

    async def _pace_write(self, action: str) -> None:
        """写前限速:先补足与上一次写请求的最小间隔,再占该动作的配额名额。

        顺序不能反:占名额即记账,占完再睡会让记账早于实际发送,窗口提前放出名额。
        """
        if self._write_min_interval > 0:
            delay = self._write_min_interval - (time.monotonic() - self._last_write)
            if delay > 0:
                await anyio.sleep(delay)
        await self._limiters.get(action, self._unlimited).acquire()

    async def _write(self, action: str, data: dict[str, Any], **kwargs: Any) -> Any:
        """带 csrf token 的写操作;token 失效时刷新重试一次,撞限时冷却后重试。"""
        refresh_token = token_refreshed = False
        cooldowns = 0
        async with self._write_lock:
            while True:
                post_data = {
                    "action": action,
                    "token": await self.csrf_token(refresh=refresh_token),
                    **data,
                }
                res = await self._post(post_data, write_action=action, **kwargs)
                error = res.get("error")
                if error is None:
                    return res
                code = error.get("code", "")
                # 只有 badtoken 才换 token,且只换一次;撞限重试沿用当前 token
                refresh_token = code == "badtoken" and not token_refreshed
                if refresh_token:
                    token_refreshed = True
                    continue
                if code == "ratelimited" and cooldowns < MAX_RATELIMIT_RETRIES:
                    cooldowns += 1
                    limiter = self._limiters.get(action, self._unlimited)
                    logger.warning(
                        f"Rate limited on {action}; cooling down before retry"
                    )
                    await limiter.cooldown()
                    continue
                raise WikiError(code, error.get("info", ""))

    @staticmethod
    def _form(args: dict[str, Any], boolargs: set[str]) -> dict[str, Any]:
        """把 None 过滤掉,布尔标志按 MediaWiki 的习惯传 ``"1"``。"""
        data: dict[str, Any] = {}
        for key, value in args.items():
            if value is None:
                continue
            if key in boolargs:
                if value:
                    data[key] = "1"
            else:
                data[key] = value
        return data

    # ----- 编辑 -----

    async def edit(
        self,
        title: str | None = None,
        pageid: int | str | None = None,
        section: int | str | None = None,
        sectiontitle: str | None = None,
        text: str | None = None,
        summary: str | None = None,
        minor: bool | None = None,
        # 布尔标志传 None 表示不带这个参数;历史调用里 createonly 也有传 "1" 的
        bot: bool | None = True,
        createonly: bool | str | None = None,
        nocreate: bool | None = None,
        prependtext: str | None = None,
        appendtext: str | None = None,
        redirect: bool | None = None,
        contentformat: str | None = None,
        contentmodel: str | None = None,
        basetimestamp: str | None = None,
        starttimestamp: str | None = None,
    ) -> dict[str, Any] | None:
        """
        :param title: 要编辑的页面标题。不能与pageid一起使用。
        :param pageid:要编辑的页面的页面 ID。不能与title一起使用。
        :param section:段落数。0用于首段，new用于新的段落。NOTICE:会覆盖==xx==的部分
        :param sectiontitle:新段落的标题。
        :param text:页面内容。
        :param summary:编辑摘要。当section=new且未设置sectiontitle时，还包括小节标题。
        :param minor:小编辑。
        :param bot:机器人编辑。
        :param createonly:不要编辑页面，如果已经存在。
        :param nocreate:如果该页面不存在，则抛出一个错误。
        :param prependtext:将该文本添加到该页面的开始。覆盖text。
        :param appendtext:将该文本添加到该页面的结尾。覆盖text。
        :param redirect:自动解决重定向。
        :param contentformat:用于输入文本的内容序列化格式。application/json、
            text/plain、text/css、text/x-wiki、text/javascript
        :param contentmodel:新内容的内容模型。GadgetDefinition、Scribunto、
            sanitized-css、flow-board、wikitext、javascript、json、css、text、smw/schema
        :param basetimestamp:所基于版本的时间戳,页面在此之后被改过时报 editconflict。
        :param starttimestamp:开始编辑的时间,页面在此之后被删除时报 pagedeleted。
            两者都取自 :meth:`read_revisions` 的结果。
        :return: API 返回的 JSON;dev 模式下只打印参数并返回 None,
            ``createonly`` 而页面已存在时也返回 None
        """
        args = locals().copy()
        args.pop("self")
        if self.mode != "product":
            logger.info("\n" + str(args) + "\n")
            return None
        boolargs = {"minor", "createonly", "nocreate", "redirect", "bot"}
        try:
            return await self._write("edit", self._form(args, boolargs))
        except WikiError as e:
            # createonly 的本意就是「已存在则不动」,各 job 每次都会对已有页面调用
            if createonly and e.code == "articleexists":
                logger.info(f"Page already exists, skip: {title or pageid}")
                return None
            raise

    async def create(
        self,
        title: str,
        text: str,
        *,
        protections: str | None = None,
        protect_reason: str = "protect",
        **edit_args: Any,
    ) -> bool:
        """新建页面,建成后按 ``protections`` 加保护;页面已存在时两样都不做。

        已存在的页面可能是占了名字的重定向或同名的其它页面,给它加保护会挡住
        之后的人工处理(如删除重定向),所以只保护自己建的页面。
        ``edit_args`` 原样传给 :meth:`edit`。

        :return: 是否建了页面;dev 模式下不知道页面在不在,按建了处理
        """
        res = await self.edit(title=title, text=text, createonly=True, **edit_args)
        if res is None and self.mode == "product":
            return False
        if protections is not None:
            await self.protect(
                title=title, protections=protections, reason=protect_reason
            )
        return True

    async def protect(
        self,
        title: str | None = None,
        pageid: int | str | None = None,
        protections: str | None = None,
        reason: str | None = None,
        cascade: bool | None = None,
    ) -> dict[str, Any] | None:
        """
        :param title:要（解除）保护的页面标题。不能与pageid一起使用。
        :param pageid:要（解除）保护的页面ID。不能与title一起使用。
        :param protections:保护等级列表，格式：action=level（例如edit=sysop）。
            等级all意味着任何人都可以执行操作，也就是说没有限制。
            注意：未列出的操作将移除限制。
        :param reason:（解除）保护的原因。
        :param cascade:启用连锁保护（也就是保护包含于此页面的页面）。
            如果所有提供的保护等级不支持连锁，就将其忽略。
        """
        args = locals().copy()
        args.pop("self")
        if self.mode != "product":
            logger.info("\n" + "\n" + str(args) + "\n")
            return None
        return await self._write(
            "protect", {"expiry": "infinite", **self._form(args, {"cascade"})}
        )

    async def upload(
        self,
        filepath: str,
        filename: str,
        comment: str | None = None,
        text: str | None = None,
    ) -> dict[str, Any]:
        """
        :param filepath:文件路径
        :param filename:目标文件名
        :param comment:上传注释。如果没有指定text，那么它也被用于新文件的初始页面文本。
        :param text:用于新文件的初始页面文本。
        """
        content = await anyio.Path(filepath).read_bytes()
        data = self._form(
            {
                "filename": filename,
                "ignorewarnings": "1",
                "comment": comment,
                "text": text,
            },
            set(),
        )
        return await self._write(
            "upload", data, files={"file": (quote(filename), content)}
        )

    # ----- 读取 -----

    @staticmethod
    def _page_text(page: dict[str, Any]) -> str | None:
        revisions = page.get("revisions")
        if not revisions:
            return None
        return revisions[0]["*"]

    async def read(self, title: str) -> str:
        """
        :param title: 名称空间:页面名
        :return: wikitext;页面不存在时抛 KeyError
        """
        res = await self._query(
            {"titles": title, "prop": "revisions", "rvprop": "content"}
        )
        for page in res["query"]["pages"].values():
            text = self._page_text(page)
            if text is None:
                raise KeyError(title)
            return text
        raise KeyError(title)

    async def read_many(self, titles: Iterable[str]) -> dict[str, str]:
        """批量读取,返回 ``{标题: wikitext}``;不存在的页面不在结果里。

        每 :data:`READ_CHUNK` 个标题合并成一个请求。结果按调用方写的标题索引
        (服务器会把下划线、首字母大小写规范化,这里映射回去)。响应超过 API
        大小上限时 MediaWiki 会把部分页面的内容截掉,这些页面再单独读一次。
        """
        titles = list(dict.fromkeys(titles))
        result: dict[str, str] = {}
        for start in range(0, len(titles), READ_CHUNK):
            chunk = titles[start : start + READ_CHUNK]
            requested = set(chunk)
            res = await self._query(
                {
                    "titles": "|".join(chunk),
                    "prop": "revisions",
                    "rvprop": "content",
                }
            )
            query = res["query"]
            aliases: dict[str, list[str]] = {}
            for item in query.get("normalized", []):
                aliases.setdefault(item["to"], []).append(item["from"])
            truncated: list[str] = []
            for page in query.get("pages", {}).values():
                if "missing" in page:
                    continue
                title = page["title"]
                keys = [t for t in (title, *aliases.get(title, [])) if t in requested]
                text = self._page_text(page)
                if text is None:
                    truncated.extend(keys)
                else:
                    for key in keys:
                        result[key] = text
            for title in truncated:
                result[title] = await self.read(title)
        return result

    async def read_revisions(self, titles: Iterable[str]) -> dict[str, PageRevision]:
        """批量读取页面最新版本,返回 ``{标题: PageRevision}``;不存在的页面不在结果里。

        分批、标题映射与截断后单独重读的规则同 :meth:`read_many`,只是多带回
        版本号、时间戳、内容模型和是否为重定向,供改写页面时检测编辑冲突。
        """
        titles = list(dict.fromkeys(titles))
        chunks = [titles[i : i + READ_CHUNK] for i in range(0, len(titles), READ_CHUNK)]
        result: dict[str, PageRevision] = {}
        while chunks:
            chunk = chunks.pop(0)
            requested = set(chunk)
            res = await self._query(
                {
                    "titles": "|".join(chunk),
                    "prop": "revisions|info",
                    "rvprop": "ids|timestamp|content",
                    "curtimestamp": 1,
                }
            )
            query = res["query"]
            aliases: dict[str, list[str]] = {}
            for item in query.get("normalized", []):
                aliases.setdefault(item["to"], []).append(item["from"])
            for page in query.get("pages", {}).values():
                if "missing" in page or "invalid" in page:
                    continue
                title = page["title"]
                keys = [t for t in (title, *aliases.get(title, [])) if t in requested]
                text = self._page_text(page)
                if text is None:
                    if len(chunk) == 1:
                        raise KeyError(title)
                    chunks.extend([key] for key in keys)
                    continue
                revision = page["revisions"][0]
                snapshot = PageRevision(
                    title=title,
                    text=text,
                    revid=revision["revid"],
                    timestamp=revision["timestamp"],
                    starttimestamp=res["curtimestamp"],
                    redirect="redirect" in page,
                    contentmodel=page.get("contentmodel", "wikitext"),
                )
                for key in keys:
                    result[key] = snapshot
        return result

    async def category(self, category: str) -> list[str]:
        CM_LIMIT = 1000  # noqa: N806
        cat_page_list: list[str] = []
        params: dict[str, Any] = {
            "list": "categorymembers",
            "cmtitle": category,
            "cmlimit": CM_LIMIT,
            "cmprop": "ids|title|sortkey",
        }
        ret = (await self._query(params))["query"]["categorymembers"]
        cat_page_list.extend(page["title"] for page in ret)

        while len(ret) >= CM_LIMIT:
            cmprefix = ret[-1]["sortkey"]
            ret = (await self._query({**params, "cmstarthexsortkey": cmprefix}))[
                "query"
            ]["categorymembers"]
            cat_page_list.pop()  # 两次查询的头尾会重复，移除其中一个
            cat_page_list.extend(page["title"] for page in ret)
        return cat_page_list

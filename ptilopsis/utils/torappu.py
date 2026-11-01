"""torappu (https://torappu.prts.wiki) 的 HTTP 客户端。

torappu 是 Mooncell 自建的明日方舟资源仓库,会持续解包国服客户端并把解出来的
gamedata 按 resVersion 存档。本模块只封装机器人需要的三类接口:

* ``GET /api/v1/version``             全部已收录版本,按 id 升序;
* ``GET /gamedata/<resVersion>/<path>``  直接下载某版本的 gamedata 文件;
* ``GET /api/v1/files/<path>``         目录列举(整个路径必须编码成一段)。

某个版本的 gamedata 是否已经解包完成,以 ``gamedata/<resVersion>/.gamedata-ready.json``
是否存在为准;``/api/v1/version`` 里的 ``isReady`` 只表示 AB 包下载完毕。

客户端是 async 的(httpx2 + anyio,与 torappu 自己的做法一致):HTTP/2 让上千个
小文件复用一条连接,Happy Eyeballs 让 CDN 的多个 A 记录并发试连,不再被单个
不通的节点拖住整个 connect timeout。同一时刻的下载数由信号量限制。

完整 API 文档见 https://torappu.prts.wiki/api/v1/scalar 。
"""

import time
from collections.abc import AsyncIterator
from typing import Any
from urllib.parse import quote

import anyio
import httpx2
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)

from ptilopsis.log import logger
from ptilopsis.utils.http import log_retry, make_client

__all__ = [
    "READY_MARKER",
    "ChallengePageError",
    "TorappuClient",
    "TorappuEntry",
    "TorappuVersion",
]

READY_MARKER = ".gamedata-ready.json"
"""gamedata 解包完成后 torappu 在版本目录下写的标记文件。"""


class TorappuVersion(BaseModel):
    """``/api/v1/version`` 列表里的一项。"""

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, extra="ignore"
    )

    id: int
    client_version: str
    res_version: str
    is_ready: bool
    """AB 包是否已全部下载;gamedata 是否可用另看 :meth:`TorappuClient.has_gamedata`。"""
    asset_mapping_status: str = ""


class TorappuEntry(BaseModel):
    """``/api/v1/files`` 目录列举里的一项。"""

    model_config = ConfigDict(extra="ignore")

    name: str
    path: str
    """相对 torappu 文件根的路径,如 ``gamedata/<resVersion>/excel/item_table.json``。"""
    size: int = 0
    is_dir: bool


class ChallengePageError(httpx2.HTTPError):
    """CDN 用 200 返回了 HTML 挑战页,而不是文件内容。

    torappu 前面的 CDN(Tengine)触发 CC 防护时,会对任意路径(包括本该 404 的)
    返回 ``<html><script>document.location.reload();</script></html>`` 并下发
    cookie。按网络错误重试:客户端带着 cookie 再请求一次;重试用完仍是挑战页
    就抛出,绝不能把它当成文件内容缓存、写进页面。
    """


def _is_html(resp: httpx2.Response) -> bool:
    if resp.headers.get("content-type", "").startswith("text/html"):
        return True
    # 没带 content-type 时看正文开头;gamedata 只有 json / txt 等,不会是 HTML
    return resp.content.lstrip()[:5].lower() == b"<html"


def _transient(name: str) -> Any:
    """最多 3 次、间隔 2 秒,只重试网络与 HTTP 错误。

    404 已转成 FileNotFoundError,数据解析失败重试也没用;取消(CancelledError)
    更不能被当成失败重试,否则 Ctrl+C 会被吞掉。
    """
    return retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(2),
        retry=retry_if_exception_type(httpx2.HTTPError),
        before_sleep=log_retry(name, with_args=True),
        reraise=True,
    )


class TorappuClient:
    """按版本读取 torappu 上的 gamedata。"""

    def __init__(
        self,
        base_url: str,
        client: httpx2.AsyncClient | None = None,
        timeout: float = 60,
        max_concurrency: int = 16,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.client = client or make_client(timeout)
        self._semaphore = anyio.Semaphore(max_concurrency)

    async def aclose(self) -> None:
        await self.client.aclose()

    # ----- URL -----

    def gamedata_url(self, res_version: str, path: str) -> str:
        """``path`` 相对 gamedata 根,如 ``excel/item_table.json``。

        ``[uc]`` 之类的方括号目录需要按 RFC 3986 编码,只保留 ``/``。
        """
        return f"{self.base_url}/gamedata/{res_version}/{quote(path, safe='/')}"

    def files_url(self, full_path: str) -> str:
        """目录列举接口只把最后一段当路径,所以整个路径都要编码,包括 ``/``。"""
        return f"{self.base_url}/api/v1/files/{quote(full_path, safe='')}"

    # ----- 版本 -----

    @_transient("list_versions")
    async def list_versions(self) -> list[TorappuVersion]:
        """全部已收录版本,按 id 升序(与接口返回顺序一致)。"""
        resp = await self.client.get(f"{self.base_url}/api/v1/version")
        resp.raise_for_status()
        versions = [TorappuVersion.model_validate(item) for item in resp.json()]
        return sorted(versions, key=lambda v: v.id)

    @_transient("has_gamedata")
    async def has_gamedata(self, res_version: str) -> bool:
        """该版本的 gamedata 是否已解包完成。"""
        resp = await self.client.get(
            self.gamedata_url(res_version, READY_MARKER),
            # 标记文件走 CDN,带个时间戳避免刚生成时命中缓存的 404
            params={"_": int(time.time())},
        )
        if resp.status_code == 404:
            return False
        resp.raise_for_status()
        return True

    async def latest_version(self, max_probe: int = 10) -> TorappuVersion:
        """最新的、gamedata 已解包完成的版本。

        从最新往旧最多探测 ``max_probe`` 个;正常情况下最新或次新就是。
        """
        candidates = (await self.list_versions())[::-1][:max_probe]
        for version in candidates:
            if await self.has_gamedata(version.res_version):
                return version
            logger.info(f"[torappu] {version.res_version} gamedata not ready yet, skip")
        raise RuntimeError(
            f"torappu has no version with ready gamedata among the latest "
            f"{len(candidates)}: {[v.res_version for v in candidates]}"
        )

    # ----- 文件 -----

    @_transient("fetch")
    async def fetch(self, res_version: str, path: str) -> bytes:
        """下载 ``gamedata/<res_version>/<path>``;不存在时抛 FileNotFoundError。"""
        url = self.gamedata_url(res_version, path)
        async with self._semaphore:
            resp = await self.client.get(url)
        if resp.status_code == 404:
            raise FileNotFoundError(f"torappu has no {path!r} for {res_version}")
        resp.raise_for_status()
        if _is_html(resp):
            raise ChallengePageError(f"torappu returned an HTML page for {path!r}")
        return resp.content

    @_transient("exists")
    async def exists(self, res_version: str, path: str) -> bool:
        """``gamedata/<res_version>/<path>`` 是否是一个存在的文件。"""
        resp = await self.client.head(
            self.gamedata_url(res_version, path), follow_redirects=True
        )
        if resp.status_code == 404:
            return False
        resp.raise_for_status()
        return True

    @_transient("list_dir")
    async def list_dir(self, res_version: str, path: str = "") -> list[TorappuEntry]:
        """列出 ``gamedata/<res_version>/<path>`` 目录下的直接子项。"""
        full_path = f"gamedata/{res_version}"
        if path:
            full_path = f"{full_path}/{path.strip('/')}"
        resp = await self.client.get(self.files_url(full_path))
        # 目录不存在时接口返回 500 而不是 404
        if resp.status_code in (404, 500):
            raise FileNotFoundError(
                f"torappu has no directory {path!r} for {res_version}"
            )
        resp.raise_for_status()
        return [TorappuEntry.model_validate(item) for item in resp.json()["children"]]

    async def walk(self, res_version: str, path: str = "") -> AsyncIterator[str]:
        """递归列出 ``path`` 下所有文件,产出相对 gamedata 根的路径。

        ``path`` 本身是文件时只产出它自己。
        """
        prefix = f"gamedata/{res_version}/"
        pending = [path.strip("/")]
        while pending:
            current = pending.pop(0)
            try:
                entries = await self.list_dir(res_version, current)
            except FileNotFoundError:
                # 目录接口对「不存在」和「是文件」都报错,再确认一次是不是文件
                if current and await self.exists(res_version, current):
                    yield current
                    continue
                raise
            for entry in entries:
                relative = entry.path.removeprefix(prefix)
                if entry.is_dir:
                    pending.append(relative)
                else:
                    yield relative

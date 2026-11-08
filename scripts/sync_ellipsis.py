"""把 2.7.71 客户端更新里游戏文本的省略号规范化同步到 wiki。

2.7.71(resVersion ``26-09-03-04-06-00_ed95a2``)起,游戏把语音、档案、模组、家具、
敌人、道具、皮肤、关卡 CG 等文本里的英文句点串(绝大多数是 ``......``,也有 ``...``、
``.....`` 等)批量改成了中文省略号(``……`` / ``…``)。

语音记录、干员密录、悖论模拟(干员页内)由 ``special`` 模式的 job 整体刷新,剧情页由
其它机器人维护,都已经同步;其余页面只建页不更新,停留在旧文本:干员档案、模组基础信息、
相关道具,家具 / 敌人 / 道具描述,悖论模拟关卡,以及关卡一览里的 CG 与故事集简介。

这里不重新生成页面,而是对比改动前后两个版本的 excel,把每一处被改的点串连同两侧
上下文做成一条替换规则:页面上能对上上下文的点串才改,人工修订过的其它文字都不动。

    # 预览:匿名读取页面,把 diff 和 report.json 写到 out/ellipsis
    uv run python scripts/sync_ellipsis.py out/ellipsis
    # 登录并写入
    uv run python scripts/sync_ellipsis.py out/ellipsis --apply
    # 只处理指定页面
    uv run python scripts/sync_ellipsis.py out/ellipsis --only 白面鸮 --only 梅尔
"""

import argparse
import difflib
import json
import re
from collections import Counter, defaultdict
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import anyio

from ptilopsis.config import config, get_settings
from ptilopsis.log import logger
from ptilopsis.utils.torappu import TorappuClient
from ptilopsis.utils.wiki import Wiki, WikiError

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".cache" / "torappu"

OLD_VERSION = "26-08-17-11-25-42_dbc172"
"""2.7.61 的最后一个版本,文本还是英文句点。"""
NEW_VERSION = "26-09-03-04-06-00_ed95a2"
"""2.7.71 的第一个版本,批量替换在这一版。"""

TABLES = (
    "building_data",
    "character_table",
    "charword_table",
    "display_meta_table",
    "enemy_handbook_table",
    "handbook_info_table",
    "item_table",
    "medal_table",
    "shop_client_table",
    "skin_table",
    "stage_table",
    "uniequip_table",
)
"""这次有文本被替换的 excel 表。"""

CATEGORIES = (
    "分类:干员",
    "分类:道具",
    "分类:未实装道具",
    "分类:家具",
    "分类:敌人",
    "分类:悖论模拟关卡",
)
PREFIXES = ("关卡一览/",)
"""CG 回想与故事集简介的页面不在分类里,按标题前缀列举。"""

SUMMARY = "同步游戏文本:省略号“......”改为“……”"

CONTEXT = 4
"""点串两侧各取到多少个文字(``\\w``)为止作为上下文。"""
MIN_CONTEXT = 2
"""两侧上下文合计少于这么多文字的点串(如整条文本只有“呃......！”)不处理。"""
ONE_SIDED_CONTEXT = 8
ONE_SIDED_MIN = 6
"""两侧对不上(页面上另一侧被人改过、截断或插了模板)时,退而只用一侧上下文:
取 8 个文字,不足 6 个不用。"""
SIMILARITY = 0.9
"""同一条文本还夹带了别的小改动时,按相似度兜底配对的下限。"""

DOTS = re.compile(r"\.{3,}")
ELLIPSIS = re.compile(r"…+")
SEP = r"(?:\s|<br\s*/?>|\\n)*"
"""游戏文本里的空白 / 换行在页面上可能是换行、``<br>`` 或 JSON 里的 ``\\n``。"""
_SKIP_LEFT = re.compile(r"(?:\s|<br\s*/?>|\\n|\\|[.…])+$")
_SKIP_RIGHT = re.compile(r"^(?:\s|<br\s*/?>|\\n|\\|[.…])+")
FIELD_START = r"(?:^|(?<=[=|>\"\n\t]))[ \t]*"
FIELD_END = r"[ \t]*(?=[|<\"\n\t}]|$)"
"""上下文碰到文本开头 / 结尾时,页面上对应位置必须是参数、标签、JSON 字符串、
表格单元或行的边界。"""


# ----- 新旧文本配对 -----


def _strings(node: Any) -> Iterator[str]:
    if isinstance(node, dict):
        for value in node.values():
            yield from _strings(value)
    elif isinstance(node, list):
        for value in node:
            yield from _strings(value)
    elif isinstance(node, str):
        yield node


def _key(text: str) -> str:
    """去掉点串、省略号和空白,新旧版本的同一条文本得到同一个 key。"""
    return re.sub(r"\.{3,}|…+|\s+", "", text)


def _only_ellipsis_changes(old: str, new: str) -> bool:
    """两段文本的差异是否只有「点串 → 省略号」和空白。"""
    o, n = old.replace("\r", ""), new.replace("\r", "")
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
        None, o, n, autojunk=False
    ).get_opcodes():
        if tag == "equal":
            continue
        seg_o, seg_n = o[i1:i2].strip(), n[j1:j2].strip()
        if not seg_o and not seg_n:
            continue
        if not (DOTS.search(seg_o) and ELLIPSIS.fullmatch(seg_n)):
            return False
    return True


def changed_texts(old_table: Any, new_table: Any) -> list[tuple[str, str]]:
    """两个版本的同一张表里,被替换过点串的文本 ``(旧, 新)``。

    不按字段路径对齐(列表顺序会变),而是按 :func:`_key` 配对整张表的字符串;
    同一条文本还夹带了别的小改动(删个逗号、改个引号)而配不上的,按相似度兜底。
    """
    old_all = set(_strings(old_table))
    new_all = set(_strings(new_table))
    news: dict[str, set[str]] = defaultdict(set)
    for text in new_all:
        news[_key(text)].add(text)
    pairs: list[tuple[str, str]] = []
    unpaired: list[str] = []
    for old in sorted(old_all):
        if not DOTS.search(old) or old in new_all:
            continue  # 没有点串,或原样保留
        candidates = [
            new
            for new in news[_key(old)] - old_all
            if new.replace("\r", "") != old.replace("\r", "")
            and _only_ellipsis_changes(old, new)
        ]
        if len(candidates) == 1:
            pairs.append((old, candidates[0]))
        else:
            unpaired.append(old)
    # 比较相似度前把点串和省略号都归一成同一个占位,免得它们本身拉低相似度
    pool = {_similar_key(text): text for text in new_all - old_all if "…" in text}
    for old in unpaired:
        close = difflib.get_close_matches(
            _similar_key(old), sorted(pool), n=1, cutoff=SIMILARITY
        )
        if close:
            pairs.append((old, pool[close[0]]))
    return pairs


def _similar_key(text: str) -> str:
    return re.sub(r"\.{3,}|…+", "…", text.replace("\r", ""))


# ----- 替换规则 -----


def _words(text: str) -> int:
    return len(re.findall(r"\w", text))


def _left_context(text: str, words: int = CONTEXT) -> tuple[str, bool]:
    """从 ``text`` 末尾往前取到 ``words`` 个文字;第二项表示是否取到了文本开头。"""
    count = 0
    for i in range(len(text) - 1, -1, -1):
        count += text[i].isalnum() or text[i] == "_"
        if count >= words:
            return text[i:], False
    return text, True


def _right_context(text: str, words: int = CONTEXT) -> tuple[str, bool]:
    count = 0
    for i, ch in enumerate(text):
        count += ch.isalnum() or ch == "_"
        if count >= words:
            return text[: i + 1], False
    return text, True


_QUOTES = {'"': '\\\\?"', "“": "[“”]", "”": "[“”]"}
"""引号可能被 JSON 转义;中文引号在页面上偶有左右写反的。"""


def _pattern(text: str) -> str:
    """上下文转正则:空白可对应换行 / ``<br>`` / ``\\n``,引号见 ``_QUOTES``。"""
    parts: list[str] = []
    for chunk in re.split(r"(\s+)", text):
        if not chunk:
            continue
        if chunk.isspace():
            parts.append(SEP)
        else:
            parts.append("".join(_QUOTES.get(ch) or re.escape(ch) for ch in chunk))
    return "".join(parts)


def _compile(
    left: str, left_edge: bool, dots: str, right: str, right_edge: bool
) -> re.Pattern[str]:
    """三个分组:左侧上下文、点串、右侧上下文;点串不能是更长点串的一部分。"""
    return re.compile(
        f"({FIELD_START if left_edge else ''}{_pattern(left)})"
        f"(?<!\\.)({re.escape(dots)})(?!\\.)"
        f"({_pattern(right)}{FIELD_END if right_edge else ''})"
    )


def neighbor_left(text: str, pos: int) -> str:
    """``pos`` 左边最近的一个字符,跳过空白、换行标记和点 / 省略号。"""
    window = _SKIP_LEFT.sub("", text[max(0, pos - 40) : pos])
    return window[-1:] if window else ""


def neighbor_right(text: str, pos: int) -> str:
    window = _SKIP_RIGHT.sub("", text[pos : pos + 40])
    return window[:1]


@dataclass(frozen=True)
class Rule:
    """页面上一处 ``dots`` → ``ellipsis`` 的替换。"""

    source: str
    """来源表名,统计用。"""
    order: tuple[int, int]
    """(文本序号, 文本内第几处);同一段文本内的规则须按顺序应用。"""
    dots: str
    ellipsis: str
    patterns: tuple[re.Pattern[str], ...]
    """依次尝试:两侧上下文、只用左侧、只用右侧。"""
    keys: tuple[tuple[str, str], ...]
    """``(点串, 左/右邻字符)``,用来从页面上的点串快速找到候选规则。"""


def _patterns(prefix: str, dots: str, suffix: str) -> tuple[re.Pattern[str], ...]:
    patterns: list[re.Pattern[str]] = []
    left, left_edge = _left_context(prefix)
    right, right_edge = _right_context(suffix)
    if _words(left) + _words(right) >= MIN_CONTEXT:
        patterns.append(_compile(left, left_edge, dots, right, right_edge))
    left, left_edge = _left_context(prefix, ONE_SIDED_CONTEXT)
    if _words(left) >= ONE_SIDED_MIN:
        patterns.append(_compile(left, left_edge, dots, "", False))
    right, right_edge = _right_context(suffix, ONE_SIDED_CONTEXT)
    if _words(right) >= ONE_SIDED_MIN:
        patterns.append(_compile("", False, dots, right, right_edge))
    return tuple(patterns)


def rules_for(source: str, index: int, old: str, new: str) -> list[Rule]:
    """一段文本里每处被替换的点串一条规则。

    上下文按应用到这一处时页面的样子取:前面的点串已经换成省略号,后面的还没换,
    夹带的其它改动(删字、改引号)页面上还是旧的。
    """
    o, n = old.replace("\r", ""), new.replace("\r", "")
    rules: list[Rule] = []
    done: list[str] = []
    """``o`` 已处理部分在页面上的样子。"""
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
        None, o, n, autojunk=False
    ).get_opcodes():
        segment, ellipsis = o[i1:i2], n[j1:j2].strip()
        match = DOTS.search(segment) if tag != "equal" else None
        if match is None or not ELLIPSIS.fullmatch(ellipsis):
            done.append(segment)
            continue
        dots = match.group()
        prefix = "".join(done) + segment[: match.start()]
        suffix = segment[match.end() :] + o[i2:]
        done.append(segment[: match.start()] + ellipsis + segment[match.end() :])
        patterns = _patterns(prefix, dots, suffix)
        if not patterns:
            continue
        rules.append(
            Rule(
                source=source,
                order=(index, len(rules)),
                dots=dots,
                ellipsis=ellipsis,
                patterns=patterns,
                keys=(
                    (dots, neighbor_left(prefix, len(prefix))),
                    (dots, neighbor_right(suffix, 0)),
                ),
            )
        )
    return rules


class Rulebook:
    def __init__(self, rules: Iterable[Rule]) -> None:
        self.rules = list(rules)
        self._index: dict[tuple[str, str], list[Rule]] = defaultdict(list)
        for rule in self.rules:
            for key in set(rule.keys):
                if key[1]:
                    self._index[key].append(rule)

    @classmethod
    def from_tables(
        cls, old_tables: dict[str, Any], new_tables: dict[str, Any]
    ) -> "Rulebook":
        rules: list[Rule] = []
        index = 0
        for name in TABLES:
            for old, new in changed_texts(old_tables[name], new_tables[name]):
                rules += rules_for(name, index, old, new)
                index += 1
        return cls(rules)

    def candidates(self, text: str) -> list[Rule]:
        found: set[Rule] = set()
        for match in DOTS.finditer(text):
            for key in (
                (match.group(), neighbor_left(text, match.start())),
                (match.group(), neighbor_right(text, match.end())),
            ):
                found.update(self._index.get(key, ()))
        return sorted(found, key=lambda rule: rule.order)

    def apply(self, text: str) -> tuple[str, Counter[str]]:
        """返回替换后的文本和各来源表替换的处数。"""
        applied: Counter[str] = Counter()
        for rule in self.candidates(text):
            # 两侧都对上的先换;换过的点串已不是点串,不会被后面的宽松模式重复匹配
            for pattern in rule.patterns:
                text, count = pattern.subn(
                    lambda m, r=rule: m[1] + r.ellipsis + m[3], text
                )
                if count:
                    applied[rule.source] += count
        return text, applied


# ----- 数据与页面 -----


async def load_tables(torappu: TorappuClient, version: str) -> dict[str, Any]:
    """读取某版本的 excel 表,缓存位置与 GameData 相同。"""
    tables: dict[str, Any] = {}

    async def load(name: str) -> None:
        path = anyio.Path(CACHE_DIR / version / "excel" / f"{name}.json")
        if not await path.is_file():
            content = await torappu.fetch(version, f"excel/{name}.json")
            await path.parent.mkdir(parents=True, exist_ok=True)
            await path.write_bytes(content)
        tables[name] = json.loads(await path.read_bytes())

    async with anyio.create_task_group() as tg:
        for name in TABLES:
            tg.start_soon(load, name)
    return tables


async def _list(wiki: Wiki, params: dict[str, Any], key: str) -> list[str]:
    """按 ``continue`` 翻完一个列表查询。

    不用 :meth:`Wiki.category`:它按每页 1000 条判断是否翻页,匿名预览时
    每页最多只给 500 条,会只拿到第一页。
    """
    titles: list[str] = []
    while True:
        res = await wiki._query(params)
        titles += [page["title"] for page in res["query"][key]]
        if "continue" not in res:
            return titles
        params = {**params, **res["continue"]}


async def candidate_titles(wiki: Wiki) -> list[str]:
    titles: list[str] = []
    for category in CATEGORIES:
        titles += await _list(
            wiki,
            {
                "list": "categorymembers",
                "cmtitle": category,
                "cmnamespace": 0,
                "cmlimit": "max",
            },
            "categorymembers",
        )
    for prefix in PREFIXES:
        titles += await _list(
            wiki,
            {
                "list": "allpages",
                "apprefix": prefix,
                "apnamespace": 0,
                "apfilterredir": "nonredirects",
                "aplimit": "max",
            },
            "allpages",
        )
    return list(dict.fromkeys(titles))


def _safe_name(title: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", title)


async def run(out: Path, apply: bool, only: list[str]) -> None:
    torappu = TorappuClient(config.torappu_url)
    try:
        old_tables = await load_tables(torappu, OLD_VERSION)
        new_tables = await load_tables(torappu, NEW_VERSION)
    finally:
        await torappu.aclose()
    book = Rulebook.from_tables(old_tables, new_tables)
    logger.info(f"{len(book.rules)} 条替换规则")

    if apply:
        settings = get_settings()
        username, password = settings.require_wiki_credentials()
        wiki = await Wiki.login(
            config.api_url,
            username,
            password,
            rate_safety=settings.rate_safety,
            write_min_interval=settings.write_min_interval,
        )
    else:
        wiki = Wiki(config.api_url, mode="dev")
    try:
        titles = only or await candidate_titles(wiki)
        logger.info(f"读取 {len(titles)} 个候选页面")
        pages = await wiki.read_revisions(titles)

        out_dir = anyio.Path(out)
        await out_dir.mkdir(parents=True, exist_ok=True)
        report: dict[str, dict[str, int]] = {}
        totals: Counter[str] = Counter()
        for page in {p.title: p for p in pages.values()}.values():
            if page.redirect or page.contentmodel != "wikitext":
                continue
            text, applied = book.apply(page.text)
            if text == page.text:
                continue
            report[page.title] = dict(applied)
            totals.update(applied)
            diff = difflib.unified_diff(
                page.text.splitlines(keepends=True),
                text.splitlines(keepends=True),
                f"{page.title} (r{page.revid})",
                page.title,
            )
            await (out_dir / f"{_safe_name(page.title)}.diff").write_text(
                "".join(diff), encoding="utf-8"
            )
            if not apply:
                continue
            try:
                await wiki.edit(
                    title=page.title,
                    text=text,
                    summary=SUMMARY,
                    minor=True,
                    nocreate=True,
                    basetimestamp=page.timestamp,
                    starttimestamp=page.starttimestamp,
                )
            except WikiError as e:
                if e.code not in {"editconflict", "pagedeleted", "missingtitle"}:
                    raise
                logger.warning(f"{page.title} 读取后被改动或删除,跳过")
                report[page.title]["skipped"] = 1
                continue
            logger.info(f"Updated: {page.title} {dict(applied)}")

        await (out_dir / "report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        logger.info(
            f"{len(report)} 个页面共 {sum(totals.values())} 处:{dict(totals)}"
            + ("" if apply else f";diff 见 {out}")
        )
    finally:
        await wiki.aclose()


def main() -> None:
    parser = argparse.ArgumentParser(description="把游戏文本的省略号规范化同步到 wiki")
    parser.add_argument("out", type=Path, help="diff 与 report.json 的输出目录")
    parser.add_argument("--apply", action="store_true", help="登录并实际写入 wiki")
    parser.add_argument(
        "--only", action="append", default=[], help="只处理这些页面(可重复)"
    )
    args = parser.parse_args()
    anyio.run(run, args.out, args.apply, args.only)


if __name__ == "__main__":
    main()

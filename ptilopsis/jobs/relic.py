"""集成战略收藏品页面:新建缺失的页面,给已有页面补上新主题。

每个收藏品一个页面,正文是 {{收藏品/common}}。页面上的主题按游戏内 rogue 编号的
先后从 1 连续编号(主题1、主题2 …),与 rogue_N 的 N 本身无关。维护规则是幂等的,
重复运行不会产生新的编辑,所以不需要额外记录状态:

- 页面不存在:按全部主题新建。
- 页面已存在:刷新 iconId / 稀有度 / 描述,按顺序插入缺少的主题;
  已有主题的字段、人工添加的参数和模板以外的正文都不动。
- 页面结构拿不准(重定向、不是收藏品页面等)时跳过
  并记 warning,交给人工处理。
"""

import html
import re
from dataclasses import dataclass
from itertools import pairwise

from ptilopsis.gamedata.roguelike_table import RoguelikeItem
from ptilopsis.gamedata.roguelike_topic_table import (
    RoguelikeGameItemData,
    RoguelikeTopicDetail,
)
from ptilopsis.jobs.params import RoguelikeTable, RoguelikeTopicTable
from ptilopsis.log import logger
from ptilopsis.utils.job import job
from ptilopsis.utils.wiki import Wiki, WikiError
from ptilopsis.wikitext import WikiTemplate, inline_template

TEMPLATE = "收藏品/common"
MAX_THEMES = 7
"""模板:收藏品/common 支持的主题数。"""
LEGACY_THEME = "刻俄柏的灰蕈迷境"
PAGE_TITLES = {
    "酸液源石虫": "酸液源石虫(收藏品)",
    "“复仇者”": "“复仇者”(收藏品)",
}
"""与敌人等页面重名的收藏品,页面名加 (收藏品) 后缀。"""
RARITIES = {"NORMAL": 0, "RARE": 1, "SUPER_RARE": 2}
"""收藏品稀有度 → |稀有度=;新表售价按 (稀有度 + 2) × 4 计算。"""
GENERIC_OBTAIN = "在集成战略模式中获得"
"""绝大多数收藏品的获取方式都是这句,页面上留空。"""
REFRESHED_FIELDS = ("iconId", "稀有度", "描述")
"""已有页面上随游戏数据刷新的字段;其余字段写上之后就交给人工维护。"""
THEME_FIELD = re.compile(
    r"^(?:主题|角标|售价|易与售价|货币|效果|效果高度|获取条件|解锁条件)([1-9]\d*)$"
)
"""带主题编号的参数。"""

PREAMBLE = (
    "{{Cbox2|mdi=true|icon=information-variant-circle|text="
    "'''在非标准模式下，一些特殊收藏品可能会通过坎诺特的商店以源石锭标价出售'''，"
    "此时：\n"
    "* '''低稀有度'''收藏品售价8源石锭\n"
    "* {{color|#2ac5c9|'''中稀有度'''}}收藏品售价12源石锭\n"
    "* {{color|#7d0022|'''高稀有度'''}}收藏品售价16源石锭\n"
    "若无特殊说明，下列的“商店售价”为不受收藏品和对应主题下负面效果等影响时的"
    "基础售价<br>部分收藏品的稀有度在不同主题中会发生变化，本表格模板标题使用的"
    "收藏品稀有度默认为'''当期主题'''下的稀有度，关于不同主题下的稀有度，"
    "请您以对应主题下的“售价”为准}}\n"
    "{{Cbox2|mdi=true|icon=information-variant-circle|text="
    "本表格中“主题”一栏中存在部分通用角标以展示部分不便在表格中标注的信息，"
    "以下是部分角标：<br>"
    '<span style="background:#2f2f2f;color:white;padding:0px 5px;'
    "border: 1px solid #ffffff85;border-radius:2px;"
    '">{{mdi|alpha-x-box-outline}}</span> '
    "标志表示收藏品为【内容拓展·X】加入的收藏品<br/>"
    "'''{{模板:收藏品/角标|notrade}}''' 标志表示收藏品不可在【失与得】节点被交换出去。"
    "<br/>'''{{模板:收藏品/角标|stack}}''' 标志表示收藏品拥有计数机制，"
    "会对其对应条件进行计数。在查看已持有收藏品时会显示目前其已叠加的层数。"
    "<br/>'''{{模板:收藏品/角标|oneoff}}''' 标志表示收藏品为一次性收藏品，"
    "其生效后即无法再次生效（查看收藏品时标记为'''已使用'''）<br>\n"
    "如果您想查看本页面会出现的所有角标，您应当查阅页面[[模板:收藏品/角标]]\n"
    "}}"
)
"""新建页面时放在模板前的两段说明,与现有收藏品页面一致。"""


# ----- 游戏数据 -----


@dataclass(frozen=True)
class RelicVariant:
    """收藏品在某个主题里的一个难度变体;没有难度变体时只有一个。"""

    difficulty: int
    """从哪个难度开始生效。"""
    item: RoguelikeGameItemData | RoguelikeItem


@dataclass(frozen=True)
class RelicTheme:
    """收藏品在某个主题里的数据。"""

    number: int
    """rogue_N 的 N;灰蕈为 0。"""
    name: str
    variants: list[RelicVariant]
    """按生效难度升序,第一个是基础版本。"""

    @property
    def rarity(self) -> int:
        return RARITIES[self.variants[0].item.rarity]


@dataclass
class Relic:
    """一个收藏品页面:同名收藏品在各主题里的数据。"""

    name: str
    themes: list[RelicTheme]
    """按 rogue 编号升序。"""

    @property
    def title(self) -> str:
        return PAGE_TITLES.get(self.name, self.name)

    @property
    def is_active_tool(self) -> bool:
        return self.themes[-1].variants[0].item.type == "ACTIVE_TOOL"

    @property
    def icon_id(self) -> str:
        """编号最新的主题里的图标;并列时取先出现的(基础版本)。"""
        icons = [v.item.icon_id for t in self.themes for v in t.variants]
        return max(filter(None, icons), key=lambda i: rogue_number(i) or 0, default="")


def clean(value: str | None) -> str:
    return (value or "").replace("\r\n", "\n").strip()


def wiki_text(value: str | None) -> str:
    """游戏文本转成能放进模板参数的 wikitext:转义 HTML 与模板/链接符号,换行转 <br/>。"""
    text = html.escape(clean(value), quote=True)
    for char in "|{}[]":
        text = text.replace(char, f"&#{ord(char)};")
    return text.replace("\n", "<br/>")


def rogue_number(identifier: str) -> int | None:
    """``rogue_3`` / ``rogue_3_relic_xxx`` → 3;不是这种格式时为 None。"""
    match = re.match(r"rogue_(\d+)(?:_|$)", identifier)
    return int(match[1]) if match else None


def theme_relics(detail: RoguelikeTopicDetail) -> dict[str, list[RelicVariant]]:
    """一个主题里的收藏品,按页面名分组;难度变体(xx-α 等)归到基础版本名下。"""
    items = {
        k: v
        for k, v in (detail.items or {}).items()
        if v.type in {"RELIC", "ACTIVE_TOOL"}
    }
    # 难度变体 id → (基础版本 id, 生效难度)
    upgrades: dict[str, tuple[str, int]] = {}
    for group in (detail.difficulty_upgrade_relic_groups or {}).values():
        members = sorted(group.relic_data or [], key=lambda m: m.equivalent_grade)
        base_id = members[0].relic_id if members else None
        for member in members:
            if base_id and member.relic_id:
                upgrades[member.relic_id] = (base_id, member.equivalent_grade)
    relics: dict[str, list[RelicVariant]] = {}
    for item_id, item in items.items():
        base_id, difficulty = upgrades.get(item_id, (item_id, 0))
        name = clean(items[base_id].name if base_id in items else None)
        if not name:
            logger.warning(f"收藏品 {item_id} 没有名称,跳过")
            continue
        variant = RelicVariant(difficulty, item)
        relics.setdefault(name, []).append(variant)
    for name, variants in list(relics.items()):
        variants.sort(key=lambda v: v.difficulty)
        difficulties = [v.difficulty for v in variants]
        if len(set(difficulties)) != len(difficulties):
            logger.warning(f"收藏品 {name} 在同一主题里重名或难度变体不明确,跳过")
            del relics[name]
    return relics


def collect_relics(
    topic_table: RoguelikeTopicTable, legacy_table: RoguelikeTable
) -> list[Relic]:
    """按名称汇总各主题的收藏品;不同主题里的同名收藏品是同一个页面。"""
    relics: dict[str, Relic] = {}
    if legacy_table.item_table:
        for item in (legacy_table.item_table.items or {}).values():
            if item.type != "RELIC" or item.rarity == "BORN":
                continue
            name = clean(item.name)
            relics[name] = Relic(
                name, [RelicTheme(0, LEGACY_THEME, [RelicVariant(0, item)])]
            )
    for topic_id, topic in (topic_table.topics or {}).items():
        number = rogue_number(topic_id)
        detail = (topic_table.details or {}).get(topic_id)
        if number is None or not topic.name or detail is None:
            raise ValueError(f"无法识别的集成战略主题:{topic_id}")
        for name, variants in theme_relics(detail).items():
            relic = relics.setdefault(name, Relic(name, []))
            relic.themes.append(RelicTheme(number, topic.name, variants))
    for relic in relics.values():
        relic.themes.sort(key=lambda theme: theme.number)
    return list(relics.values())


# ----- 渲染 -----


def variant_text(
    variants: list[RelicVariant], values: list[str], *, by_difficulty: bool
) -> str:
    """把各难度变体的同一字段合成一个参数值。

    ``by_difficulty`` 时逐个变体标出生效难度,否则相同的内容只保留一份。
    """
    if not any(values):
        return ""
    if not by_difficulty or len(variants) == 1:
        return "<br/><br/>".join(wiki_text(v) for v in dict.fromkeys(values) if v)
    return "<br/>".join(
        inline_template("color", "#d800db", f"难度{variant.difficulty}及以上生效：")
        + (wiki_text(value) or "－")
        for variant, value in zip(variants, values, strict=True)
    )


def header_fields(relic: Relic) -> dict[str, str]:
    """模板头部取最新主题的数据;描述只取原表 description,不追加效果术语解释。"""
    latest = relic.themes[-1]
    descriptions = [clean(v.item.description) for v in latest.variants]
    fields = {
        "名称": wiki_text(relic.name),
        "iconId": relic.icon_id,
        "稀有度": str(latest.rarity),
        "描述": variant_text(latest.variants, descriptions, by_difficulty=False),
    }
    if relic.is_active_tool:
        fields["类型"] = "支援装备"
    return fields


def theme_fields(theme: RelicTheme, index: int) -> dict[str, str]:
    """页面上第 ``index`` 个主题的字段;角标留给人工填写。"""
    items = [variant.item for variant in theme.variants]
    base = items[0]
    # 支援装备没有售价字段,不套用普通收藏品的稀有度公式;价格由 wiki 人工补充。
    price = ""
    if base.type != "ACTIVE_TOOL":
        price = str(
            base.value if isinstance(base, RoguelikeItem) else (theme.rarity + 2) * 4
        )
    usage = [clean(item.usage) for item in items]
    obtain = [clean(item.obtain_approach) for item in items]
    obtain = ["" if text == GENERIC_OBTAIN else text for text in obtain]
    unlock = [clean(item.unlock_cond_desc) for item in items]
    return {
        f"主题{index}": wiki_text(theme.name),
        f"角标{index}": "",
        f"售价{index}": price,
        f"效果{index}": variant_text(theme.variants, usage, by_difficulty=True),
        f"获取条件{index}": variant_text(
            theme.variants, obtain, by_difficulty=len(set(obtain)) > 1
        ),
        f"解锁条件{index}": variant_text(
            theme.variants, unlock, by_difficulty=len(set(unlock)) > 1
        ),
    }


def render_page(relic: Relic) -> str:
    template = WikiTemplate(TEMPLATE).add_all(header_fields(relic))
    for index, theme in enumerate(relic.themes, 1):
        template.add_all(theme_fields(theme, index))
    preamble = PREAMBLE
    if relic.is_active_tool:
        preamble = (
            "{{Cbox2|lv=2|mdi=true|icon=progress-question|"
            "title=这是一件{{color|#a77d21|支援装备}}。|"
            "text=本页记录[[集成战略]]支援装备在各主题中的效果。}}\n" + PREAMBLE
        )
    return f"{preamble}\n\n{template}\n"


# ----- 合并到已有页面 -----


class MergeError(ValueError):
    """页面结构拿不准,需要人工处理。"""


OPAQUE_TAG = re.compile(r"<(nowiki|pre|source|syntaxhighlight|math|ref)\b[^>]*>", re.I)
"""内容不按 wikitext 解析的标签,里面的括号和竖线不算数。"""


def scan(text: str) -> tuple[list[tuple[int, int]], list[int], list[int]]:
    """找出顶层模板调用的范围,以及不在模板、链接里的 ``|`` 与 ``=`` 的位置。

    只处理收藏品页面会用到的语法:注释、nowiki 一类标签、模板、模板参数、
    内部链接;遇到拿不准的写法抛 MergeError。
    """
    stack: list[tuple[str, int]] = []
    links = 0
    spans: list[tuple[int, int]] = []
    pipes: list[int] = []
    equals: list[int] = []
    i = 0
    while i < len(text):
        if text.startswith("<!--", i):
            end = text.find("-->", i + 4)
            if end < 0:
                raise MergeError("有未闭合的注释")
            i = end + 3
            continue
        if tag := OPAQUE_TAG.match(text, i):
            if tag.group().endswith("/>"):
                i = tag.end()
                continue
            close = re.compile(rf"</{tag[1]}\s*>", re.I).search(text, tag.end())
            if not close:
                raise MergeError(f"有未闭合的 <{tag[1]}> 标签")
            i = close.end()
            continue
        if text.startswith("{{{{", i):
            raise MergeError("有连续四个以上的 {,需要完整的 MediaWiki 解析器")
        if text.startswith("{{{", i):
            stack.append(("argument", i))
            i += 3
            continue
        if text.startswith("{{", i):
            stack.append(("template", i))
            i += 2
            continue
        if stack and text.startswith("}}}" if stack[-1][0] == "argument" else "}}", i):
            kind, start = stack.pop()
            i += 3 if kind == "argument" else 2
            if not stack and kind == "template" and not links:
                spans.append((start, i))
            continue
        if text.startswith("}}", i):
            raise MergeError("有多余的模板结束括号")
        if text.startswith("[[", i):
            links += 1
            i += 2
            continue
        if text.startswith("]]", i):
            if not links:
                raise MergeError("有多余的链接结束括号")
            links -= 1
            i += 2
            continue
        if not stack and not links:
            if text[i] == "|":
                pipes.append(i)
            elif text[i] == "=":
                equals.append(i)
        i += 1
    if stack or links:
        raise MergeError("有未闭合的模板、模板参数或链接")
    return spans, pipes, equals


@dataclass(frozen=True)
class Parameter:
    """{{收藏品/common}} 的一个命名参数;偏移量相对整个页面。"""

    start: int
    """参数前 ``|`` 的位置。"""
    value_start: int
    value_end: int
    """到下一个 ``|`` 或模板结尾为止,包含值前后的空白。"""
    raw: str

    @property
    def value(self) -> str:
        return self.raw.strip()


@dataclass(frozen=True)
class CommonCall:
    """页面上唯一的 {{收藏品/common}} 调用。"""

    end: int
    """结尾 ``}}`` 的位置。"""
    params: dict[str, Parameter]


def find_common(text: str) -> CommonCall:
    spans, _, _ = scan(text)
    calls: list[CommonCall] = []
    for start, end in spans:
        offset = start + 2
        inner = text[offset : end - 2]
        _, pipes, _ = scan(inner)
        name = inner[: pipes[0] if pipes else len(inner)].strip().replace("_", " ")
        name = re.sub(r"^(?:模板|template)\s*:\s*", "", name, flags=re.I)
        if name.casefold() != TEMPLATE.casefold():
            continue
        params: dict[str, Parameter] = {}
        for left, right in pairwise([*pipes, len(inner)]):
            part = inner[left + 1 : right]
            _, _, equals = scan(part)
            if not equals:
                if part.strip():
                    raise MergeError(f"{TEMPLATE} 里有未命名参数")
                continue
            key = part[: equals[0]].strip()
            if not key or key in params:
                raise MergeError(f"{TEMPLATE} 的参数名为空或重复:{key}")
            if any(char in key for char in "{}[]<>\n"):
                raise MergeError(f"{TEMPLATE} 的参数名里有模板或注释,无法判断归属")
            value_start = offset + left + 1 + equals[0] + 1
            value_end = offset + right
            params[key] = Parameter(
                offset + left, value_start, value_end, text[value_start:value_end]
            )
        calls.append(CommonCall(end - 2, params))
    if not calls:
        raise MergeError("页面已存在但不是收藏品页面,需要人工建立消歧义页")
    if len(calls) > 1:
        raise MergeError(f"页面上有 {len(calls)} 个 {TEMPLATE}")
    return calls[0]


def theme_identity(value: str) -> str:
    """主题名去掉加粗与链接,用来和游戏数据比较,不改动页面上的写法。"""
    value = value.strip()
    if len(value) >= 6 and value.startswith("'''") and value.endswith("'''"):
        value = value[3:-3].strip()
    link = re.fullmatch(r"\[\[([^\[\]|]+)(?:\|[^\[\]]*)?\]\]", value)
    return (link[1] if link else value).strip()


def page_themes(params: dict[str, Parameter]) -> list[str]:
    """页面上已有的主题名,按编号排列。"""
    themes = {
        int(key[2:]): theme_identity(param.value)
        for key, param in params.items()
        if re.fullmatch(r"主题[1-9]\d*", key)
    }
    names = [themes[number] for number in sorted(themes)]
    if sorted(themes) != list(range(1, len(themes) + 1)):
        raise MergeError("页面上的主题编号不是从 1 连续编号")
    if not all(names) or len(set(names)) != len(names):
        raise MergeError("页面上的主题名为空或重复")
    for key in params:
        match = THEME_FIELD.match(key)
        if match and int(match[1]) > len(themes):
            raise MergeError(f"参数 {key} 没有对应的主题")
    return names


def replace_value(raw: str, value: str) -> str:
    """换掉参数值,保留原来值前后的空白(通常是换行)。"""
    if not raw.strip():
        return value + raw
    leading = raw[: len(raw) - len(raw.lstrip())]
    trailing = raw[len(raw.rstrip()) :]
    return leading + value + trailing


def merge_page(text: str, relic: Relic) -> str:
    """把游戏数据合并进已有页面,返回新正文;与原文相同表示不需要编辑。"""
    call = find_common(text)
    params = call.params
    live = page_themes(params)
    names = [clean(theme.name) for theme in relic.themes]

    page_theme = rogue_number(params["iconId"].value) if "iconId" in params else None
    if page_theme is not None and page_theme > relic.themes[-1].number:
        raise MergeError("页面 iconId 所在的主题比游戏数据还新,数据源可能落后")
    if unknown := [name for name in live if name not in names]:
        raise MergeError(f"页面上的主题与游戏数据对不上:{'、'.join(unknown)}")
    order = [names.index(name) for name in live]
    missing = [index for index, name in enumerate(names) if name not in live]
    if order != sorted(order):
        raise MergeError("页面上的主题顺序与游戏数据不一致")

    edits: list[tuple[int, int, str]] = []
    header = header_fields(relic)
    absent = []
    for key in REFRESHED_FIELDS:
        param = params.get(key)
        if param is None:
            absent.append(f"|{key}={header[key]}\n")
        elif param.value != header[key]:
            value = replace_value(param.raw, header[key])
            edits.append((param.value_start, param.value_end, value))
    if absent:
        first = min((param.start for param in params.values()), default=call.end)
        edits.append((first, first, "".join(absent)))
    if missing:
        # 只改已有参数的编号,保留值、注释和空白。
        theme_params: dict[int, list[Parameter]] = {}
        for key, param in params.items():
            if match := THEME_FIELD.fullmatch(key):
                old = int(match[1])
                theme_params.setdefault(old, []).append(param)
                new = order[old - 1] + 1
                if new != old:
                    prefix = text[param.start : param.value_start]
                    prefix = re.sub(r"\d+(\s*=)$", rf"{new}\g<1>", prefix)
                    edits.append((param.start, param.value_start, prefix))
        insertions: dict[int, str] = {}
        for source in missing:
            following = next((i + 1 for i, n in enumerate(order) if n > source), None)
            at = (
                min(p.start for p in theme_params[following])
                if following is not None
                else max(
                    (p.value_end for group in theme_params.values() for p in group),
                    default=call.end,
                )
            )
            block = "".join(
                f"|{key}={value}\n"
                for key, value in theme_fields(relic.themes[source], source + 1).items()
            )
            insertions[at] = insertions.get(at, "") + block
        for at, block in insertions.items():
            edits.append((at, at, block if text[:at].endswith("\n") else "\n" + block))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


# ----- job -----


def valid_title(name: str) -> bool:
    return not re.search(r"[#<>\[\]{}|:]", name)


@job
async def run(
    wiki: Wiki, topic_table: RoguelikeTopicTable, legacy_table: RoguelikeTable
) -> None:
    relics = collect_relics(topic_table, legacy_table)
    if invalid := [relic.name for relic in relics if not valid_title(relic.name)]:
        logger.warning(f"收藏品名不能直接作为页面标题,跳过:{'、'.join(invalid)}")
        relics = [relic for relic in relics if valid_title(relic.name)]
    if crowded := [relic.name for relic in relics if len(relic.themes) > MAX_THEMES]:
        logger.warning(
            f"{len(crowded)} 个收藏品超过 {TEMPLATE} 支持的 {MAX_THEMES} 个主题,"
            f"需要先扩展模板:{'、'.join(crowded)}"
        )

    pages = await wiki.read_revisions(relic.title for relic in relics)
    created = updated = 0
    for relic in relics:
        page = pages.get(relic.title)
        if page is None:
            await wiki.edit(
                title=relic.title,
                text=render_page(relic),
                summary="init",
                createonly=True,
            )
            created += 1
            continue
        try:
            if page.redirect:
                raise MergeError("页面是重定向")
            if page.contentmodel != "wikitext":
                raise MergeError(f"页面内容模型是 {page.contentmodel}")
            text = merge_page(page.text, relic)
        except MergeError as e:
            logger.warning(f"收藏品页面 {page.title} 未处理:{e}")
            continue
        if text == page.text:
            continue
        try:
            await wiki.edit(
                title=page.title,
                text=text,
                summary="update",
                nocreate=True,
                basetimestamp=page.timestamp,
                starttimestamp=page.starttimestamp,
            )
        except WikiError as e:
            if e.code not in {"editconflict", "pagedeleted", "missingtitle"}:
                raise
            logger.warning(f"收藏品页面 {page.title} 读取后被改动或删除,下次运行再合并")
            continue
        updated += 1
    logger.info(f"收藏品页面:新建 {created} 个,更新 {updated} 个")

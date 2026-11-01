"""敌人页面:按敌人图鉴与 enemy_database 建页,并维护 ``敌人一览/数据``。"""

import bisect
import json
import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Annotated, Any

from ptilopsis.gamedata.enemy_database import (
    EnemyDatabaseAttributesData,
    EnemyDatabaseEnemyData,
    EnemyDatabaseEnemyLevel,
    UndefinableBool,
    UndefinableFloat,
    UndefinableInt,
    UndefinableStr,
)
from ptilopsis.gamedata.enemy_handbook_table import (
    EnemyHandBookData,
    EnemyHandBookDataAbilty,
    EnemyHandBookDataGroup,
    EnemyHandbookLevelInfoData,
    EnemyHandbookLevelInfoDataRangePair,
)
from ptilopsis.jobs.params import (
    EnemyHandbookTable,
    EnemyLevels,
    RichText,
    RichTextHtml,
    category,
)
from ptilopsis.log import logger
from ptilopsis.utils import richtext
from ptilopsis.utils.job import job
from ptilopsis.utils.wiki import PAGE_PROTECTIONS, Wiki

EnemyPages = Annotated[list[str], category("分类:敌人")]
"""wiki ``分类:敌人`` 下的页面名。"""

ENEMY_LEVEL_NAMES = {"NORMAL": "普通", "ELITE": "精英", "BOSS": "领袖"}
MOTION_NAMES = {"FLY": "飞行", "WALK": "地面"}
APPLY_WAY_NAMES = {
    "ALL": "近战 远程",
    "RANGED": "远程",
    "MELEE": "近战",
    "NONE": "不攻击",
}
DAMAGE_TYPE_NAMES = {
    "PHYSIC": "物理",
    "MAGIC": "法术",
    "NO_DAMAGE": "无",
    "HEAL": "治疗",
}
SP_TYPE_NAMES = {
    "INCREASE_WITH_TIME": "自动回复",
    "INCREASE_WHEN_ATTACK": "攻击回复",
    "INCREASE_WHEN_TAKEN_DAMAGE": "受击回复",
}

# 参与图鉴等级评定的属性(EnemyDatabaseAttributesData 的字段名),
# 顺序即 LevelSummary.attributes 的下标
CLASS_LEVEL_ATTRIBUTES = (
    "max_hp",
    "atk",
    "def_",
    "magic_resistance",
    "move_speed",
    "base_attack_time",
    "ep_resistance",
    "ep_damage_resistance",
)

# 级别页里逐项列出的属性:(字段名, 模板参数名, 值的写法)
LEVEL_ATTRIBUTE_ROWS: tuple[tuple[str, str, str], ...] = (
    ("max_hp", "最大生命值", "i"),
    ("atk", "攻击力", "i"),
    ("def_", "防御力", "i"),
    ("magic_resistance", "法术抗性", "i"),
    ("move_speed", "移动速度", "f"),
    ("attack_speed", "攻击速度", "i"),
    ("base_attack_time", "攻击间隔", "f"),
    ("hp_recovery_per_sec", "生命恢复速度", "i"),
    ("sp_recovery_per_sec", "sp恢复速度", "i"),
    ("mass_level", "重量等级", "i"),
    ("ep_resistance", "损伤抵抗", "i"),
    ("ep_damage_resistance", "元素抗性", "i"),
    ("taunt_level", "基础嘲讽等级", "i"),
    ("stun_immune", "眩晕抗性", "b"),
    ("silence_immune", "沉默抗性", "b"),
    ("sleep_immune", "沉睡抗性", "b"),
    ("frozen_immune", "冻结抗性", "b"),
    ("levitate_immune", "浮空抗性", "b"),
    ("disarmed_combat_immune", "战栗抗性", "b"),
    ("feared_immune", "恐惧抗性", "b"),
    ("palsy_immune", "麻痹抗性", "b"),
    ("attract_immune", "诱导抗性", "b"),
    ("teleport_immune", "传送抗性", "b"),
    ("ground_bound_immune", "缚地抗性", "b"),
)

INDEXED_PAGE_ENEMIES = frozenset({"DC3", "HI02", "STU2", "OB19"})
"""和别的敌人重名、页面名后面加上 ``(enemyIndex)`` 的图鉴条目。

如 OB19 的 enemy_10262_dsjred 和 GAB 的 enemy_10128_fearpj 都叫“惘核”,
它的页面是 ``“惘核”(OB19)``。页面里的 ``|名称=`` 仍是原名。
"""

PAGE_TITLE_OVERRIDES: dict[str, str] = {
    "enemy_1602_blksnk2": "不死的黑蛇(第二形态)",
    "enemy_1603_hlystp2": "最后的圣愚(第二形态)",
}
"""enemy_id → 页面名。和别的敌人同名同 enemyIndex、要单独建页的图鉴条目。

页面里的 ``|名称=`` 仍是原名。
"""

Undefinable = UndefinableStr | UndefinableInt | UndefinableFloat | UndefinableBool
"""enemy_database 里"可能没定义"的一项属性。"""


def _lookup(names: dict[str, str], key: str | None, default: str) -> str:
    return names.get(key, default) if key is not None else default


def page_title(enemy: EnemyHandBookData) -> str:
    """敌人页面的标题:一般是图鉴名,重名条目后面加 ``(enemyIndex)``。

    ``PAGE_TITLE_OVERRIDES`` 里的条目直接用其中的页面名。
    """

    if enemy.enemy_id in PAGE_TITLE_OVERRIDES:
        return PAGE_TITLE_OVERRIDES[enemy.enemy_id]
    name = (enemy.name or "").strip()
    if enemy.enemy_index in INDEXED_PAGE_ENEMIES:
        return f"{name}({enemy.enemy_index})"
    return name


def race_name_table(handbook: EnemyHandBookDataGroup) -> dict[str, str]:
    """种类标签 id → 图鉴里的种类名。"""

    return {
        race.id: race.race_name
        for race in (handbook.race_data or {}).values()
        if race.id is not None and race.race_name is not None
    }


def damage_type_names(enemy: EnemyHandBookData) -> str:
    return " ".join(DAMAGE_TYPE_NAMES.get(x, "未知") for x in enemy.damage_type or [])


def get_value(
    idx: int, v: Undefinable | None, name: str, kind: str, rts: richtext.RichText
) -> str:
    """级别 ``idx`` 的一项属性,写成 ``\\n|name=值``。

    级别 0 总是输出(没定义时填默认值),更高级别只输出本级定义了的项;
    ``kind`` 为 s / i / f / b,决定值怎么写。
    """

    if v is None or not v.m_defined:
        if idx != 0:
            return ""
        s = {"i": "0", "f": "0.0", "s": "", "b": "无"}.get(kind, "")
        if name == "攻击范围半径":
            s = ""
        if name == "攻击速度":
            s = "100"
        if name == "数量":
            s = "1"
        return f"\n|{name}={s}"

    value = v.m_value
    s = ""
    if kind == "s":
        s = rts.compile(value) if isinstance(value, str) else ""
    elif kind == "i" and isinstance(value, int | float) and value >= 0:
        s = str(int(value) if value == int(value) else value)
    elif kind == "f" and isinstance(value, int | float) and value >= 0:
        s = str(value)
    elif kind == "b":
        s = "有" if value is True else "无"
    return f"\n|{name}={s}"


def format_ability_list(
    ability_list: list[EnemyHandBookDataAbilty] | None,
    rts: richtext.RichText,
    html: bool = False,
) -> str:
    """图鉴里的能力列表:每条按 textFormat 加前缀 / 标色,``<br>`` 分隔。"""

    if not ability_list:
        return ""
    a_content = ""
    for ability in ability_list:
        text = rts.compile(ability.text)
        if ability.text_format == "NORMAL":
            a_content += "·" + text + "<br>"
        elif ability.text_format == "SILENCE":
            a_content += "※" + text + "<br>"
        elif ability.text_format == "TITLE":
            if html:
                a_content += '<span style="color:#FF4F0B">' + text + "</span><br>"
            else:
                a_content += "{{color|#FF4F0B|" + text + "}}<br>"
        else:
            a_content += text + "<br>"
    return a_content[:-4]


def _range_min(pair: EnemyHandbookLevelInfoDataRangePair | None) -> float:
    return pair.min if pair is not None else 0.0


class ClassLevel:
    """按图鉴 levelInfoList 各档的下限,把数值换算成图鉴里的等级字母。"""

    def __init__(self, level_info_list: list[EnemyHandbookLevelInfoData]) -> None:
        self.attack: list[float] = []
        self.defence: list[float] = []
        self.magic_res: list[float] = []
        self.max_hp: list[float] = []
        self.move_speed: list[float] = []
        self.base_attack_time: list[float] = []
        self.ep_res: list[float] = []
        self.ep_damage_res: list[float] = []
        self.level: list[str | None] = []
        # 默认YJ给的数据按序排列
        for info in reversed(level_info_list):
            self.attack.append(_range_min(info.attack))
            self.defence.append(_range_min(info.def_))
            self.magic_res.append(_range_min(info.magic_res))
            self.max_hp.append(_range_min(info.max_hp))
            self.move_speed.append(_range_min(info.move_speed))
            self.base_attack_time.append(_range_min(info.attack_speed))
            self.ep_res.append(_range_min(info.enemy_res))
            self.ep_damage_res.append(_range_min(info.enemy_damage_res))
            self.level.append(info.class_level)
        self.base_attack_time = list(reversed(self.base_attack_time))

    def get_attack(self, target_attack: float) -> str | None:
        return self.level[max(1, bisect.bisect_right(self.attack, target_attack)) - 1]

    def get_def(self, target_def: float) -> str | None:
        return self.level[max(1, bisect.bisect_right(self.defence, target_def)) - 1]

    def get_magic_res(self, target_magic_res: float) -> str | None:
        return self.level[
            max(1, bisect.bisect_right(self.magic_res, target_magic_res)) - 1
        ]

    def get_max_hp(self, target_max_hp: float) -> str | None:
        return self.level[max(1, bisect.bisect_right(self.max_hp, target_max_hp)) - 1]

    def get_move_speed(self, target_move_speed: float) -> str | None:
        return self.level[
            max(1, bisect.bisect_right(self.move_speed, target_move_speed)) - 1
        ]

    def get_base_attack_time(self, target_base_attack_time: float) -> str | None:
        if target_base_attack_time < 0:
            return self.level[
                len(self.level) - bisect.bisect_right(self.base_attack_time, 1.0)
            ]
        return self.level[
            len(self.level)
            - bisect.bisect_right(self.base_attack_time, target_base_attack_time)
        ]

    def get_enemy_damage_res(self, target_enemy_damage_res: float) -> str | None:
        return self.level[
            max(1, bisect.bisect_right(self.ep_damage_res, target_enemy_damage_res)) - 1
        ]

    def get_enemy_res(self, target_enemy_res: float) -> str | None:
        return self.level[
            max(1, bisect.bisect_right(self.ep_res, target_enemy_res)) - 1
        ]


def iter_levels(
    levels: list[EnemyDatabaseEnemyLevel], enemy_name: str | None
) -> Iterator[tuple[int, EnemyDatabaseEnemyData]]:
    """按顺序产出 ``(级别序号, 该级别数据)``;序号对不上或缺数据的条目记日志后跳过。"""

    for idx, level in enumerate(levels):
        if level.level != idx or level.enemy_data is None:
            logger.info(f"enemy {enemy_name} database order error.")
            continue
        yield idx, level.enemy_data


@dataclass
class LevelSummary:
    """各级别数据的汇总:等级评定用的属性首次定义的值、攻击 / 行动方式、种类标签。"""

    attributes: list[float] = field(default_factory=lambda: [-1.0] * 8)
    """按 CLASS_LEVEL_ATTRIBUTES 的顺序,-1 表示各级别都没定义。"""
    apply_way: str | None = None
    motion: str | None = None
    race_tags: set[str] = field(default_factory=set)


def summarize_levels(
    levels: list[EnemyDatabaseEnemyLevel], enemy_name: str | None
) -> LevelSummary:
    summary = LevelSummary()
    for _, lv in iter_levels(levels, enemy_name):
        attributes = lv.attributes or EnemyDatabaseAttributesData()
        for i, field_name in enumerate(CLASS_LEVEL_ATTRIBUTES):
            attr: UndefinableInt | UndefinableFloat | None = getattr(
                attributes, field_name
            )
            if attr is not None and attr.m_defined and summary.attributes[i] == -1:
                summary.attributes[i] = attr.m_value
        if lv.apply_way is not None and lv.apply_way.m_defined:
            if summary.apply_way is None:
                summary.apply_way = lv.apply_way.m_value
        if lv.motion is not None and lv.motion.m_defined:
            if summary.motion is None:
                summary.motion = lv.motion.m_value
        tags = lv.enemy_tags
        if tags is not None and tags.m_defined and tags.m_value:
            summary.race_tags.update(tags.m_value)
    return summary


def level_section(
    idx: int,
    lv: EnemyDatabaseEnemyData,
    rts: richtext.RichText,
    race_names: dict[str, str],
) -> str:
    """``==级别idx==`` 一节,内容是 ``{{敌人信息/levelcontent}}`` 模板。"""

    content = f"\n==级别{idx}=="
    content += f"\n{{{{敌人信息/levelcontent\n|index={idx}"
    content += get_value(idx, lv.name, "名称", "s", rts)
    if lv.level_type is not None and lv.level_type.m_defined:
        content += f"\n|地位={ENEMY_LEVEL_NAMES.get(lv.level_type.m_value, '普通')}"
    elif idx == 0:
        content += "\n|地位=普通"
    tags = lv.enemy_tags
    if tags is not None and tags.m_defined and tags.m_value is not None:
        content += "\n|种类=" + ",".join(
            race_names.get(r, "未知") for r in tags.m_value
        )
    content += get_value(idx, lv.description, "描述", "s", rts)
    if lv.apply_way is not None and lv.apply_way.m_defined:
        content += f"\n|攻击方式={APPLY_WAY_NAMES.get(lv.apply_way.m_value, '未知')}"
    elif idx == 0:
        content += "\n|攻击方式=未知"
    if lv.motion is not None and lv.motion.m_defined:
        content += f"\n|行动方式={MOTION_NAMES.get(lv.motion.m_value, '地面')}"
    elif idx == 0:
        content += "\n|行动方式=地面"
    content += get_value(idx, lv.life_point_reduce, "数量", "i", rts)
    content += get_value(idx, lv.range_radius, "攻击范围半径", "f", rts)
    attributes = lv.attributes or EnemyDatabaseAttributesData()
    for field_name, param, kind in LEVEL_ATTRIBUTE_ROWS:
        content += get_value(idx, getattr(attributes, field_name), param, kind, rts)
    if lv.sp_data is not None:
        sp = lv.sp_data
        content += f"\n|初始技力={sp.init_sp}"
        content += f"\n|技力上限={sp.max_sp}"
        content += f"\n|技力槽回复类型={SP_TYPE_NAMES.get(sp.sp_type, '')}"
        content += f"\n|技力回复速度={sp.increment}"
    if lv.talent_blackboard:
        # 天赋黑板原样(key / value / valueStr)写进注释,供页面脚本读取
        blackboard = [pair.model_dump(by_alias=True) for pair in lv.talent_blackboard]
        dumped = json.dumps(blackboard, indent=4, ensure_ascii=False)
        content += f"\n|天赋=<!--{dumped}-->"
    content += "\n}}"
    return content


def linked_enemy_links(
    link_ids: list[str],
    enemy_data_table: dict[str, EnemyHandBookData],
    enemy_levels: dict[str, list[EnemyDatabaseEnemyLevel]],
) -> list[str]:
    """相关敌人的 ``[[名称]]``。

    优先用图鉴名;图鉴里没有的敌人取 enemy_database 级别 0 的名字。
    """

    links = []
    for link_id in link_ids:
        handbook = enemy_data_table.get(link_id)
        if handbook is not None:
            links.append(f"[[{(handbook.name or '').strip()}]]")
            continue
        levels = enemy_levels.get(link_id)
        if not levels or levels[0].enemy_data is None:
            continue
        name = levels[0].enemy_data.name
        if name is not None and name.m_value is not None:
            links.append(f"[[{name.m_value.strip()}]]")
    return links


@job
async def run(
    wiki: Wiki,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    rts: RichText,
    enemy_pages: EnemyPages,
) -> None:
    """给图鉴里尚未建页的敌人建页(正文与 /spine)并加保护。"""

    existing = {page.replace("(敌方)", "") for page in enemy_pages}
    enemy_data_table = enemy_handbook_table.enemy_data or {}
    race_names = race_name_table(enemy_handbook_table)

    for enemy in enemy_data_table.values():
        name = (enemy.name or "").strip()
        title = page_title(enemy)
        if title in existing or name == "-" or enemy.hide_in_handbook:
            continue

        # 先分析database中数据
        levels = enemy_levels.get(enemy.enemy_id, []) if enemy.enemy_id else []
        summary = summarize_levels(levels, name)
        content_lv = "".join(
            level_section(idx, lv, rts, race_names)
            for idx, lv in iter_levels(levels, name)
        )

        content = "{{Navigator|敌人一览}}\n{{敌人信息/common2"
        content += f"\n|id={enemy.sort_id}"
        content += f"\n|名称={name}"
        content += f"\n|index={enemy.enemy_index}"
        content += f"\n|地位级别={ENEMY_LEVEL_NAMES.get(enemy.enemy_level, '其他')}"
        content += f"\n|描述={rts.compile(enemy.description)}"
        content += f"\n|伤害类型={damage_type_names(enemy)}"
        content += f"\n|攻击方式={_lookup(APPLY_WAY_NAMES, summary.apply_way, '未知')}"
        content += f"\n|行动方式={_lookup(MOTION_NAMES, summary.motion, '地面')}"
        if summary.race_tags:
            content += "\n|种类=" + ",".join(
                race_names.get(r, "未知") for r in summary.race_tags
            )
        if enemy.ability_list:
            content += "\n|能力=" + format_ability_list(enemy.ability_list, rts)
        if enemy.link_enemies:
            links = linked_enemy_links(
                enemy.link_enemies, enemy_data_table, enemy_levels
            )
            content += "\n|相关敌人=" + ",".join(links)
        content += "\n}}"

        content += content_lv + "\n==敌人模型==\n{{spine}}<references/>{{敌人导航}}"

        spine_content = {
            "prefix": f"https://torappu.prts.wiki/assets/enemy_spine/{enemy.enemy_id}/",
            "name": name,
            "skin": {"默认": {"战斗": {"file": f"{enemy.enemy_id}"}}},
        }

        # 图鉴里可能有多个同名条目(如 KNT 的两个“坎诺特”),只按第一个建页
        existing.add(title)
        created = await wiki.create(
            title=title,
            text=content,
            summary="init",
            bot=None,
            minor=True,
            protections=PAGE_PROTECTIONS,
        )
        if not created:
            # 不在分类:敌人里却已存在,多半是重定向或同名的其它页面,要人工处理
            logger.warning(
                f"Page {title} ({enemy.enemy_id}) already exists but is not "
                "in 分类:敌人; skipped, resolve it manually and rerun"
            )
            continue
        await wiki.create(
            title=title + "/spine",
            text=json.dumps(spine_content, indent=4, ensure_ascii=False),
            summary="init",
            bot=None,
            minor=True,
            contentmodel="json",
            protections=PAGE_PROTECTIONS,
        )
        logger.info(f"Created: {title}.")


@job
async def update_data(
    wiki: Wiki,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    rts_html: RichTextHtml,
    enemy_pages: EnemyPages,
) -> None:
    """重写 ``敌人一览/数据``:每个敌人一条 JSON,给敌人一览页面的脚本用。"""

    override_list = [
        page.replace("(敌方)", "") for page in enemy_pages if "(敌方)" in page
    ]
    override_list2 = ["SD49", "SD47", "SD45"]

    race_names = race_name_table(enemy_handbook_table)
    level_standard = ClassLevel(enemy_handbook_table.level_info_list or [])
    new_enemy_table: list[dict[str, Any]] = []

    for enemy in (enemy_handbook_table.enemy_data or {}).values():
        if enemy.name is None or enemy.name == "-" or enemy.hide_in_handbook:
            continue

        levels = enemy_levels.get(enemy.enemy_id, []) if enemy.enemy_id else []
        summary = summarize_levels(levels, enemy.name)
        attrs = summary.attributes
        name = enemy.name.strip()
        new_data: dict[str, Any] = {
            "enemyIndex": enemy.enemy_index,
            "sortId": enemy.sort_id,
            "name": name,
            "enemyLink": name,
            "enemyRace": "其他",
            "enemyLevel": "",
            "attackType": _lookup(APPLY_WAY_NAMES, summary.apply_way, "未知"),
            "damageType": damage_type_names(enemy),
            "motion": _lookup(MOTION_NAMES, summary.motion, "未知"),
            "endure": level_standard.get_max_hp(attrs[0]),
            "attack": level_standard.get_attack(attrs[1]),
            "defence": level_standard.get_def(attrs[2]),
            "moveSpeed": level_standard.get_move_speed(attrs[4]),
            "attackSpeed": level_standard.get_base_attack_time(attrs[5]),
            "resistance": level_standard.get_magic_res(attrs[3]),
            "enemyRes": level_standard.get_enemy_res(attrs[6]),
            "enemyDamageRes": level_standard.get_enemy_damage_res(attrs[7]),
            "ability": "",
        }
        if enemy.invisible_detail:
            for key in (
                "endure",
                "attack",
                "defence",
                "moveSpeed",
                "attackSpeed",
                "resistance",
                "enemyRes",
                "enemyDamageRes",
            ):
                new_data[key] = "?"
        # 链接
        if new_data["enemyLink"] in override_list:
            new_data["enemyLink"] += "(敌方)"
        if new_data["enemyIndex"] in override_list2:
            new_data["enemyLink"] += "(我方)"
        if new_data["enemyIndex"] in INDEXED_PAGE_ENEMIES:
            new_data["enemyLink"] += f'({new_data["enemyIndex"]})'
        if enemy.enemy_id in PAGE_TITLE_OVERRIDES:
            new_data["enemyLink"] = PAGE_TITLE_OVERRIDES[enemy.enemy_id]
        # 种族
        if summary.race_tags:
            new_data["enemyRace"] = ",".join(
                race_names.get(r, "未知") for r in summary.race_tags
            )
        # 地位
        new_data["enemyLevel"] = ENEMY_LEVEL_NAMES.get(enemy.enemy_level, "其他")
        # 能力
        new_data["ability"] = format_ability_list(
            enemy.ability_list, rts_html, html=True
        )

        new_enemy_table.append(new_data)

    await wiki.edit(
        title="敌人一览/数据",
        text=json.dumps(new_enemy_table, ensure_ascii=False),
        summary="update",
    )
    logger.info("Updated: 敌人一览/数据.")


@job
def update_summary(
    enemy_handbook_table: EnemyHandbookTable, enemy_levels: EnemyLevels
) -> None:
    """(尚未实现)"""


@job
async def update_immune(
    wiki: Wiki,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    rts: RichText,
    enemy_pages: EnemyPages,
) -> None:
    """给已建页的敌人各级别补上后来新增的 ``战栗抗性`` 一项。"""

    page_titles = {page.replace("(敌方)", ""): page for page in enemy_pages}
    enemies = [
        (page_titles[enemy.name.strip()].strip(), enemy)
        for enemy in (enemy_handbook_table.enemy_data or {}).values()
        if enemy.name is not None and enemy.name != "-"
    ]
    # 一次性批量读取全部敌人页,再逐个比对、按需编辑
    texts = await wiki.read_many(title for title, _ in enemies)
    for title, enemy in enemies:
        old_page = texts[title]
        new_page = old_page

        levels = enemy_levels.get(enemy.enemy_id, []) if enemy.enemy_id else []
        for idx, lv in iter_levels(levels, enemy.name):
            lv_idx = new_page.find(f"==级别{idx}==")
            lv_idx2 = new_page.find(f"==级别{idx + 1}==")
            lv_piece = new_page[lv_idx:lv_idx2]
            immune = lv.attributes.disarmed_combat_immune if lv.attributes else None
            new_immune = get_value(idx, immune, "战栗抗性", "b", rts)
            if new_immune != "" and "|战栗抗性=" not in lv_piece:
                a = re.findall(r"(\|.*?抗性=.*?)\n", lv_piece)
                if a:
                    flag = lv_piece.find(a[-1]) + len(a[-1])
                    lv_piece = lv_piece[:flag] + new_immune + lv_piece[flag:]
                    new_page = new_page[:lv_idx] + lv_piece + new_page[lv_idx2:]

        if new_page != old_page:
            await wiki.edit(title=title, text=new_page, summary="更新抗性")
            # 多个敌人 ID 可能共用一个页面,后面的比对要基于这次改过的文本
            texts[title] = new_page
            logger.info(f"Updated: {enemy.name}.")

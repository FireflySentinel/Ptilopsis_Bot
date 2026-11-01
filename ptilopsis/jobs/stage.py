import copy
import json
import re
from collections.abc import Callable, Sequence
from typing import Annotated

from pydantic import BaseModel, ValidationError

from ptilopsis.gamedata import campaign_table as campaign_models
from ptilopsis.gamedata.activity_table import ActivityTable
from ptilopsis.gamedata.building_data import BuildingData
from ptilopsis.gamedata.campaign_table import CampaignTable
from ptilopsis.gamedata.character_table import CharacterData
from ptilopsis.gamedata.crisis_v2_table import RecalRuneStageData
from ptilopsis.gamedata.enemy_database import EnemyDatabaseEnemyLevel
from ptilopsis.gamedata.enemy_handbook_table import (
    EnemyHandBookData,
    EnemyHandBookDataGroup,
)
from ptilopsis.gamedata.handbook_info_table import HandbookStoryStageData
from ptilopsis.gamedata.item_table import InventoryData
from ptilopsis.gamedata.level_data import (
    BlackboardDataPair,
    EnemyDatabaseEnemyData,
    LegacyInLevelRuneData,
    LevelData,
    LevelDataEnemyDataDbReference,
    LevelDataOptions,
    LevelDataWaveDataFragmentDataActionData,
    UndefinableFloat,
    UndefinableInt,
    UndefinableStr,
)
from ptilopsis.gamedata.roguelike_topic_table import RoguelikeGameStageData
from ptilopsis.gamedata.sandbox_perm_table import SandboxV2StageData
from ptilopsis.gamedata.skill_table import SkillDataBundle
from ptilopsis.gamedata.stage_table import (
    StageData,
    StageDataDisplayDetailRewards,
    StageTable,
    TileAppendInfo,
)
from ptilopsis.gamedata.zone_table import ZoneTable
from ptilopsis.homepage import (
    NEW_STAGES_PAGE,
    render_new_stages,
    render_stage_list,
)
from ptilopsis.jobs.params import (
    BattleMiscTable,
    CharacterTable,
    CrisisV2Table,
    EnemyHandbookTable,
    EnemyLevels,
    HandbookInfoTable,
    ItemTable,
    LevelLoader,
    Levels,
    RichText,
    RoguelikeTopicTable,
    SandboxPermTable,
    SkillTable,
    StoryReviewMetaTable,
    table,
)
from ptilopsis.log import logger
from ptilopsis.utils.http import make_client
from ptilopsis.utils.job import job
from ptilopsis.utils.wiki import Wiki
from ptilopsis.wikitext import WikiTemplate, inline_template

# 关卡表与剿灭表各自生成了一份同名的 DisplayDetailRewards 模型,字段完全一致
DisplayDetailRewards = (
    StageDataDisplayDetailRewards | campaign_models.StageDataDisplayDetailRewards
)
EnemyTable = dict[str, EnemyHandBookData]
"""enemy_handbook_table 的 enemyData:敌人 id → 图鉴条目。"""
EnemyLevelIndex = dict[str, list[EnemyDatabaseEnemyLevel]]
"""enemy_database 按敌人 id 索引的各级别数据(即 params.EnemyLevels)。"""
NotCountList = dict[str, list[int]]
"""不计入敌人总数的敌人:id → 标记了 notCountInTotal 的 level 列表。"""


def _require[T](value: T | None, what: str = "field") -> T:
    """生成模型里 string / table 字段一律可空;取到 None 时按旧代码缺键的行为抛
    KeyError,由调用方原有的兜底接住,或者像以前一样让这一关失败。"""

    if value is None:
        raise KeyError(what)
    return value


# 渲染视图,字段与页面上的 wiki 模板参数一一对应


class DropView(BaseModel):
    name: str
    furniture: bool = False
    occurrence: str = ""


class RewardGroupView(BaseModel):
    label: str
    drops: list[DropView]


class LevelInfoView(BaseModel):
    character_limit: int
    initial_cost: int
    max_cost: int
    max_life_point: int
    enemy_count: str
    map_size: str
    time_label: str
    time: str


class BlackboardView(BaseModel):
    # 黑板值只会被 str() 进注释,类型放宽到上游可能出现的所有形态:
    # 收窄成 int | float 会让一条注释的降级变成整个 job 的 ValidationError
    key: str
    value: int | float | str | None
    value_str: str | None


class TileEffectView(BaseModel):
    name: str
    blackboards: list[list[BlackboardView]]


class SandboxMapView(BaseModel):
    code: str
    name: str
    stage_id: str


class BasicStageView(BaseModel):
    heading: str | None = None
    code: str
    name: str
    stage_id: str
    map_override: str = ""
    stage_type: str
    subtype: str | None = None
    boss: bool = False
    difficulty: str | None = None
    battle_stage: bool | None = None
    unlock_condition: str | None = None
    recommended_level: str | None = None
    zone: str | None = None
    level: LevelInfoView | None = None
    description: str | None = None
    ap_cost: int | None = None
    practice_cost: int | None = None
    resource_overview: list[str] | None = None
    action_cost: int | None = None
    power_cost: int | None = None
    rewards: list[RewardGroupView] = []
    tile_effects: list[TileEffectView] = []
    terrain_tags: list[str] | None = None
    sandbox_map: SandboxMapView | None = None


class AssaultStageView(BaseModel):
    heading: str
    code: str
    name: str
    stage_type: str
    subtype: str | None = None
    difficulty: str
    unlock_condition: str
    recommended_level: str | None = None
    zone: str
    character_limit: int
    initial_cost: int
    max_cost: int
    description: str
    ap_cost: int
    practice_cost: int
    rewards: list[RewardGroupView] = []
    intelligence: list[str] = []


class CampaignStageView(BaseModel):
    code: str
    name: str
    stage_id: str
    commission: bool
    stage_type: str
    difficulty: str
    unlock_condition: str
    zone: str
    level: LevelInfoView | None = None
    description: str
    ap_cost: int
    rewards: list[RewardGroupView] = []
    ap_returns: list[str] = []
    diamond_rewards: list[str] = []
    terrain_tags: list[str] | None = None


class EnemyOverrideView(BaseModel):
    label: str
    # 覆盖值原样进模板,构造时就 str() 掉:上游给什么类型都不会校验失败,
    # 且与重构前的 "{}".format(m_value) 逐字节一致(None 也渲染成 None)
    value: str


class EnemyView(BaseModel):
    index: int
    name: str
    count: str
    level: int
    display_name: str | None = None
    count_lower: str | None = None
    note: str | None = None
    overrides: list[EnemyOverrideView] = []


class SquadUnitView(BaseModel):
    name: str
    simulation: bool = False
    phase: int | str = ""
    level: int | str = ""
    skill_name: str = ""
    main_skill_level: int | str = ""
    potential: int | None = None


class SquadSectionView(BaseModel):
    title: str
    units: list[SquadUnitView]
    note: str


class CampaignProgressItemView(BaseModel):
    name: str
    count: int


class CampaignProgressRowView(BaseModel):
    kill_count: int
    items: list[CampaignProgressItemView]
    break_fee_add: int


class CampaignProgressView(BaseModel):
    rows: list[CampaignProgressRowView]


class NormalPageView(BaseModel):
    normal: BasicStageView
    assault: AssaultStageView | None = None
    enemies: list[EnemyView] | None = None
    squads: list[SquadSectionView] = []
    material_drop: bool = False


class CampaignPageView(BaseModel):
    stage: CampaignStageView
    enemies: list[EnemyView] | None = None
    squads: list[SquadSectionView] = []
    progress: CampaignProgressView


class RoguelikePageView(BaseModel):
    normal: BasicStageView
    assault: AssaultStageView | None = None
    enemies: list[EnemyView] | None = None
    see_also: tuple[str, str] | None = None
    """同名关卡的另一个页面:``(页面名, 说明)``,渲染成 {{参阅}}。"""


class BasicPageView(BaseModel):
    stage: BasicStageView
    enemies: list[EnemyView] | None = None
    squads: list[SquadSectionView] = []


class RecalRunePageView(BasicPageView):
    display_title: str


class DisambiguationLinkView(BaseModel):
    page_name: str
    activity_name: str | None = None


def parse_stage_type(stage_type):
    return {
        "MAIN": "主线",
        "SUB": "支线",
        "DAILY": "日常",
        "GUIDE": "教程",
        "ACTIVITY": "活动",
        "CAMPAIGN": "剿灭",
        "SPECIAL_STORY": "特殊剧情",
        "CLIMB_TOWER": "保全派驻",
    }.get(stage_type, "未知类型")


def parse_drop_type(drop_type):
    return {
        0: "None",
        1: "首次掉落",
        2: "常规掉落",
        3: "特殊掉落",
        4: "额外物资",
        5: "作战失败返回",
        6: "报酬",  # 剿灭给的合成玉
        7: "幸运掉落",  # 家具
        8: "三星获得",
        "NONE": "None",
        "ONCE": "首次掉落",
        "NORMAL": "常规掉落",
        "SPECIAL": "特殊掉落",
        "ADDITIONAL": "额外物资",
        "APRETURN": "作战失败返回",
        "DIAMOND_MATERIAL": "报酬",  # 剿灭给的合成玉
        "FUNITURE_DROP": "幸运掉落",  # 家具
        "COMPLETE": "三星获得",
    }.get(drop_type, "None")


def parse_occ_type(occ_percent, drop_type, if_furni):
    if if_furni:
        ex = ":2="
    else:
        ex = ":"
    if drop_type in [4, 6, 7] or drop_type in [
        "ADDITIONAL",
        "DIAMOND_MATERIAL",
        "FUNITURE_DROP",
    ]:
        return ""
    elif drop_type == 8 or drop_type == "COMPLETE":
        return ex + "三星获得"
    elif drop_type == 1 or drop_type == "ONCE":
        return ex + "首次掉落"
    else:
        return ex + {
            0: "固定掉落",  # Always
            1: "大概率",  # Almost
            2: "概率掉落",  # Usual
            3: "小概率",  # Often
            4: "罕见",  # Sometimes
            5: "从不",  # Never
            6: "完成",  # Complete
            "ALWAYS": "固定掉落",  # Always
            "ALMOST": "大概率",  # Almost
            "USUAL": "概率掉落",  # Usual
            "OFTEN": "小概率",  # Often
            "SOMETIMES": "罕见",  # Sometimes
            "NEVER": "从不",  # Never
            "DEFINITELY_BUFF": "完成",  # Complete
        }.get(occ_percent, "未知类型")


def parse_rune_profession(profession_mask):
    if profession_mask == 0:
        return "未知职业范围"
    p_list = bin(profession_mask)[2:]
    p_list = "0" * (10 - len(p_list)) + p_list
    p_text = []
    if p_list[0] == "1":
        p_text.append("先锋")
    if p_list[1] == "1":
        p_text.append("障碍物")
    if p_list[2] == "1":
        p_text.append("召唤物")
    if p_list[3] == "1":
        p_text.append("特种")
    if p_list[4] == "1":
        p_text.append("术师")
    if p_list[5] == "1":
        p_text.append("辅助")
    if p_list[6] == "1":
        p_text.append("医疗")
    if p_list[7] == "1":
        p_text.append("重装")
    if p_list[8] == "1":
        p_text.append("狙击")
    if p_list[9] == "1":
        p_text.append("近卫")
    return "和".join(p_text) + "干员"


def _profession_mask(rune: LegacyInLevelRuneData) -> int | str:
    """runes[].professionMask 在数据里多是职业位掩码整数,偶尔是单个职业的枚举名;
    生成模型把数字统一成了字符串,这里还原成整数,让 parse_rune_profession 照常工作。"""

    mask = rune.profession_mask
    return int(mask) if mask.isdigit() else mask


def build_rune_buffs(runes: list[LegacyInLevelRuneData]) -> tuple[int, list[str]]:
    """扫描 runes,取出部署位增减和敌方属性加成。

    返回 (部署上限增量, 情报行)。突袭和集成战略紧急作战两处都要这份结果。
    """

    climit = 0
    ebuff: dict[str | None, float] = {"atk": 1.0, "def": 1.0, "max_hp": 1.0, "flag": 0}
    for rune in runes:
        blackboard = rune.blackboard or []
        if rune.key in ["gbuff_placable_char_num", "global_placable_char_num_add"]:
            climit = int(blackboard[0].value)
        if rune.key in ["enemy_attribute_mul", "ebuff_attribute"]:
            ebuff["flag"] = 1
            for item in blackboard:
                ebuff[item.key] = item.value

    intelligence = []
    if ebuff["flag"] == 1:
        ebuff_desc = []
        if ebuff["atk"] != 1.0:
            ebuff_desc.append("攻击力提升至{:.0%}".format(ebuff["atk"]))
        if ebuff["def"] != 1.0:
            ebuff_desc.append("防御力提升至{:.0%}".format(ebuff["def"]))
        if ebuff["max_hp"] != 1.0:
            ebuff_desc.append("生命值提升至{:.0%}".format(ebuff["max_hp"]))
        if ebuff_desc:
            intelligence.append("敌方单位的" + "，".join(ebuff_desc))
        else:
            intelligence.append("敌方单位无变化")
    return climit, intelligence


def build_rune_lines(runes: list[LegacyInLevelRuneData]) -> list[str]:
    # 各枚举字段在模型里是成员名(NORMAL / MELEE …),不再需要兼容早期数据里的数字
    rune_lines = []
    for rune in runes:
        text = []
        if rune.difficulty_mask in ["FOUR_STAR", "SIX_STAR"]:  # 突袭
            pass
        elif rune.difficulty_mask == "NORMAL":  # 普通
            text.append("普通难度")
        elif rune.difficulty_mask == "EASY":  # 普通
            text.append("简单难度")
        elif rune.difficulty_mask == "NONE":  # 未知
            text.append("未知关卡难度")

        if rune.buildable_mask == "ALL":  # 全部单位
            pass
        elif rune.buildable_mask == "RANGED":  # 远程单位
            text.append("远程单位")
        elif rune.buildable_mask == "MELEE":  # 近战单位
            text.append("近战单位")
        elif rune.buildable_mask == "NONE":  # 未知
            text.append("未知单位")

        profession_mask = _profession_mask(rune)
        if profession_mask != 1023:
            if isinstance(profession_mask, int):
                text.append(parse_rune_profession(profession_mask))
            else:
                text.append(profession_mask)
        text.append(rune.key or "")

        blackboard = []
        for i in rune.blackboard or []:
            text2 = f"{i.key}: {i.value}"
            if i.value_str is not None:
                text2 += f" ({i.value_str})"
            blackboard.append(text2)

        rune_lines.append(" ".join(text) + ": " + ", ".join(blackboard))
    return rune_lines


def parse_drop_item(
    item_type: str,
    item_id: str | None,
    character_table: dict[str, CharacterData],
    building_data: BuildingData,
    item_table: InventoryData,
) -> str:
    """把掉落物的类型与 id 翻译成 wiki 上的显示名。

    关卡的 displayDetailRewards、回忆关卡的 rewardItem、剿灭进度奖励虽然是不同的
    模型,取字段这一步留给调用方,这里只认类型和 id。查不到(含名字为 null)时
    退化成 "物品<id>"。
    """

    try:
        item_id = _require(item_id, "id")
        if item_type == "CHAR":
            return _require(character_table[item_id].name, "name")
        if item_type == "FURN":
            custom_data = _require(building_data.custom_data, "customData")
            furnitures = _require(custom_data.furnitures, "furnitures")
            return _require(furnitures[item_id].name, "name")
        if item_type not in [
            "MATERIAL",
            "CARD_EXP",
            "TKT_RECRUIT",
            "GOLD",
            "ACTIVITY_COIN",
            "ACTIVITY_ITEM",
            "ET_STAGE",
            "DIAMOND",
            "DIAMOND_SHD",
            "LGG_SHD",
            "HGG_SHD",
        ]:
            logger.info(f"Unknown drop item {item_id}")
        items = _require(item_table.items, "items")
        return _require(items[item_id].name, "name").strip()
    except (AttributeError, KeyError, TypeError):
        return f"物品{item_id}"


def build_enemy_overrides(
    overwritten_data: EnemyDatabaseEnemyData,
) -> list[EnemyOverrideView]:
    attributes = overwritten_data.attributes
    fields: list[
        tuple[UndefinableStr | UndefinableInt | UndefinableFloat | None, str]
    ] = [
        (overwritten_data.name, "显示名"),
        (attributes.max_hp if attributes else None, "生命值"),
        (attributes.atk if attributes else None, "攻击力"),
        (attributes.def_ if attributes else None, "防御力"),
        (attributes.magic_resistance if attributes else None, "法术抗性"),
        (attributes.base_attack_time if attributes else None, "攻击间隔"),
        (attributes.mass_level if attributes else None, "重量等级"),
        (attributes.move_speed if attributes else None, "移动速度"),
        (attributes.hp_recovery_per_sec if attributes else None, "生命恢复速度"),
        (overwritten_data.range_radius, "攻击范围半径"),
        (overwritten_data.life_point_reduce, "目标价值"),
    ]
    overrides = []
    for value, label in fields:
        if value is not None and value.m_defined:
            overrides.append(EnemyOverrideView(label=label, value=str(value.m_value)))
    return overrides


def build_reward_groups(
    rewards: Sequence[DisplayDetailRewards],
    character_table: dict[str, CharacterData],
    building_data: BuildingData,
    item_table: InventoryData,
) -> list[RewardGroupView]:
    reward_list: dict[str, list[DropView]] = {
        "NONE": [],
        "ONCE": [],
        "NORMAL": [],
        "SPECIAL": [],
        "ADDITIONAL": [],
        "APRETURN": [],
        "DIAMOND_MATERIAL": [],
        "FUNITURE_DROP": [],
        "COMPLETE": [],
        "CHARM_DROP": [],
        "OVERRIDE_DROP": [],
        "ITEM_RETURN": [],
    }
    for reward in rewards:
        furniture = reward.type == "FURN"
        occurrence = parse_occ_type(reward.occ_percent, reward.drop_type, furniture)
        occurrence_prefix = ":2=" if furniture else ":"
        if occurrence.startswith(occurrence_prefix):
            occurrence = occurrence.removeprefix(occurrence_prefix)
        drop = DropView(
            name=parse_drop_item(
                reward.type, reward.id, character_table, building_data, item_table
            ),
            furniture=furniture,
            occurrence=occurrence,
        )
        if reward.drop_type not in reward_list:
            reward_list[reward.drop_type] = []
        reward_list[reward.drop_type].append(drop)
    reward_list["ONCE"] = reward_list["COMPLETE"] + reward_list["ONCE"]
    reward_list["COMPLETE"] = []

    groups = []
    for drop_type in reward_list:
        label = parse_drop_type(drop_type)
        drops = reward_list[drop_type]
        if drops and label != "None":
            group = RewardGroupView(label=label, drops=drops)
            groups.append(group)
            if drop_type == 2 or drop_type == "NORMAL":
                logger.info("\t—— " + render_reward_group(group))
    return groups


def analyze_action(
    actions: list[LevelDataWaveDataFragmentDataActionData],
    normal_hidden_group: list[str | None],
    not_count_list: NotCountList,
) -> tuple[float, int, int, bool]:
    action_list = [ActionInfo(action) for action in actions]
    pack_dict = {}
    for action in action_list:
        if action.random_key is not None and action.random_pack is not None:
            if (
                action.random_pack in pack_dict
                and pack_dict[action.random_pack] != action.random_key
            ):
                logger.info(
                    "Error: randomSpawnGroupPackKey duplicate! "
                    f"({action.random_key} - {action.random_pack})"
                )
            pack_dict[action.random_pack] = action.random_key
    for action in action_list:
        action.update_pack(pack_dict)
    min_time, action_enemy_min, action_enemy_max = 0.0, 0, 0
    fragment_flag = False

    def time_filter(action):
        return action.hidden_group is None or action.hidden_group in normal_hidden_group

    def num_filter(action):
        return (action.key is not None or action.random_key is not None) and (
            action.hidden_group is None or action.hidden_group in normal_hidden_group
        )

    time_dict = {"fix_time": -1.0, "random_group": {}}
    num_dict = {"base_num": 0, "random_group": {}}
    # 最短用时
    for action in filter(time_filter, action_list):
        fragment_flag = True
        if action.random_key is not None:
            if action.random_key not in time_dict["random_group"]:
                time_dict["random_group"][action.random_key] = {
                    "single": 1000000.0,
                    "pack": {},
                }
            if action.random_pack is not None:
                if (
                    action.random_pack
                    not in time_dict["random_group"][action.random_key]["pack"]
                ):
                    time_dict["random_group"][action.random_key]["pack"][
                        action.random_pack
                    ] = -1.0
                time_dict["random_group"][action.random_key]["pack"][
                    action.random_pack
                ] = max(
                    action.time,
                    time_dict["random_group"][action.random_key]["pack"][
                        action.random_pack
                    ],
                )
            else:
                time_dict["random_group"][action.random_key]["single"] = min(
                    action.time, time_dict["random_group"][action.random_key]["single"]
                )
        else:
            time_dict["fix_time"] = max(action.time, time_dict["fix_time"])
    if time_dict["random_group"] != {}:
        pack_time_list = [0.0]
        for action_k_iter in time_dict["random_group"]:
            pack_time = 1000000.0
            if time_dict["random_group"][action_k_iter]["pack"] != {}:
                pack_time = min(
                    pack_time,
                    min(time_dict["random_group"][action_k_iter]["pack"].values()),
                )
            if time_dict["random_group"][action_k_iter]["single"] != {}:
                pack_time = min(
                    pack_time,
                    max(time_dict["random_group"][action_k_iter]["single"], 0),
                )
            pack_time_list.append(pack_time)
        min_time = max(0.0, time_dict["fix_time"], min(pack_time_list))
    else:
        min_time = max(0.0, time_dict["fix_time"])

    # 敌人数量
    for action in filter(num_filter, action_list):
        if action.key in not_count_list:
            continue
        if action.random_key is not None:
            if action.random_key not in num_dict["random_group"]:
                num_dict["random_group"][action.random_key] = {"single": [], "pack": {}}
            if action.random_pack is not None:
                if (
                    action.random_pack
                    not in num_dict["random_group"][action.random_key]["pack"]
                ):
                    num_dict["random_group"][action.random_key]["pack"][
                        action.random_pack
                    ] = 0
                num_dict["random_group"][action.random_key]["pack"][
                    action.random_pack
                ] += action.count
            else:
                num_dict["random_group"][action.random_key]["single"].append(
                    action.count
                )
        else:
            num_dict["base_num"] += action.count
    if num_dict["random_group"] != {}:
        for action_k_iter in num_dict["random_group"]:
            pack_min, pack_max = 100000, -1
            if num_dict["random_group"][action_k_iter]["pack"] != {}:
                pack_min = min(
                    pack_min,
                    min(num_dict["random_group"][action_k_iter]["pack"].values()),
                )
                pack_max = max(
                    pack_max,
                    max(num_dict["random_group"][action_k_iter]["pack"].values()),
                )
            if num_dict["random_group"][action_k_iter]["single"] != []:
                pack_min = min(
                    pack_min, min(num_dict["random_group"][action_k_iter]["single"])
                )
                pack_max = max(
                    pack_max, max(num_dict["random_group"][action_k_iter]["single"])
                )
            action_enemy_min += pack_min
            action_enemy_max += pack_max
        action_enemy_min += num_dict["base_num"]
        action_enemy_max += num_dict["base_num"]
    else:
        action_enemy_min = num_dict["base_num"]
        action_enemy_max = num_dict["base_num"]

    return min_time, action_enemy_min, action_enemy_max, fragment_flag


def build_level_info(
    level: LevelData, not_count_list: NotCountList, *, use_countdown: bool = False
) -> LevelInfoView:
    enemy_count = {"min": 0, "max": 0}
    min_time = 0.0
    normal_hidden_group = analyze_normal_hidden_group(level)
    not_count_list_level = copy.deepcopy(not_count_list)
    for enemy in level.enemy_db_refs or []:
        if enemy.use_db is False:
            overwritten = enemy.overwritten_data
            flag = overwritten.not_count_in_total if overwritten is not None else None
            if (
                flag is not None
                and flag.m_defined is True
                and flag.m_value is True
                and enemy.id is not None
            ):
                if enemy.id not in not_count_list_level:
                    not_count_list_level[enemy.id] = []
                not_count_list_level[enemy.id].append(enemy.level)
    for wave in level.waves or []:
        min_time += wave.pre_delay + wave.post_delay
        for fragment in wave.fragments or []:
            time, action_enemy_min, action_enemy_max, fragment_flag = analyze_action(
                fragment.actions or [], normal_hidden_group, not_count_list_level
            )
            enemy_count["min"] += action_enemy_min
            enemy_count["max"] += action_enemy_max
            if fragment_flag:
                min_time += fragment.pre_delay
                min_time += time
    if enemy_count["min"] == enemy_count["max"]:
        enemy_count_text = str(enemy_count["min"])
    else:
        enemy_count_text = f"{enemy_count['min']}~{enemy_count['max']}"

    options = level.options or LevelDataOptions()
    if use_countdown and options.max_play_time > 0:
        max_play_time = options.max_play_time
        time_label = "倒计时"
        time_text = f"{int(max_play_time / 60)}分{int(max_play_time % 60)}秒"
    elif abs(min_time - int(min_time)) < 0.0001:
        time_label = "最短用时"
        time_text = f"{int(min_time / 60)}分{int(min_time % 60)}秒"
    else:
        time_label = "最短用时"
        time_text = f"{int(min_time / 60)}分{min_time % 60:.1f}秒"

    # mapData.map 是原始嵌套 list(模型里是 Any)
    map_matrix = (level.map_data.map if level.map_data is not None else None) or []
    return LevelInfoView(
        character_limit=options.character_limit,
        initial_cost=options.initial_cost,
        max_cost=options.max_cost,
        max_life_point=options.max_life_point,
        enemy_count=enemy_count_text,
        map_size=f"{len(map_matrix[0])}×{len(map_matrix)}",
        time_label=time_label,
        time=time_text,
    )


def analyze_normal_hidden_group(level: LevelData) -> list[str | None]:
    normal_hidden_group: list[str | None] = []
    for rune in level.runes or []:
        if rune.difficulty_mask == "NORMAL" and rune.key == "level_hidden_group_enable":
            for d in rune.blackboard or []:
                if d.key == "key":
                    normal_hidden_group.append(d.value_str)
    return normal_hidden_group


def _skill_name(
    char: CharacterData, skill_index: int, skill_table: dict[str, SkillDataBundle]
) -> str:
    """干员第 skill_index 个技能 1 级时的名字;-1 表示不带技能。

    数据缺失时抛 KeyError / IndexError,由调用方按"这一关没有编队"兜底。
    """

    if skill_index == -1:
        return ""
    skill_id = _require(
        _require(char.skills, "skills")[skill_index].skill_id, "skillId"
    )
    levels = _require(skill_table[skill_id].levels, "levels")
    return _require(levels[0].name, "name")


def build_char_card_info(
    level: LevelData,
    stage_page_name: str,
    character_table: dict[str, CharacterData],
    skill_table: dict[str, SkillDataBundle],
    stage_char_id: str | None = None,
) -> SquadSectionView | None:
    units = []
    memory_desc = ""
    favor_point, fp_set = [], set()
    try:
        predefines = level.predefines
        if predefines is None or predefines.character_cards is None:
            return None
        for char_card in predefines.character_cards:
            inst = _require(char_card.inst, "inst")
            character_key = _require(inst.character_key, "characterKey")
            char_card_name = _require(character_table[character_key].name, "name")
            if stage_char_id is not None and character_key == stage_char_id:
                units.append(SquadUnitView(name=char_card_name, simulation=True))
                memory_desc = "模拟对象干员的状态数据与玩家持有的一致，请以实际情况为准"
                continue
            skill_name = _skill_name(
                character_table[character_key], char_card.skill_index, skill_table
            )
            potential_rank = inst.potential_rank
            units.append(
                SquadUnitView(
                    name=char_card_name,
                    phase={
                        "PHASE_0": 0,
                        "PHASE_1": 1,
                        "PHASE_2": 2,
                        "PHASE_3": 3,
                    }.get(inst.phase, inst.phase),
                    level=inst.level,
                    skill_name=skill_name,
                    main_skill_level=char_card.main_skill_lvl,
                    potential=potential_rank + 1 if potential_rank != 0 else None,
                )
            )
            this_p = min(200, inst.favor_point * 2)
            fp_set.add(this_p)
            favor_point.append(f"{char_card_name}信赖值为{this_p}%")
        if units:
            if favor_point and memory_desc:
                memory_desc = "<br>" + memory_desc
            if len(fp_set) == 1 and len(favor_point) > 1:
                if stage_char_id is not None:
                    fp_desc = (
                        f"本关卡除模拟对象干员外的随队干员信赖值都为{fp_set.pop()}%"
                    )
                else:
                    fp_desc = f"本关卡随队干员信赖值都为{fp_set.pop()}%"
            else:
                fp_desc = "，".join(favor_point)
            return SquadSectionView(
                title="固定编队", units=units, note=fp_desc + memory_desc
            )
    # 干员数据缺字段时只该丢掉这一关的固定编队,不能让异常冒泡打断整轮三千多个
    # 关卡的生成:模型字段为 None 时 _require 抛 KeyError,视图校验失败抛
    # ValidationError,都在这里接住
    except (AttributeError, IndexError, KeyError, TypeError, ValidationError):
        logger.info(f"{stage_page_name}: characterCards error.")
    return None


def build_char_insert_info(
    level: LevelData,
    stage_page_name: str,
    character_table: dict[str, CharacterData],
    skill_table: dict[str, SkillDataBundle],
) -> SquadSectionView | None:
    units = []
    favor_point, fp_set = [], set()
    try:
        predefines = level.predefines
        if predefines is None or predefines.character_insts is None:
            return None
        for char_insert in predefines.character_insts:
            inst = _require(char_insert.inst, "inst")
            character_key = _require(inst.character_key, "characterKey")
            char_insert_name = _require(character_table[character_key].name, "name")
            skill_name = _skill_name(
                character_table[character_key], char_insert.skill_index, skill_table
            )
            potential_rank = inst.potential_rank
            units.append(
                SquadUnitView(
                    name=char_insert_name,
                    phase={
                        "PHASE_0": 0,
                        "PHASE_1": 1,
                        "PHASE_2": 2,
                        "PHASE_3": 3,
                    }.get(inst.phase, inst.phase),
                    level=inst.level,
                    skill_name=skill_name,
                    main_skill_level=char_insert.main_skill_lvl,
                    potential=potential_rank + 1 if potential_rank != 0 else None,
                )
            )
            this_p = min(200, inst.favor_point * 2)
            fp_set.add(this_p)
            favor_point.append(f"{char_insert_name}信赖值为{this_p}%")
        if units:
            if len(fp_set) == 1 and len(favor_point) > 1:
                fp_desc = f"本关卡已部署干员信赖值都为{fp_set.pop()}%"
            else:
                fp_desc = "，".join(favor_point)
            return SquadSectionView(title="已部署干员", units=units, note=fp_desc)
    except (AttributeError, IndexError, KeyError, TypeError, ValidationError):
        logger.info(f"{stage_page_name}: characterInsts error.")
    return None


def build_squad_sections(
    level: LevelData,
    stage_page_name: str,
    character_table: dict[str, CharacterData],
    skill_table: dict[str, SkillDataBundle],
    *,
    stage_char_id: str | None = None,
    include_inserted: bool = True,
) -> list[SquadSectionView]:
    sections = []
    fixed = build_char_card_info(
        level,
        stage_page_name,
        character_table,
        skill_table,
        stage_char_id=stage_char_id,
    )
    if fixed is not None:
        sections.append(fixed)
    if include_inserted:
        inserted = build_char_insert_info(
            level, stage_page_name, character_table, skill_table
        )
        if inserted is not None:
            sections.append(inserted)
    return sections


def build_tile_effects(
    level: LevelData, stage_tile_info: dict[str, TileAppendInfo]
) -> list[TileEffectView]:
    tiles = level.map_data.tiles if level.map_data is not None else None
    if not tiles:
        return []
    tile_blackboard_dict: dict[str, list[list[BlackboardDataPair]]] = {}
    for tile in tiles:
        if not tile.blackboard:
            continue
        tile_key = tile.tile_key or ""
        if tile_key not in tile_blackboard_dict:
            tile_blackboard_dict[tile_key] = []
        if tile.blackboard not in tile_blackboard_dict[tile_key]:
            tile_blackboard_dict[tile_key].append(tile.blackboard)
    if tile_blackboard_dict == {}:
        return []

    effects = []
    for tile_key, blackboards in tile_blackboard_dict.items():
        tile_info = stage_tile_info.get(tile_key)
        # tileInfo 里有条目但名字为 null 时输出空名,与旧模型的默认值一致
        tile_name = (tile_info.name or "") if tile_info is not None else tile_key
        effects.append(
            TileEffectView(
                name=tile_name,
                blackboards=[
                    [
                        BlackboardView(
                            key=item.key or "",
                            value=item.value,
                            value_str=item.value_str,
                        )
                        for item in blackboard
                    ]
                    for blackboard in blackboards
                ],
            )
        )
    return effects


def _override_name(enemy: LevelDataEnemyDataDbReference) -> str:
    """useDb 为 false 的敌人只有 overwrittenData.name 这一处名字。"""

    data = _require(enemy.overwritten_data, "overwrittenData")
    return _require(_require(data.name, "name").m_value, "name.m_value")


def _database_name(levels: list[EnemyDatabaseEnemyLevel]) -> str:
    """图鉴里没有的敌人退回 enemy_database 第 0 级的名字。"""

    data = _require(levels[0].enemy_data, "enemyData")
    return _require(_require(data.name, "name").m_value, "name.m_value")


def build_enemies(
    level: LevelData,
    enemy_table: EnemyTable,
    enemy_levels: EnemyLevelIndex,
    flag_skip0: bool,
) -> list[EnemyView]:
    def enemy_db_refs_sort(item: LevelDataEnemyDataDbReference) -> int:
        handbook = enemy_table.get(item.id) if item.id is not None else None
        return handbook.sort_id if handbook is not None else 9999999

    normal_hidden_group = analyze_normal_hidden_group(level)
    enemy_count_dict = {}
    for wave in level.waves or []:
        for fragment in wave.fragments or []:
            action_list = [ActionInfo(action) for action in fragment.actions or []]
            pack_dict = {}
            actions_count_type = {}
            for action in action_list:
                if action.random_key is not None and action.random_pack is not None:
                    pack_dict[action.random_pack] = action.random_key
                if action.key is not None and action.key not in enemy_count_dict:
                    enemy_count_dict[action.key] = {"min": 0, "max": 0}
                if action.key is not None and action.key not in actions_count_type:
                    actions_count_type[action.key] = {"min": 0, "max": 0}
            for action in action_list:
                action.update_pack(pack_dict)
            actions_count = {"fixed": copy.deepcopy(actions_count_type), "random": {}}
            for action in action_list:
                if (action.key is not None or action.random_key is not None) and (
                    action.hidden_group is None
                    or action.hidden_group in normal_hidden_group
                ):
                    if action.random_key is not None:
                        if action.random_key not in actions_count["random"]:
                            actions_count["random"][action.random_key] = {
                                "single": [],
                                "pack": {},
                            }
                        if action.random_pack is not None:
                            if (
                                action.random_pack
                                not in actions_count["random"][action.random_key][
                                    "pack"
                                ]
                            ):
                                actions_count["random"][action.random_key]["pack"][
                                    action.random_pack
                                ] = copy.deepcopy(actions_count_type)
                            if action.key is not None:
                                actions_count["random"][action.random_key]["pack"][
                                    action.random_pack
                                ][action.key]["min"] += action.count
                                actions_count["random"][action.random_key]["pack"][
                                    action.random_pack
                                ][action.key]["max"] += action.count
                        else:
                            actions_count["random"][action.random_key]["single"].append(
                                copy.deepcopy(actions_count_type)
                            )
                            if action.key is not None:
                                actions_count["random"][action.random_key]["single"][
                                    -1
                                ][action.key]["min"] = action.count
                                actions_count["random"][action.random_key]["single"][
                                    -1
                                ][action.key]["max"] = action.count
                    else:
                        if action.key is not None:
                            actions_count["fixed"][action.key]["min"] += action.count
                            actions_count["fixed"][action.key]["max"] += action.count
            if actions_count["random"] != {}:
                for k_iter in actions_count["random"]:
                    if actions_count["random"][k_iter]["pack"] != {}:
                        for count_p in actions_count["random"][k_iter]["pack"].values():
                            actions_count["random"][k_iter]["single"].append(count_p)
                    if actions_count["random"][k_iter]["single"] != {}:
                        for enemy_k in actions_count_type:
                            actions_count["fixed"][enemy_k]["min"] += min(
                                x[enemy_k]["min"]
                                for x in actions_count["random"][k_iter]["single"]
                            )
                            actions_count["fixed"][enemy_k]["max"] += max(
                                x[enemy_k]["max"]
                                for x in actions_count["random"][k_iter]["single"]
                            )
            for k in enemy_count_dict:
                if k in actions_count["fixed"]:
                    enemy_count_dict[k]["min"] += actions_count["fixed"][k]["min"]
                    enemy_count_dict[k]["max"] += actions_count["fixed"][k]["max"]
    enemy_num_dict = {}
    for k in enemy_count_dict:
        if enemy_count_dict[k]["min"] == enemy_count_dict[k]["max"]:
            enemy_num_dict[k] = f"{enemy_count_dict[k]['min']}"
        else:
            enemy_num_dict[k] = (
                f"{enemy_count_dict[k]['min']},{enemy_count_dict[k]['max']}"
            )
    enemy_db_refs_sorted = sorted(level.enemy_db_refs or [], key=enemy_db_refs_sort)
    enemies = []
    for enemy in enemy_db_refs_sorted:
        if enemy.id not in enemy_num_dict:
            enemy_num_dict[enemy.id] = "0"
        if flag_skip0 and enemy_num_dict[enemy.id] == "0":
            continue
        count_text = enemy_num_dict[enemy.id]
        if "," in count_text:
            count_lower, count_upper = count_text.split(",")
        else:
            count_lower, count_upper = None, count_text

        display_name = None
        note = None
        overrides = []
        # 只有明确的 False 才读 overwrittenData;与 build_level_info 里对同一字段的
        # 判断保持一致
        if enemy.use_db is False:
            enemy_name = _override_name(enemy)
            note = "需人工复查！"
        else:
            handbook = enemy_table.get(enemy.id) if enemy.id is not None else None
            if handbook is not None:
                enemy_name = _require(handbook.name, "name")
                if enemy_name in ["W", "泥岩", "多萝西", "弑君者"]:
                    display_name = enemy_name
                    enemy_name += "(敌方)"
            else:
                enemy_name = ""
                db_levels = enemy_levels.get(enemy.id) if enemy.id is not None else None
                if db_levels is not None:
                    enemy_name = _database_name(db_levels)
            if enemy.overwritten_data is not None:
                overrides = build_enemy_overrides(enemy.overwritten_data)

        enemies.append(
            EnemyView(
                index=len(enemies) + 1,
                name=enemy_name,
                display_name=display_name,
                count=count_upper,
                count_lower=count_lower,
                level=enemy.level,
                note=note,
                overrides=overrides,
            )
        )
    return enemies


def format_zone(zone_table: ZoneTable, zone_id: str | None) -> str:
    """拼接所属区域名。

    zone_table 里有 62 个区域(guide_1、camp_zone_* 等)两个名字字段都是 null,
    此处刻意保留旧行为输出字面量 None,而不是让参数从 wikitext 里消失 ——
    MediaWiki 模板对「参数缺失」和「参数为 None」的处理并不相同。
    """
    zone_data = (zone_table.zones or {})[_require(zone_id, "zoneId")]
    if zone_data.zone_name_first:
        return f"{zone_data.zone_name_first} {zone_data.zone_name_second}"
    return f"{zone_data.zone_name_second}"


def _terrain_tags(level: LevelData | None) -> list[str] | None:
    """mapData.tags;没有关卡或字段为 null 时为 None(页面上不输出 |地形tag=)。"""

    if level is None or level.map_data is None:
        return None
    return level.map_data.tags


def _display_detail_rewards(stage: StageData) -> list[StageDataDisplayDetailRewards]:
    drop_info = stage.stage_drop_info
    return (drop_info.display_detail_rewards if drop_info is not None else None) or []


def build_normal_stage(
    stage: StageData,
    table: StageTable,
    zone_table: ZoneTable,
    character_table: dict[str, CharacterData],
    building_data: BuildingData,
    item_table: InventoryData,
    level: LevelData | None,
    not_count_list: NotCountList,
    compile_rich_text: Callable[[str], str],
    map_override: str = "",
) -> BasicStageView:
    subtype = None
    if stage.hilight_mark:
        subtype = "难关"
    elif stage.appearance_style == "HIGH_DIFFICULTY":
        subtype = "绝境"
    elif stage.appearance_style == "MIST_OPS":
        subtype = "迷雾"

    stages = table.stages or {}
    unlock_conditions = []
    for unlock in stage.unlock_condition or []:
        previous_stage = stages[_require(unlock.stage_id, "stageId")]
        if_tough = ""
        if previous_stage.difficulty == "SIX_STAR":
            if_tough = "险地"
        elif (
            previous_stage.diff_group == "TOUGH"
            and previous_stage.appearance_style != "HIGH_DIFFICULTY"
        ):
            if_tough = "磨难"
        rank = {"PASS": 2, "COMPLETE": 3}.get(
            unlock.complete_state, unlock.complete_state
        )
        unlock_conditions.append(
            f"{rank}星通关[[{if_tough}{previous_stage.code} {previous_stage.name}]]"
        )

    zone = format_zone(zone_table, stage.zone_id)

    description = ""
    if stage.description:
        description = compile_rich_text(stage.description.replace("\\n", "<br/>"))

    rewards = []
    display_detail_rewards = _display_detail_rewards(stage)
    if display_detail_rewards:
        rewards = build_reward_groups(
            display_detail_rewards, character_table, building_data, item_table
        )

    tile_effects = []
    if level is not None:
        tile_effects = build_tile_effects(level, table.tile_info or {})

    view = BasicStageView(
        heading="普通",
        code=(stage.code or "").strip(),
        name=(stage.name or "").strip(),
        stage_id=stage.stage_id or "",
        map_override=map_override,
        stage_type=parse_stage_type(stage.stage_type),
        subtype=subtype,
        boss=stage.boss_mark,
        difficulty=stage.difficulty,
        # levelId 缺失(None)才算非战斗关卡;空字符串不是,与地图信息的截断判断不同
        battle_stage=stage.level_id is not None,
        unlock_condition=", ".join(unlock_conditions),
        recommended_level=stage.danger_level or "-",
        zone=zone,
        level=build_level_info(level, not_count_list) if level is not None else None,
        description=description,
        ap_cost=stage.ap_cost,
        practice_cost=stage.practice_ticket_cost if stage.can_practice else -1,
        rewards=rewards,
        tile_effects=tile_effects,
        terrain_tags=_terrain_tags(level),
    )
    return view


def build_4star_stage(
    stage: StageData,
    table: StageTable,
    zone_table: ZoneTable,
    character_table: dict[str, CharacterData],
    building_data: BuildingData,
    item_table: InventoryData,
    level: LevelData,
    compile_rich_text: Callable[[str], str],
) -> AssaultStageView:
    stages = table.stages or {}
    unlock_conditions = []
    for unlock in stage.unlock_condition or []:
        previous_stage = stages[_require(unlock.stage_id, "stageId")]
        rank = {"PASS": 2, "COMPLETE": 3}.get(
            unlock.complete_state, unlock.complete_state
        )
        if previous_stage.code != stage.code:
            unlock_condition = (
                f"{rank}星通关[[{previous_stage.code} {previous_stage.name}]]"
            )
        else:
            unlock_condition = (
                f"{rank}星通关[[#普通|{previous_stage.code} "
                f"{previous_stage.name}]]普通难度"
            )
        unlock_conditions.append(unlock_condition)

    zone = format_zone(zone_table, stage.zone_id)

    runes = level.runes or []
    climit, intelligence = build_rune_buffs(runes)

    rewards = []
    display_detail_rewards = _display_detail_rewards(stage)
    if display_detail_rewards:
        rewards = build_reward_groups(
            display_detail_rewards, character_table, building_data, item_table
        )

    intelligence.extend(build_rune_lines(runes))

    options = level.options or LevelDataOptions()
    view = AssaultStageView(
        heading="突袭",
        code=(stage.code or "").strip(),
        name=(stage.name or "").strip(),
        stage_type=parse_stage_type(stage.stage_type),
        difficulty=stage.difficulty,
        unlock_condition=", ".join(unlock_conditions),
        recommended_level=str(stage.danger_level),
        zone=zone,
        character_limit=options.character_limit + climit,
        initial_cost=options.initial_cost,
        max_cost=options.max_cost,
        description=compile_rich_text(
            (stage.description or "").replace("\\n", "<br/>")
        ),
        ap_cost=stage.ap_cost,
        practice_cost=stage.practice_ticket_cost if stage.can_practice else -1,
        rewards=rewards,
        intelligence=intelligence,
    )
    return view


def build_campaign_stage(
    stage: StageData,
    table: StageTable,
    campaign_table: CampaignTable,
    character_table: dict[str, CharacterData],
    building_data: BuildingData,
    item_table: InventoryData,
    level: LevelData | None,
    not_count_list: NotCountList,
    compile_rich_text: Callable[[str], str],
) -> CampaignStageView:
    stages = table.stages or {}
    unlock_conditions = []
    for unlock in stage.unlock_condition or []:
        previous_stage = stages[_require(unlock.stage_id, "stageId")]
        rank = {"PASS": 2, "COMPLETE": 3}.get(
            unlock.complete_state, unlock.complete_state
        )
        unlock_conditions.append(
            f"{rank}星通关[[{previous_stage.code} {previous_stage.name}]]"
        )

    campaign_zones = campaign_table.campaign_zones or {}
    zone_data = campaign_zones.get(stage.zone_id) if stage.zone_id is not None else None
    zone = _require(zone_data.name, "name") if zone_data is not None else "NONE"

    description = ""
    if stage.description:
        description = compile_rich_text(stage.description.replace("\\n", "<br/>"))

    stage_id = stage.stage_id or ""
    campaign_detail = (campaign_table.campaigns or {})[stage_id]
    drop_gains = campaign_detail.drop_gains or {}
    if drop_gains["PERMANENT"].gain_ladders != []:
        gain_flag = "PERMANENT"
    else:
        gain_flag = "ROTATE"
    drop_gain = drop_gains[gain_flag]

    rewards = []
    if drop_gain.display_detail_rewards:
        rewards = build_reward_groups(
            drop_gain.display_detail_rewards,
            character_table,
            building_data,
            item_table,
        )

    gain_ladders = drop_gain.gain_ladders or []
    ap_returns = [f"+{ladder.ap_fail_return}" for ladder in gain_ladders]
    diamond_rewards = []
    for ladder in gain_ladders:
        if ladder.display_diamond_shd_num == 0:
            diamond_rewards.append(f"+{ladder.display_diamond_shd_num}")
        else:
            diamond_rewards.append(f"+约{ladder.display_diamond_shd_num}")

    view = CampaignStageView(
        code=(stage.code or "").strip(),
        name=(stage.name or "").strip(),
        stage_id=stage_id,
        commission="_r_" in stage_id,
        stage_type=parse_stage_type(stage.stage_type),
        difficulty=stage.difficulty,
        unlock_condition=", ".join(unlock_conditions),
        zone=zone,
        level=build_level_info(level, not_count_list) if level is not None else None,
        description=description,
        ap_cost=stage.ap_cost,
        rewards=rewards,
        ap_returns=ap_returns,
        diamond_rewards=diamond_rewards,
        terrain_tags=_terrain_tags(level),
    )
    return view


def build_crisis_stage(
    stage_detail: dict,
    level: LevelData | None,
    not_count_list: NotCountList,
    compile_rich_text: Callable[[str], str],
) -> BasicStageView:
    # stage_detail 来自 weedy 的 crisis_info.json,不是 gamedata,仍按 dict 访问
    if "description" in stage_detail:
        stage_desc = compile_rich_text(
            stage_detail["description"].replace("\\n", "<br/>")
        )
    elif "desc" in stage_detail:
        stage_desc = compile_rich_text(stage_detail["desc"].replace("\\n", "<br/>"))
    else:
        stage_desc = ""

    view = BasicStageView(
        code=stage_detail["code"].strip(),
        name=stage_detail["name"].strip(),
        stage_id=stage_detail["stageId"],
        stage_type="活动",
        difficulty="NORMAL",
        unlock_condition="—",
        recommended_level="—",
        zone=stage_detail["code"].strip(),
        level=build_level_info(level, not_count_list) if level is not None else None,
        description=stage_desc,
        ap_cost=0,
        practice_cost=-1,
    )
    return view


def build_roguelike_stage(
    stage: RoguelikeGameStageData,
    level: LevelData | None,
    not_count_list: NotCountList,
    compile_rich_text: Callable[[str], str],
) -> BasicStageView:
    view = BasicStageView(
        heading="普通",
        code=_require(stage.code, "code").strip(),
        name=_require(stage.name, "name").strip(),
        stage_id=_require(stage.id, "id"),
        stage_type="活动",
        difficulty="NORMAL",
        unlock_condition="—",
        recommended_level="—",
        zone="—",
        level=build_level_info(level, not_count_list) if level is not None else None,
        description=compile_rich_text(
            _require(stage.description, "description").replace("\\n", "<br/>")
        ),
        ap_cost=0,
        practice_cost=-1,
        terrain_tags=_terrain_tags(level),
    )
    return view


def build_roguelike_4star_stage(
    stage: RoguelikeGameStageData,
    level: LevelData,
    compile_rich_text: Callable[[str], str],
) -> AssaultStageView:
    climit, intelligence = build_rune_buffs(level.runes or [])

    options = level.options or LevelDataOptions()
    view = AssaultStageView(
        heading="紧急作战",
        code=_require(stage.code, "code").strip(),
        name=_require(stage.name, "name").strip(),
        stage_type="活动",
        subtype="紧急作战",
        difficulty="FOUR_STAR",
        unlock_condition="-",
        zone="-",
        character_limit=options.character_limit + climit,
        initial_cost=options.initial_cost,
        max_cost=options.max_cost,
        description=compile_rich_text(
            _require(stage.elite_desc, "eliteDesc").replace("\\n", "<br/>")
        ),
        ap_cost=0,
        practice_cost=-1,
        intelligence=intelligence,
    )
    return view


def build_memory_stage(
    stage: HandbookStoryStageData,
    level: LevelData | None,
    compile_rich_text: Callable[[str], str],
    character_table: dict[str, CharacterData],
    building_data: BuildingData,
    item_table: InventoryData,
    not_count_list: NotCountList,
) -> BasicStageView:
    unlock_cond = ""
    for p in stage.unlock_param or []:
        if unlock_cond != "":
            unlock_cond += "，"
        if p.unlock_type == "AWAKE":
            unlock_cond += f"提升至精英阶段{p.unlock_param_1}等级{p.unlock_param_2}"
        elif p.unlock_type == "FAVOR":
            unlock_cond += f"提升信赖至{p.unlock_param_1}"
        else:
            logger.info(f"Unknown unlockType {p.unlock_type}")
    unlock_cond = (
        "干员'''[[{}]]'''".format(
            character_table[_require(stage.char_id, "charId")].name
        )
        + unlock_cond
    )

    reward_items = [
        DropView(
            name=parse_drop_item(
                r.type, r.id, character_table, building_data, item_table
            ),
            occurrence="三星获得",
        )
        for r in stage.reward_item or []
    ]
    view = BasicStageView(
        code="悖论模拟",
        name=_require(stage.name, "name").strip(),
        stage_id=_require(stage.stage_id, "stageId"),
        stage_type="悖论模拟",
        difficulty="NORMAL",
        unlock_condition=unlock_cond,
        recommended_level="—",
        zone=stage.zone_id,
        level=build_level_info(level, not_count_list) if level is not None else None,
        description=compile_rich_text(
            _require(stage.description, "description").replace("\n", "<br/>")
        ),
        ap_cost=0,
        practice_cost=-1,
        rewards=[RewardGroupView(label="首次掉落", drops=reward_items)],
        terrain_tags=_terrain_tags(level),
    )
    return view


def build_sandbox_v2_stage(
    stage: SandboxV2StageData,
    compile_rich_text: Callable[[str], str],
    level: LevelData | None,
    not_count_list: NotCountList,
) -> BasicStageView:
    code = _require(stage.code, "code")
    name = _require(stage.name, "name")
    stage_id = _require(stage.stage_id, "stageId")
    view = BasicStageView(
        code=code,
        name=name,
        stage_id=stage_id,
        stage_type="生息演算",
        level=(
            build_level_info(level, not_count_list, use_countdown=True)
            if level is not None
            else None
        ),
        description=compile_rich_text(
            _require(stage.description, "description")
            .replace("\\n", "<br/>")
            .replace("\n", "<br/>")
        ),
        action_cost=stage.action_cost,
        terrain_tags=_terrain_tags(level),
        sandbox_map=SandboxMapView(code=code, name=name, stage_id=stage_id),
    )
    return view


def build_recal_rune_stage(
    stage: RecalRuneStageData,
    compile_rich_text: Callable[[str], str],
    level: LevelData | None,
    not_count_list: NotCountList,
) -> BasicStageView:
    view = BasicStageView(
        code=_require(stage.level_code, "levelCode"),
        name=_require(stage.level_name, "levelName"),
        stage_id=_require(stage.stage_id, "stageId"),
        stage_type="全息作战矩阵",
        level=build_level_info(level, not_count_list) if level is not None else None,
        description=compile_rich_text(
            _require(stage.level_desc, "levelDesc")
            .replace("\\n", "<br/>")
            .replace("\n", "<br/>")
        ),
        ap_cost=0,
        practice_cost=-1,
        terrain_tags=_terrain_tags(level),
    )
    return view


# --- 渲染:把视图序列化成 wikitext。纯参数表的模板用 WikiTemplate,
#     带自由文本/wikitable 的部分(固定编队表格、剿灭进度表、特殊地形注释、
#     各页面骨架)直接拼字符串。 ---


def render_drop(drop: DropView) -> str:
    # 家具的参数位置与普通物品不同: :家具=yes:1=名称[:2=概率]
    if drop.furniture:
        text = f":家具=yes:1={drop.name}"
        if drop.occurrence:
            text += f":2={drop.occurrence}"
        return text
    text = drop.name
    if drop.occurrence:
        text += f":{drop.occurrence}"
    return text


def render_reward_group(group: RewardGroupView) -> str:
    return ",".join(render_drop(drop) for drop in group.drops)


def add_level_info(template: WikiTemplate, level: LevelInfoView) -> None:
    # 用量标签是动态键名(最短用时/倒计时),声明式方案表达不了,直接拼 dict
    template.add_all(
        {
            "部署上限": level.character_limit,
            "初始COST": level.initial_cost,
            "COST上限": level.max_cost,
            "目标点耐久": level.max_life_point,
            "敌人数量": level.enemy_count,
            "地图大小": level.map_size,
            level.time_label: level.time,
        }
    )


def render_blackboard(blackboard: list[BlackboardView]) -> str:
    # 一组黑板键值,以制表符起首、逗号空格结尾,占据独立的一行
    parts = []
    for item in blackboard:
        part = f"{item.key} {item.value}"
        if item.value_str is not None:
            part += f" {item.value_str}"
        parts.append(part)
    return "\t" + ", ".join(parts) + ", "


def render_tile(tile: TileEffectView) -> str:
    lines = [f"{tile.name}:"]
    lines.extend(render_blackboard(b) for b in tile.blackboards)
    return "\n".join(lines)


def render_tile_effects(tiles: list[TileEffectView]) -> str:
    # 特殊地形黑板数据包在 HTML 注释里,仅作为编辑者复查的参考
    body = "\n".join(render_tile(tile) for tile in tiles)
    return f"<!--\n{body}\n-->"


def render_basic_stage(stage: BasicStageView) -> str:
    blocks = []
    if stage.heading is not None:
        blocks.append(f"=={stage.heading}==")
    template = WikiTemplate("普通关卡信息")
    template.add("关卡代号", stage.code)
    template.add("关卡名", stage.name)
    template.add("关卡id", stage.stage_id)
    template.add_optional("地图预览override", stage.map_override)
    template.add("关卡类型", stage.stage_type)
    template.add_if_set("子类型", stage.subtype)
    if stage.boss:
        template.add("领袖标志", "Yes")
    template.add_if_set("关卡难度", stage.difficulty)
    # 仅 False 时输出;None / True 都不输出
    if stage.battle_stage is False:
        template.add("战斗关卡", "false")
    template.add_if_set("解锁条件", stage.unlock_condition)
    template.add_if_set("推荐等级", stage.recommended_level)
    template.add_if_set("所属区域", stage.zone)
    if stage.level is not None:
        add_level_info(template, stage.level)
    template.add_if_set("关卡描述", stage.description)
    template.add_if_set("作战消耗", stage.ap_cost)
    template.add_if_set("演习消耗", stage.practice_cost)
    if stage.resource_overview is not None:
        template.add(
            "资源概览",
            "".join(inline_template("资源概览", r) for r in stage.resource_overview),
        )
    template.add_if_set("action消耗", stage.action_cost)
    template.add_if_set("power消耗", stage.power_cost)
    for reward in stage.rewards:
        template.add(reward.label, render_reward_group(reward))
    if stage.tile_effects:
        template.add("特殊地形效果", render_tile_effects(stage.tile_effects))
    if stage.terrain_tags is not None:
        template.add("地形tag", ",".join(stage.terrain_tags))
    if stage.sandbox_map is not None:
        template.add(
            "特殊地图",
            "<tabber>\n"
            "实景地图=\n"
            f'<img alt="{stage.sandbox_map.code} {stage.sandbox_map.name} 地图" '
            'loading="lazy" '
            f'src="//torappu.prts.wiki/assets/map_preview/'
            f'{stage.sandbox_map.stage_id}.png" width="580"/>\n'
            "|-|\n"
            "全地图={{#Widget:XbMapViewer|data={{:{{FULLPAGENAME}}/data}}}}\n"
            "</tabber>",
        )
    blocks.append(str(template))
    return "\n".join(blocks)


def render_assault_stage(stage: AssaultStageView) -> str:
    template = WikiTemplate("突袭关卡信息")
    template.add("关卡代号", stage.code)
    template.add("关卡名", stage.name)
    template.add("关卡类型", stage.stage_type)
    template.add_if_set("子类型", stage.subtype)
    template.add("关卡难度", stage.difficulty)
    template.add("解锁条件", stage.unlock_condition)
    template.add_if_set("推荐等级", stage.recommended_level)
    template.add("所属区域", stage.zone)
    template.add_all(
        {
            "部署上限": stage.character_limit,
            "初始COST": stage.initial_cost,
            "COST上限": stage.max_cost,
        }
    )
    template.add("关卡描述", stage.description)
    template.add_all({"作战消耗": stage.ap_cost, "演习消耗": stage.practice_cost})
    for reward in stage.rewards:
        template.add(reward.label, render_reward_group(reward))
    # 情报保留在注释中,供编辑者复查;没有情报时注释里也不留空行
    template.add_raw("\n".join(["<!--|情报=", *stage.intelligence, "-->"]))
    return f"=={stage.heading}==\n{template}"


def render_campaign_stage(stage: CampaignStageView) -> str:
    template = WikiTemplate("剿灭关卡信息")
    template.add("关卡代号", stage.code)
    template.add("关卡名", stage.name)
    template.add("关卡id", stage.stage_id)
    if stage.commission:
        template.add("剿灭委托", "true")
    template.add("关卡类型", stage.stage_type)
    template.add("关卡难度", stage.difficulty)
    template.add("解锁条件", stage.unlock_condition)
    template.add("所属区域", stage.zone)
    if stage.level is not None:
        add_level_info(template, stage.level)
    template.add("关卡描述", stage.description)
    template.add("作战消耗", stage.ap_cost)
    for reward in stage.rewards:
        template.add(reward.label, render_reward_group(reward))
    for index, value in enumerate(stage.ap_returns, 1):
        template.add(f"理智返还{index}", value)
    for index, value in enumerate(stage.diamond_rewards, 1):
        template.add(f"合成玉获得{index}", value)
    if stage.terrain_tags is not None:
        template.add("地形tag", ",".join(stage.terrain_tags))
    return f"==关卡==\n{template}"


def add_enemy_params(template: WikiTemplate, enemy: EnemyView) -> None:
    # 敌人参数键名带序号,显式拼出比再加一层抽象更清楚
    index = enemy.index
    template.add(f"敌人{index}", enemy.name)
    if enemy.display_name is not None:
        template.add(f"敌人{index}显示名", enemy.display_name)
    template.add(f"敌人{index}数量", enemy.count)
    if enemy.count_lower is not None:
        template.add(f"敌人{index}数量下限", enemy.count_lower)
    template.add(f"敌人{index}级别", enemy.level)
    if enemy.note is not None:
        template.add(f"敌人{index}备注", enemy.note)
    for override in enemy.overrides:
        template.add(f"敌人{index}{override.label}", override.value)


def render_enemies(enemies: list[EnemyView]) -> str:
    template = WikiTemplate("敌方情报")
    for enemy in enemies:
        add_enemy_params(template, enemy)
    return f"==敌方情报==\n{template}"


def render_squad_unit(unit: SquadUnitView) -> str:
    if unit.simulation:
        return inline_template("悖论模拟对象", unit.name)
    args = [unit.name, unit.phase, unit.level, unit.skill_name, unit.main_skill_level]
    if unit.potential is not None:
        # 潜能是第 6 个位置参数,前面补一个空位(第 5 位留空)
        args += ["", unit.potential]
    return inline_template("编队单位", *args)


def render_squad(section: SquadSectionView) -> str:
    units = "".join(render_squad_unit(unit) for unit in section.units)
    return (
        f"=={section.title}==\n"
        '{| class="wikitable hlist logo mw-collapsed mw-collapsible" '
        'style="text-align:center; width:min(567px,100%); white-space:normal;"\n'
        f'!style="background-color:#0098DC;color:#FFFFFF"|{section.title}\n'
        f"|-\n"
        f"|{units}\n"
        f"|-\n"
        f"!备注\n"
        f"|-\n"
        f"|{section.note}\n"
        f"|}}"
    )


def render_squads(squads: list[SquadSectionView]) -> str:
    return "\n".join(render_squad(section) for section in squads)


def render_progress_items(items: list[CampaignProgressItemView]) -> str:
    parts = [inline_template("材料消耗", item.name, item.count) for item in items]
    return " ".join(parts)


def render_progress_row(row: CampaignProgressRowView) -> str:
    text = f"|-\n|{row.kill_count}||{render_progress_items(row.items)}"
    if row.break_fee_add:
        text += f" {inline_template('材料消耗', '合成玉', 'i+')}(+{row.break_fee_add})"
    return text + "\n"


def render_campaign_progress(progress: CampaignProgressView) -> str:
    rows = "".join(render_progress_row(row) for row in progress.rows)
    return (
        "==作战进度奖励==\n"
        '{| class="wikitable mw-collapsible mw-collapsed" '
        'style="text-align:center;width:min(600px,100%);"\n'
        '!style="width:200px;color:white;font-weight:bold;'
        'background-color:#575757;"|击溃人数\n'
        '!style="width:400px;color:white;font-weight:bold;'
        'background-color:#575757;"|奖励\n'
        f"{rows}"
        "|}"
    )


# --- 页面骨架:各 page 模板,把上面的片段按页面布局组合。 ---


def render_normal_page(page: NormalPageView) -> str:
    blocks = ["{{pathnav2|关卡一览}}", render_basic_stage(page.normal)]
    if page.assault is not None:
        blocks.append(render_assault_stage(page.assault))
    if page.enemies is not None:
        blocks.append(render_enemies(page.enemies))
    if page.squads:
        blocks.append(render_squads(page.squads))
    if page.material_drop:
        blocks.append("==材料掉落==\n{{关卡材料掉落}}")
    blocks.append("==注释与链接==\n<references/>\n{{关卡导航}}")
    return "\n".join(blocks)


def render_campaign_page(page: CampaignPageView) -> str:
    blocks = ["{{pathnav2|关卡一览}}", render_campaign_stage(page.stage)]
    if page.enemies is not None:
        blocks.append(render_enemies(page.enemies))
    if page.squads:
        blocks.append(render_squads(page.squads))
    blocks.append(render_campaign_progress(page.progress))
    blocks.append("==注释与链接==\n<references/>\n{{关卡导航}}")
    return "\n".join(blocks)


def render_basic_page(
    page: BasicPageView,
    *,
    notoc: bool = False,
    extra_sections: list[str] | None = None,
    categories: list[str] | None = None,
) -> str:
    """危机合约/悖论模拟/生息演算/训练场/全息作战矩阵/id 页面共用。

    带 __NOTOC__ 的页面(crisis/memory/mechanism/id)把 notoc 置 True;
    生息演算历来不带,不要顺手打开。
    extra_sections 插在敌方情报与固定编队之后、注释与链接之前(如危机合约的合约详情),
    categories 追加在 {{关卡导航}} 之后(如分类:危机合约关卡)。
    """
    blocks = ["{{pathnav2|关卡一览}}"]
    if notoc:
        blocks.append("__NOTOC__")
    blocks.append(render_basic_stage(page.stage))
    if page.enemies is not None:
        blocks.append(render_enemies(page.enemies))
    if page.squads:
        blocks.append(render_squads(page.squads))
    if extra_sections:
        blocks.extend(extra_sections)
    blocks.append("==注释与链接==\n<references/>\n{{关卡导航}}")
    if categories:
        blocks.extend(categories)
    return "\n".join(blocks)


def render_roguelike_page(page: RoguelikePageView) -> str:
    blocks = ["{{pathnav2|关卡一览}}"]
    if page.see_also is not None:
        blocks.append(inline_template("参阅", *page.see_also))
    blocks.append(render_basic_stage(page.normal))
    if page.assault is not None:
        blocks.append(render_assault_stage(page.assault))
    if page.enemies is not None:
        blocks.append(render_enemies(page.enemies))
    blocks.append("==注释与链接==\n<references/>\n{{关卡导航}}")
    blocks.append("[[分类:集成战略关卡]]")
    return "\n".join(blocks)


def render_recal_rune_page(page: RecalRunePageView) -> str:
    blocks = [
        "{{pathnav2|关卡一览}}",
        f"<noinclude>{{{{DISPLAYTITLE:{page.display_title}}}}}</noinclude>",
    ]
    blocks.append(render_basic_stage(page.stage))
    if page.enemies is not None:
        blocks.append(render_enemies(page.enemies))
    if page.squads:
        blocks.append(render_squads(page.squads))
    blocks.append("==注释与链接==\n<references/>\n{{关卡导航}}")
    return "\n".join(blocks)


def render_disambiguation(links: list[DisambiguationLinkView]) -> str:
    lines = ["{{消歧义页}}", "<big><big>你要找的结果可能如下：</big></big>"]
    for link in links:
        line = f"*<big>'''[[{link.page_name}]]'''"
        if link.activity_name is not None:
            line += f"（[[{link.activity_name}]]关卡）"
        line += "</big>"
        lines.append(line)
    return "\n".join(lines)


class ActionInfo:
    def __init__(self, action: LevelDataWaveDataFragmentDataActionData) -> None:
        if action.action_type == "SPAWN" and action.key != "":
            self.key = action.key
        else:
            self.key = None
        if self.key is not None:
            self.time = action.pre_delay + (action.count - 1) * action.interval
            self.count = action.count
        else:
            self.time = 0.0
            self.count = 0
        self.hidden_group = action.hidden_group
        self.random_type = 0
        self.random_key = action.random_spawn_group_key
        if self.random_key is not None:
            self.random_type += 1
        self.random_pack = action.random_spawn_group_pack_key
        if self.random_pack is not None:
            self.random_type += 2

    def update_pack(self, pack_dict: dict[str, str]) -> None:
        if self.random_key is None and self.random_pack is not None:
            if self.random_pack in pack_dict:
                self.random_key = pack_dict[self.random_pack]
            else:
                logger.info(
                    f"Error: cannot find random_key for pack {self.random_pack}"
                )


def check_duplicate(
    stage_table: StageTable, activity_table: ActivityTable
) -> dict[str, str]:
    """同名关卡代号 -> 消歧义页 wikitext。"""
    stages = stage_table.stages or {}
    basic_info = activity_table.basic_info or {}

    stage_code_dict: dict[str, list[str]] = {}
    duplicate_dict: dict[str, str] = {}
    for s in stages.values():
        if s.name is None or s.code is None:
            continue
        if (
            s.difficulty in ["FOUR_STAR", "SIX_STAR"]
            or s.stage_type == "GUIDE"
            or s.diff_group in ["EASY", "TOUGH"]
        ):
            continue
        # 沿用旧代码:判重用原始 code,建键用 strip 后的 code
        if s.code not in stage_code_dict:
            stage_code_dict[s.code.strip()] = []
        stage_code_dict[s.code.strip()].append(_require(s.stage_id, "stageId"))
    for code, s_list in stage_code_dict.items():
        if len(s_list) > 1:
            links = []
            seen_links = set()
            for sid in s_list:
                target = stages[sid]
                activity_name = None
                if target.stage_type == "ACTIVITY":
                    result = _require(re.search("^([^_]+)[_-]", sid), "activity id")
                    act_id = result.group(1)
                    if act_id in basic_info:
                        activity_name = _require(
                            basic_info[act_id].name, "name"
                        ).replace("#", "/0")
                page_name = "{} {}".format(
                    (target.code or "").strip(), (target.name or "").strip()
                )
                link_key = (page_name, activity_name)
                if link_key not in seen_links:
                    links.append(
                        DisambiguationLinkView(
                            page_name=page_name,
                            activity_name=activity_name,
                        )
                    )
                    seen_links.add(link_key)
            duplicate_dict[code] = render_disambiguation(links)
    return duplicate_dict


def _get_list_not_count_in_total(enemy_levels: EnemyLevelIndex) -> NotCountList:
    """enemy_database 里标记了 notCountInTotal 的敌人及其 level。

    某一级明确标记为 true 时记下该级;未定义的级别若紧接着已记下的上一级,
    视为沿用上一级的标记。
    """

    not_count_list: NotCountList = {}
    for key, levels in enemy_levels.items():
        for enemy_level in levels:
            data = enemy_level.enemy_data
            flag = data.not_count_in_total if data is not None else None
            if flag is None:
                continue
            if flag.m_defined is True:
                if flag.m_value is True:
                    if key not in not_count_list:
                        not_count_list[key] = []
                    not_count_list[key].append(enemy_level.level)
            elif key in not_count_list and enemy_level.level - 1 in not_count_list[key]:
                not_count_list[key].append(enemy_level.level)
    return not_count_list


def _build_enemy_views(
    level: LevelData,
    enemy_handbook_table: EnemyHandBookDataGroup,
    enemy_levels: EnemyLevelIndex,
    flag_skip0: bool = False,
) -> list[EnemyView]:
    return build_enemies(
        level, enemy_handbook_table.enemy_data or {}, enemy_levels, flag_skip0
    )


async def _existing_stage_ids(wiki: Wiki, pages: dict[str, str]) -> set[str]:
    """``pages`` 是 stageId → 按名字拼出、但分类里没有的页面名;返回其中已经建过页的。

    关卡改名后(如 6-13「没有火,没有光」的逗号改成全角)按名字找不到旧页面,
    会被当成新关卡再建一页、写进首页/新增关卡。建页时总会顺手建一个以 stageId
    命名的重定向页,它仍指向旧页面,能解析到已有页面就说明这关早就建过;
    旧页面要不要随之改名留给编辑处理。
    """

    existing = await wiki.resolve(pages)
    for stage_id, page in existing.items():
        logger.warning(
            f"{stage_id} already has page {page!r}, "
            f"skip creating {pages[stage_id]!r} (stage renamed?)."
        )
    return set(existing)


@job
async def run(
    wiki: Wiki,
    stage_table: Annotated[StageTable, table("stage_table")],
    activity_table: Annotated[ActivityTable, table("activity_table")],
    zone_table: Annotated[ZoneTable, table("zone_table")],
    character_table: CharacterTable,
    skill_table: SkillTable,
    building_data: Annotated[BuildingData, table("building_data")],
    item_table: ItemTable,
    battle_misc_table: BattleMiscTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    stages = stage_table.stages or {}
    level_scene_pairs = battle_misc_table.level_scene_pairs or {}

    stage_list = await wiki.category("分类:普通难度关卡")
    new_stage_list: list[tuple[StageData, str]] = []
    duplicate_dict = check_duplicate(stage_table, activity_table)
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    # 先筛出要建页的关卡,把它们的关卡文件一次并发下载进缓存,再逐个建页
    candidates: list[tuple[str, StageData, str, str]] = []
    for stage_id, stage in stages.items():
        if stage.name is None or stage.code is None:
            continue
        if (
            stage.stage_type
            not in [
                "MAIN",
                "SUB",
                "DAILY",
                "ACTIVITY",
                "SPECIAL_STORY",
                "CLIMB_TOWER",
            ]
            or stage.difficulty in ["FOUR_STAR"]
            or stage.diff_group in ["EASY"]
        ):
            continue
        # 改名直接写回表里:后面的关卡在解锁条件里引用它时,用的就是这个名字
        stage.name = {
            "act21side_01_t": "新城区大街(德克萨斯)",
            "act21side_02_t": "萨卢佐家(拉普兰德2)",
            "act21side_03_m2": "后巷(拉普兰德1)",
            "act21side_04_m1": "萨卢佐家(拉普兰德1)",
            "act21side_05_m1": "后巷(乔万娜)",
            "act21side_05_t": "后巷(拉普兰德2)",
            "act21side_06_t": "新城区大街(丹布朗)",
        }.get(stage_id, stage.name.strip())
        code = stage.code.strip()
        stage_page_name = code + " " + stage.name
        if stage.difficulty == "SIX_STAR":
            stage_page_name = "险地" + stage_page_name
        elif (
            stage.diff_group == "TOUGH" and stage.appearance_style != "HIGH_DIFFICULTY"
        ):
            stage_page_name = "磨难" + stage_page_name
        if stage_page_name in stage_list:
            continue
        candidates.append((stage_id, stage, code, stage_page_name))
    existing = await _existing_stage_ids(
        wiki, {stage_id: page for stage_id, _, _, page in candidates}
    )
    candidates = [c for c in candidates if c[0] not in existing]

    # 预取时不校验 pair.level_id:缺失的情况留给下面的循环按原逻辑记日志跳过
    await levels.prefetch(
        pair.level_id if pair is not None and pair.level_id else stage.level_id
        for _, stage, _, _ in candidates
        if stage.level_id
        for pair in (level_scene_pairs.get(stage.level_id),)
    )

    for stage_id, stage, code, stage_page_name in candidates:
        map_override = ""
        level = None
        if stage.level_id:
            try:
                # battle_misc_table 登记了替换场景的关卡,读实际加载的那份关卡文件
                pair = level_scene_pairs.get(stage.level_id)
                if pair is not None:
                    level = await levels(_require(pair.level_id, "levelId"))
                    if pair.hooked_map_preview_id is not None:
                        map_override = pair.hooked_map_preview_id
                else:
                    level = await levels(stage.level_id)
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        normal_stage = build_normal_stage(
            stage,
            stage_table,
            zone_table,
            character_table,
            building_data,
            item_table,
            level,
            not_count_list,
            rts.compile,
            map_override=map_override,
        )
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )
        assault_stage = None
        if stage.hard_staged_id:
            assault_stage = build_4star_stage(
                stages[stage.hard_staged_id],
                stage_table,
                zone_table,
                character_table,
                building_data,
                item_table,
                _require(level, "level"),
                rts.compile,
            )
        # dropType 在数据里是枚举名,这个数字比较沿用旧代码(恒为 False),
        # 页面输出与迁移前一致;要不要改成按枚举名判断另行决定
        has_material_drop = any(
            reward.drop_type in [2, 3, 4] for reward in _display_detail_rewards(stage)
        )
        squads = (
            build_squad_sections(level, stage_page_name, character_table, skill_table)
            if level is not None
            else []
        )

        stage_content = render_normal_page(
            NormalPageView(
                normal=normal_stage,
                assault=assault_stage,
                enemies=enemies,
                squads=squads,
                material_drop=has_material_drop,
            )
        )
        stage_redirect = f"#redirect [[{stage_page_name}]]"

        if code in duplicate_dict:
            await wiki.edit(title=code, text=duplicate_dict[code], summary="消歧义")
        else:
            if stage.difficulty == "SIX_STAR":
                redirect_title = "险地" + code
            elif (
                stage.diff_group == "TOUGH"
                and stage.appearance_style != "HIGH_DIFFICULTY"
            ):
                redirect_title = "磨难" + code
            else:
                redirect_title = code
            await wiki.edit(
                title=redirect_title,
                text=stage_redirect,
                summary="init",
                createonly="1",
            )
        await wiki.edit(
            title=_require(stage.stage_id, "stageId").strip(),
            text=stage_redirect,
            summary="init",
            createonly="1",
        )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            createonly="1",
            bot=None,
            minor=True,
        )
        logger.info(f"Created: {stage_page_name}.")

        new_stage_list.append((stage, stage_page_name))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            text=render_new_stages(new_stage_list, zone_table, activity_table),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")


@job
async def run_campaign(
    wiki: Wiki,
    stage_table: Annotated[StageTable, table("stage_table")],
    campaign_table: Annotated[CampaignTable, table("campaign_table")],
    character_table: CharacterTable,
    skill_table: SkillTable,
    building_data: Annotated[BuildingData, table("building_data")],
    item_table: ItemTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    stages = stage_table.stages or {}
    campaigns = campaign_table.campaigns or {}

    stage_list = await wiki.category("分类:剿灭关卡")
    new_stage_list: list[tuple[str, str]] = []
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    candidates: list[tuple[StageData, str, str]] = []
    for stage in stages.values():
        if stage.stage_type != "CAMPAIGN":
            continue
        name = _require(stage.name, "name").strip()
        stage_page_name = _require(stage.code, "code").strip() + " " + name
        if stage_page_name in stage_list:
            continue
        candidates.append((stage, name, stage_page_name))
    existing = await _existing_stage_ids(
        wiki, {_require(s.stage_id, "stageId"): page for s, _, page in candidates}
    )
    candidates = [c for c in candidates if c[0].stage_id not in existing]

    await levels.prefetch(
        stage.level_id for stage, _, _ in candidates if stage.level_id
    )

    for stage, name, stage_page_name in candidates:
        level = None
        if stage.level_id:
            try:
                level = await levels(stage.level_id)
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        campaign_stage = build_campaign_stage(
            stage,
            stage_table,
            campaign_table,
            character_table,
            building_data,
            item_table,
            level,
            not_count_list,
            rts.compile,
        )
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )
        squads = (
            build_squad_sections(
                level,
                stage_page_name,
                character_table,
                skill_table,
                include_inserted=False,
            )
            if level is not None
            else []
        )
        stage_id = _require(stage.stage_id, "stageId")
        progress_rows = []
        for r in campaigns[stage_id].break_ladders or []:
            progress_rows.append(
                CampaignProgressRowView(
                    kill_count=r.kill_cnt,
                    items=[
                        CampaignProgressItemView(
                            name=parse_drop_item(
                                reward.type,
                                reward.id,
                                character_table,
                                building_data,
                                item_table,
                            ),
                            count=reward.count,
                        )
                        for reward in r.rewards or []
                    ],
                    break_fee_add=r.break_fee_add,
                )
            )

        stage_content = render_campaign_page(
            CampaignPageView(
                stage=campaign_stage,
                enemies=enemies,
                squads=squads,
                progress=CampaignProgressView(rows=progress_rows),
            )
        )
        stage_redirect = f"#redirect [[{stage_page_name}]]"

        await wiki.edit(
            title=name,
            text=stage_redirect,
            summary="init",
            createonly="1",
        )
        await wiki.edit(
            title=stage_id.strip(),
            text=stage_redirect,
            summary="init",
            createonly="1",
        )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            bot=None,
            minor=True,
        )
        logger.info(f"Created: {stage_page_name}.")

        new_stage_list.append(((stage.code or "").strip(), stage_page_name))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            text=render_stage_list("剿灭作战", new_stage_list),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")


@job
async def run_crisis(
    wiki: Wiki,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    # 危机合约的关卡表不在 gamedata 里,从 weedy 读(外部数据,保持 dict)
    # https://weedy.prts.wiki/crisis_info.json
    async with make_client() as client:
        resp = await client.get(
            "https://weedy.prts.wiki/crisis_info.json", follow_redirects=True
        )
        resp.raise_for_status()
        stage_list = resp.json()["info"]["mapStageDataMap"]
    await levels.prefetch(
        stage_detail["levelId"]
        for stage_detail in stage_list.values()
        if stage_detail["levelId"]
    )
    for stage_detail in stage_list.values():
        stage_page_name = (
            stage_detail["code"].strip() + " " + stage_detail["name"].strip()
        )

        level = None
        if stage_detail["levelId"]:
            try:
                level = await levels(stage_detail["levelId"])
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        crisis_stage = build_crisis_stage(
            stage_detail, level, not_count_list, rts.compile
        )
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )

        stage_content = render_basic_page(
            BasicPageView(stage=crisis_stage, enemies=enemies),
            notoc=True,
            extra_sections=["==合约详情==\n{{合约详情}}"],
            categories=["[[分类:危机合约关卡]]"],
        )
        stage_redirect = f"#redirect [[{stage_page_name}]]"

        await wiki.edit(
            title=stage_detail["name"].strip(),
            text=stage_redirect,
            summary="init",
            createonly="1",
        )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            bot=None,
            minor=True,
            createonly="1",
        )
        logger.info(f"Created: {stage_page_name}.")


ROGUE_TOPIC = "rogue_6"
"""run_rogue_like 处理的集成战略主题。"""

ROGUE_DLC_SUFFIX = {"rogue_5": "今昔境", "rogue_6": "熄日余径"}
"""DLC 关卡(``*_dlc1``)与本体关卡同名,单独建「代号 名字(后缀)」页面;后缀由编辑组定。"""


def insert_see_also(text: str, see_also: str) -> str:
    """把 {{参阅}} 插到页面开头的 {{pathnav2}} 之后(没有 pathnav2 时放在最前)。"""
    head, sep, rest = text.partition("\n")
    if head.startswith("{{pathnav2"):
        return f"{head}\n{see_also}{sep}{rest}"
    return f"{see_also}\n{text}"


@job
async def run_rogue_like(
    wiki: Wiki,
    roguelike_topic_table: RoguelikeTopicTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    rogue_stages = (roguelike_topic_table.details or {})[ROGUE_TOPIC].stages or {}
    dlc_suffix = ROGUE_DLC_SUFFIX.get(ROGUE_TOPIC)
    # (本体页面, DLC 页面),循环结束后给本体页面补上指向 DLC 页面的 {{参阅}}
    dlc_pages: list[tuple[str, str]] = []

    not_count_list = _get_list_not_count_in_total(enemy_levels)

    await levels.prefetch(
        stage.level_replace_ids[0] if stage.level_replace_ids else stage.level_id
        for stage_key, stage in rogue_stages.items()
        if stage.difficulty != "FOUR_STAR" and stage_key != "ro4_b_9" and stage.level_id
    )

    for stage_key, stage in rogue_stages.items():
        if stage.difficulty == "FOUR_STAR":
            continue
        if stage_key == "ro4_b_9":
            continue

        name = _require(stage.name, "name").strip()
        base_page_name = _require(stage.code, "code").strip() + " " + name
        is_dlc = dlc_suffix is not None and stage_key.endswith("_dlc1")
        if is_dlc:
            stage_page_name = f"{base_page_name}({dlc_suffix})"
            see_also = (base_page_name, f"{dlc_suffix}外的该关卡")
        else:
            stage_page_name = base_page_name
            see_also = None

        level = None
        if stage.level_id:
            try:
                if stage.level_replace_ids and len(stage.level_replace_ids) >= 1:
                    level = await levels(stage.level_replace_ids[0])
                else:
                    level = await levels(stage.level_id)
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        normal_stage = build_roguelike_stage(stage, level, not_count_list, rts.compile)
        linked_stages = [
            k for k, s in rogue_stages.items() if s.linked_stage_id == stage_key
        ]
        if len(linked_stages) >= 1:
            assault_stage = build_roguelike_4star_stage(
                rogue_stages[linked_stages[0]],
                _require(level, "level"),
                rts.compile,
            )
        else:
            assault_stage = None
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )

        stage_content = render_roguelike_page(
            RoguelikePageView(
                normal=normal_stage,
                assault=assault_stage,
                enemies=enemies,
                see_also=see_also,
            )
        )

        if is_dlc:
            # 同名重定向归本体页面
            dlc_pages.append((base_page_name, stage_page_name))
        else:
            await wiki.edit(
                title=name,
                text=f"#redirect [[{stage_page_name}]]",
                summary="init",
                createonly="1",
            )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            bot=None,
            minor=True,
            createonly="1",
        )
        logger.info(f"Created: {stage_page_name}.")

    # 本体页面在上面的循环里已经建好(或早已存在),统一在这里补 {{参阅}}
    for base_page_name, dlc_page_name in dlc_pages:
        try:
            text = await wiki.read(base_page_name)
        except KeyError:
            logger.warning(f"本体页面 {base_page_name} 不存在,未添加参阅")
            continue
        if dlc_page_name in text:
            continue
        see_also_line = inline_template(
            "参阅", dlc_page_name, f"{dlc_suffix}中的该关卡"
        )
        await wiki.edit(
            title=base_page_name,
            text=insert_see_also(text, see_also_line),
            summary=f"参阅{dlc_suffix}关卡",
            minor=True,
            nocreate=True,
        )
        logger.info(f"Updated: {base_page_name}.")


@job
async def run_memory(
    wiki: Wiki,
    handbook_info_table: HandbookInfoTable,
    character_table: CharacterTable,
    skill_table: SkillTable,
    building_data: Annotated[BuildingData, table("building_data")],
    item_table: ItemTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    stage_list = await wiki.category("分类:悖论模拟关卡")
    new_stage_list: list[tuple[str, str]] = []
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    candidates: list[tuple[HandbookStoryStageData, str, str]] = []
    for stage in (handbook_info_table.handbook_stage_data or {}).values():
        name = _require(stage.name, "name").strip()
        stage_page_name = f"悖论模拟 {name}"
        if stage_page_name in stage_list:
            continue
        candidates.append((stage, name, stage_page_name))

    await levels.prefetch(
        stage.level_id for stage, _, _ in candidates if stage.level_id
    )

    for stage, name, stage_page_name in candidates:
        level = None
        if stage.level_id:
            try:
                level = await levels(stage.level_id)
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        memory_stage = build_memory_stage(
            stage,
            level,
            rts.compile,
            character_table,
            building_data,
            item_table,
            not_count_list,
        )
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )
        squads = (
            build_squad_sections(
                level,
                stage_page_name,
                character_table,
                skill_table,
                stage_char_id=stage.char_id,
            )
            if level is not None
            else []
        )

        stage_content = render_basic_page(
            BasicPageView(
                stage=memory_stage,
                enemies=enemies,
                squads=squads,
            ),
            notoc=True,
        )
        stage_redirect = f"#redirect [[{stage_page_name}]]"

        await wiki.edit(
            title=name,
            text=stage_redirect,
            summary="init",
            createonly="1",
        )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            createonly="1",
            bot=None,
            minor=True,
        )
        logger.info(f"Created: {stage_page_name}.")

        new_stage_list.append(("", stage_page_name))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            appendtext="\n" + render_stage_list("悖论模拟", new_stage_list),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")


@job
async def run_sandbox(
    wiki: Wiki,
    sandbox_perm_table: SandboxPermTable,
    character_table: CharacterTable,
    skill_table: SkillTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    sandbox_acts = _require(sandbox_perm_table.detail, "detail").sandbox_v2 or {}

    stage_list = await wiki.category("分类:生息演算关卡")
    new_stage_list: list[tuple[str, str]] = []
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    candidates: list[tuple[SandboxV2StageData, str]] = []
    for act in sandbox_acts.values():
        for stage in (act.stage_data or {}).values():
            stage.name = _require(stage.name, "name").strip()
            stage_page_name = f"{stage.code} {stage.name}(沙洲遗闻)"
            if stage_page_name in stage_list:
                continue
            candidates.append((stage, stage_page_name))

    await levels.prefetch(stage.level_id for stage, _ in candidates if stage.level_id)

    for stage, stage_page_name in candidates:
        # /data 页面要原样发布整个关卡 JSON,所以先取原始 dict 再自己校验
        level = None
        raw_level: dict = {}
        if stage.level_id:
            try:
                raw_level = await levels.raw(stage.level_id)
                level = LevelData.model_validate(raw_level)
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        sandbox_stage = build_sandbox_v2_stage(
            stage, rts.compile, level, not_count_list
        )
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )
        squads = (
            build_squad_sections(level, stage_page_name, character_table, skill_table)
            if level is not None
            else []
        )
        # 生息演算页面不加 __NOTOC__,与 crisis/memory/mechanism/id 不同
        stage_content = render_basic_page(
            BasicPageView(
                stage=sandbox_stage,
                enemies=enemies,
                squads=squads,
            ),
        )

        await wiki.edit(
            title=stage_page_name + "/data",
            text=json.dumps(raw_level, ensure_ascii=False),
            summary="init",
            createonly=True,
            contentmodel="json",
        )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            createonly=True,
            bot=None,
            minor=True,
        )
        logger.info(f"Created: {stage_page_name}.")

        new_stage_list.append((stage.code or "", stage_page_name))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            appendtext="\n" + render_stage_list("生息演算", new_stage_list),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")


@job
async def run_mechanism(
    wiki: Wiki,
    story_review_meta_table: StoryReviewMetaTable,
    character_table: CharacterTable,
    skill_table: SkillTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
) -> None:
    training_camp = _require(
        story_review_meta_table.training_camp_data, "trainingCampData"
    )

    new_stage_list: list[tuple[str, str]] = []
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    await levels.prefetch(
        stage.level_id
        for stage in (training_camp.stage_data or {}).values()
        if stage.level_id
    )

    for stage in (training_camp.stage_data or {}).values():
        name = _require(stage.name, "name").strip()
        stage_page_name = f"{stage.code} {name}"

        # 训练场关卡一定带关卡文件;没有的话页面上的地图信息无从谈起
        if not stage.level_id:
            logger.info(f"Cannot find level data of {stage_page_name}.")
            continue
        try:
            level = await levels(stage.level_id)
        except Exception:
            logger.info(f"Cannot find level data of {stage_page_name}.")
            continue

        mechanism_stage = BasicStageView(
            code=_require(stage.code, "code"),
            name=name,
            stage_id=_require(stage.stage_id, "stageId"),
            stage_type="训练场",
            difficulty="NORMAL",
            unlock_condition="—",
            recommended_level="—",
            zone="-",
            level=build_level_info(level, not_count_list),
            description=stage.description,
            ap_cost=0,
            practice_cost=-1,
        )

        enemies = _build_enemy_views(level, enemy_handbook_table, enemy_levels)
        squads = build_squad_sections(
            level, stage_page_name, character_table, skill_table
        )
        stage_content = render_basic_page(
            BasicPageView(
                stage=mechanism_stage,
                enemies=enemies,
                squads=squads,
            ),
            notoc=True,
        )

        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            bot=None,
            minor=True,
        )
        logger.info(f"Created: {stage_page_name}.")
        new_stage_list.append((stage.code or "", stage_page_name))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            appendtext="\n" + render_stage_list("训练场", new_stage_list),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")


@job
async def run_recalrune(
    wiki: Wiki,
    crisis_v2_table: CrisisV2Table,
    character_table: CharacterTable,
    skill_table: SkillTable,
    enemy_handbook_table: EnemyHandbookTable,
    enemy_levels: EnemyLevels,
    levels: Levels,
    rts: RichText,
) -> None:
    recal_rune_data = _require(crisis_v2_table.recal_rune_data, "recalRuneData")

    stage_list = await wiki.category("分类:全息作战矩阵关卡")
    new_stage_list: list[tuple[str, str]] = []
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    candidates: list[tuple[RecalRuneStageData, str, str]] = []
    for season_info in (recal_rune_data.seasons or {}).values():
        for stage in (season_info.stages or {}).values():
            stage.level_name = _require(stage.level_name, "levelName").strip()
            level_name = stage.level_name
            stage_page_name = f"全息{stage.level_code} {level_name.replace('#', '＃')}"
            if stage_page_name in stage_list:
                continue
            candidates.append((stage, level_name, stage_page_name))

    await levels.prefetch(
        stage.level_id for stage, _, _ in candidates if stage.level_id
    )

    for stage, level_name, stage_page_name in candidates:
        level = None
        if stage.level_id:
            try:
                level = await levels(stage.level_id)
            except Exception:
                logger.info(f"Cannot find level data of {stage_page_name}.")
                continue

        recal_rune_stage = build_recal_rune_stage(
            stage, rts.compile, level, not_count_list
        )
        enemies = (
            _build_enemy_views(level, enemy_handbook_table, enemy_levels)
            if level is not None
            else None
        )
        squads = (
            build_squad_sections(level, stage_page_name, character_table, skill_table)
            if level is not None
            else []
        )
        stage_content = render_recal_rune_page(
            RecalRunePageView(
                stage=recal_rune_stage,
                enemies=enemies,
                squads=squads,
                display_title=f"全息{stage.level_code} {level_name}",
            )
        )
        stage_redirect = f"#redirect [[{stage_page_name}]]"

        await wiki.edit(
            title=f"全息{stage.level_code}",
            text=stage_redirect,
            summary="init",
            createonly="1",
        )
        await wiki.edit(
            title=stage_page_name,
            text=stage_content,
            summary="init",
            createonly=True,
            bot=None,
            minor=True,
        )
        logger.info(f"Created: {stage_page_name}.")

        new_stage_list.append((stage.level_code or "", stage_page_name))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            appendtext="\n" + render_stage_list("全息作战矩阵", new_stage_list),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")


async def run_id(
    wiki: Wiki,
    levels: LevelLoader,
    path: str,
    *,
    stage_table: StageTable,
    character_table: dict[str, CharacterData],
    skill_table: dict[str, SkillDataBundle],
    enemy_handbook_table: EnemyHandBookDataGroup,
    enemy_levels: EnemyLevelIndex,
) -> None:
    """手动调用的调试入口:把 ``gamedata/<path>`` 下尚未登记进 stage_table 的
    关卡文件各建一页。带额外参数,不注册成 job,调用方自己准备好各张表。"""

    known_level_ids = {
        stage.level_id.lower()
        for stage in (stage_table.stages or {}).values()
        if stage.level_id is not None
    }
    not_count_list = _get_list_not_count_in_total(enemy_levels)

    new_stage_list: list[tuple[str, str]] = []
    level_ids = await levels.list_ids(path)
    await levels.prefetch(
        level_id for level_id in level_ids if level_id.lower() not in known_level_ids
    )
    for level_id in level_ids:
        stage_id = level_id.rsplit("/", 1)[-1]
        if level_id.lower() in known_level_ids:
            logger.info(f"{stage_id} already in stage_table. Pass.")
            continue
        level = await levels(level_id)

        unknown_stage = BasicStageView(
            code="—",
            name=stage_id,
            stage_id=stage_id.replace("level_", ""),
            stage_type="活动",
            difficulty="NORMAL",
            unlock_condition="—",
            recommended_level="—",
            zone="-",
            level=build_level_info(level, not_count_list),
            description="",
            ap_cost=0,
            practice_cost=-1,
        )

        enemies = _build_enemy_views(level, enemy_handbook_table, enemy_levels)
        squads = build_squad_sections(level, stage_id, character_table, skill_table)
        stage_content = render_basic_page(
            BasicPageView(
                stage=unknown_stage,
                enemies=enemies,
                squads=squads,
            ),
            notoc=True,
        )

        await wiki.edit(
            title=stage_id, text=stage_content, summary="init", bot=None, minor=True
        )
        logger.info(f"Created: {stage_id}.")
        new_stage_list.append(("", stage_id))

    if new_stage_list != []:
        await wiki.edit(
            title=NEW_STAGES_PAGE,
            appendtext="\n" + render_stage_list("", new_stage_list),
            summary="update",
            bot=None,
            minor=True,
        )
        logger.info(f"Updated: {NEW_STAGES_PAGE}.")

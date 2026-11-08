"""roguelike_table.json(初代集成战略,已停更)的数据模型(手写)。

这张旧表在客户端里是普通 JSON,OpenArknightsFBS 里没有它的 schema;
这里按客户端 ``Torappu.RoguelikeTable`` 手写 ``itemTable`` 与 ``stages``,
其余键(``constTable`` / ``zones`` / ``choices`` …)原样忽略。
``itemTable.items`` 同时包含收藏品、分队效果和招募券等物品,由调用方按 ``type`` 筛选;
现行集成战略数据在 ``roguelike_topic_table``。
"""

from ptilopsis.gamedata._base import GameDataModel

__all__ = [
    "BlackboardDataPair",
    "RoguelikeBuff",
    "RoguelikeItem",
    "RoguelikeItemTable",
    "RoguelikeRecruitTicket",
    "RoguelikeRelic",
    "RoguelikeStableUnlockCondition",
    "RoguelikeStage",
    "RoguelikeTable",
    "RoguelikeUpgradeTicket",
]


class RoguelikeStableUnlockCondition(GameDataModel):
    """clz_Torappu_RelicStableUnlockParam"""

    unlock_cond_detail: str | None = None
    unlock_cnt: int = 0


class RoguelikeItem(GameDataModel):
    """clz_Torappu_RoguelikeItemData"""

    id: str | None = None
    name: str | None = None
    description: str | None = None
    usage: str | None = None
    obtain_approach: str | None = None
    icon_id: str | None = None
    # enum__Torappu_RoguelikeItemType 的成员名
    type: str = "NONE"
    # enum__Torappu_RoguelikeItemRarity 的成员名
    rarity: str = "NONE"
    value: int = 0
    sort_id: int = 0
    unlock_cond: str | None = None
    unlock_cond_desc: str | None = None
    unlock_cond_params: list[str] | None = None
    stable_unlock_cond: RoguelikeStableUnlockCondition | None = None


class BlackboardDataPair(GameDataModel):
    """clz_Torappu_Blackboard_DataPair"""

    key: str | None = None
    value: float = 0.0
    value_str: str | None = None


class RoguelikeBuff(GameDataModel):
    """clz_Torappu_RoguelikeBuff"""

    key: str | None = None
    blackboard: list[BlackboardDataPair] | None = None


class RoguelikeRelic(GameDataModel):
    """clz_Torappu_RoguelikeRelicFeature"""

    id: str | None = None
    buffs: list[RoguelikeBuff] | None = None


class RoguelikeRecruitTicket(GameDataModel):
    """clz_Torappu_RoguelikeRecruitTicketFeature"""

    id: str | None = None
    # 旧表里位掩码枚举存的是数值:enum__Torappu_ProfessionCategory /
    # enum__Torappu_RarityRankMask;展开后的列表分别是职业成员名和
    # enum__Torappu_RarityRank 的数值(0 = 一星)
    profession: int = 0
    rarity: int = 0
    profession_list: list[str] | None = None
    rarity_list: list[int] | None = None
    extra_elite_num: int = 0
    extra_free_rarity: list[int] | None = None
    extra_char_ids: list[str] | None = None


class RoguelikeUpgradeTicket(GameDataModel):
    """clz_Torappu_RoguelikeUpgradeTicketFeature"""

    id: str | None = None
    # 取值同 RoguelikeRecruitTicket
    profession: int = 0
    rarity: int = 0
    profession_list: list[str] | None = None
    rarity_list: list[int] | None = None


class RoguelikeItemTable(GameDataModel):
    """clz_Torappu_RoguelikeItemTable"""

    items: dict[str, RoguelikeItem] | None = None
    # 以下三张表的键分别是 items 里 type 为 RECRUIT_TICKET / UPGRADE_TICKET /
    # RELIC 的物品 id
    recruit_tickets: dict[str, RoguelikeRecruitTicket] | None = None
    upgrade_tickets: dict[str, RoguelikeUpgradeTicket] | None = None
    relics: dict[str, RoguelikeRelic] | None = None


class RoguelikeStage(GameDataModel):
    """clz_Torappu_RoguelikeStageData"""

    id: str | None = None
    linked_stage_id: str | None = None
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None
    description: str | None = None
    elite_desc: str | None = None
    is_boss: int = 0
    is_elite: int = 0
    # enum__Torappu_LevelData_Difficulty 的成员名
    difficulty: str = "NONE"


class RoguelikeTable(GameDataModel):
    """clz_Torappu_RoguelikeTable(仅 itemTable / stages)"""

    item_table: RoguelikeItemTable | None = None
    stages: dict[str, RoguelikeStage] | None = None

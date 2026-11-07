"""roguelike_table.json(初代集成战略,已停更)的数据模型(手写)。

这张旧表没有 FBS schema,手写关卡与物品数据模型。
``itemTable.items`` 同时包含收藏品、分队效果和招募券等物品,由调用方按类型筛选;
现行集成战略数据在 ``roguelike_topic_table``。
"""

from ptilopsis.gamedata._base import GameDataModel

__all__ = [
    "RoguelikeItem",
    "RoguelikeItemTable",
    "RoguelikeStableUnlockCondition",
    "RoguelikeStage",
    "RoguelikeTable",
]


class RoguelikeStableUnlockCondition(GameDataModel):
    """跨局累计的物品解锁条件。"""

    unlock_cond_detail: str | None = None
    unlock_cnt: int = 0


class RoguelikeItem(GameDataModel):
    """初代集成战略物品,保留原表的售价、排序和解锁字段。"""

    id: str | None = None
    name: str | None = None
    description: str | None = None
    usage: str | None = None
    obtain_approach: str | None = None
    icon_id: str | None = None
    type: str = "NONE"
    rarity: str = "NONE"
    value: int = 0
    sort_id: int = 0
    unlock_cond: str | None = None
    unlock_cond_desc: str | None = None
    unlock_cond_params: list[str] | None = None
    stable_unlock_cond: RoguelikeStableUnlockCondition | None = None


class RoguelikeItemTable(GameDataModel):
    """旧表的物品目录,不在读取层过滤物品类型或稀有度。"""

    items: dict[str, RoguelikeItem] | None = None


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
    """初代集成战略的关卡与物品目录。"""

    item_table: RoguelikeItemTable | None = None
    stages: dict[str, RoguelikeStage] | None = None

"""story_review_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/story_review_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import TypeAdapter

from ptilopsis.gamedata._base import GameDataModel


class StoryReviewEntryType(IntEnum):
    """enum__Torappu_StoryReviewEntryType"""

    NONE = 0
    ACTIVITY = 1
    MINI_ACTIVITY = 2
    MAINLINE = 3


class StoryReviewType(IntEnum):
    """enum__Torappu_StoryReviewType"""

    NONE = 0
    ACTIVITY_STORY = 1
    MINI_STORY = 2
    MAIN_STORY = 3


class ItemType(IntEnum):
    """enum__Torappu_ItemType"""

    NONE = 0
    CHAR = 1
    CARD_EXP = 2
    MATERIAL = 3
    GOLD = 4
    EXP_PLAYER = 5
    TKT_TRY = 6
    TKT_RECRUIT = 7
    TKT_INST_FIN = 8
    TKT_GACHA = 9
    ACTIVITY_COIN = 10
    DIAMOND = 11
    DIAMOND_SHD = 12
    HGG_SHD = 13
    LGG_SHD = 14
    FURN = 15
    AP_GAMEPLAY = 16
    AP_BASE = 17
    SOCIAL_PT = 18
    CHAR_SKIN = 19
    TKT_GACHA_10 = 20
    TKT_GACHA_PRSV = 21
    AP_ITEM = 22
    AP_SUPPLY = 23
    RENAMING_CARD = 24
    RENAMING_CARD_2 = 25
    ET_STAGE = 26
    ACTIVITY_ITEM = 27
    VOUCHER_PICK = 28
    VOUCHER_CGACHA = 29
    VOUCHER_MGACHA = 30
    CRS_SHOP_COIN = 31
    CRS_RUNE_COIN = 32
    LMTGS_COIN = 33
    EPGS_COIN = 34
    LIMITED_TKT_GACHA_10 = 35
    LIMITED_FREE_GACHA = 36
    REP_COIN = 37
    ROGUELIKE = 38
    LINKAGE_TKT_GACHA_10 = 39
    VOUCHER_ELITE_II_4 = 40
    VOUCHER_ELITE_II_5 = 41
    VOUCHER_ELITE_II_6 = 42
    VOUCHER_SKIN = 43
    RETRO_COIN = 44
    PLAYER_AVATAR = 45
    UNI_COLLECTION = 46
    VOUCHER_FULL_POTENTIAL = 47
    RL_COIN = 48
    RETURN_CREDIT = 49
    MEDAL = 50
    CHARM = 51
    HOME_BACKGROUND = 52
    EXTERMINATION_AGENT = 53
    OPTIONAL_VOUCHER_PICK = 54
    ACT_CART_COMPONENT = 55
    VOUCHER_LEVELMAX_6 = 56
    VOUCHER_LEVELMAX_5 = 57
    VOUCHER_LEVELMAX_4 = 58
    VOUCHER_SKILL_SPECIALLEVELMAX_6 = 59
    VOUCHER_SKILL_SPECIALLEVELMAX_5 = 60
    VOUCHER_SKILL_SPECIALLEVELMAX_4 = 61
    ACTIVITY_POTENTIAL = 62
    ITEM_PACK = 63
    SANDBOX = 64
    FAVOR_ADD_ITEM = 65
    CLASSIC_SHD = 66
    CLASSIC_TKT_GACHA = 67
    CLASSIC_TKT_GACHA_10 = 68
    LIMITED_BUFF = 69
    CLASSIC_FES_PICK_TIER_5 = 70
    CLASSIC_FES_PICK_TIER_6 = 71
    RETURN_PROGRESS = 72
    NEW_PROGRESS = 73
    MCARD_VOUCHER = 74
    MATERIAL_ISSUE_VOUCHER = 75
    CRS_SHOP_COIN_V2 = 76
    HOME_THEME = 77
    SANDBOX_PERM = 78
    SANDBOX_TOKEN = 79
    TEMPLATE_TRAP = 80
    NAME_CARD_SKIN = 81
    EMOTICON_SET = 82
    EXCLUSIVE_TKT_GACHA = 83
    EXCLUSIVE_TKT_GACHA_10 = 84
    SO_CHAR_EXP = 85
    GIFTPACKAGE_TKT = 86
    VOUCHER_SKIN_V2 = 87
    RANDOM_VOUCHER_SKIN = 88
    ACT1VHALFIDLE_ITEM = 89
    PLOT_ITEM = 90
    MAGAZINE_LEAF = 91
    STICKER = 92
    ARKHUB = 93
    LINKAGE_TKT_GACHA = 94
    AUTOCHESS_SKIN = 95
    AUTOCHESS_MISSION_POINT = 96
    OPEN_SERVER_CREDIT = 97


class StoryReviewUnlockType(IntEnum):
    """enum__Torappu_StoryReviewUnlockType"""

    STAGE_CLEAR = 0
    USE_ITEM = 1
    BY_START_TIME = 2
    NOTHING = 3


class PlayerStageState(IntEnum):
    """enum__Torappu_PlayerStageState"""

    UNLOCKED = 0
    PLAYED = 1
    PASS = 2
    COMPLETE = 3


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class StoryDataConditionStageCondition(GameDataModel):
    """clz_Torappu_StoryData_Condition_StageCondition"""

    stage_id: str | None = None
    min_state: str = "UNLOCKED"
    max_state: str = "UNLOCKED"


class StoryReviewInfoClientData(GameDataModel):
    """clz_Torappu_StoryReviewInfoClientData"""

    story_review_type: str = "NONE"
    story_id: str | None = None
    story_group: str | None = None
    story_sort: int = 0
    story_dependence: str | None = None
    story_can_show: int = 0
    story_code: str | None = None
    story_name: str | None = None
    story_pic: str | None = None
    story_info: str | None = None
    story_can_enter: int = 0
    story_txt: str | None = None
    avg_tag: str | None = None
    un_lock_type: str = "STAGE_CLEAR"
    cost_item_type: str = "NONE"
    cost_item_id: str | None = None
    cost_item_count: int = 0
    stage_count: int = 0
    required_stages: list[StoryDataConditionStageCondition] | None = None


class StoryReviewGroupClientData(GameDataModel):
    """clz_Torappu_StoryReviewGroupClientData"""

    id: str | None = None
    name: str | None = None
    entry_type: str = "NONE"
    act_type: str = "NONE"
    start_time: int = 0
    end_time: int = 0
    start_show_time: int = 0
    end_show_time: int = 0
    remake_start_time: int = 0
    remake_end_time: int = 0
    story_entry_pic_id: str | None = None
    story_pic_id: str | None = None
    story_main_color: str | None = None
    custom_type: int = 0
    story_complete_medal_id: str | None = None
    rewards: list[ItemBundle] | None = None
    info_unlock_datas: list[StoryReviewInfoClientData] | None = None


# root_type clz_Torappu_SimpleKVTable_clz_Torappu_StoryReviewGroupClientData
# JSON 里去掉了外层的 story_reviews,直接是 {id: ...}
StoryReviewTable = TypeAdapter(dict[str, StoryReviewGroupClientData])


ItemBundle.model_rebuild()
StoryDataConditionStageCondition.model_rebuild()
StoryReviewInfoClientData.model_rebuild()
StoryReviewGroupClientData.model_rebuild()

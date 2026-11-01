"""handbook_info_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/handbook_info_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class DataUnlockType(IntEnum):
    """enum__Torappu_DataUnlockType"""

    DIRECT = 0
    AWAKE = 1
    FAVOR = 2
    STAGE = 3
    ITEM = 4
    NEVER = 5
    PATCH = 6
    NONE = 7


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


class ProfessionCategory(IntEnum):
    """enum__Torappu_ProfessionCategory"""

    NONE = 0
    WARRIOR = 1
    SNIPER = 2
    TANK = 4
    MEDIC = 8
    SUPPORT = 16
    CASTER = 32
    SPECIAL = 64
    TOKEN = 128
    TRAP = 256
    PIONEER = 512


class IllustNPCResType(IntEnum):
    """enum__Torappu_IllustNPCResType"""

    NONE = 0
    NPC = 1
    CHAR = 2


class HandbookDisplayConditionDisplayType(IntEnum):
    """enum__Torappu_HandbookDisplayCondition_DisplayType"""

    DISPLAY_IF_CHAREXIST = 0
    INVISIBLE_IF_CHAREXIST = 1


class HandBookStoryViewDataStoryText(GameDataModel):
    """clz_Torappu_HandBookStoryViewData_StoryText"""

    story_text: str | None = None
    un_lock_type: str = "DIRECT"
    un_lock_param: str | None = None
    show_type: str = "DIRECT"
    show_param: str | None = None
    un_lock_string: str | None = None
    patch_id_list: list[str] | None = None


class HandBookStoryViewData(GameDataModel):
    """clz_Torappu_HandBookStoryViewData"""

    stories: list[HandBookStoryViewDataStoryText] | None = None
    story_title: str | None = None
    un_lockor_not: bool = False


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class HandbookUnlockParam(GameDataModel):
    """clz_Torappu_HandbookUnlockParam"""

    unlock_type: str = "DIRECT"
    unlock_param_1: str | None = None
    unlock_param_2: str | None = None
    unlock_param_3: str | None = None


class HandbookAvgData(GameDataModel):
    """clz_Torappu_HandbookAvgData"""

    story_id: str | None = None
    story_set_id: str | None = None
    story_sort: int = 0
    story_can_show: bool = False
    story_intro: str | None = None
    story_info: str | None = None
    story_txt: str | None = None


class HandbookAvgGroupData(GameDataModel):
    """clz_Torappu_HandbookAvgGroupData"""

    story_set_id: str | None = None
    story_set_name: str | None = None
    sort_id: int = 0
    story_get_time: int = 0
    reward_item: list[ItemBundle] | None = None
    unlock_param: list[HandbookUnlockParam] | None = None
    avg_list: list[HandbookAvgData] | None = None
    char_id: str | None = None


class HandbookInfoData(GameDataModel):
    """clz_Torappu_HandbookInfoData"""

    char_id: str | None = Field(default=None, alias="charID")
    info_name: str | None = None
    is_limited: bool = False
    story_text_audio: list[HandBookStoryViewData] | None = None
    handbook_avg_list: list[HandbookAvgGroupData] | None = None


class NPCUnlock(GameDataModel):
    """clz_Torappu_NPCUnlock"""

    un_lock_type: str = "DIRECT"
    un_lock_param: str | None = None
    un_lock_string: str | None = None


class NPCData(GameDataModel):
    """clz_Torappu_NPCData"""

    npc_id: str | None = None
    name: str | None = None
    appellation: str | None = None
    profession: str = "NONE"
    illust_list: list[str] | None = None
    designer_list: list[str] | None = None
    cv: str | None = None
    display_number: str | None = None
    nation_id: str | None = None
    group_id: str | None = None
    team_id: str | None = None
    res_type: str = "NONE"
    npc_show_audio_info_flag: bool = False
    unlock_dict: dict[str, NPCUnlock] | None = None


class HandbookTeamMission(GameDataModel):
    """clz_Torappu_HandbookTeamMission"""

    id: str | None = None
    sort: int = 0
    power_id: str | None = None
    power_name: str | None = None
    item: ItemBundle | None = None
    favor_point: int = 0


class HandbookDisplayCondition(GameDataModel):
    """clz_Torappu_HandbookDisplayCondition"""

    char_id: str | None = None
    condition_char_id: str | None = None
    type: str = "DISPLAY_IF_CHAREXIST"


class HandbookStoryStageData(GameDataModel):
    """clz_Torappu_HandbookStoryStageData"""

    char_id: str | None = None
    stage_id: str | None = None
    level_id: str | None = None
    zone_id: str | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None
    description: str | None = None
    unlock_param: list[HandbookUnlockParam] | None = None
    reward_item: list[ItemBundle] | None = None
    stage_get_time: int = 0


class HandbookStageTimeData(GameDataModel):
    """clz_Torappu_HandbookStageTimeData"""

    timestamp: int = 0
    char_set: list[str] | None = None


class HandbookInfoTable(GameDataModel):
    """clz_Torappu_HandbookInfoTable"""

    handbook_dict: dict[str, HandbookInfoData] | None = None
    npc_dict: dict[str, NPCData] | None = None
    team_mission_list: dict[str, HandbookTeamMission] | None = None
    handbook_display_condition_list: dict[str, HandbookDisplayCondition] | None = None
    handbook_stage_data: dict[str, HandbookStoryStageData] | None = None
    handbook_stage_time: list[HandbookStageTimeData] | None = None


# root_type clz_Torappu_HandbookInfoTable


HandBookStoryViewDataStoryText.model_rebuild()
HandBookStoryViewData.model_rebuild()
ItemBundle.model_rebuild()
HandbookUnlockParam.model_rebuild()
HandbookAvgData.model_rebuild()
HandbookAvgGroupData.model_rebuild()
HandbookInfoData.model_rebuild()
NPCUnlock.model_rebuild()
NPCData.model_rebuild()
HandbookTeamMission.model_rebuild()
HandbookDisplayCondition.model_rebuild()
HandbookStoryStageData.model_rebuild()
HandbookStageTimeData.model_rebuild()
HandbookInfoTable.model_rebuild()

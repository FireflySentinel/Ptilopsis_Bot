"""zone_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/zone_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class ZoneType(IntEnum):
    """enum__Torappu_ZoneType"""

    NONE = 0
    MAINLINE = 1
    WEEKLY = 2
    ACTIVITY = 3
    GUIDE = 4
    TRAINING = 5
    CAMPAIGN = 6
    SIDESTORY = 7
    BRANCHLINE = 8
    ROGUELIKE = 9
    CLIMB_TOWER = 10
    MAINLINE_ACTIVITY = 11
    MAINLINE_RETRO = 12


class WeeklyType(IntEnum):
    """enum__Torappu_WeeklyType"""

    NONE = 0
    MATERIAL = 1
    SPECIAL = 2
    EVOLVE = 3


class MainlineZoneDataZoneReplayBtnType(IntEnum):
    """enum__Torappu_MainlineZoneData_ZoneReplayBtnType"""

    NONE = 0
    RECAP = 1
    REPLAY = 2


class StageDiffGroup(IntEnum):
    """enum__Torappu_StageDiffGroup"""

    NONE = 0
    EASY = 1
    NORMAL = 2
    TOUGH = 4
    ALL = 7


class RecordRewardStageDiff(IntEnum):
    """enum__Torappu_RecordRewardStageDiff"""

    NONE = 0
    EASY = 1
    NORMAL = 2
    TOUGH = 3
    PREDEFINED = 4
    HARD = 5


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


class ZoneData(GameDataModel):
    """clz_Torappu_ZoneData"""

    zone_id: str | None = Field(default=None, alias="zoneID")
    zone_index: int = 0
    type: str = "NONE"
    zone_name_first: str | None = None
    zone_name_second: str | None = None
    zone_name_title_current: str | None = None
    zone_name_title_un_current: str | None = None
    zone_name_title_ex: str | None = None
    zone_name_third: str | None = None
    locked_text: str | None = None
    anti_spoiler_id: str | None = None
    can_preview: bool = False
    has_additional_panel: bool = False
    six_star_milestone_group_id: str | None = None
    bind_mainline_zone_id: str | None = None
    bind_mainline_retro_zone_id: str | None = None
    diamond_reward_count: int = 0


class WeeklyZoneData(GameDataModel):
    """clz_Torappu_WeeklyZoneData"""

    days_of_week: list[int] | None = None
    type: str = "NONE"


class ZoneValidInfo(GameDataModel):
    """clz_Torappu_ZoneValidInfo"""

    start_ts: int = 0
    end_ts: int = 0


class MainlineZoneData(GameDataModel):
    """clz_Torappu_MainlineZoneData"""

    zone_id: str | None = None
    chapter_id: str | None = None
    preposed_zone_id: str | None = None
    zone_index: int = 0
    start_stage_id: str | None = None
    end_stage_id: str | None = None
    game_music_id: str | None = None
    recap_id: str | None = None
    recap_pre_stage_id: str | None = None
    button_name: str | None = None
    button_style: str = "NONE"
    spoil_alert: bool = False
    zone_open_time: int = 0
    diff_group: list[str] | None = None


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class RecordRewardInfo(GameDataModel):
    """clz_Torappu_RecordRewardInfo"""

    bind_stage_id: str | None = None
    stage_diff_1: str = "NONE"
    stage_diff: str = "NONE"
    pic_res: str | None = None
    text_path: str | None = None
    text_desc: str | None = None
    record_reward: list[ItemBundle] | None = None


class ZoneRecordData(GameDataModel):
    """clz_Torappu_ZoneRecordData"""

    record_id: str | None = None
    zone_id: str | None = None
    record_title_name: str | None = None
    pre_record_id: str | None = None
    node_title_1: str | None = None
    node_title_2: str | None = None
    rewards: list[RecordRewardInfo] | None = None


class ZoneRecordUnlockData(GameDataModel):
    """clz_Torappu_ZoneRecordUnlockData"""

    note_id: str | None = None
    zone_id: str | None = None
    initial_name: str | None = None
    final_name: str | None = None
    according_expose_id: str | None = None
    initial_des: str | None = None
    final_des: str | None = None
    remind_des: str | None = None


class ZoneRecordGroupData(GameDataModel):
    """clz_Torappu_ZoneRecordGroupData"""

    zone_id: str | None = None
    records: list[ZoneRecordData] | None = None
    unlock_data: ZoneRecordUnlockData | None = None


class ZoneRecordMissionData(GameDataModel):
    """clz_Torappu_ZoneRecordMissionData"""

    mission_id: str | None = None
    record_stage_id: str | None = None
    template_desc: str | None = None
    desc: str | None = None


class ZoneMetaData(GameDataModel):
    """clz_Torappu_ZoneMetaData"""

    zone_record_mission_data: dict[str, ZoneRecordMissionData] | None = Field(default=None, alias="ZoneRecordMissionData")


class ZoneTable(GameDataModel):
    """clz_Torappu_ZoneTable"""

    zones: dict[str, ZoneData] | None = None
    weekly_addition_info: dict[str, WeeklyZoneData] | None = None
    zone_valid_info: dict[str, ZoneValidInfo] | None = None
    mainline_addition_info: dict[str, MainlineZoneData] | None = None
    zone_record_grouped_data: dict[str, ZoneRecordGroupData] | None = None
    zone_record_reward_data: dict[str, list[str]] | None = None
    mainline_zone_id_list: list[str] | None = None
    zone_meta_data: ZoneMetaData | None = None


# root_type clz_Torappu_ZoneTable


ZoneData.model_rebuild()
WeeklyZoneData.model_rebuild()
ZoneValidInfo.model_rebuild()
MainlineZoneData.model_rebuild()
ItemBundle.model_rebuild()
RecordRewardInfo.model_rebuild()
ZoneRecordData.model_rebuild()
ZoneRecordUnlockData.model_rebuild()
ZoneRecordGroupData.model_rebuild()
ZoneRecordMissionData.model_rebuild()
ZoneMetaData.model_rebuild()
ZoneTable.model_rebuild()

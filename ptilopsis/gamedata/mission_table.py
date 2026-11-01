"""mission_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/mission_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class MissionType(IntEnum):
    """enum__Torappu_MissionType"""

    UNKNOWN = 0
    MAIN = 1
    DAILY = 2
    WEEKLY = 3
    GUIDE = 4
    SUB = 5
    ACTIVITY = 6
    OPENSERVER = 7
    TOWERSEASON = 8
    RETRO = 9
    SPECIAL_OPERATOR = 10
    SPECIAL_OPERATOR_WEEKLY = 11
    GUIDE_V3 = 12


class MissionItemBgType(IntEnum):
    """enum__Torappu_MissionItemBgType"""

    COMMON = 0
    Equipment = 1
    Char = 2


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


class CrossAppShareMissionType(IntEnum):
    """enum__Torappu_CrossAppShareMissionType"""

    NORMAL = 0
    ACTIVITY = 1


class MissionDisplayRewards(GameDataModel):
    """clz_Torappu_MissionDisplayRewards"""

    type: str = "NONE"
    id: str | None = None
    count: int = 0


class MissionData(GameDataModel):
    """clz_Torappu_MissionData"""

    id: str | None = None
    sort_id: int = 0
    description: str | None = None
    type: str = "UNKNOWN"
    item_bg_type: str = "COMMON"
    pre_mission_ids: list[str] | None = None
    template: str | None = None
    template_type: str | None = None
    param: list[str] | None = None
    unlock_condition: str | None = None
    unlock_param: list[str] | None = None
    mission_group: str | None = None
    to_page: str | None = None
    periodical_point: int = 0
    rewards: list[MissionDisplayRewards] | None = None
    back_image_path: str | None = None
    fold_id: str | None = None
    have_sub_mission_to_unlock: bool = False
    count_end_ts: int = 0


class MissionGroup(GameDataModel):
    """clz_Torappu_MissionGroup"""

    id: str | None = None
    title: str | None = None
    type: str = "UNKNOWN"
    pre_mission_group: str | None = None
    period: list[int] | None = None
    rewards: list[MissionDisplayRewards] | None = None
    mission_ids: list[str] | None = None
    start_ts: int = 0
    end_ts: int = 0


class MissionDailyRewardConf(GameDataModel):
    """clz_Torappu_MissionDailyRewardConf"""

    group_id: str | None = None
    id: str | None = None
    periodical_point_cost: int = 0
    type: str = "UNKNOWN"
    sort_index: int = 0
    rewards: list[MissionDisplayRewards] | None = None


class MissionWeeklyRewardConf(GameDataModel):
    """clz_Torappu_MissionWeeklyRewardConf"""

    begin_time: int = 0
    end_time: int = 0
    group_id: str | None = None
    id: str | None = None
    periodical_point_cost: int = 0
    type: str = "UNKNOWN"
    sort_index: int = 0
    rewards: list[MissionDisplayRewards] | None = None


class SOCharMissionGroup(GameDataModel):
    """clz_Torappu_SOCharMissionGroup"""

    group_id: str | None = None
    mission_ids: list[str] | None = None
    start_ts: int = 0
    end_ts: int = 0


class DailyMissionGroupInfoPeriodInfo(GameDataModel):
    """clz_Torappu_DailyMissionGroupInfo_periodInfo"""

    mission_group_id: str | None = None
    reward_group_id: str | None = None
    period: list[int] | None = None


class DailyMissionGroupInfo(GameDataModel):
    """clz_Torappu_DailyMissionGroupInfo"""

    start_time: int = 0
    end_time: int = 0
    tag_state: str | None = None
    period_list: list[DailyMissionGroupInfoPeriodInfo] | None = None


class MainlineMissionEndImageData(GameDataModel):
    """clz_Torappu_MainlineMissionEndImageData"""

    image_id: str | None = None
    priority: int = 0


class CrossAppShareMission(GameDataModel):
    """clz_Torappu_CrossAppShareMission"""

    share_mission_id: str | None = None
    mission_type: str = "NORMAL"
    relate_activity_id: str | None = None
    start_time: int = 0
    end_time: int = 0
    limit_count: int = 0
    cond_template: str | None = None
    cond_param: list[str] | None = None
    rewards_list: list[MissionDisplayRewards] | None = None


class CrossAppShareMissionConst(GameDataModel):
    """clz_Torappu_CrossAppShareMissionConst"""

    name_card_share_mission_id: str | None = None


class GuideMissionGroupInfo(GameDataModel):
    """clz_Torappu_GuideMissionGroupInfo"""

    group_id: str | None = None
    sort_id: int = 0
    short_name: str | None = None
    unlock_desc: str | None = None


class MissionTable(GameDataModel):
    """clz_Torappu_MissionTable"""

    missions: dict[str, MissionData] | None = None
    mission_groups: dict[str, MissionGroup] | None = None
    periodical_rewards: dict[str, MissionDailyRewardConf] | None = None
    weekly_rewards: dict[str, MissionWeeklyRewardConf] | None = None
    so_char_mission_group_info: dict[str, SOCharMissionGroup] | None = None
    daily_mission_group_info: dict[str, DailyMissionGroupInfo] | None = None
    daily_mission_period_info: list[DailyMissionGroupInfo] | None = None
    mainline_mission_end_image_data_list: list[MainlineMissionEndImageData] | None = (
        None
    )
    cross_app_share_missions: dict[str, CrossAppShareMission] | None = None
    cross_app_share_mission_const: CrossAppShareMissionConst | None = None
    guide_mission_group_info: dict[str, GuideMissionGroupInfo] | None = None


# root_type clz_Torappu_MissionTable


MissionDisplayRewards.model_rebuild()
MissionData.model_rebuild()
MissionGroup.model_rebuild()
MissionDailyRewardConf.model_rebuild()
MissionWeeklyRewardConf.model_rebuild()
SOCharMissionGroup.model_rebuild()
DailyMissionGroupInfoPeriodInfo.model_rebuild()
DailyMissionGroupInfo.model_rebuild()
MainlineMissionEndImageData.model_rebuild()
CrossAppShareMission.model_rebuild()
CrossAppShareMissionConst.model_rebuild()
GuideMissionGroupInfo.model_rebuild()
MissionTable.model_rebuild()

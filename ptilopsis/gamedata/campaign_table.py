"""campaign_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/campaign_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


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


class CampaignStageType(IntEnum):
    """enum__Torappu_CampaignStageType"""

    NONE = 0
    PERMANENT = 1
    ROTATE = 2
    TRAINING = 3


class StageDropType(IntEnum):
    """enum__Torappu_StageDropType"""

    NONE = 0
    ONCE = 1
    NORMAL = 2
    SPECIAL = 3
    ADDITIONAL = 4
    APRETURN = 5
    DIAMOND_MATERIAL = 6
    FUNITURE_DROP = 7
    COMPLETE = 8
    CHARM_DROP = 9
    OVERRIDE_DROP = 10
    ITEM_RETURN = 11
    CONDITION_DROP = 12


class OccPer(IntEnum):
    """enum__Torappu_OccPer"""

    ALWAYS = 0
    ALMOST = 1
    USUAL = 2
    OFTEN = 3
    SOMETIMES = 4
    NEVER = 5
    DEFINITELY_BUFF = 6


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class CampaignDataBreakRewardLadder(GameDataModel):
    """clz_Torappu_CampaignData_BreakRewardLadder"""

    kill_cnt: int = 0
    break_fee_add: int = 0
    rewards: list[ItemBundle] | None = None


class WeightItemBundle(GameDataModel):
    """clz_Torappu_WeightItemBundle"""

    id: str | None = None
    type: str = "NONE"
    drop_type: str = "NONE"
    count: int = 0
    weight: int = 0


class StageDataDisplayDetailRewards(GameDataModel):
    """clz_Torappu_StageData_DisplayDetailRewards"""

    occ_percent: str = "ALWAYS"
    type: str = "NONE"
    id: str | None = None
    drop_type: str = "NONE"


class CampaignDataCampaignDropInfo(GameDataModel):
    """clz_Torappu_CampaignData_CampaignDropInfo"""

    first_pass_rewards: list[ItemBundle] | None = None
    pass_rewards: list[list[WeightItemBundle]] | None = None
    display_detail_rewards: list[StageDataDisplayDetailRewards] | None = None


class CampaignDataDropLadder(GameDataModel):
    """clz_Torappu_CampaignData_DropLadder"""

    kill_cnt: int = 0
    drop_info: CampaignDataCampaignDropInfo | None = None


class CampaignDataGainLadder(GameDataModel):
    """clz_Torappu_CampaignData_GainLadder"""

    kill_cnt: int = 0
    ap_fail_return: int = 0
    favor: int = 0
    exp_gain: int = 0
    gold_gain: int = 0
    display_diamond_shd_num: int = 0


class StageDataDisplayRewards(GameDataModel):
    """clz_Torappu_StageData_DisplayRewards"""

    type: str = "NONE"
    id: str | None = None
    drop_type: str = "NONE"


class CampaignDataDropGainInfo(GameDataModel):
    """clz_Torappu_CampaignData_DropGainInfo"""

    drop_ladders: list[CampaignDataDropLadder] | None = None
    gain_ladders: list[CampaignDataGainLadder] | None = None
    display_rewards: list[StageDataDisplayRewards] | None = None
    display_detail_rewards: list[StageDataDisplayDetailRewards] | None = None


class CampaignData(GameDataModel):
    """clz_Torappu_CampaignData"""

    stage_id: str | None = None
    is_small_scale: int = 0
    break_ladders: list[CampaignDataBreakRewardLadder] | None = None
    is_customized: bool = False
    drop_gains: dict[str, CampaignDataDropGainInfo] | None = None


class CampaignGroupData(GameDataModel):
    """clz_Torappu_CampaignGroupData"""

    group_id: str | None = None
    active_camps: list[str] | None = None
    start_ts: int = 0
    end_ts: int = 0


class CampaignRegionData(GameDataModel):
    """clz_Torappu_CampaignRegionData"""

    id: str | None = None
    is_unknwon: int = 0


class CampaignZoneData(GameDataModel):
    """clz_Torappu_CampaignZoneData"""

    id: str | None = None
    name: str | None = None
    region_id: str | None = None
    template_id: str | None = None


class CampaignMissionData(GameDataModel):
    """clz_Torappu_CampaignMissionData"""

    id: str | None = None
    sort_id: int = 0
    param: list[str] | None = None
    description: str | None = None
    break_fee_add: int = 0


class CampaignConstTable(GameDataModel):
    """clz_Torappu_CampaignConstTable"""

    system_preposed_stage: str | None = None
    rotate_start_time: int = 0
    rotate_preposed_stage: str | None = None
    zone_unlock_stage: str | None = None
    first_rotate_region: str | None = None
    sweep_start_time: int = 0


class CampaignRotateOpenTimeData(GameDataModel):
    """clz_Torappu_CampaignRotateOpenTimeData"""

    group_id: str | None = None
    stage_id: str | None = None
    map_id: str | None = None
    unknown_regions: list[str] | None = None
    duration: int = 0
    start_ts: int = 0
    end_ts: int = 0


class CampaignTrainingOpenTimeData(GameDataModel):
    """clz_Torappu_CampaignTrainingOpenTimeData"""

    group_id: str | None = None
    stages: list[str] | None = None
    start_ts: int = 0
    end_ts: int = 0


class CampaignTrainingAllOpenTimeData(GameDataModel):
    """clz_Torappu_CampaignTrainingAllOpenTimeData"""

    group_id: str | None = None
    start_ts: int = 0
    end_ts: int = 0


class UnityEngineVector2(GameDataModel):
    """clz_UnityEngine_Vector2"""

    x: float = 0.0
    y: float = 0.0


class CampaignStageMapData(GameDataModel):
    """clz_Torappu_CampaignStageMapData"""

    position: UnityEngineVector2 | None = None


class CampaignTable(GameDataModel):
    """clz_Torappu_CampaignTable"""

    campaigns: dict[str, CampaignData] | None = None
    campaign_groups: dict[str, CampaignGroupData] | None = None
    campaign_regions: dict[str, CampaignRegionData] | None = None
    campaign_zones: dict[str, CampaignZoneData] | None = None
    campaign_missions: dict[str, CampaignMissionData] | None = None
    stage_index_in_zone_map: dict[str, int] | None = None
    campaign_const_table: CampaignConstTable | None = None
    campaign_rotate_stage_open_times: list[CampaignRotateOpenTimeData] | None = None
    campaign_training_stage_open_times: list[CampaignTrainingOpenTimeData] | None = None
    campaign_training_all_open_times: list[CampaignTrainingAllOpenTimeData] | None = None
    campaign_zone_map_data: dict[str, dict[str, CampaignStageMapData]] | None = None


# root_type clz_Torappu_CampaignTable


ItemBundle.model_rebuild()
CampaignDataBreakRewardLadder.model_rebuild()
WeightItemBundle.model_rebuild()
StageDataDisplayDetailRewards.model_rebuild()
CampaignDataCampaignDropInfo.model_rebuild()
CampaignDataDropLadder.model_rebuild()
CampaignDataGainLadder.model_rebuild()
StageDataDisplayRewards.model_rebuild()
CampaignDataDropGainInfo.model_rebuild()
CampaignData.model_rebuild()
CampaignGroupData.model_rebuild()
CampaignRegionData.model_rebuild()
CampaignZoneData.model_rebuild()
CampaignMissionData.model_rebuild()
CampaignConstTable.model_rebuild()
CampaignRotateOpenTimeData.model_rebuild()
CampaignTrainingOpenTimeData.model_rebuild()
CampaignTrainingAllOpenTimeData.model_rebuild()
UnityEngineVector2.model_rebuild()
CampaignStageMapData.model_rebuild()
CampaignTable.model_rebuild()

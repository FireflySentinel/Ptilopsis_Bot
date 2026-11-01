"""crisis_v2_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/crisis_v2_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class CrisisV2AppraiseType(IntEnum):
    """enum__Torappu_CrisisV2AppraiseType"""

    RANK_D = 0
    RANK_C = 1
    RANK_B = 2
    RANK_A = 3
    RANK_S = 4
    RANK_SS = 5
    RANK_SSS = 6


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


class BuildableType(IntEnum):
    """enum__Torappu_BuildableType"""

    NONE = 0
    MELEE = 1
    RANGED = 2
    ALL = 3


class PlayerSideMask(IntEnum):
    """enum__Torappu_PlayerSideMask"""

    ALL = 0
    SIDE_A = 2
    SIDE_B = 4
    SIDE_C = 8
    SIDE_D = 16
    NONE = 255


class MapLayerMask(IntEnum):
    """enum__Torappu_MapLayerMask"""

    ALL = 0
    LAYER_A = 2
    LAYER_B = 4
    LAYER_C = 8
    LAYER_D = 16
    NONE = 255


class BattleSideType(IntEnum):
    """enum__Torappu_Battle_SideType"""

    NONE = 0
    ALLY = 1
    ENEMY = 2
    BOTH_ALLY_AND_ENEMY = 3
    NEUTRAL = 4
    ALL = 7


class TileDataHeightTypeMask(IntEnum):
    """enum__Torappu_TileData_HeightTypeMask"""

    NONE = 0
    LOWLAND = 1
    HIGHLAND = 2
    ALL = 3


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


class CrisisV2SeasonInfo(GameDataModel):
    """clz_Torappu_CrisisV2SeasonInfo"""

    season_id: str | None = None
    name: str | None = None
    start_ts: int = 0
    end_ts: int = 0
    medal_group_id: str | None = None
    medal_id: str | None = None
    theme_color_1: str | None = None
    theme_color_2: str | None = None
    theme_color_3: str | None = None
    season_bgm: str | None = None
    season_bgm_challenge: str | None = None
    crisis_v2_season_code: str | None = None


class CrisisV2AppraiseWrap(GameDataModel):
    """clz_Torappu_CrisisV2AppraiseWrap"""

    appraise_type: str = "RANK_D"


class CrisisV2ConstData(GameDataModel):
    """clz_Torappu_CrisisV2ConstData"""

    sys_start_time: int = 0
    black_score_threshold: int = 0
    red_score_threshold: int = 0
    detail_bkg_red_threshold: int = 0
    voice_grade: int = 0
    season_button_unlock_info: int = 0
    shop_coin_id: str | None = None
    hard_bgm_switch_score: int = 0
    stage_id: str | None = None
    hide_todo_when_stage_finish: bool = False


class RuneDataSelector(GameDataModel):
    """clz_Torappu_RuneData_Selector"""

    profession_mask: str = "NONE"
    buildable_mask: str = "NONE"
    player_side_mask: str = "ALL"
    map_layer_mask: str = "ALL"
    side_type: str = "NONE"
    char_id_filter: list[str] | None = None
    char_id_exclude_filter: list[str] | None = None
    enemy_id_filter: list[str] | None = None
    enemy_id_exclude_filter: list[str] | None = None
    enemy_level_type_filter: list[str] | None = None
    enemy_action_hidden_group_filter: list[str] | None = None
    skill_id_filter: list[str] | None = None
    tile_key_filter: list[str] | None = None
    group_tag_filter: list[str] | None = None
    filter_tag_filter: list[str] | None = None
    filter_tag_exclude_filter: list[str] | None = None
    sub_profession_exclude_filter: list[str] | None = None
    map_tag_filter: list[str] | None = None
    height_type_mask: str = "NONE"


class BlackboardDataPair(GameDataModel):
    """clz_Torappu_Blackboard_DataPair"""

    key: str | None = None
    value: float = 0.0
    value_str: str | None = None


class RuneData(GameDataModel):
    """clz_Torappu_RuneData"""

    key: str | None = None
    selector: RuneDataSelector | None = None
    blackboard: list[BlackboardDataPair] | None = None


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class RuneTablePackedRuneData(GameDataModel):
    """clz_Torappu_RuneTable_PackedRuneData"""

    id: str | None = None
    points: float = 0.0
    mutex_group_key: str | None = None
    description: str | None = None
    runes: list[RuneData] | None = None


class RecalRuneRuneData(GameDataModel):
    """clz_Torappu_RecalRuneRuneData"""

    rune_id: str | None = None
    score: int = 0
    sort_id: int = 0
    essential: bool = False
    exclusive_group_id: str | None = None
    rune_icon: str | None = None
    packed_rune: RuneTablePackedRuneData | None = None


class RecalRuneStageData(GameDataModel):
    """clz_Torappu_RecalRuneStageData"""

    stage_id: str | None = None
    level_id: str | None = None
    junior_medal_id: str | None = None
    senior_medal_id: str | None = None
    junior_medal_score: int = 0
    senior_medal_score: int = 0
    runes: dict[str, RecalRuneRuneData] | None = None
    source_name: str | None = None
    source_type: str | None = None
    use_name: bool = False
    level_name: str | None = None
    level_code: str | None = None
    level_desc: str | None = None
    fixed_rune_series_name: str | None = None
    logo_id: str | None = None
    main_pic_id: str | None = None
    loading_pic_id: str | None = None


class RecalRuneSeasonData(GameDataModel):
    """clz_Torappu_RecalRuneSeasonData"""

    season_id: str | None = None
    sort_id: int = 0
    start_ts: int = 0
    season_code: str | None = None
    junior_reward: ItemBundle | None = None
    senior_reward: ItemBundle | None = None
    senior_reward_hint: str | None = None
    main_medal_id: str | None = None
    pic_id: str | None = None
    stages: dict[str, RecalRuneStageData] | None = None


class RecalRuneConstData(GameDataModel):
    """clz_Torappu_RecalRuneConstData"""

    stage_count_per_season: int = 0
    junior_reward_medal_count: int = 0
    senior_reward_medal_count: int = 0
    unlock_level_ids: list[str] | None = None


class RecalRuneSharedData(GameDataModel):
    """clz_Torappu_RecalRuneSharedData"""

    seasons: dict[str, RecalRuneSeasonData] | None = None
    const_data: RecalRuneConstData | None = None


class CrisisV2SharedData(GameDataModel):
    """clz_Torappu_CrisisV2SharedData"""

    season_info_data_map: dict[str, CrisisV2SeasonInfo] | None = None
    score_level_to_appraise_data_map: dict[int, CrisisV2AppraiseWrap] | None = None
    const_data: CrisisV2ConstData | None = None
    battle_comment_rune_data: dict[str, list[RuneData]] | None = None
    recal_rune_data: RecalRuneSharedData | None = None


# root_type clz_Torappu_CrisisV2SharedData
CrisisV2Table = CrisisV2SharedData


CrisisV2SeasonInfo.model_rebuild()
CrisisV2AppraiseWrap.model_rebuild()
CrisisV2ConstData.model_rebuild()
RuneDataSelector.model_rebuild()
BlackboardDataPair.model_rebuild()
RuneData.model_rebuild()
ItemBundle.model_rebuild()
RuneTablePackedRuneData.model_rebuild()
RecalRuneRuneData.model_rebuild()
RecalRuneStageData.model_rebuild()
RecalRuneSeasonData.model_rebuild()
RecalRuneConstData.model_rebuild()
RecalRuneSharedData.model_rebuild()
CrisisV2SharedData.model_rebuild()

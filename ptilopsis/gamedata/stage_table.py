"""stage_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/stage_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class StageType(IntEnum):
    """enum__Torappu_StageType"""

    MAIN = 0
    DAILY = 1
    TRAINING = 2
    ACTIVITY = 3
    GUIDE = 4
    SUB = 5
    CAMPAIGN = 6
    SPECIAL_STORY = 7
    HANDBOOK_BATTLE = 8
    CLIMB_TOWER = 9
    ENUM = 10


class LevelDataDifficulty(IntEnum):
    """enum__Torappu_LevelData_Difficulty"""

    NONE = 0
    NORMAL = 1
    FOUR_STAR = 2
    EASY = 4
    SIX_STAR = 8
    ALL = 15


class StageDataPerformanceStageFlag(IntEnum):
    """enum__Torappu_StageData_PerformanceStageFlag"""

    NORMAL_STAGE = 0
    PERFORMANCE_STAGE = 1


class StageDiffGroup(IntEnum):
    """enum__Torappu_StageDiffGroup"""

    NONE = 0
    EASY = 1
    NORMAL = 2
    TOUGH = 4
    ALL = 7


class PlayerBattleRank(IntEnum):
    """enum__Torappu_PlayerBattleRank"""

    FAIL = 1
    PASS = 2
    COMPLETE = 3
    ERR_ZERO = 0


class AppearanceStyle(IntEnum):
    """enum__Torappu_AppearanceStyle"""

    MAIN_NORMAL = 0
    MAIN_PREDEFINED = 1
    SUB = 2
    TRAINING = 3
    HIGH_DIFFICULTY = 4
    MIST_OPS = 5
    SPECIAL_STORY = 6


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


class StageDataSpecialStageUnlockProgressType(IntEnum):
    """enum__Torappu_StageData_SpecialStageUnlockProgressType"""

    ONCE = 0
    PROGRESS = 1


class FogType(IntEnum):
    """enum__Torappu_FogType"""

    ZONE = 0
    STAGE = 1


class StageButtonInFogRenderType(IntEnum):
    """enum__Torappu_StageButtonInFogRenderType"""

    HIDE = 0
    SHOW_WITH_FOG_SIX_STAR = 1


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


class OverrideGameMode(IntEnum):
    """enum__Torappu_OverrideGameMode"""

    NONE = 0
    ACT27SIDE = 1


class StorylineType(IntEnum):
    """enum__Torappu_StorylineType"""

    CONTINUE = 0
    DISCRETE = 1


class StorylineLocationType(IntEnum):
    """enum__Torappu_StorylineLocationType"""

    STORY_SET = 0
    BEFORE = 1
    AFTER = 2
    MAINLINE_SPLIT = 3


class StorylineStorySetType(IntEnum):
    """enum__Torappu_StorylineStorySetType"""

    MAINLINE = 0
    SS = 1
    COLLECT = 2


class CGGalleryCGSource(IntEnum):
    """enum__Torappu_CGGalleryCGSource"""

    IMAGE = 0
    BACKGROUND = 1
    ITEM = 2


class CGGalleryCGCompositeType(IntEnum):
    """enum__Torappu_CGGalleryCGCompositeType"""

    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2
    GRID = 3


class SixStarMilestoneRewardType(IntEnum):
    """enum__Torappu_SixStarMilestoneRewardType"""

    UNLOCK_STAGE = 0
    REWARD = 1


class SixStarStageCompatibleDropType(IntEnum):
    """enum__Torappu_SixStarStageCompatibleDropType"""

    COMPLETE_ONLY = 0


class StageDataConditionDesc(GameDataModel):
    """clz_Torappu_StageData_ConditionDesc"""

    stage_id: str | None = None
    complete_state: str = "ERR_ZERO"


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class WeightItemBundle(GameDataModel):
    """clz_Torappu_WeightItemBundle"""

    id: str | None = None
    type: str = "NONE"
    drop_type: str = "NONE"
    count: int = 0
    weight: int = 0


class StageDataDisplayRewards(GameDataModel):
    """clz_Torappu_StageData_DisplayRewards"""

    type: str = "NONE"
    id: str | None = None
    drop_type: str = "NONE"


class StageDataDisplayDetailRewards(GameDataModel):
    """clz_Torappu_StageData_DisplayDetailRewards"""

    occ_percent: str = "ALWAYS"
    type: str = "NONE"
    id: str | None = None
    drop_type: str = "NONE"


class StageDataStageDropInfo(GameDataModel):
    """clz_Torappu_StageData_StageDropInfo"""

    first_pass_rewards: list[ItemBundle] | None = None
    first_complete_rewards: list[ItemBundle] | None = None
    pass_rewards: list[list[WeightItemBundle]] | None = None
    complete_rewards: list[list[WeightItemBundle]] | None = None
    display_rewards: list[StageDataDisplayRewards] | None = None
    display_detail_rewards: list[StageDataDisplayDetailRewards] | None = None


class StageDataExtraConditionDesc(GameDataModel):
    """clz_Torappu_StageData_ExtraConditionDesc"""

    index: int = 0
    template: str | None = None
    unlock_param: list[str] | None = None


class StageDataSpecialProgressInfo(GameDataModel):
    """clz_Torappu_StageData_SpecialProgressInfo"""

    progress_type: str = "ONCE"
    desc_list: dict[int, str] | None = None


class StageDataSpecialStoryInfo(GameDataModel):
    """clz_Torappu_StageData_SpecialStoryInfo"""

    stage_id: str | None = None
    rewards: list[ItemBundle] | None = None
    progress_info: StageDataSpecialProgressInfo | None = None
    image_id: str | None = None
    key_item_id: str | None = None
    unlock_desc: str | None = None


class StageData(GameDataModel):
    """clz_Torappu_StageData"""

    stage_type: str = "MAIN"
    difficulty: str = "NONE"
    performance_stage_flag: str = "NORMAL_STAGE"
    diff_group: str = "NONE"
    unlock_condition: list[StageDataConditionDesc] | None = None
    stage_id: str | None = None
    level_id: str | None = None
    zone_id: str | None = None
    code: str | None = None
    name: str | None = None
    description: str | None = None
    hard_staged_id: str | None = None
    six_star_stage_id: str | None = None
    danger_level: str | None = None
    danger_point: float = 0.0
    loading_pic_id: str | None = None
    battle_finish_loading_pic_id: str | None = None
    can_practice: bool = False
    can_battle_replay: bool = False
    ap_cost: int = 0
    ap_fail_return: int = 0
    max_slot: int = 0
    et_item_id: str | None = None
    et_cost: int = 0
    et_fail_return: int = 0
    et_button_style: str | None = None
    ap_protect_times: int = 0
    diamond_once_drop: int = 0
    practice_ticket_cost: int = 0
    daily_stage_difficulty: int = 0
    exp_gain: int = 0
    gold_gain: int = 0
    lose_exp_gain: int = 0
    lose_gold_gain: int = 0
    pass_favor: int = 0
    complete_favor: int = 0
    sl_progress: int = 0
    display_main_item: str | None = None
    hilight_mark: bool = False
    boss_mark: bool = False
    is_predefined: bool = False
    is_hard_predefined: bool = False
    is_skill_selectable_predefined: bool = False
    is_story_only: bool = False
    appearance_style: str = "MAIN_NORMAL"
    stage_drop_info: StageDataStageDropInfo | None = None
    level_map_id: str | None = None
    can_use_charm: bool = False
    can_use_tech: bool = False
    can_use_trap_tool: bool = False
    can_use_battle_performance: bool = False
    can_use_firework: bool = False
    can_multiple_battle: bool = False
    start_button_override_id: str | None = None
    is_stage_patch: bool = False
    main_stage_id: str | None = None
    extra_condition: list[StageDataExtraConditionDesc] | None = None
    extra_info: list[StageDataSpecialStoryInfo] | None = None
    six_star_base_desc: str | None = None
    six_star_display_reward_list: list[ItemBundle] | None = None
    advanced_rune_id_list_1: list[str] | None = None
    advanced_rune_id_list_2: list[str] | None = None
    use_special_size_map_preview: bool = False


class RuneStageGroupDataRuneStageInst(GameDataModel):
    """clz_Torappu_RuneStageGroupData_RuneStageInst"""

    stage_id: str | None = None
    active_packed_rune_ids: list[str] | None = None


class RuneStageGroupData(GameDataModel):
    """clz_Torappu_RuneStageGroupData"""

    group_id: str | None = None
    active_rune_stages: list[RuneStageGroupDataRuneStageInst] | None = None
    start_ts: int = 0
    end_ts: int = 0


class MapThemeData(GameDataModel):
    """clz_Torappu_MapThemeData"""

    theme_id: str | None = None
    unit_color: str | None = None
    buildable_color: str | None = None
    theme_type: str | None = None
    trap_tint_color: str | None = None
    emission_color: str | None = None
    highland_buildable_color: str | None = None
    highland_emission_color: str | None = None


class TileAppendInfo(GameDataModel):
    """clz_Torappu_TileAppendInfo"""

    tile_key: str | None = None
    name: str | None = None
    description: str | None = None
    is_functional: bool = False


class WeeklyForceOpenTable(GameDataModel):
    """clz_Torappu_WeeklyForceOpenTable"""

    id: str | None = None
    start_time: int = 0
    end_time: int = 0
    force_open_list: list[str] | None = None


class TimelyDropTimeInfo(GameDataModel):
    """clz_Torappu_TimelyDropTimeInfo"""

    start_ts: int = 0
    end_ts: int = 0
    stage_pic: str | None = None
    drop_pic_id: str | None = None
    stage_unlock: str | None = None
    entrance_down_pic_id: str | None = None
    entrance_up_pic_id: str | None = None
    timely_group_id: str | None = None
    weekly_pic_id: str | None = None
    is_replace: bool = False
    ap_supply_out_of_date_dict: dict[str, int] | None = None


class OverrideDropInfo(GameDataModel):
    """clz_Torappu_OverrideDropInfo"""

    item_id: str | None = None
    start_ts: int = 0
    end_ts: int = 0
    zone_range: str | None = None
    times: int = 0
    name: str | None = None
    eg_name: str | None = None
    desc_1: str | None = None
    desc_2: str | None = None
    desc_3: str | None = None
    drop_tag: str | None = None
    drop_type_desc: str | None = None
    drop_info: dict[str, StageDataStageDropInfo] | None = None


class OverrideUnlockInfo(GameDataModel):
    """clz_Torappu_OverrideUnlockInfo"""

    group_id: str | None = None
    start_time: int = 0
    end_time: int = 0
    unlock_dict: dict[str, list[StageDataConditionDesc]] | None = None


class TimelyDropInfo(GameDataModel):
    """clz_Torappu_TimelyDropInfo"""

    drop_info: dict[str, StageDataStageDropInfo] | None = None


class StageValidInfo(GameDataModel):
    """clz_Torappu_StageValidInfo"""

    start_ts: int = 0
    end_ts: int = 0


class StageFogInfo(GameDataModel):
    """clz_Torappu_StageFogInfo"""

    lock_id: str | None = None
    fog_type: str = "ZONE"
    stage_button_in_fog_render_type: str = "HIDE"
    stage_id: str | None = None
    lock_name: str | None = None
    lock_desc: str | None = None
    unlock_item_id: str | None = None
    unlock_item_type: str = "NONE"
    unlock_item_num: int = 0
    preposed_stage_id: str | None = None
    preposed_lock_id: str | None = None


class StageStartCondRequireChar(GameDataModel):
    """clz_Torappu_StageStartCond_RequireChar"""

    char_id: str | None = None
    evolve_phase: str = "PHASE_0"


class StageStartCond(GameDataModel):
    """clz_Torappu_StageStartCond"""

    require_chars: list[StageStartCondRequireChar] | None = None
    exclude_assists: list[str] | None = None
    is_not_pass: bool = False


class StageDiffGroupTable(GameDataModel):
    """clz_Torappu_StageDiffGroupTable"""

    normal_id: str | None = None
    tough_id: str | None = None
    easy_id: str | None = None


class StoryStageShowGroup(GameDataModel):
    """clz_Torappu_StoryStageShowGroup"""

    display_record_id: str | None = None
    stage_id: str | None = None
    according_stage_id: str | None = None
    diff_group: str = "NONE"


class SpecialBattleFinishStageData(GameDataModel):
    """clz_Torappu_SpecialBattleFinishStageData"""

    stage_id: str | None = None
    skip_accomplish_perform: bool = False


class RecordRewardServerData(GameDataModel):
    """clz_Torappu_RecordRewardServerData"""

    stage_id: str | None = None
    rewards: list[ItemBundle] | None = None


class ApProtectZoneInfoTimeRange(GameDataModel):
    """clz_Torappu_ApProtectZoneInfo_TimeRange"""

    start_ts: int = 0
    end_ts: int = 0


class ApProtectZoneInfo(GameDataModel):
    """clz_Torappu_ApProtectZoneInfo"""

    zone_id: str | None = None
    time_ranges: list[ApProtectZoneInfoTimeRange] | None = None


class ActCustomStageData(GameDataModel):
    """clz_Torappu_ActCustomStageData"""

    override_game_mode: str = "NONE"


class StorylineMainlineSplitData(GameDataModel):
    """clz_Torappu_StorylineMainlineSplitData"""

    icon_id: str | None = None
    sub_name: str | None = None


class StorylineLocationData(GameDataModel):
    """clz_Torappu_StorylineLocationData"""

    location_id: str | None = None
    location_type: str = "STORY_SET"
    sort_id: int = 0
    start_time: int = 0
    present_stage_id: str | None = None
    unlock_stage_id: str | None = None
    relevant_story_set_id: str | None = None
    mainline_split_data: StorylineMainlineSplitData | None = None


class StorylineData(GameDataModel):
    """clz_Torappu_StorylineData"""

    storyline_id: str | None = None
    storyline_type: str = "CONTINUE"
    sort_id: int = 0
    storyline_name: str | None = None
    storyline_icon_id: str | None = None
    storyline_logo_id: str | None = None
    background_id: str | None = None
    has_video_to_play: bool = False
    start_ts: int = 0
    locations: dict[str, StorylineLocationData] | None = None


class StorylineMainlineData(GameDataModel):
    """clz_Torappu_StorylineMainlineData"""

    zone_id: str | None = None
    retro_id: str | None = None
    deco_image_id: str | None = None
    desc: str | None = None
    background_id: str | None = None
    tags: list[str] | None = None


class StorylineSSData(GameDataModel):
    """clz_Torappu_StorylineSSData"""

    desc: str | None = None
    background_id: str | None = None
    tags: list[str] | None = None
    reopen_activity_id: str | None = None
    retro_activity_id: str | None = None
    is_recommended: bool = False
    recommend_hide_stage_id: str | None = None
    override_stage_list: list[str] | None = None


class StorylineCollectData(GameDataModel):
    """clz_Torappu_StorylineCollectData"""

    desc: str | None = None
    background_id: str | None = None


class StorylineStorySetData(GameDataModel):
    """clz_Torappu_StorylineStorySetData"""

    story_set_id: str | None = None
    story_set_type: str = "MAINLINE"
    sort_by_year: int = 0
    sort_within_year: int = 0
    kv_image_id: str | None = None
    title_image_id: str | None = None
    have_video_to_play: bool = False
    background_id: str | None = None
    game_music_id: str | None = None
    core_reward_type: str = "NONE"
    core_reward_id: str | None = None
    relevant_activity_id: str | None = None
    mainline_data: StorylineMainlineData | None = None
    ss_data: StorylineSSData | None = None
    collect_data: StorylineCollectData | None = None


class StorylineTagData(GameDataModel):
    """clz_Torappu_StorylineTagData"""

    tag_id: str | None = None
    sort_id: int = 0
    tag_desc: str | None = None
    text_color: str | None = None
    bkg_color: str | None = None


class StorylineConstData(GameDataModel):
    """clz_Torappu_StorylineConstData"""

    recommend_hide_guide_group_id: list[str] | None = None
    tutorial_select_storyline_id: str | None = None
    mainline_storyline_id: str | None = None


class CGGalleryDisplayData(GameDataModel):
    """clz_Torappu_CGGalleryDisplayData"""

    display_id: str | None = None
    cg_list: list[str] | None = None
    cg_source: str = "IMAGE"
    display_name: str | None = None
    display_desc: str | None = None
    story_set_id: str | None = None
    sort_id: int = 0
    related_story_id: str | None = None
    related_stage_id: str | None = None


class CGGalleryGroupData(GameDataModel):
    """clz_Torappu_CGGalleryGroupData"""

    story_set_id: str | None = None
    storyline_id: str | None = None
    location_id: str | None = None
    displays: list[str] | None = None


class CGGalleryCGCompositeData(GameDataModel):
    """clz_Torappu_CGGalleryCGCompositeData"""

    cg_id: str | None = None
    width: int = 0
    height: int = 0


class CGGalleryCGData(GameDataModel):
    """clz_Torappu_CGGalleryCGData"""

    cg_id: str | None = None
    sort_id: int = 0
    composite_type: str = "NONE"
    composite_list: list[CGGalleryCGCompositeData] | None = None
    story_set_id: str | None = None


class SixStarRuneData(GameDataModel):
    """clz_Torappu_SixStarRuneData"""

    rune_id: str | None = None
    rune_desc: str | None = None
    rune_key: str | None = None


class SixStarMilestoneItemData(GameDataModel):
    """clz_Torappu_SixStarMilestoneItemData"""

    id: str | None = None
    sort_id: int = 0
    node_point: int = 0
    reward_type: str = "UNLOCK_STAGE"
    unlock_stage_fog: str | None = None
    unlock_stage_id: str | None = None
    unlock_stage_name: str | None = None
    reward_list: list[ItemBundle] | None = None


class SixStarMilestoneGroupData(GameDataModel):
    """clz_Torappu_SixStarMilestoneGroupData"""

    group_id: str | None = None
    stage_id_list: list[str] | None = None
    milestone_data_list: list[SixStarMilestoneItemData] | None = None


class SixStarLinkedStageCompatibleInfo(GameDataModel):
    """clz_Torappu_SixStarLinkedStageCompatibleInfo"""

    stage_id: str | None = None
    ap_cost: int = 0
    ap_fail_return: int = 0
    drop_type: str = "COMPLETE_ONLY"


class ConditionalDropInfo(GameDataModel):
    """clz_Torappu_ConditionalDropInfo"""

    template: str | None = None
    param: list[str] | None = None
    count_limit: int = 0


class StageTable(GameDataModel):
    """clz_Torappu_StageTable"""

    stages: dict[str, StageData] | None = None
    rune_stage_groups: dict[str, RuneStageGroupData] | None = None
    map_themes: dict[str, MapThemeData] | None = None
    tile_info: dict[str, TileAppendInfo] | None = None
    force_open_table: dict[str, WeeklyForceOpenTable] | None = None
    timely_stage_drop_info: dict[str, TimelyDropTimeInfo] | None = None
    override_drop_info: dict[str, OverrideDropInfo] | None = None
    override_unlock_info: dict[str, OverrideUnlockInfo] | None = None
    timely_table: dict[str, TimelyDropInfo] | None = None
    stage_valid_info: dict[str, StageValidInfo] | None = None
    stage_fog_info: dict[str, StageFogInfo] | None = None
    stage_start_conds: dict[str, StageStartCond] | None = None
    diff_group_table: dict[str, StageDiffGroupTable] | None = None
    story_stage_show_group: dict[str, dict[str, StoryStageShowGroup]] | None = None
    special_battle_finish_stage_data: dict[str, SpecialBattleFinishStageData] | None = None
    record_reward_data: dict[str, RecordRewardServerData] | None = None
    ap_protect_zone_info: dict[str, ApProtectZoneInfo] | None = None
    anti_spoiler_dict: dict[str, list[str]] | None = None
    act_custom_stage_datas: dict[str, ActCustomStageData] | None = None
    sp_normal_stage_id_for_4_star_list: list[str] | None = None
    storylines: dict[str, StorylineData] | None = None
    storyline_story_sets: dict[str, StorylineStorySetData] | None = None
    storyline_tags: dict[str, StorylineTagData] | None = None
    storyline_const: StorylineConstData | None = None
    cg_gallery_displays: dict[str, CGGalleryDisplayData] | None = None
    cg_gallery_groups: dict[str, CGGalleryGroupData] | None = None
    cg_gallery_cgs: dict[str, CGGalleryCGData] | None = None
    six_star_rune_data: dict[str, SixStarRuneData] | None = None
    six_star_milestone_info: dict[str, SixStarMilestoneGroupData] | None = None
    six_star_compatible_info: dict[str, SixStarLinkedStageCompatibleInfo] | None = None
    conditional_drop_info: dict[str, ConditionalDropInfo] | None = None


# root_type clz_Torappu_StageTable


StageDataConditionDesc.model_rebuild()
ItemBundle.model_rebuild()
WeightItemBundle.model_rebuild()
StageDataDisplayRewards.model_rebuild()
StageDataDisplayDetailRewards.model_rebuild()
StageDataStageDropInfo.model_rebuild()
StageDataExtraConditionDesc.model_rebuild()
StageDataSpecialProgressInfo.model_rebuild()
StageDataSpecialStoryInfo.model_rebuild()
StageData.model_rebuild()
RuneStageGroupDataRuneStageInst.model_rebuild()
RuneStageGroupData.model_rebuild()
MapThemeData.model_rebuild()
TileAppendInfo.model_rebuild()
WeeklyForceOpenTable.model_rebuild()
TimelyDropTimeInfo.model_rebuild()
OverrideDropInfo.model_rebuild()
OverrideUnlockInfo.model_rebuild()
TimelyDropInfo.model_rebuild()
StageValidInfo.model_rebuild()
StageFogInfo.model_rebuild()
StageStartCondRequireChar.model_rebuild()
StageStartCond.model_rebuild()
StageDiffGroupTable.model_rebuild()
StoryStageShowGroup.model_rebuild()
SpecialBattleFinishStageData.model_rebuild()
RecordRewardServerData.model_rebuild()
ApProtectZoneInfoTimeRange.model_rebuild()
ApProtectZoneInfo.model_rebuild()
ActCustomStageData.model_rebuild()
StorylineMainlineSplitData.model_rebuild()
StorylineLocationData.model_rebuild()
StorylineData.model_rebuild()
StorylineMainlineData.model_rebuild()
StorylineSSData.model_rebuild()
StorylineCollectData.model_rebuild()
StorylineStorySetData.model_rebuild()
StorylineTagData.model_rebuild()
StorylineConstData.model_rebuild()
CGGalleryDisplayData.model_rebuild()
CGGalleryGroupData.model_rebuild()
CGGalleryCGCompositeData.model_rebuild()
CGGalleryCGData.model_rebuild()
SixStarRuneData.model_rebuild()
SixStarMilestoneItemData.model_rebuild()
SixStarMilestoneGroupData.model_rebuild()
SixStarLinkedStageCompatibleInfo.model_rebuild()
ConditionalDropInfo.model_rebuild()
StageTable.model_rebuild()

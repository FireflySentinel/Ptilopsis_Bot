"""gamedata_const.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/gamedata_const.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

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


class SubProfessionAttackType(IntEnum):
    """enum__Torappu_SubProfessionAttackType"""

    NONE = 0
    PHYSICAL = 1
    MAGICAL = 2
    HEAL = 3


class GameDataConstsCharAssistRefreshTimeState(GameDataModel):
    """clz_Torappu_GameDataConsts_CharAssistRefreshTimeState"""

    hour: int = Field(default=0, alias="Hour")
    minute: int = Field(default=0, alias="Minute")


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class TermDescriptionData(GameDataModel):
    """clz_Torappu_TermDescriptionData"""

    term_id: str | None = None
    term_name: str | None = None
    description: str | None = None


class GameDataConstsFeverGameData(GameDataModel):
    """clz_Torappu_GameDataConsts_FeverGameData"""

    fever_duration: float = 0.0
    fever_need: float = 0.0


class GameDataConstsAVGReaderModeDefaultSetting(GameDataModel):
    """clz_Torappu_GameDataConsts_AVGReaderModeDefaultSetting"""

    default_reader_fontsize: int = 0
    default_reader_linespace: int = 0
    default_reader_background_alpha: int = 0
    default_name_reader_fontsize: int = 0


class GameDataConsts(GameDataModel):
    """clz_Torappu_GameDataConsts"""

    max_player_level: int = 0
    player_exp_map: list[int] | None = None
    player_ap_map: list[int] | None = None
    max_level: list[list[int]] | None = None
    character_exp_map: list[list[int]] | None = None
    character_upgrade_cost_map: list[list[int]] | None = None
    evolve_gold_cost: list[list[int]] | None = None
    complete_gain_bonus: float = 0.0
    player_ap_regen_speed: int = 0
    max_practice_ticket: int = 0
    advanced_gacha_crystal_cost: int = 0
    complete_crystal_bonus: int = 0
    init_player_gold: int = 0
    init_player_diamond_shard: int = 0
    init_campaign_total_fee: int = 0
    init_recruit_tag_list: list[int] | None = None
    init_char_id_list: list[str] | None = None
    attack_max: float = 0.0
    def_max: float = 0.0
    hp_max: float = 0.0
    re_max: float = 0.0
    diamond_to_shd_rate: int = 0
    request_same_friend_cd: int = Field(default=0, alias="requestSameFriendCD")
    base_max_friend_num: int = 0
    max_star_friend_num: int = 0
    max_squad_assist_display_num: int = 0
    friend_star_edit_track_ts: int = 0
    hard_diamond_drop: int = 0
    inst_fin_dmd_shd_cost: int = 0
    easy_crystal_bonus: int = 0
    diamond_material_to_shard_exchange_ratio: int = 0
    diamond_handbook_stage_gain: int = 0
    ap_buy_cost: int = 0
    ap_buy_threshold: int = 0
    credit_limit: int = 0
    monthly_sub_remain_time_limit_days: int = 0
    friend_assist_rarity_limit: list[int] | None = None
    mainline_compatible_desc: str | None = None
    mainline_tough_desc: str | None = None
    mainline_easy_desc: str | None = None
    mainline_normal_desc: str | None = None
    reject_sp_char_mission: int = 0
    added_reward_display_zone: str | None = None
    one_diamond_ap: int = 0
    char_rotation_preset_max_cnt: int = 0
    char_rotation_skin_list_max_cnt: int = 0
    default_cr_preset_char_id: str | None = Field(default=None, alias="defaultCRPresetCharId")
    default_cr_preset_char_skin_id: str | None = Field(default=None, alias="defaultCRPresetCharSkinId")
    default_cr_preset_bg_id: str | None = Field(default=None, alias="defaultCRPresetBGId")
    default_cr_preset_theme_id: str | None = Field(default=None, alias="defaultCRPresetThemeId")
    default_cr_preset_name: str | None = Field(default=None, alias="defaultCRPresetName")
    char_rotation_preset_track_ts: int = 0
    uniequip_archive_sys_track_ts: int = 0
    manufact_prompt_time: int = 0
    main_guide_actived_stage_id: str | None = None
    rich_text_styles: dict[str, str] | None = None
    char_assist_refresh_time: list[GameDataConstsCharAssistRefreshTimeState] | None = None
    normal_recruit_locked_string: list[str] | None = None
    common_potential_lvl_up_count: int = 0
    weekly_override_desc: str | None = None
    voucher_div: int = 0
    recruit_pool_version: int = 0
    v_006_recruit_time_step_1_refresh: int = 0
    v_006_recruit_time_step_2_check: int = 0
    v_006_recruit_time_step_2_flush: int = 0
    buy_ap_time_no_limit_flag: bool = False
    is_lmgts_enabled: bool = Field(default=False, alias="isLMGTSEnabled")
    legacy_time: int = 0
    legacy_item_list: list[ItemBundle] | None = None
    use_assist_social_pt: int = 0
    use_assist_social_pt_max_count: int = 0
    assist_be_used_social_pt: dict[int, int] | None = None
    push_forces: list[float] | None = None
    push_force_zero_index: int = 0
    normal_gacha_unlock_price: list[int] | None = None
    pull_forces: list[float] | None = None
    pull_force_zero_index: int = 0
    multi_in_come_by_rank: list[str] | None = None
    lmtgs_to_epgs_ratio: int = Field(default=0, alias="LMTGSToEPGSRatio")
    new_bee_gift_epgs: int = Field(default=0, alias="newBeeGiftEPGS")
    l_mtgs_desc_const_one: str | None = Field(default=None, alias="lMTGSDescConstOne")
    l_mtgs_desc_const_two: str | None = Field(default=None, alias="lMTGSDescConstTwo")
    def_cd_prim_color: str | None = Field(default=None, alias="defCDPrimColor")
    def_cd_sec_color: str | None = Field(default=None, alias="defCDSecColor")
    mail_banner_type: list[str] | None = None
    monthly_sub_warning_time: int = 0
    unlimit_skin_out_of_time: int = Field(default=0, alias="UnlimitSkinOutOfTime")
    replicate_shop_start_time: int = 0
    tso: int = Field(default=0, alias="TSO")
    is_dyn_illust_enabled: bool = False
    is_dyn_illust_start_enabled: bool = False
    is_classic_qc_shop_enabled: bool = Field(default=False, alias="isClassicQCShopEnabled")
    is_roguelike_topic_func_enabled: bool = False
    is_sandbox_perm_func_enabled: bool = False
    is_roguelike_avg_achieve_func_enabled: bool = False
    is_classic_potential_item_func_enabled: bool = False
    is_classic_gacha_pool_func_enabled: bool = False
    is_special_gacha_pool_func_enabled: bool = False
    is_voucher_classic_item_distinguishable: bool = False
    is_recal_rune_func_enabled: bool = False
    voucher_skin_redeem: int = 0
    voucher_skin_desc: str | None = None
    charm_equip_count: int = 0
    term_description_dict: dict[str, TermDescriptionData] | None = None
    story_review_unlock_item_lack_tip: str | None = None
    data_version: str | None = None
    res_pref_version: str | None = None
    announce_web_bus_type: str | None = None
    video_player_web_bus_type: str | None = None
    gacha_log_bus_type: str | None = None
    default_min_multiple_battle_times: int = 0
    default_max_multiple_battle_times: int = 0
    multiple_action_open: bool = False
    sub_profession_damage_type_pairs: dict[str, str] | None = None
    classic_protect_char: list[str] | None = None
    fever_game_data: GameDataConstsFeverGameData | None = None
    birthday_setting_desc: str | None = None
    birthday_setting_confirm_desc: str | None = None
    birthday_setting_leap_confirm_desc: str | None = None
    leap_birthday_reward_month: int = 0
    leap_birthday_reward_day: int = 0
    birthday_setting_show_stage_id: str | None = None
    is_birthday_func_enabled: bool = False
    is_so_char_enabled: bool = False
    avg_reader_mode_default_setting: GameDataConstsAVGReaderModeDefaultSetting | None = None
    friend_add_uid_limit: int = 0
    friend_url_format: str | None = None


# root_type clz_Torappu_GameDataConsts
GamedataConst = GameDataConsts


GameDataConstsCharAssistRefreshTimeState.model_rebuild()
ItemBundle.model_rebuild()
TermDescriptionData.model_rebuild()
GameDataConstsFeverGameData.model_rebuild()
GameDataConstsAVGReaderModeDefaultSetting.model_rebuild()
GameDataConsts.model_rebuild()

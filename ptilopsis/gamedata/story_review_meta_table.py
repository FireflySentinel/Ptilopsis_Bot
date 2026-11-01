"""story_review_meta_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/story_review_meta_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class MiniActTrialDataRuleType(IntEnum):
    """enum__Torappu_MiniActTrialData_RuleType"""

    NONE = 0
    TITLE = 1
    CONTENT = 2


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


class ActArchivePicType(IntEnum):
    """enum__Torappu_ActArchivePicType"""

    IMAGE = 0
    BACKGROUND = 1
    ENDING_IMAGE = 2
    ROGUE_IMAGE = 3


class ActArchiveResDataArchiveNewsLineType(IntEnum):
    """enum__Torappu_ActArchiveResData_ArchiveNewsLineType"""

    TextContent = 0
    ImageContent = 1


class Act17sideDataChapterIconType(IntEnum):
    """enum__Torappu_Act17sideData_ChapterIconType"""

    NORMAL = 0
    EX = 1
    HARD = 2


class MiniActTrialDataRuleData(GameDataModel):
    """clz_Torappu_MiniActTrialData_RuleData"""

    rule_type: str = "NONE"
    rule_text: str | None = None


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class MiniActTrialDataMiniActTrialRewardData(GameDataModel):
    """clz_Torappu_MiniActTrialData_MiniActTrialRewardData"""

    trial_reward_id: str | None = None
    order_id: int = 0
    act_id: str | None = None
    target_story_count: int = 0
    item: ItemBundle | None = None


class MiniActTrialDataMiniActTrialSingleData(GameDataModel):
    """clz_Torappu_MiniActTrialData_MiniActTrialSingleData"""

    act_id: str | None = None
    reward_start_time: int = 0
    theme_color: str | None = None
    reward_list: list[MiniActTrialDataMiniActTrialRewardData] | None = None


class MiniActTrialData(GameDataModel):
    """clz_Torappu_MiniActTrialData"""

    pre_show_days: int = 0
    rule_data_list: list[MiniActTrialDataRuleData] | None = None
    mini_act_trial_data_map: (
        dict[str, MiniActTrialDataMiniActTrialSingleData] | None
    ) = None


class ActArchiveResDataPicArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_PicArchiveResItemData"""

    id: str | None = None
    desc: str | None = None
    asset_path: str | None = None
    type: str = "IMAGE"
    sub_type: str | None = None
    pic_description: str | None = None
    kv_id: str | None = None


class ActArchiveResDataAudioArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_AudioArchiveResItemData"""

    id: str | None = None
    desc: str | None = None
    name: str | None = None


class ActArchiveResDataAvgArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_AvgArchiveResItemData"""

    id: str | None = None
    desc: str | None = None
    breif_path: str | None = None
    content_path: str | None = None
    image_path: str | None = None
    raw_brief: str | None = None
    title_icon_path: str | None = None


class ActArchiveResDataStoryArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_StoryArchiveResItemData"""

    id: str | None = None
    desc: str | None = None
    date: str | None = None
    pic: str | None = None
    text: str | None = None
    title_pic: str | None = None


class ActArchiveResDataNewsFormatData(GameDataModel):
    """clz_Torappu_ActArchiveResData_NewsFormatData"""

    type_id: str | None = None
    type_name: str | None = None
    type_logo: str | None = None
    type_main_logo: str | None = None
    type_main_sealing: str | None = None


class ActArchiveResDataActivityNewsLine(GameDataModel):
    """clz_Torappu_ActArchiveResData_ActivityNewsLine"""

    line_type: str = "TextContent"
    content: str | None = None


class ActArchiveResDataNewsArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_NewsArchiveResItemData"""

    id: str | None = None
    desc: str | None = None
    news_type: str | None = None
    news_format: ActArchiveResDataNewsFormatData | None = None
    news_text: str | None = None
    news_author: str | None = None
    param_p0: int = 0
    param_k: int = 0
    param_r: float = 0.0
    news_lines: list[ActArchiveResDataActivityNewsLine] | None = None


class ActArchiveResDataLandmarkArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_LandmarkArchiveResItemData"""

    landmark_id: str | None = None
    landmark_name: str | None = None
    landmark_pic: str | None = None
    landmark_desc: str | None = None
    landmark_eng_name: str | None = None


class ActArchiveResDataLogArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_LogArchiveResItemData"""

    log_id: str | None = None
    log_desc: str | None = None


class ActArchiveResDataChallengeBookArchiveResItemData(GameDataModel):
    """clz_Torappu_ActArchiveResData_ChallengeBookArchiveResItemData"""

    story_id: str | None = None
    title_name: str | None = None
    story_name: str | None = None
    text_id: str | None = None


class ActArchiveResData(GameDataModel):
    """clz_Torappu_ActArchiveResData"""

    pics: dict[str, ActArchiveResDataPicArchiveResItemData] | None = None
    audios: dict[str, ActArchiveResDataAudioArchiveResItemData] | None = None
    avgs: dict[str, ActArchiveResDataAvgArchiveResItemData] | None = None
    stories: dict[str, ActArchiveResDataStoryArchiveResItemData] | None = None
    news: dict[str, ActArchiveResDataNewsArchiveResItemData] | None = None
    landmarks: dict[str, ActArchiveResDataLandmarkArchiveResItemData] | None = None
    logs: dict[str, ActArchiveResDataLogArchiveResItemData] | None = None
    challenge_books: (
        dict[str, ActArchiveResDataChallengeBookArchiveResItemData] | None
    ) = None


class ActArchiveTimelineItemData(GameDataModel):
    """clz_Torappu_ActArchiveTimelineItemData"""

    timeline_id: str | None = None
    timeline_sort_id: int = 0
    timeline_title: str | None = None
    timeline_des: str | None = None
    pic_id_list: list[str] | None = None
    audio_id_list: list[str] | None = None
    avg_id_list: list[str] | None = None
    story_id_list: list[str] | None = None
    news_id_list: list[str] | None = None


class ActArchiveTimelineData(GameDataModel):
    """clz_Torappu_ActArchiveTimelineData"""

    timeline_list: list[ActArchiveTimelineItemData] | None = None


class ActArchiveMusicItemData(GameDataModel):
    """clz_Torappu_ActArchiveMusicItemData"""

    music_id: str | None = None
    music_sort_id: int = 0


class ActArchiveMusicData(GameDataModel):
    """clz_Torappu_ActArchiveMusicData"""

    musics: dict[str, ActArchiveMusicItemData] | None = None


class ActArchivePicItemData(GameDataModel):
    """clz_Torappu_ActArchivePicItemData"""

    pic_id: str | None = None
    pic_sort_id: int = 0


class ActArchivePicData(GameDataModel):
    """clz_Torappu_ActArchivePicData"""

    pics: dict[str, ActArchivePicItemData] | None = None


class ActArchiveStoryItemData(GameDataModel):
    """clz_Torappu_ActArchiveStoryItemData"""

    story_id: str | None = None
    story_sort_id: int = 0


class ActArchiveStoryData(GameDataModel):
    """clz_Torappu_ActArchiveStoryData"""

    stories: dict[str, ActArchiveStoryItemData] | None = None


class ActArchiveAvgItemData(GameDataModel):
    """clz_Torappu_ActArchiveAvgItemData"""

    avg_id: str | None = None
    avg_sort_id: int = 0


class ActArchiveAvgData(GameDataModel):
    """clz_Torappu_ActArchiveAvgData"""

    avgs: dict[str, ActArchiveAvgItemData] | None = None


class ActArchiveNewsItemData(GameDataModel):
    """clz_Torappu_ActArchiveNewsItemData"""

    news_id: str | None = None
    news_sort_id: int = 0


class ActArchiveNewsData(GameDataModel):
    """clz_Torappu_ActArchiveNewsData"""

    news: dict[str, ActArchiveNewsItemData] | None = None


class ActArchiveLandmarkItemData(GameDataModel):
    """clz_Torappu_ActArchiveLandmarkItemData"""

    landmark_id: str | None = None
    landmark_sort_id: int = 0


class ActArchiveChapterLogData(GameDataModel):
    """clz_Torappu_ActArchiveChapterLogData"""

    chapter_name: str | None = None
    display_id: str | None = None
    unlock_des: str | None = None
    logs: list[str] | None = None
    chapter_icon: str = "NORMAL"


class ActArchiveChallengeBookItemData(GameDataModel):
    """clz_Torappu_ActArchiveChallengeBookItemData"""

    story_id: str | None = None
    sort_id: int = 0


class ActArchiveChallengeBookData(GameDataModel):
    """clz_Torappu_ActArchiveChallengeBookData"""

    stories: dict[str, ActArchiveChallengeBookItemData] | None = None


class ActArchiveComponentData(GameDataModel):
    """clz_Torappu_ActArchiveComponentData"""

    timeline: ActArchiveTimelineData | None = None
    music: ActArchiveMusicData | None = None
    pic: ActArchivePicData | None = None
    story: ActArchiveStoryData | None = None
    avg: ActArchiveAvgData | None = None
    news: ActArchiveNewsData | None = None
    landmark: dict[str, ActArchiveLandmarkItemData] | None = None
    log: dict[str, ActArchiveChapterLogData] | None = None
    challenge_book: ActArchiveChallengeBookData | None = None


class ActArchiveComponentTable(GameDataModel):
    """clz_Torappu_ActArchiveComponentTable"""

    components: dict[str, ActArchiveComponentData] | None = None


class TrainingCampStageData(GameDataModel):
    """clz_Torappu_TrainingCampStageData"""

    stage_id: str | None = None
    stage_icon_id: str | None = None
    sort_id: int = 0
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None
    description: str | None = None
    end_char_id: str | None = None
    update_ts: int = 0


class NewTrainingCampStageData(GameDataModel):
    """clz_Torappu_NewTrainingCampStageData"""

    update_ts: int = 0
    stages: list[str] | None = None


class TrainingCampConsts(GameDataModel):
    """clz_Torappu_TrainingCampConsts"""

    unlock_stage_id: str | None = None
    update_desc: str | None = None
    reward_item: ItemBundle | None = None


class TrainingCampData(GameDataModel):
    """clz_Torappu_TrainingCampData"""

    stage_data: dict[str, TrainingCampStageData] | None = None
    new_training_camp_stages: list[NewTrainingCampStageData] | None = None
    consts: TrainingCampConsts | None = None


class StoryReviewMetaTable(GameDataModel):
    """clz_Torappu_StoryReviewMetaTable"""

    mini_act_trial_data: MiniActTrialData | None = None
    act_archive_res_data: ActArchiveResData | None = None
    act_archive_data: ActArchiveComponentTable | None = None
    training_camp_data: TrainingCampData | None = None


# root_type clz_Torappu_StoryReviewMetaTable


MiniActTrialDataRuleData.model_rebuild()
ItemBundle.model_rebuild()
MiniActTrialDataMiniActTrialRewardData.model_rebuild()
MiniActTrialDataMiniActTrialSingleData.model_rebuild()
MiniActTrialData.model_rebuild()
ActArchiveResDataPicArchiveResItemData.model_rebuild()
ActArchiveResDataAudioArchiveResItemData.model_rebuild()
ActArchiveResDataAvgArchiveResItemData.model_rebuild()
ActArchiveResDataStoryArchiveResItemData.model_rebuild()
ActArchiveResDataNewsFormatData.model_rebuild()
ActArchiveResDataActivityNewsLine.model_rebuild()
ActArchiveResDataNewsArchiveResItemData.model_rebuild()
ActArchiveResDataLandmarkArchiveResItemData.model_rebuild()
ActArchiveResDataLogArchiveResItemData.model_rebuild()
ActArchiveResDataChallengeBookArchiveResItemData.model_rebuild()
ActArchiveResData.model_rebuild()
ActArchiveTimelineItemData.model_rebuild()
ActArchiveTimelineData.model_rebuild()
ActArchiveMusicItemData.model_rebuild()
ActArchiveMusicData.model_rebuild()
ActArchivePicItemData.model_rebuild()
ActArchivePicData.model_rebuild()
ActArchiveStoryItemData.model_rebuild()
ActArchiveStoryData.model_rebuild()
ActArchiveAvgItemData.model_rebuild()
ActArchiveAvgData.model_rebuild()
ActArchiveNewsItemData.model_rebuild()
ActArchiveNewsData.model_rebuild()
ActArchiveLandmarkItemData.model_rebuild()
ActArchiveChapterLogData.model_rebuild()
ActArchiveChallengeBookItemData.model_rebuild()
ActArchiveChallengeBookData.model_rebuild()
ActArchiveComponentData.model_rebuild()
ActArchiveComponentTable.model_rebuild()
TrainingCampStageData.model_rebuild()
NewTrainingCampStageData.model_rebuild()
TrainingCampConsts.model_rebuild()
TrainingCampData.model_rebuild()
StoryReviewMetaTable.model_rebuild()

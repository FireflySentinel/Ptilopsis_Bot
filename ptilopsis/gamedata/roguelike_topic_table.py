"""roguelike_topic_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/roguelike_topic_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class RoguelikeModuleType(IntEnum):
    """enum__Torappu_RoguelikeModuleType"""

    NONE = 0
    SANCHECK = 1
    DICE = 2
    CHAOS = 3
    TOTEMBUFF = 4
    VISION = 5
    FRAGMENT = 6
    DISASTER = 7
    NODE_UPGRADE = 8
    COPPER = 9
    WRATH = 10
    CANDLE = 11
    SKY = 12
    GRID_ZONE = 13
    WEATHER = 14
    SCRAP = 15


class RoguelikeMonthChatTrigType(IntEnum):
    """enum__Torappu_RoguelikeMonthChatTrigType"""

    NONE = 0
    TRANSITING = 1
    DUNGEON = 2


class RoguelikeCharState(IntEnum):
    """enum__Torappu_RoguelikeCharState"""

    NORMAL = 0
    UPGRADE = 1
    UPGRADE_BUFF = 2
    UPGRADE_BONUS = 3
    FREE = 4
    ASSIST = 5
    THIRD = 6
    MONTHLY = 7
    THIRD_LOW = 8
    MERCENARY = 9


class RoguelikeEnrollType(IntEnum):
    """enum__Torappu_RoguelikeEnrollType"""

    DLC = 0
    REVIEW = 1


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


class RoguelikeGameMonthTaskClass(IntEnum):
    """enum__Torappu_RoguelikeGameMonthTaskClass"""

    NONE = 0
    C = 1
    B = 2
    A = 3


class RoguelikeTopicMode(IntEnum):
    """enum__Torappu_RoguelikeTopicMode"""

    NONE = 0
    EASY = 1
    NORMAL = 2
    HARD = 3
    NORML_END = 4
    MONTH_TEAM = 5
    CHALLENGE = 6


class RoguelikeTopicDifficultyWarningType(IntEnum):
    """enum__Torappu_RoguelikeTopicDifficultyWarningType"""

    NONE = 0
    NORMAL = 1
    HARD = 2


class RoguelikeTopicBankRewardType(IntEnum):
    """enum__Torappu_RoguelikeTopicBankRewardType"""

    NONE = 0
    UNLOCK_ITEM = 1
    ADD_SHOP_POS = 2
    UNLOCK_WITHDRAW = 3
    UNLOCK_SHOP_BATTLE = 4
    UNLOCK_SHOP_REFRESH = 5


class ActArchiveTotemType(IntEnum):
    """enum__Torappu_ActArchiveTotemType"""

    LOCATION = 0
    EFFECT = 1
    AFFIX = 2


class ActArchiveCopperType(IntEnum):
    """enum__Torappu_ActArchiveCopperType"""

    LUCK = 1
    COPPER = 2
    GILD = 3
    ERR_ZERO = 0


class RoguelikeCopperType(IntEnum):
    """enum__Torappu_RoguelikeCopperType"""

    NONE = 0
    BLANK = 1
    FIGHT = 2
    RESOURCE = 3
    UNSOUND = 4
    TREASURE = 5
    SPECIAL = 6


class RoguelikeCopperLuckyLevel(IntEnum):
    """enum__Torappu_RoguelikeCopperLuckyLevel"""

    NONE = 0
    HIGH = 1
    MID = 2
    LOW = 3


class ActArchiveType(IntEnum):
    """enum__Torappu_ActArchiveType"""

    NONE = 0
    TIMELINE = 1
    MUSIC = 2
    PIC = 3
    AVG = 4
    STORY = 5
    NEWS = 6
    BUFF = 7
    RELIC = 8
    CAPSULE = 9
    TRAP = 10
    CHAT = 11
    LANDMARK = 12
    LOG = 13
    ACTIVITY_ENTRY = 14
    DYNAMIC_MUSIC = 15
    DYNAMIC_PIC = 16
    ENDBOOK = 17
    DYNAMIC_STORY = 18
    TOTEM = 19
    CHAOS = 20
    CHALLENGE_BOOK = 21
    ACHIEVEMENT = 22
    QUEST = 23
    FRAGMENT = 24
    DISASTER = 25
    COPPER = 26
    WRATH = 27
    SCRAP = 28
    WEATHER = 29


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


class LevelDataDifficulty(IntEnum):
    """enum__Torappu_LevelData_Difficulty"""

    NONE = 0
    NORMAL = 1
    FOUR_STAR = 2
    EASY = 4
    SIX_STAR = 8
    ALL = 15


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


class RarityRankMask(IntEnum):
    """enum__Torappu_RarityRankMask"""

    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 4
    TIER_4 = 8
    TIER_5 = 16
    TIER_6 = 32
    ALL = 63


class ProfessionID(IntEnum):
    """enum__Torappu_ProfessionID"""

    WARRIOR = 0
    SNIPER = 1
    TANK = 2
    MEDIC = 3
    SUPPORT = 4
    CASTER = 5
    SPECIAL = 6
    PIONEER = 9
    TOKEN = 7
    TRAP = 8


class RarityRank(IntEnum):
    """enum__Torappu_RarityRank"""

    TIER_1 = 0
    TIER_2 = 1
    TIER_3 = 2
    TIER_4 = 3
    TIER_5 = 4
    TIER_6 = 5
    E_NUM = 6


class CustomTicketType(IntEnum):
    """enum__Torappu_CustomTicketType"""

    NONE = 0
    PURIFY = 1
    GET_CANDLE = 2


class RoguelikeGameRelicCheckType(IntEnum):
    """enum__Torappu_RoguelikeGameRelicCheckType"""

    NONE = 0
    PROFESSION = 1
    SUB_PROFESSION = 2
    UPGRADE = 3


class RoguelikeGameChoiceType(IntEnum):
    """enum__Torappu_RoguelikeGameChoiceType"""

    NONE = 0
    LEAVE = 1
    NEXT = 2
    NEXT_PROB = 3
    TRADE = 4
    TRADE_PROB = 5
    SACRIFICE = 6
    TELEPORT = 7
    EXPEDITION = 8
    WISH = 9
    TRADE_PROB_SHOW = 10
    SACRIFICE_TOTEM = 11
    WISH_ALL = 12
    KILL = 13
    USE_STASHED_TICKET = 14
    EXPEDITION_ALL = 15
    EXPEDITION_RETURN_ALL = 16
    PACIFY_WRATH = 17
    GILD_COPPER = 18
    ITEM_REROLL = 19
    ITEM_TOP_UP = 20
    GILD_COPPER_ALL = 21
    JUMP_PROB = 22
    JUMP = 23
    ZONE_END = 24
    MOVE = 25
    VISION = 26
    SCRAP_PAY_SHOW = 27


class RoguelikeChoiceLeftDecoType(IntEnum):
    """enum__Torappu_RoguelikeChoiceLeftDecoType"""

    NONE = 0
    TASK = 1
    TASK_REWARD = 2
    DICE = 3
    VISION = 4


class RoguelikeChoiceDisplayType(IntEnum):
    """enum__Torappu_RoguelikeChoiceDisplayType"""

    NONE = 0
    NORMAL = 1
    ITEM = 2
    TASK = 3


class RoguelikeChoiceHintType(IntEnum):
    """enum__Torappu_RoguelikeChoiceHintType"""

    NONE = 0
    ITEM = 1
    CANDLED_CHAR = 2
    GUIDED_CHAR = 3
    SACRIFICE = 4
    SACRIFICE_TOTEM = 5
    SACRIFICE_SCRAP = 6
    EXPEDITION = 7
    CANDLE = 8
    GUIDED = 9
    HP = 10
    VISION = 11
    STASHED_RECRUIT = 12
    SEED_COST = 13
    ITEM_COST = 14
    CHAOS = 15
    FRAGMENT = 16
    SP_ZONE_AP = 17
    COPPER_LUCK = 18
    AP_LEFT = 19


class RoguelikeEventType(IntEnum):
    """enum__Torappu_RoguelikeEventType"""

    NONE = 0
    BATTLE_NORMAL = 1
    BATTLE_ELITE = 2
    BATTLE_BOSS = 4
    SHOP = 8
    REST = 16
    INCIDENT = 32
    TREASURE = 64
    ENTERTAINMENT = 128
    UNKNOWN = 256
    WISH = 512
    SACRIFICE = 1024
    EXPEDITION = 2048
    BATTLE_SHOP = 4096
    PORTAL = 8192
    MISSION = 16384
    STORY = 32768
    STORY_HIDDEN = 65536
    ALCHEMY = 131072
    DUEL = 262144
    STASHED_RECRUIT = 524288
    SPECIAL_ZONE = 1048576
    SCRAP_SHOP = 2097152
    DOOR = 4194304
    FINAL = 8388608
    EVACUATE = 16777216
    EMPLOY = 33554432
    LIGHT = 67108864
    BATTLE_SAVAGE = 134217728
    EMPTY = 268435456
    BATTLES = 134217735
    CHOICES = 27127536
    EVENTS = 402521848
    ALL = 536739583


class RoguelikeGameVariationType(IntEnum):
    """enum__Torappu_RoguelikeGameVariationType"""

    NONE = 0
    MAP = 1
    RES = 2
    BAT = 3


class RoguelikeGameCharBuffType(IntEnum):
    """enum__Torappu_RoguelikeGameCharBuffType"""

    NONE = 0
    MUTATION = 1
    EVOLUTION = 2
    FROM_RELIC = 3


class RoguelikeTaskRarity(IntEnum):
    """enum__Torappu_RoguelikeTaskRarity"""

    NORMAL = 0
    RARE = 1
    SUPER_RARE = 2


class RoguelikeBankRewardCountType(IntEnum):
    """enum__Torappu_RoguelikeBankRewardCountType"""

    HIGHEST_RECORD = 0
    TOTAL_SUM = 1


class RoguelikeRewardExDropTagSrcType(IntEnum):
    """enum__Torappu_RoguelikeRewardExDropTagSrcType"""

    NONE = 0
    TREASURE = 1
    TOTEM = 2
    EXPLORE_TOOL = 3
    COPPER = 4
    EVIL_TEMPLE = 5
    TREASURE_MAP = 6
    LOOP_CHIP = 7
    STEP = 8
    GREED = 9
    GOLDEN_AGE = 10
    ADVENTURER_EXTRA = 11


class TipDataCategory(IntEnum):
    """enum__Torappu_TipData_Category"""

    NONE = 0
    BATTLE = 1
    UI = 2
    BUILDING = 4
    GACHA = 8
    MISC = 16
    ALL = 31


class RoguelikeGameItemType(IntEnum):
    """enum__Torappu_RoguelikeGameItemType"""

    NONE = 0
    HP = 1
    HPMAX = 2
    GOLD = 3
    POPULATION = 4
    EXP = 5
    SQUAD_CAPACITY = 6
    RECRUIT_TICKET = 7
    UPGRADE_TICKET = 8
    RELIC = 9
    BP_POINT = 10
    GROW_POINT = 11
    BAND = 12
    ACTIVE_TOOL = 13
    CAPSULE = 14
    POOL = 15
    RL_BP = 16
    RL_GP = 17
    KEY_POINT = 18
    SAN_POINT = 19
    DICE_POINT = 20
    DICE_TYPE = 21
    SHIELD = 22
    LOCKED_TREASURE = 23
    CUSTOM_TICKET = 24
    TOTEM = 25
    TOTEM_EFFECT = 26
    FEATURE = 27
    VISION = 28
    CHAOS = 29
    CHAOS_PURIFY = 30
    CHAOS_LEVEL = 31
    EXPLORE_TOOL = 32
    FRAGMENT = 33
    MAX_WEIGHT = 34
    DISASTER = 35
    DISASTER_TYPE = 36
    ABSTRACT_DISASTER = 37
    PILL = 38
    BIGPILL = 39
    COPPER = 40
    COPPER_BUFF = 41
    DIVINATION_KIT = 42
    WRATH = 43
    SPECIAL_ZONE_AP = 44
    COPPER_DRAW_NUM = 45
    STASH_RECRUIT_LIMIT = 46
    NODE_BUOY = 47
    SCRAP = 48
    LEGACY = 49
    CHARACTER = 50


class RoguelikeGameItemSubType(IntEnum):
    """enum__Torappu_RoguelikeGameItemSubType"""

    NONE = 0
    CURSE = 1
    TEMP_TICKET = 2
    TOTEM_UPPER = 4
    TOTEM_LOWER = 8
    SECRET = 16
    SINGLE_RAND_FREE = 32
    RED_CAPSULE = 64


class RoguelikeGameItemRarity(IntEnum):
    """enum__Torappu_RoguelikeGameItemRarity"""

    NONE = 0
    BORN = 1
    NORMAL = 2
    RARE = 3
    SUPER_RARE = 4


class RoguelikeEndingDetailTextType(IntEnum):
    """enum__Torappu_RoguelikeEndingDetailText_Type"""

    SHOW_CHOICE = 0
    SHOW_RELIC = 1
    SHOW_CAPSULE = 2
    SHOW_ACTIVE_TOOL = 3
    SHOW_ACCELERATE_CHAR = 4
    SHOW_NORMAL_RECRUIT = 5
    SHOW_DIRECT_RECRUIT = 6
    SHOW_FRIEND_RECRUIT = 7
    SHOW_FREE_RECRUIT = 8
    BUY = 9
    INVEST = 10
    SHOW_STAGE = 11
    SHOW_CONST = 12
    SUM = 13
    SHOW_BOSS_END = 14
    SHOW_BATTLE = 15


class RoguelikeExpStyleConfigParam(IntEnum):
    """enum__Torappu_RoguelikeExpStyleConfigParam"""

    BATTLE_END_HP_LOSE_TEXT = 0


class RoguelikeActivityType(IntEnum):
    """enum__Torappu_RoguelikeActivityType"""

    NONE = 0
    SEED_MODE = 1


class SanEffectRank(IntEnum):
    """enum__Torappu_SanEffectRank"""

    SAN_EFFECT_0 = 0
    SAN_EFFECT_1 = 1
    SAN_EFFECT_2 = 2
    SAN_EFFECT_3 = 3


class DiceResultClass(IntEnum):
    """enum__Torappu_DiceResultClass"""

    VERYBAD = 0
    BAD = 1
    NORMAL = 2
    GOOD = 3
    GREAT = 4
    BEST = 4


class DiceResultShowType(IntEnum):
    """enum__Torappu_DiceResultShowType"""

    RAW_TEXT = 0
    MUTATION = 1
    VIRTUE = 2


class ChaosEffectRank(IntEnum):
    """enum__Torappu_ChaosEffectRank"""

    CHAOS_EFFECT_0 = 0
    CHAOS_EFFECT_1 = 1
    CHAOS_EFFECT_2 = 2


class RoguelikeTotemColorType(IntEnum):
    """enum__Torappu_RoguelikeTotemColorType"""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    ALL = 4


class RoguelikeTotemPosType(IntEnum):
    """enum__Torappu_RoguelikeTotemPosType"""

    LOCATION = 0
    EFFECT = 1


class RoguelikeTotemBlurNodeType(IntEnum):
    """enum__Torappu_RoguelikeTotemBlurNodeType"""

    NONE = 0
    BATTLE = 1
    NO_BATTLE = 2


class RoguelikeVisionModuleDataVisionChoiceCheckType(IntEnum):
    """enum__Torappu_RoguelikeVisionModuleData_VisionChoiceCheckType"""

    LOWER = 0
    UPPER = 1


class RoguelikeFragmentType(IntEnum):
    """enum__Torappu_RoguelikeFragmentType"""

    NONE = 0
    INSPIRATION = 1
    WISH = 2
    IDEA = 3


class AlchemyPoolRarityType(IntEnum):
    """enum__Torappu_AlchemyPoolRarityType"""

    NONE = -1
    NORMAL = 0
    RARE = 1
    SUPER_RARE = 2


class RoguelikeCopperBuffType(IntEnum):
    """enum__Torappu_RoguelikeCopperBuffType"""

    NONE = 0
    REFRESH = 1
    MOVE = 2


class RoguelikeCopperDivineType(IntEnum):
    """enum__Torappu_RoguelikeCopperDivineType"""

    NONE = 0
    DIVINE = 1
    EVENT = 2


class RoguelikeCopperDivineResultType(IntEnum):
    """enum__Torappu_RoguelikeCopperDivineResultType"""

    NONE = 0
    GOOD = 1
    NORMAL = 2
    BAD = 3


class RoguelikeSkyZoneNodeType(IntEnum):
    """enum__Torappu_RoguelikeSkyZoneNodeType"""

    NONE = 0
    ORIGIN = 1
    BATTLE = 2
    TRIAL_GATE = 4
    INCIDENT = 8
    TREASURE = 16
    SHOP = 32
    SACRIFICE = 64
    ENTERTAINMENT = 128
    MARKET = 256
    BATTLE_HARD = 512
    INCIDENT_BOSS = 1024
    INCIDENT_BOSS_ONLY = 2048
    CHOICES = 3548
    BATTLES = 514


class RoguelikeScrapType(IntEnum):
    """enum__Torappu_RoguelikeScrapType"""

    ERROR = -1
    NONE = 0
    MOVE = 1
    GOODS = 2
    PASSIVE = 3


class RoguelikeMoveScrapRangeType(IntEnum):
    """enum__Torappu_RoguelikeMoveScrapRangeType"""

    RANGE = 0
    FULL_MAP = 1
    FULL_ROW_COL = 2


class SharedConstsDirection(IntEnum):
    """enum__Torappu_SharedConsts_Direction"""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    E_NUM = 4
    INVALID = 4


class RoguelikeTopicDevNodeType(IntEnum):
    """enum__Torappu_RoguelikeTopicDevNodeType"""

    BRANCH = 0
    KEY = 1
    NONE = 10


class RoguelikeTopicDevTokenDisplayForm(IntEnum):
    """enum__Torappu_RoguelikeTopicDevTokenDisplayForm"""

    ABSOLUTE_VAL = 0
    PERCENTAGE = 1


class RL02DevelopmentNodeType(IntEnum):
    """enum__Torappu_RL02DevelopmentNodeType"""

    NONE = 0
    SMALL = 1
    NORMAL = 2
    LARGE_RHODES = 3
    LARGE_ABYSSAL = 4
    LARGE_IBERIA = 5


class RL02DevelopmentEffectType(IntEnum):
    """enum__Torappu_RL02DevelopmentEffectType"""

    BUFF = 0
    RAW_TEXT_EFFECT = 1
    RAW_TEXT_BAND = 2
    NONE = 10


class RL03DevelopmentNodeType(IntEnum):
    """enum__Torappu_RL03DevelopmentNodeType"""

    NONE = 0
    NORMAL = 1
    KEY = 2
    DIFFICULTY = 3


class RL03DevelopmentEffectType(IntEnum):
    """enum__Torappu_RL03DevelopmentEffectType"""

    BUFF = 0
    RAW_TEXT_EFFECT = 1
    RAW_TEXT_BAND = 2


class RoguelikeCommonDevelopmentNodeType(IntEnum):
    """enum__Torappu_RoguelikeCommonDevelopmentNodeType"""

    NONE = 0
    NORMAL = 1
    KEY = 2
    DIFFICULTY = 3


class RoguelikeCommonDevelopmentEffectType(IntEnum):
    """enum__Torappu_RoguelikeCommonDevelopmentEffectType"""

    BUFF = 0
    RAW_TEXT_EFFECT = 1
    RAW_TEXT_BAND = 2


class RoguelikeTopicBasicDataHomeEntryDisplayData(GameDataModel):
    """clz_Torappu_RoguelikeTopicBasicData_HomeEntryDisplayData"""

    topic_id: str | None = None
    display_id: str | None = None
    start_ts: int = 0
    end_ts: int = 0


class RoguelikeTopicConfig(GameDataModel):
    """clz_Torappu_RoguelikeTopicConfig"""

    load_char_card_plugin: bool = False
    web_bus_type: str | None = None
    month_chat_trig_type: str = "NONE"
    load_reward_hp_deco_plugin: bool = False
    load_reward_extra_info_plugin: bool = False


class RoguelikeTopicBasicData(GameDataModel):
    """clz_Torappu_RoguelikeTopicBasicData"""

    id: str | None = None
    name: str | None = None
    start_time: int = 0
    disappear_time_on_main_screen: int = 0
    sort: int = 0
    show_medal_id: str | None = None
    medal_group_id: str | None = None
    full_stored_time: int = 0
    line_text: str | None = None
    home_entry_display_data: (
        list[RoguelikeTopicBasicDataHomeEntryDisplayData] | None
    ) = None
    module_types: list[str] | None = None
    config: RoguelikeTopicConfig | None = None


class RoguelikeTopicConstPredefinedChar(GameDataModel):
    """clz_Torappu_RoguelikeTopicConst_PredefinedChar"""

    char_id: str | None = None
    can_be_free: bool = False
    uni_equip_id: str | None = None
    recruit_type: str = "NORMAL"


class RoguelikeTopicConst(GameDataModel):
    """clz_Torappu_RoguelikeTopicConst"""

    milestone_token_ratio: int = 0
    outer_buff_token_ratio: float = 0.0
    relic_token_ratio: int = 0
    rogue_system_unlock_stage: str | None = None
    ordi_mode_re_open_cool_down: int = 0
    month_mode_re_open_cool_down: int = 0
    monthly_task_uncompleted_time: int = 0
    monthly_task_manual_refresh_limit: int = 0
    monthly_team_uncompleted_time: int = 0
    bp_purchase_system_unlock_time: int = 0
    predefined_chars: dict[str, RoguelikeTopicConstPredefinedChar] | None = None


class RoguelikeTopicUpdate(GameDataModel):
    """clz_Torappu_RoguelikeTopicUpdate"""

    update_id: str | None = None
    topic_update_time: int = 0
    topic_end_time: int = 0


class RoguelikeTopicEnroll(GameDataModel):
    """clz_Torappu_RoguelikeTopicEnroll"""

    enroll_id: str | None = None
    enroll_time: int = 0
    enroll_type: str = "DLC"
    enroll_notice_end_time: int = 0


class RoguelikeTopicBP(GameDataModel):
    """clz_Torappu_RoguelikeTopicBP"""

    id: str | None = None
    level: int = 0
    token_num: int = 0
    next_token_num: int = 0
    item_id: str | None = Field(default=None, alias="itemID")
    item_type: str = "NONE"
    item_count: int = 0
    is_good_prize: bool = False
    is_grand_prize: bool = False
    is_return_display: bool = False
    return_sort_id: int = 0


class RoguelikeTopicMilestoneUpdateData(GameDataModel):
    """clz_Torappu_RoguelikeTopicMilestoneUpdateData"""

    update_time: int = 0
    end_time: int = 0
    max_bp_level: int = 0
    max_bp_count: int = 0
    max_display_bp_count: int = 0


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class RoguelikeTopicBPGrandPrize(GameDataModel):
    """clz_Torappu_RoguelikeTopicBPGrandPrize"""

    grand_prize_display_id: str | None = None
    sort_id: int = 0
    display_unlock_year: int = 0
    display_unlock_month: int = 0
    acquire_title: str | None = None
    purchase_title: str | None = None
    display_name: str | None = None
    display_discription: str | None = None
    bp_level_id: str | None = None
    item_bundle: ItemBundle | None = None
    detail_announce_time: str | None = None
    pic_id_aftrer_unlock: str | None = None


class RoguelikeTopicMonthMission(GameDataModel):
    """clz_Torappu_RoguelikeTopicMonthMission"""

    id: str | None = None
    task_name: str | None = None
    task_class: str = "NONE"
    inner_class_weight: int = 0
    template: str | None = None
    param_list: list[str] | None = None
    desc: str | None = None
    token_reward_num: int = 0


class RoguelikeTopicMonthSquadTeamChar(GameDataModel):
    """clz_Torappu_RoguelikeTopicMonthSquadTeamChar"""

    team_char_id: str | None = None
    team_tmpl_id: str | None = None


class RoguelikeTopicMonthSquad(GameDataModel):
    """clz_Torappu_RoguelikeTopicMonthSquad"""

    id: str | None = None
    team_name: str | None = None
    team_sub_name: str | None = None
    team_flavor_desc: str | None = None
    team_des: str | None = None
    team_color: str | None = None
    team_month: str | None = None
    team_year: str | None = None
    team_index: str | None = None
    team_chars: list[RoguelikeTopicMonthSquadTeamChar] | None = None
    zone_id: str | None = None
    chat_id: str | None = None
    token_reward_num: int = 0
    items: list[ItemBundle] | None = None
    start_time: int = 0
    end_time: int = 0
    task_des: str | None = None


class RoguelikeTopicChallengeTask(GameDataModel):
    """clz_Torappu_RoguelikeTopicChallengeTask"""

    task_id: str | None = None
    task_des: str | None = None
    completion_class: str | None = None
    completion_params: list[str] | None = None


class RoguelikeTopicChallenge(GameDataModel):
    """clz_Torappu_RoguelikeTopicChallenge"""

    challenge_id: str | None = None
    sort_id: int = 0
    challenge_name: str | None = None
    challenge_group: int = 0
    challenge_group_sort_id: int = 0
    challenge_group_name: str | None = None
    challenge_unlock_desc: str | None = None
    challenge_unlock_toast_desc: str | None = None
    challenge_des: str | None = None
    challenge_condition_des: list[str] | None = None
    challenge_tasks: dict[str, RoguelikeTopicChallengeTask] | None = None
    default_task_id: str | None = None
    rewards: list[ItemBundle] | None = None
    challenge_story_id: str | None = None


class RoguelikeTopicDifficultyRuleDescReplacement(GameDataModel):
    """clz_Torappu_RoguelikeTopicDifficulty_RuleDescReplacement"""

    enroll_id: str | None = None
    rule_desc: str | None = None


class RoguelikeTopicDifficulty(GameDataModel):
    """clz_Torappu_RoguelikeTopicDifficulty"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    name: str | None = None
    name_image: str | None = None
    sub_name: str | None = None
    enroll_id: str | None = None
    have_initial_relic_icon: bool = False
    score_factor: float = 0.0
    can_unlock_item: bool = False
    do_month_task: bool = False
    rule_desc: str | None = None
    rule_desc_replacements: list[RoguelikeTopicDifficultyRuleDescReplacement] | None = (
        None
    )
    fail_title: str | None = None
    fail_image_id: str | None = None
    fail_force_desc: str | None = None
    sort_id: int = 0
    equivalent_grade: int = 0
    color: str | None = None
    bp_value: int = 0
    boss_value: int = 0
    add_desc: str | None = None
    warning_type: str = "NONE"
    unlock_text: str | None = None
    display_icon_id: str | None = None
    hide_ending_story: bool = False
    have_legacy: bool = False


class RoguelikeTopicBankReward(GameDataModel):
    """clz_Torappu_RoguelikeTopicBankReward"""

    reward_id: str | None = None
    unlock_gold_cnt: int = 0
    reward_type: str = "NONE"
    desc: str | None = None


class ActArchiveRelicItemData(GameDataModel):
    """clz_Torappu_ActArchiveRelicItemData"""

    relic_id: str | None = None
    relic_sort_id: int = 0
    relic_group_id: int = 0
    order_id: str | None = None
    is_sp_relic: bool = False
    enroll_id: str | None = None


class ActArchiveRelicData(GameDataModel):
    """clz_Torappu_ActArchiveRelicData"""

    relic: dict[str, ActArchiveRelicItemData] | None = None


class ActArchiveCapsuleItemData(GameDataModel):
    """clz_Torappu_ActArchiveCapsuleItemData"""

    capsule_id: str | None = None
    capsule_sort_id: int = 0
    english_name: str | None = None
    enroll_id: str | None = None


class ActArchiveCapsuleData(GameDataModel):
    """clz_Torappu_ActArchiveCapsuleData"""

    capsule: dict[str, ActArchiveCapsuleItemData] | None = None


class ActArchiveTrapItemData(GameDataModel):
    """clz_Torappu_ActArchiveTrapItemData"""

    trap_id: str | None = None
    trap_sort_id: int = 0
    order_id: str | None = None
    enroll_id: str | None = None


class ActArchiveTrapData(GameDataModel):
    """clz_Torappu_ActArchiveTrapData"""

    trap: dict[str, ActArchiveTrapItemData] | None = None


class ActArchiveChatItemData(GameDataModel):
    """clz_Torappu_ActArchiveChatItemData"""

    floor: int = 0
    chat_zone_id: str | None = None
    chat_desc: str | None = None
    chat_story_id: str | None = None


class ActArchiveChatGroupData(GameDataModel):
    """clz_Torappu_ActArchiveChatGroupData"""

    sort_id: int = 0
    chat_item_list: list[ActArchiveChatItemData] | None = None


class ActArchiveChatData(GameDataModel):
    """clz_Torappu_ActArchiveChatData"""

    chat: dict[str, ActArchiveChatGroupData] | None = None


class ActArchiveEndbookItemData(GameDataModel):
    """clz_Torappu_ActArchiveEndbookItemData"""

    end_book_id: str | None = None
    sort_id: int = 0
    enroll_id: str | None = None
    is_last: bool = False
    endbook_name: str | None = None
    unlock_desc: str | None = None
    text_id: str | None = None


class ActArchiveEndbookGroupData(GameDataModel):
    """clz_Torappu_ActArchiveEndbookGroupData"""

    end_id: str | None = None
    ending_id: str | None = None
    sort_id: int = 0
    title: str | None = None
    cg_id: str | None = None
    back_blur_id: str | None = None
    card_id: str | None = None
    has_avg: bool = False
    avg_id: str | None = None
    client_endbook_item_datas: list[ActArchiveEndbookItemData] | None = None


class ActArchiveEndbookData(GameDataModel):
    """clz_Torappu_ActArchiveEndbookData"""

    endbook: dict[str, ActArchiveEndbookGroupData] | None = None


class ActArchiveBuffItemData(GameDataModel):
    """clz_Torappu_ActArchiveBuffItemData"""

    buff_id: str | None = None
    buff_group_index: int = 0
    inner_sort_id: int = 0
    name: str | None = None
    icon_id: str | None = None
    usage: str | None = None
    desc: str | None = None
    color: str | None = None


class ActArchiveBuffData(GameDataModel):
    """clz_Torappu_ActArchiveBuffData"""

    buff: dict[str, ActArchiveBuffItemData] | None = None


class ActArchiveTotemItemData(GameDataModel):
    """clz_Torappu_ActArchiveTotemItemData"""

    id: str | None = None
    type: str = "LOCATION"
    enroll_condition_id: str | None = None
    sort_id: int = 0


class ActArchiveTotemData(GameDataModel):
    """clz_Torappu_ActArchiveTotemData"""

    totem: dict[str, ActArchiveTotemItemData] | None = None


class ActArchiveChaosItemData(GameDataModel):
    """clz_Torappu_ActArchiveChaosItemData"""

    id: str | None = None
    is_hidden: bool = False
    enroll_id: str | None = None
    sort_id: int = 0


class ActArchiveChaosData(GameDataModel):
    """clz_Torappu_ActArchiveChaosData"""

    chaos: dict[str, ActArchiveChaosItemData] | None = None


class ActArchiveFragmentItemData(GameDataModel):
    """clz_Torappu_ActArchiveFragmentItemData"""

    fragment_id: str | None = None
    sort_id: int = 0
    enroll_condition_id: str | None = None


class ActArchiveFragmentData(GameDataModel):
    """clz_Torappu_ActArchiveFragmentData"""

    fragment: dict[str, ActArchiveFragmentItemData] | None = None


class ActArchiveDisasterItemData(GameDataModel):
    """clz_Torappu_ActArchiveDisasterItemData"""

    disaster_id: str | None = None
    sort_id: int = 0
    enroll_condition_id: str | None = None
    pic_small_id: str | None = None
    pic_big_active_id: str | None = None
    pic_big_inactive_id: str | None = None


class ActArchiveDisasterData(GameDataModel):
    """clz_Torappu_ActArchiveDisasterData"""

    disasters: dict[str, ActArchiveDisasterItemData] | None = None


class ActArchiveWrathItemData(GameDataModel):
    """clz_Torappu_ActArchiveWrathItemData"""

    wrath_id: str | None = None
    sort_id: int = 0
    pic_title_id: str | None = None
    pic_small_inactive_id: str | None = None
    pic_small_active_id: str | None = None
    pic_big_active_id: str | None = None
    pic_big_inactive_id: str | None = None
    enroll_id: str | None = None
    is_sp: bool = False


class ActArchiveWrathData(GameDataModel):
    """clz_Torappu_ActArchiveWrathData"""

    wraths: dict[str, ActArchiveWrathItemData] | None = None


class ActArchiveCopperItemData(GameDataModel):
    """clz_Torappu_ActArchiveCopperItemData"""

    id: str | None = None
    display_copper_id: str | None = None
    archive_type: str = "ERR_ZERO"
    copper_type: str = "NONE"
    sort_id: int = 0
    enroll_id: str | None = None
    coppers_in_group: list[str] | None = None


class ActArchiveCopperTypeData(GameDataModel):
    """clz_Torappu_ActArchiveCopperTypeData"""

    copper_type: str = "NONE"
    type_name: str | None = None
    type_icon_id: str | None = None


class ActArchiveCopperGildData(GameDataModel):
    """clz_Torappu_ActArchiveCopperGildData"""

    gild_type_id: str | None = None
    gild_name: str | None = None
    gild_desc: str | None = None


class ActArchiveCopperLuckyLevelData(GameDataModel):
    """clz_Torappu_ActArchiveCopperLuckyLevelData"""

    lucky_level: str = "NONE"
    lucky_name: str | None = None
    lucky_desc: str | None = None
    lucky_usage: str | None = None


class ActArchiveCopperData(GameDataModel):
    """clz_Torappu_ActArchiveCopperData"""

    coppers: dict[str, ActArchiveCopperItemData] | None = None
    copper_types: dict[str, ActArchiveCopperTypeData] | None = None
    gilds: dict[str, ActArchiveCopperGildData] | None = None
    lucky_levels: dict[str, ActArchiveCopperLuckyLevelData] | None = None


class ActArchiveScrapItemData(GameDataModel):
    """clz_Torappu_ActArchiveScrapItemData"""

    scrap_id: str | None = None
    sort_id: int = 0
    enroll_condition_id: str | None = None


class ActArchiveScrapData(GameDataModel):
    """clz_Torappu_ActArchiveScrapData"""

    scraps: dict[str, ActArchiveScrapItemData] | None = None


class ActArchiveWeatherItemData(GameDataModel):
    """clz_Torappu_ActArchiveWeatherItemData"""

    weather_id: str | None = None
    sort_id: int = 0
    enroll_condition_id: str | None = None


class ActArchiveWeatherData(GameDataModel):
    """clz_Torappu_ActArchiveWeatherData"""

    weathers: dict[str, ActArchiveWeatherItemData] | None = None


class RoguelikeArchiveComponentData(GameDataModel):
    """clz_Torappu_RoguelikeArchiveComponentData"""

    relic: ActArchiveRelicData | None = None
    capsule: ActArchiveCapsuleData | None = None
    trap: ActArchiveTrapData | None = None
    chat: ActArchiveChatData | None = None
    endbook: ActArchiveEndbookData | None = None
    buff: ActArchiveBuffData | None = None
    totem: ActArchiveTotemData | None = None
    chaos: ActArchiveChaosData | None = None
    fragment: ActArchiveFragmentData | None = None
    disaster: ActArchiveDisasterData | None = None
    wrath: ActArchiveWrathData | None = None
    copper: ActArchiveCopperData | None = None
    scrap: ActArchiveScrapData | None = None
    weather: ActArchiveWeatherData | None = None


class RoguelikeArchiveUnlockCondDesc(GameDataModel):
    """clz_Torappu_RoguelikeArchiveUnlockCondDesc"""

    archive_type: str = "NONE"
    description: str | None = None


class RoguelikeArchiveEnroll(GameDataModel):
    """clz_Torappu_RoguelikeArchiveEnroll"""

    archive_type: str = "NONE"
    enroll_id: str | None = None


class RoguelikeArchiveUnlockCondData(GameDataModel):
    """clz_Torappu_RoguelikeArchiveUnlockCondData"""

    unlock_cond_desc: dict[str, RoguelikeArchiveUnlockCondDesc] | None = None
    enroll: dict[str, RoguelikeArchiveEnroll] | None = None


class RoguelikeTopicDetailConstPlayerLevelData(GameDataModel):
    """clz_Torappu_RoguelikeTopicDetailConst_PlayerLevelData"""

    exp: int = 0
    population_up: int = 0
    squad_capacity_up: int = 0
    battle_char_limit_up: int = 0
    max_hp_up: int = 0


class RoguelikeTopicDetailConstCharUpgradeData(GameDataModel):
    """clz_Torappu_RoguelikeTopicDetailConst_CharUpgradeData"""

    evolve_phase: str = "PHASE_0"
    skill_level: int = 0
    skill_specialize_level: int = 0


class RoguelikeTopicDetailConstPredefinedPlayerLevelData(GameDataModel):
    """clz_Torappu_RoguelikeTopicDetailConst_PredefinedPlayerLevelData"""

    levels: dict[int, RoguelikeTopicDetailConstPlayerLevelData] | None = None


class RoguelikeTopicDetailConst(GameDataModel):
    """clz_Torappu_RoguelikeTopicDetailConst"""

    player_level_table: dict[int, RoguelikeTopicDetailConstPlayerLevelData] | None = (
        None
    )
    char_upgrade_table: dict[int, RoguelikeTopicDetailConstCharUpgradeData] | None = (
        None
    )
    difficulty_upgrade_relic_desc_table: dict[int, str] | None = None
    predefined_level_table: (
        dict[str, RoguelikeTopicDetailConstPredefinedPlayerLevelData] | None
    ) = None
    token_bp_id: str | None = None
    token_outer_buff_id: str | None = None
    sp_operator_locked_message: str | None = None
    previewed_rewards_according_update_id: str | None = None
    tip_button_name: str | None = None
    collect_button_name: str | None = None
    bp_system_name: str | None = None
    auto_set_kv: str | None = Field(default=None, alias="autoSetKV")
    bp_purchase_active_enroll: str | None = None
    default_expedition_select_desc: str | None = None
    got_char_mutation_buff_toast: str | None = None
    got_char_evolution_buff_toast: str | None = None
    got_squad_buff_toast: str | None = None
    lose_char_buff_toast: str | None = None
    month_team_system_name: str | None = None
    battle_pass_update_name: str | None = None
    month_char_card_tag_name: str | None = None
    month_team_desc_tag_name: str | None = None
    outer_buff_complete_text: str | None = None
    outer_progress_text_color: str | None = None
    challenge_task_target_name: str | None = None
    challenge_task_condition_name: str | None = None
    challenge_task_reward_name: str | None = None
    challenge_task_mode_name: str | None = None
    challenge_task_name: str | None = None
    outer_buff_token_sum: int = 0
    need_all_front_node: bool = False
    show_blur_back: bool = False
    ending_icon_border_difficulty: int = 0
    ending_icon_border_count: int = 0
    copy_seed_mode_info: str | None = None
    copy_succeeded_text_hint: str | None = None
    historical_records_count: int = 0
    historical_records_start_time: int = 0
    historical_records_mode: str = "NONE"


class RoguelikeGameInitData(GameDataModel):
    """clz_Torappu_RoguelikeGameInitData"""

    mode_id: str = "NONE"
    mode_grade: int = 0
    predefined_id: str | None = None
    predefined_style: str | None = None
    initial_band_relic: list[str] | None = None
    initial_recruit_group: list[str] | None = None
    initial_hp: int = 0
    initial_population: int = 0
    initial_gold: int = 0
    initial_squad_capacity: int = 0
    initial_shield: int = 0
    initial_max_hp: int = 0
    initial_key: int = 0


class RoguelikeGameStageData(GameDataModel):
    """clz_Torappu_RoguelikeGameStageData"""

    id: str | None = None
    linked_stage_id: str | None = None
    level_id: str | None = None
    level_replace_ids: list[str] | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None
    description: str | None = None
    elite_desc: str | None = None
    is_boss: int = 0
    is_elite: int = 0
    difficulty: str = "NONE"
    capsule_pool: str | None = None
    capsule_prob: float = 0.0
    vutres_prob: list[float] | None = None
    box_prob: list[float] | None = None
    special_node_id: str | None = None
    red_capsule_pool: str | None = None
    red_capsule_prob: float = 0.0


class RoguelikeGameZoneData(GameDataModel):
    """clz_Torappu_RoguelikeGameZoneData"""

    id: str | None = None
    name: str | None = None
    clock_performance: str | None = None
    display_time: str | None = None
    description: str | None = None
    buff_description: str | None = None
    ending_description: str | None = None
    background_id: str | None = None
    zone_icon_id: str | None = None
    is_hidden_zone: bool = False
    bgm_signal: str | None = None
    bgm_signal_with_low_san: str | None = None
    transition_effect_id: str | None = None


class RoguelikeZoneVariationData(GameDataModel):
    """clz_Torappu_RoguelikeZoneVariationData"""

    pass


class RoguelikeGameTrapData(GameDataModel):
    """clz_Torappu_RoguelikeGameTrapData"""

    item_id: str | None = None
    trap_id: str | None = None
    trap_desc: str | None = None


class RoguelikeGameRecruitTicketData(GameDataModel):
    """clz_Torappu_RoguelikeGameRecruitTicketData"""

    id: str | None = None
    profession: str = "NONE"
    rarity: str = "NONE"
    profession_list: list[str] | None = None
    rarity_list: list[str] | None = None
    extra_elite_num: int = 0
    extra_free_rarity: list[str] | None = None
    extra_char_ids: list[str] | None = None


class RoguelikeGameUpgradeTicketData(GameDataModel):
    """clz_Torappu_RoguelikeGameUpgradeTicketData"""

    id: str | None = None
    profession: str = "NONE"
    rarity: str = "NONE"
    profession_list: list[str] | None = None
    rarity_list: list[str] | None = None


class RoguelikeGameCustomTicketData(GameDataModel):
    """clz_Torappu_RoguelikeGameCustomTicketData"""

    id: str | None = None
    sub_type: str = "NONE"
    discard_text: str | None = None


class RoguelikeGameStashableTicketData(GameDataModel):
    """clz_Torappu_RoguelikeGameStashableTicketData"""

    ticket_id: str | None = None
    stashed_ticket_id: str | None = None


class BlackboardDataPair(GameDataModel):
    """clz_Torappu_Blackboard_DataPair"""

    key: str | None = None
    value: float = 0.0
    value_str: str | None = None


class RoguelikeBuff(GameDataModel):
    """clz_Torappu_RoguelikeBuff"""

    key: str | None = None
    blackboard: list[BlackboardDataPair] | None = None


class RoguelikeGameRelicData(GameDataModel):
    """clz_Torappu_RoguelikeGameRelicData"""

    id: str | None = None
    buffs: list[RoguelikeBuff] | None = None


class RoguelikeGameRelicCheckParam(GameDataModel):
    """clz_Torappu_RoguelikeGameRelicCheckParam"""

    value_profession_mask: str = "NONE"
    value_strs: list[str] | None = None
    value_int: int = 0


class RoguelikeGameRelicParamData(GameDataModel):
    """clz_Torappu_RoguelikeGameRelicParamData"""

    id: str | None = None
    check_char_box_types: list[str] | None = None
    check_char_box_params: list[RoguelikeGameRelicCheckParam] | None = None


class RoguelikeGameRecruitGrpData(GameDataModel):
    """clz_Torappu_RoguelikeGameRecruitGrpData"""

    id: str | None = None
    icon_id: str | None = None
    name: str | None = None
    desc: str | None = None
    unlock_desc: str | None = None


class RoguelikeChoiceDisplayData(GameDataModel):
    """clz_Torappu_RoguelikeChoiceDisplayData"""

    type: str = "NONE"
    cost_hint_type: str = "NONE"
    effect_hint_type: str = "NONE"
    func_icon_id: str | None = None
    item_id: str | None = None
    difficulty_upgrade_relic_group_id: str | None = None
    task_id: str | None = None
    inst_id: str | None = None


class RoguelikeGameChoiceData(GameDataModel):
    """clz_Torappu_RoguelikeGameChoiceData"""

    id: str | None = None
    title: str | None = None
    description: str | None = None
    locked_cover_desc: str | None = None
    type: str = "NONE"
    left_deco_type: str = "NONE"
    next_scene_id: str | None = None
    icon: str | None = None
    display_data: RoguelikeChoiceDisplayData | None = None
    force_show_when_only_leave: bool = False
    is_hidden_choice: bool = False
    sort_id: int = 0


class RoguelikeGameChoiceSceneData(GameDataModel):
    """clz_Torappu_RoguelikeGameChoiceSceneData"""

    id: str | None = None
    title: str | None = None
    description: str | None = None
    background: str | None = None
    title_icon: str | None = None
    sub_type_id: int = 0
    use_hidden_music: bool = False


class RoguelikeGameNodeTypeData(GameDataModel):
    """clz_Torappu_RoguelikeGameNodeTypeData"""

    name: str | None = None
    sub_name: str | None = None
    description: str | None = None


class RoguelikeGameNodeSubTypeData(GameDataModel):
    """clz_Torappu_RoguelikeGameNodeSubTypeData"""

    event_type: str = "NONE"
    sub_type_id: int = 0
    icon_id: str | None = None
    name: str | None = None
    description: str | None = None


class RoguelikeGameVariationData(GameDataModel):
    """clz_Torappu_RoguelikeGameVariationData"""

    id: str | None = None
    type: str = "NONE"
    outer_name: str | None = None
    inner_name: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    icon_id: str | None = None
    sound: str | None = None


class RoguelikeGameFusionData(GameDataModel):
    """clz_Torappu_RoguelikeGameFusionData"""

    id: str | None = None
    type: str = "NONE"
    name: str | None = None
    function_desc: str | None = None
    desc: str | None = None


class RoguelikeGameCharBuffData(GameDataModel):
    """clz_Torappu_RoguelikeGameCharBuffData"""

    id: str | None = None
    buff_type: str = "NONE"
    icon_id: str | None = None
    related_item_id: str | None = None
    outer_name: str | None = None
    inner_name: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    buffs: list[RoguelikeBuff] | None = None


class RoguelikeGameSquadBuffData(GameDataModel):
    """clz_Torappu_RoguelikeGameSquadBuffData"""

    id: str | None = None
    icon_id: str | None = None
    outer_name: str | None = None
    inner_name: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    buffs: list[RoguelikeBuff] | None = None


class RoguelikeTaskData(GameDataModel):
    """clz_Torappu_RoguelikeTaskData"""

    task_id: str | None = None
    task_name: str | None = None
    task_desc: str | None = None
    reward_scene_id: str | None = None
    task_rarity: str = "NORMAL"


class RoguelikeGameConst(GameDataModel):
    """clz_Torappu_RoguelikeGameConst"""

    init_scene_name: str | None = None
    fail_scene_name: str | None = None
    hp_item_id: str | None = None
    gold_item_id: str | None = None
    population_item_id: str | None = None
    squad_capacity_item_id: str | None = None
    exp_item_id: str | None = None
    initial_band_show_grade_flag: bool = False
    bank_max_gold: int = 0
    bank_cost_id: str | None = None
    bank_draw_count: int = 0
    bank_draw_limit: int = 0
    bank_reward_count_type: str = "HIGHEST_RECORD"
    sp_zone_shop_bgm_signal: str | None = None
    mimic_enemy_ids: list[str] | None = None
    boss_ids: list[str] | None = None
    gold_chest_trap_id: str | None = None
    norm_box_trap_id: str | None = None
    rare_box_trap_id: str | None = None
    bad_box_trap_id: str | None = None
    tool_box_trap_id: str | None = None
    max_hp_item_id: str | None = None
    shield_item_id: str | None = None
    key_item_id: str | None = None
    divination_kit_item_id: str | None = None
    chest_key_cnt: int = 0
    chest_key_item_id: str | None = None
    key_color_id: str | None = None
    once_node_type_list: list[str] | None = None
    vert_node_cost_dialog_use_item_icon_type: bool = False
    gp_score_ratio: int = 0
    overflow_usage_squad_buff: str | None = None
    special_trap_id: str | None = None
    trap_reward_relic_id: str | None = None
    unlock_route_item_id: str | None = None
    unlock_route_item_count: int = 0
    hide_battle_node_name: str | None = None
    hide_battle_node_description: str | None = None
    hide_non_battle_node_name: str | None = None
    hide_non_battle_node_description: str | None = None
    char_select_expedition_conflict_toast: str | None = None
    char_select_no_upgrade_conflict_toast: str | None = None
    item_drop_tag_dict: dict[str, str] | None = None
    shop_refresh_cost_id: str | None = None
    expedition_leave_toast_format: str | None = None
    expedition_return_desc_cure_upgrade: str | None = None
    expedition_return_desc_upgrade: str | None = None
    expedition_return_desc_cure: str | None = None
    expedition_return_desc: str | None = None
    expedition_select_desc_format: str | None = None
    expedition_return_desc_item: str | None = None
    exped_ending_relic: str | None = None
    exped_ending_relic_desc: str | None = None
    expedition_return_reward_black_list: list[str] | None = None
    travel_leave_toast_format: str | None = None
    char_select_travel_conflict_toast: str | None = None
    travel_return_desc_upgrade: str | None = None
    travel_return_desc: str | None = None
    travel_return_desc_item: str | None = None
    trader_return_title: str | None = None
    trader_return_desc: str | None = None
    candle_return_desc_candle_upgrade: str | None = None
    candle_return_desc_candle: str | None = None
    char_select_candle_conflict_toast: str | None = None
    char_select_guided_conflict_toast: str | None = None
    char_select_non_guided_conflict_toast: str | None = None
    gain_buff_diff_grade: int = 0
    ds_predict_tips: str | None = None
    ds_buff_active_tips: str | None = None
    totem_desc: str | None = None
    copper_gild_desc: str | None = None
    relic_desc: str | None = None
    buff_desc: str | None = None
    refresh_node_item_id: str | None = None
    storing_recruit_desc: str | None = None
    storing_recruit_succeed_toast: str | None = None
    special_recruit_reduction_desc: str | None = None
    special_recruit_func_desc: str | None = None
    special_recruit_detail_desc: str | None = None
    portal_zones: list[str] | None = None
    treasure_buffs: list[str] | None = None
    diff_display_zone_id: str | None = None
    explore_exp_on_kill: str | None = None
    fusion_name: str | None = None
    fusion_notify_toast: str | None = None
    have_custom_zone: bool = False
    got_char_candle_buff_toast: str | None = None
    got_chars_candle_buff_toast: str | None = None
    stashed_recruit_node_description: str | None = None
    stashed_recruit_empty_node_description: str | None = None
    recruit_stash_max_num: int = 0
    recruit_stash_min_num: int = 0
    has_topic_char_select_menu_button: bool = False


class RoguelikeGameShopDialogGroupData(GameDataModel):
    """clz_Torappu_RoguelikeGameShopDialogGroupData"""

    content: list[str] | None = None


class RoguelikeGameShopDialogTypeData(GameDataModel):
    """clz_Torappu_RoguelikeGameShopDialogTypeData"""

    groups: dict[str, RoguelikeGameShopDialogGroupData] | None = None


class RoguelikeGameShopDialogData(GameDataModel):
    """clz_Torappu_RoguelikeGameShopDialogData"""

    types: dict[str, RoguelikeGameShopDialogTypeData] | None = None


class RoguelikeTopicCapsule(GameDataModel):
    """clz_Torappu_RoguelikeTopicCapsule"""

    item_id: str | None = None
    mask_type: str = "NONE"
    inner_color: str | None = None


class RoguelikeGameEndingDataLevelIcon(GameDataModel):
    """clz_Torappu_RoguelikeGameEndingData_LevelIcon"""

    level: int = 0
    icon_id: str | None = None


class RoguelikeGameEndingData(GameDataModel):
    """clz_Torappu_RoguelikeGameEndingData"""

    id: str | None = None
    family_id: int = 0
    name: str | None = None
    desc: str | None = None
    bg_id: str | None = None
    icons: list[RoguelikeGameEndingDataLevelIcon] | None = None
    priority: int = 0
    change_ending_desc: str | None = None
    boss_icon_id: str | None = None


class RoguelikeGameFailEndingData(GameDataModel):
    """clz_Torappu_RoguelikeGameFailEndingData"""

    id: str | None = None
    name: str | None = None
    desc: str | None = None
    icon_id: str | None = None
    priority: int = 0


class RoguelikeBattleSummeryDescriptionData(GameDataModel):
    """clz_Torappu_RoguelikeBattleSummeryDescriptionData"""

    random_description_list: list[str] | None = None


class TipData(GameDataModel):
    """clz_Torappu_TipData"""

    tip: str | None = None
    weight: float = 0.0
    category: str = "NONE"


class RoguelikeGameItemData(GameDataModel):
    """clz_Torappu_RoguelikeGameItemData"""

    id: str | None = None
    name: str | None = None
    description: str | None = None
    usage: str | None = None
    obtain_approach: str | None = None
    icon_id: str | None = None
    item_icon_group_id: str | None = None
    type: str = "NONE"
    sub_type: str = "NONE"
    rarity: str = "NONE"
    sort_id: int = 0
    can_sacrifice: bool = False
    tiny_icon_color: str | None = None
    unlock_cond_desc: str | None = None
    short_usage: str | None = None


class RoguelikeBandRefData(GameDataModel):
    """clz_Torappu_RoguelikeBandRefData"""

    item_id: str | None = None
    band_level: int = 0
    normal_band_id: str | None = None


class RoguelikeEndingDetailText(GameDataModel):
    """clz_Torappu_RoguelikeEndingDetailText"""

    text_id: str | None = None
    text: str | None = None
    event_type: str = "NONE"
    sp_zone_evt_type: str | None = None
    show_type: str = "SHOW_CHOICE"
    choice_scene_id: str | None = None
    param_list: list[str] | None = None
    other_para_1: str | None = None


class RoguelikeEndingRelicDetailText(GameDataModel):
    """clz_Torappu_RoguelikeEndingRelicDetailText"""

    relic_id: str | None = None
    summary_event_text: str | None = None


class RoguelikeGameTreasureData(GameDataModel):
    """clz_Torappu_RoguelikeGameTreasureData"""

    treasure_id: str | None = None
    group_id: str | None = None
    sub_index: int = 0
    name: str | None = None
    usage: str | None = None


class RoguelikeDifficultyUpgradeRelicData(GameDataModel):
    """clz_Torappu_RoguelikeDifficultyUpgradeRelicData"""

    relic_id: str | None = None
    equivalent_grade: int = 0


class RoguelikeDifficultyUpgradeRelicGroupData(GameDataModel):
    """clz_Torappu_RoguelikeDifficultyUpgradeRelicGroupData"""

    relic_data: list[RoguelikeDifficultyUpgradeRelicData] | None = None


class RoguelikePredefinedStyleData(GameDataModel):
    """clz_Torappu_RoguelikePredefinedStyleData"""

    style_id: str | None = None
    style_config: int = 0


class RoguelikePredefinedExpStyleConfigData(GameDataModel):
    """clz_Torappu_RoguelikePredefinedExpStyleConfigData"""

    param_dict: dict[str, str] | None = None


class RoguelikePredefinedConstStyleData(GameDataModel):
    """clz_Torappu_RoguelikePredefinedConstStyleData"""

    exp_style_config: RoguelikePredefinedExpStyleConfigData | None = None


class RoguelikeGameExploreToolData(GameDataModel):
    """clz_Torappu_RoguelikeGameExploreToolData"""

    item_id: str | None = None
    trap_id: str | None = None
    trap_desc: str | None = None


class RoguelikeRollNodeGroupData(GameDataModel):
    """clz_Torappu_RoguelikeRollNodeGroupData"""

    node_type: str = "NONE"


class RoguelikeRollNodeData(GameDataModel):
    """clz_Torappu_RoguelikeRollNodeData"""

    zone_id: str | None = None
    groups: dict[str, RoguelikeRollNodeGroupData] | None = None


class RoguelikeRelicTipsData(GameDataModel):
    """clz_Torappu_RoguelikeRelicTipsData"""

    item_id: str | None = None
    toast_text: str | None = None


class RoguelikeLegacyItemData(GameDataModel):
    """clz_Torappu_RoguelikeLegacyItemData"""

    legacy_id: str | None = None
    hide_legacy_item: bool = False
    legacy_group_id: str | None = None


class RoguelikeActivityBasicData(GameDataModel):
    """clz_Torappu_RoguelikeActivityBasicData"""

    id: str | None = None
    type: str = "NONE"
    start_time: int = 0
    end_time: int = 0
    is_present_seed_mode: bool = False
    is_unlock_badge: bool = False
    valid_mode: str = "NONE"


class RoguelikeActivitySeedModeDataRoguelikeActivityOfficialSeedData(GameDataModel):
    """clz_Torappu_RoguelikeActivitySeedModeData_RoguelikeActivityOfficialSeedData"""

    seed: str | None = None
    sort_id: int = 0
    desc: str | None = None


class RoguelikeActivitySeedModeDataRoguelikeActivitySeedModeConstData(GameDataModel):
    """clz_Torappu_RoguelikeActivitySeedModeData_RoguelikeActivitySeedModeConstData"""

    seed_mode_intro: str | None = None
    empty_text_hint: str | None = None
    error_text_hint: str | None = None
    legitimate_text_hint: str | None = None
    seed_mode_confirm_replacement: str | None = None
    difficulty_level_text_hint: str | None = None
    locked_difficulty_level_text_hint: str | None = None
    set_difficulty_level_text_hint: str | None = None
    not_enabled_text_hint: str | None = None
    enabled_text_hint: str | None = None
    use_succeeded_text_hint: str | None = None
    official_use_succeeded_text_hint: str | None = None
    seed_mode_locked_text_hint: str | None = None


class RoguelikeActivitySeedModeData(GameDataModel):
    """clz_Torappu_RoguelikeActivitySeedModeData"""

    official_seed_data_list: (
        list[RoguelikeActivitySeedModeDataRoguelikeActivityOfficialSeedData] | None
    ) = None
    const_data: (
        RoguelikeActivitySeedModeDataRoguelikeActivitySeedModeConstData | None
    ) = None


class RoguelikeActivityTable(GameDataModel):
    """clz_Torappu_RoguelikeActivityTable"""

    seed_mode: dict[str, RoguelikeActivitySeedModeData] | None = Field(
        default=None, alias="SEED_MODE"
    )


class RoguelikeActivityData(GameDataModel):
    """clz_Torappu_RoguelikeActivityData"""

    basic_datas: dict[str, RoguelikeActivityBasicData] | None = None
    activity_table: RoguelikeActivityTable | None = None


class RoguelikeTopicDetail(GameDataModel):
    """clz_Torappu_RoguelikeTopicDetail"""

    updates: list[RoguelikeTopicUpdate] | None = None
    enrolls: dict[str, RoguelikeTopicEnroll] | None = None
    milestones: list[RoguelikeTopicBP] | None = None
    milestone_updates: list[RoguelikeTopicMilestoneUpdateData] | None = None
    grand_prizes: list[RoguelikeTopicBPGrandPrize] | None = None
    month_mission: list[RoguelikeTopicMonthMission] | None = None
    month_squad: dict[str, RoguelikeTopicMonthSquad] | None = None
    challenges: dict[str, RoguelikeTopicChallenge] | None = None
    difficulties: list[RoguelikeTopicDifficulty] | None = None
    bank_rewards: list[RoguelikeTopicBankReward] | None = None
    archive_comp: RoguelikeArchiveComponentData | None = None
    archive_unlock_cond: RoguelikeArchiveUnlockCondData | None = None
    detail_const: RoguelikeTopicDetailConst | None = None
    init: list[RoguelikeGameInitData] | None = None
    stages: dict[str, RoguelikeGameStageData] | None = None
    zones: dict[str, RoguelikeGameZoneData] | None = None
    variation: dict[str, RoguelikeZoneVariationData] | None = None
    traps: dict[str, RoguelikeGameTrapData] | None = None
    recruit_tickets: dict[str, RoguelikeGameRecruitTicketData] | None = None
    upgrade_tickets: dict[str, RoguelikeGameUpgradeTicketData] | None = None
    custom_tickets: dict[str, RoguelikeGameCustomTicketData] | None = None
    stashable_tickets: dict[str, RoguelikeGameStashableTicketData] | None = None
    relics: dict[str, RoguelikeGameRelicData] | None = None
    relic_params: dict[str, RoguelikeGameRelicParamData] | None = None
    recruit_grps: dict[str, RoguelikeGameRecruitGrpData] | None = None
    choices: dict[str, RoguelikeGameChoiceData] | None = None
    choice_scenes: dict[str, RoguelikeGameChoiceSceneData] | None = None
    node_type_data: dict[str, RoguelikeGameNodeTypeData] | None = None
    sub_type_data: list[RoguelikeGameNodeSubTypeData] | None = None
    variation_data: dict[str, RoguelikeGameVariationData] | None = None
    fusion_data: dict[str, RoguelikeGameFusionData] | None = None
    char_buff_data: dict[str, RoguelikeGameCharBuffData] | None = None
    squad_buff_data: dict[str, RoguelikeGameSquadBuffData] | None = None
    task_data: dict[str, RoguelikeTaskData] | None = None
    game_const: RoguelikeGameConst | None = None
    shop_dialog_data: RoguelikeGameShopDialogData | None = None
    capsule_dict: dict[str, RoguelikeTopicCapsule] | None = None
    endings: dict[str, RoguelikeGameEndingData] | None = None
    fail_endings: dict[str, RoguelikeGameFailEndingData] | None = None
    battle_summery_descriptions: (
        dict[str, RoguelikeBattleSummeryDescriptionData] | None
    ) = None
    battle_loading_tips: list[TipData] | None = None
    items: dict[str, RoguelikeGameItemData] | None = None
    band_ref: dict[str, RoguelikeBandRefData] | None = None
    ending_detail_list: list[RoguelikeEndingDetailText] | None = None
    ending_relic_detail_list: list[RoguelikeEndingRelicDetailText] | None = None
    treasures: dict[str, list[RoguelikeGameTreasureData]] | None = None
    difficulty_upgrade_relic_groups: (
        dict[str, RoguelikeDifficultyUpgradeRelicGroupData] | None
    ) = None
    styles: dict[str, RoguelikePredefinedStyleData] | None = None
    style_config: RoguelikePredefinedConstStyleData | None = None
    explore_tools: dict[str, RoguelikeGameExploreToolData] | None = None
    roll_node_data: dict[str, RoguelikeRollNodeData] | None = None
    relic_tips_data: dict[str, RoguelikeRelicTipsData] | None = None
    legacy_items: dict[str, RoguelikeLegacyItemData] | None = None
    activity: RoguelikeActivityData | None = None


class RoguelikeSanRangeData(GameDataModel):
    """clz_Torappu_RoguelikeSanRangeData"""

    san_max: int = 0
    dice_group_id: str | None = None
    description: str | None = None
    san_dungeon_effect: str = "SAN_EFFECT_0"
    san_effect_rank: str = "SAN_EFFECT_0"
    san_ending_desc: str | None = None


class RoguelikeSanCheckConsts(GameDataModel):
    """clz_Torappu_RoguelikeSanCheckConsts"""

    san_decrease_toast: str | None = None


class RoguelikeSanCheckModuleData(GameDataModel):
    """clz_Torappu_RoguelikeSanCheckModuleData"""

    san_ranges: list[RoguelikeSanRangeData] | None = None
    module_consts: RoguelikeSanCheckConsts | None = None


class RoguelikeDiceData(GameDataModel):
    """clz_Torappu_RoguelikeDiceData"""

    dice_id: str | None = None
    description: str | None = None
    is_upgrade_dice: int = 0
    upgrade_dice_id: str | None = None
    dice_face_count: int = 0
    battle_dice_id: str | None = None


class RoguelikeDiceRuleData(GameDataModel):
    """clz_Torappu_RoguelikeDiceRuleData"""

    dice_point_max: int = 0
    dice_result_class: str = "VERYBAD"
    dice_group_id: str | None = None
    dice_event_id: str | None = None
    result_desc: str | None = None
    show_type: str = "RAW_TEXT"
    can_reroll: bool = False
    dice_ending_scene: str | None = None
    dice_ending_desc: str | None = None
    sound: str | None = None


class RoguelikeDiceRuleGroupData(GameDataModel):
    """clz_Torappu_RoguelikeDiceRuleGroupData"""

    rule_group_id: str | None = None
    min_good_num: int = 0


class RoguelikeDicePredefineData(GameDataModel):
    """clz_Torappu_RoguelikeDicePredefineData"""

    mode_id: str = "NONE"
    mode_grade: int = 0
    predefined_id: str | None = None
    initial_dice_count: int = 0


class RoguelikeDiceModuleData(GameDataModel):
    """clz_Torappu_RoguelikeDiceModuleData"""

    dice: dict[str, RoguelikeDiceData] | None = None
    dice_events: dict[str, RoguelikeDiceRuleData] | None = None
    dice_choices: dict[str, str] | None = None
    dice_rule_groups: dict[str, RoguelikeDiceRuleGroupData] | None = None
    dice_predefines: list[RoguelikeDicePredefineData] | None = None


class RoguelikeChaosData(GameDataModel):
    """clz_Torappu_RoguelikeChaosData"""

    chaos_id: str | None = None
    level: int = 0
    next_chaos_id: str | None = None
    prev_chaos_id: str | None = None
    icon_id: str | None = None
    name: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    sound: str | None = None
    sort_id: int = 0


class RoguelikeChaosRangeData(GameDataModel):
    """clz_Torappu_RoguelikeChaosRangeData"""

    chaos_max: int = 0
    chaos_dungeon_effect: str = "CHAOS_EFFECT_0"


class RoguelikeChaosPredefineLevelInfo(GameDataModel):
    """clz_Torappu_RoguelikeChaosPredefineLevelInfo"""

    chaos_level_begin_num: int = 0
    chaos_level_end_num: int = 0


class RoguelikeChaosModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeChaosModuleConsts"""

    max_chaos_level: int = 0
    max_chaos_slot: int = 0
    chaos_not_max_description: str | None = None
    chaos_max_description: str | None = None
    chaos_predict_description: str | None = None


class RoguelikeChaosModuleData(GameDataModel):
    """clz_Torappu_RoguelikeChaosModuleData"""

    chaos_datas: dict[str, RoguelikeChaosData] | None = None
    chaos_ranges: list[RoguelikeChaosRangeData] | None = None
    level_info_dict: dict[str, dict[int, RoguelikeChaosPredefineLevelInfo]] | None = (
        None
    )
    module_consts: RoguelikeChaosModuleConsts | None = None


class RoguelikeTotemLinkedNodeTypeData(GameDataModel):
    """clz_Torappu_RoguelikeTotemLinkedNodeTypeData"""

    effective_node_types: list[str] | None = None
    blur_node_types: list[str] | None = None


class RoguelikeTotemBuffData(GameDataModel):
    """clz_Torappu_RoguelikeTotemBuffData"""

    totem_id: str | None = None
    color: str = "NONE"
    pos: str = "LOCATION"
    rhythm: str | None = None
    normal_desc: str | None = None
    synergy_desc: str | None = None
    archive_desc: str | None = None
    combine_group_name: str | None = None
    bg_icon_id: str | None = None
    is_manual: bool = False
    linked_node_type_data: RoguelikeTotemLinkedNodeTypeData | None = None
    distance_min: int = 0
    distance_max: int = 0
    vert_passable: bool = False
    expand_length: int = 0
    only_for_vert: bool = False
    portal_linked_node_type_data: RoguelikeTotemLinkedNodeTypeData | None = None


class RoguelikeTotemSubBuffData(GameDataModel):
    """clz_Torappu_RoguelikeTotemSubBuffData"""

    sub_buff_id: str | None = None
    name: str | None = None
    desc: str | None = None
    combined_desc: str | None = None
    info: str | None = None


class RoguelikeTotemModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeTotemModuleConsts"""

    totem_predict_description: str | None = None
    color_combine_desc: dict[str, str] | None = None
    boss_combine_desc: str | None = None
    battle_no_predict_description: str | None = None
    shop_no_goods_description: str | None = None


class RoguelikeTotemBuffModuleData(GameDataModel):
    """clz_Torappu_RoguelikeTotemBuffModuleData"""

    totem_buff_datas: dict[str, RoguelikeTotemBuffData] | None = None
    sub_buffs: dict[str, RoguelikeTotemSubBuffData] | None = None
    module_consts: RoguelikeTotemModuleConsts | None = None


class RoguelikeVisionData(GameDataModel):
    """clz_Torappu_RoguelikeVisionData"""

    sight_num: int = 0
    level: int = 0
    can_foresee: bool = False
    divided_dis: int = 0
    status: str | None = None
    clr: str | None = None
    desc_1: str | None = None
    desc_2: str | None = None
    icon: str | None = None


class RoguelikeVisionModuleDataVisionChoiceConfig(GameDataModel):
    """clz_Torappu_RoguelikeVisionModuleData_VisionChoiceConfig"""

    value: int = 0
    type: str = "LOWER"


class RoguelikeVisionModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeVisionModuleConsts"""

    max_vision: int = 0
    totem_bottom_description: str | None = None
    chest_bottom_description: str | None = None
    goods_bottom_description: str | None = None


class RoguelikeVisionModuleData(GameDataModel):
    """clz_Torappu_RoguelikeVisionModuleData"""

    vision_datas: dict[int, RoguelikeVisionData] | None = None
    vision_choices: dict[str, RoguelikeVisionModuleDataVisionChoiceConfig] | None = None
    module_consts: RoguelikeVisionModuleConsts | None = None


class RoguelikeFragmentData(GameDataModel):
    """clz_Torappu_RoguelikeFragmentData"""

    id: str | None = None
    type: str = "NONE"
    value: int = 0
    weight: int = 0


class RoguelikeFragmentTypeData(GameDataModel):
    """clz_Torappu_RoguelikeFragmentTypeData"""

    type: str = "NONE"
    type_name: str | None = None
    type_desc: str | None = None
    type_icon_id: str | None = None


class RoguelikeFragmentModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeFragmentModuleConsts"""

    weight_status_safe_desc: str | None = None
    weight_status_limit_desc: str | None = None
    weight_status_overweight_desc: str | None = None
    char_weight_slot: int = 0
    limit_weight_threshold_value: int = 0
    over_weight_threshold_value: int = 0
    max_alchemy_field: int = 0
    max_alchemy_count: int = 0
    fragment_bag_weight_limit_tips: str | None = None
    fragment_bag_weight_over_weight_tips: str | None = None
    weight_upgrade_toast_format: str | None = None


class RoguelikeFragmentBuffData(GameDataModel):
    """clz_Torappu_RoguelikeFragmentBuffData"""

    item_id: str | None = None
    mask_type: str = "NONE"
    desc: str | None = None


class RoguelikeAlchemyData(GameDataModel):
    """clz_Torappu_RoguelikeAlchemyData"""

    fragment_type_list: list[str] | None = None
    fragment_square_sum: int = 0
    pool_rarity: str = "NORMAL"
    relic_prop: float = 0.0
    shield_prop: float = 0.0
    population_prop: float = 0.0
    override_condition_band_ids: list[str] | None = None
    override_recipe_id: str | None = None


class RoguelikeAlchemyFormulationData(GameDataModel):
    """clz_Torappu_RoguelikeAlchemyFormulationData"""

    fragment_ids: list[str] | None = None
    reward_id: str | None = None
    reward_count: int = 0
    reward_item_type: str = "NONE"


class RoguelikeFragmentLevelRelatedData(GameDataModel):
    """clz_Torappu_RoguelikeFragmentLevelRelatedData"""

    weight_up: int = 0


class RoguelikeFragmentModuleData(GameDataModel):
    """clz_Torappu_RoguelikeFragmentModuleData"""

    fragment_data: dict[str, RoguelikeFragmentData] | None = None
    fragment_type_data: dict[str, RoguelikeFragmentTypeData] | None = None
    module_consts: RoguelikeFragmentModuleConsts | None = None
    fragment_buff_data: dict[str, RoguelikeFragmentBuffData] | None = None
    alchemy_data: dict[str, RoguelikeAlchemyData] | None = None
    alchemy_formula_data: dict[str, RoguelikeAlchemyFormulationData] | None = None
    fragment_level_data: dict[int, RoguelikeFragmentLevelRelatedData] | None = None


class RoguelikeDisasterData(GameDataModel):
    """clz_Torappu_RoguelikeDisasterData"""

    id: str | None = None
    icon_id: str | None = None
    toast_icon_id: str | None = None
    level: int = 0
    name: str | None = None
    level_name: str | None = None
    type: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    sound: str | None = None


class RoguelikeDisasterModuleData(GameDataModel):
    """clz_Torappu_RoguelikeDisasterModuleData"""

    disaster_data: dict[str, RoguelikeDisasterData] | None = None


class RoguelikePermNodeUpgradeItemData(GameDataModel):
    """clz_Torappu_RoguelikePermNodeUpgradeItemData"""

    upgrade_id: str | None = None
    node_type: str = "NONE"
    node_level: int = 0
    cost_item_id: str | None = None
    cost_item_count: int = 0
    desc: str | None = None
    node_name: str | None = None


class RoguelikeTempNodeUpgradeItemData(GameDataModel):
    """clz_Torappu_RoguelikeTempNodeUpgradeItemData"""

    upgrade_id: str | None = None
    node_type: str = "NONE"
    sort_id: int = 0
    cost_item_id: str | None = None
    cost_item_count: int = 0
    desc: str | None = None


class RoguelikeNodeUpgradeData(GameDataModel):
    """clz_Torappu_RoguelikeNodeUpgradeData"""

    node_type: str = "NONE"
    sort_id: int = 0
    perm_item_list: list[RoguelikePermNodeUpgradeItemData] | None = None
    temp_item_list: list[RoguelikeTempNodeUpgradeItemData] | None = None


class RoguelikeNodeUpgradeModuleData(GameDataModel):
    """clz_Torappu_RoguelikeNodeUpgradeModuleData"""

    node_upgrade_data_map: dict[str, RoguelikeNodeUpgradeData] | None = None


class RoguelikeCopperData(GameDataModel):
    """clz_Torappu_RoguelikeCopperData"""

    id: str | None = None
    group_id: str | None = None
    gild_type_id: str | None = None
    lucky_level: str = "NONE"
    buff_type: str = "NONE"
    layer_cnt_desc: str | None = None
    poem_list: list[str] | None = None
    always_show_count_down: bool = False
    buff_item_id_list: list[str] | None = None
    is_all_lucky_level: bool = False


class RoguelikeCopperDivineData(GameDataModel):
    """clz_Torappu_RoguelikeCopperDivineData"""

    event_id: str | None = None
    group_id: str | None = None
    show_desc: str | None = None
    divine_type: str = "NONE"
    result_type: str = "NONE"


class RoguelikeCopperGildTypeData(GameDataModel):
    """clz_Torappu_RoguelikeCopperGildTypeData"""

    gild_type_id: str | None = None
    gild_name: str | None = None
    gild_desc: str | None = None


class RoguelikeCopperModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeCopperModuleConsts"""

    copper_draw_max_num: int = 0
    copper_draw_min_num: int = 0
    copper_all_lucky_level_gild_id: str | None = None
    copper_draw_freeze_cost_item_id: str | None = None
    copper_draw_freeze_cost_count: list[int] | None = None


class RoguelikeCopperModuleData(GameDataModel):
    """clz_Torappu_RoguelikeCopperModuleData"""

    copper_data: dict[str, RoguelikeCopperData] | None = None
    copper_divine_data: dict[str, RoguelikeCopperDivineData] | None = None
    copper_gild_type_data: dict[str, RoguelikeCopperGildTypeData] | None = None
    change_copper_map: dict[str, str] | None = None
    module_consts: RoguelikeCopperModuleConsts | None = None


class RoguelikeWrathData(GameDataModel):
    """clz_Torappu_RoguelikeWrathData"""

    id: str | None = None
    group: str | None = None
    level: int = 0
    name: str | None = None
    level_name: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    is_pacified: bool = False


class RoguelikeWrathModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeWrathModuleConsts"""

    get_wrath_transition: str | None = None
    get_wrath_toast: str | None = None
    hidden_wrath_type: str | None = None
    pacified_wrath_level: int = 0


class RoguelikeWrathModuleData(GameDataModel):
    """clz_Torappu_RoguelikeWrathModuleData"""

    wrath_data: dict[str, RoguelikeWrathData] | None = None
    module_consts: RoguelikeWrathModuleConsts | None = None


class RoguelikeCandleModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeCandleModuleConsts"""

    candle_holder_buff_id: str | None = None


class RoguelikeCandleModuleData(GameDataModel):
    """clz_Torappu_RoguelikeCandleModuleData"""

    candle_ticket_id_list: list[str] | None = None
    module_consts: RoguelikeCandleModuleConsts | None = None
    candle_battle_stage_id_list: list[str] | None = None


class RoguelikeSkyNodeData(GameDataModel):
    """clz_Torappu_RoguelikeSkyNodeData"""

    evt_type: str = "NONE"
    name: str | None = None
    icon_id: str | None = None
    eff_id: str | None = None
    desc: str | None = None
    name_bkg_clr: str | None = None
    select_clr: str | None = None
    is_repeatedly: bool = False


class RoguelikeSkyNodeSubTypeData(GameDataModel):
    """clz_Torappu_RoguelikeSkyNodeSubTypeData"""

    evt_type: str = "NONE"
    sub_type_id: int = 0
    desc: str | None = None


class RoguelikeSkyModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeSkyModuleConsts"""

    sky_ap_item_id: str | None = None
    sky_max_columns: int = 0
    sky_sacrifice_choice_dynamic_key: str | None = None


class RoguelikeSkyModuleData(GameDataModel):
    """clz_Torappu_RoguelikeSkyModuleData"""

    node_data: dict[str, RoguelikeSkyNodeData] | None = None
    sub_type_data: list[RoguelikeSkyNodeSubTypeData] | None = None
    module_consts: RoguelikeSkyModuleConsts | None = None


class RoguelikeMainWeatherData(GameDataModel):
    """clz_Torappu_RoguelikeMainWeatherData"""

    id: str | None = None
    icon_id: str | None = None
    icon_big_id: str | None = None
    is_positive: bool = False
    level: int = 0
    name: str | None = None
    level_name: str | None = None
    type: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    sound: str | None = None


class RoguelikeSubWeatherData(GameDataModel):
    """clz_Torappu_RoguelikeSubWeatherData"""

    id: str | None = None
    icon_id: str | None = None
    is_positive: bool = False
    name: str | None = None
    type: str | None = None
    function_desc: str | None = None
    desc: str | None = None
    sound: str | None = None


class RoguelikeWeatherModuleData(GameDataModel):
    """clz_Torappu_RoguelikeWeatherModuleData"""

    main_weather_data: dict[str, RoguelikeMainWeatherData] | None = None
    sub_weather_data: dict[str, RoguelikeSubWeatherData] | None = None


class RoguelikeGridZoneMissionBannerData(GameDataModel):
    """clz_Torappu_RoguelikeGridZoneMissionBannerData"""

    zone_id: str | None = None
    banner_text: str | None = None
    banner_icon: str | None = None


class RoguelikeGridZoneFocusViewHintData(GameDataModel):
    """clz_Torappu_RoguelikeGridZoneFocusViewHintData"""

    zone_id: str | None = None
    hint_text: str | None = None


class RoguelikeBuoyItemData(GameDataModel):
    """clz_Torappu_RoguelikeBuoyItemData"""

    item_id: str | None = None
    is_visible: bool = False


class RoguelikeGridZoneModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeGridZoneModuleConsts"""

    savage_bubble: str | None = None
    secret_zone_disable_buff: str | None = None
    shadvr_trap_ids: list[str] | None = None
    shadvr_first_die_trap_ids: list[str] | None = None
    shadvr_alive_event_id: str | None = None
    shadvr_die_event_id: str | None = None
    shadvr_final_relic_id: str | None = None
    max_banner_difficulty: int = 0
    focus_view_boss_hint_stage_id: dict[str, bool] | None = None


class RoguelikeGridZoneModuleData(GameDataModel):
    """clz_Torappu_RoguelikeGridZoneModuleData"""

    zone_mission_banner_data: dict[str, RoguelikeGridZoneMissionBannerData] | None = (
        None
    )
    scrap_side_bar_step_zero_hint_banner_data: (
        dict[str, RoguelikeGridZoneFocusViewHintData] | None
    ) = None
    buoy_item_datas: dict[str, RoguelikeBuoyItemData] | None = None
    module_consts: RoguelikeGridZoneModuleConsts | None = None


class RoguelikeScrapTypeData(GameDataModel):
    """clz_Torappu_RoguelikeScrapTypeData"""

    type: str = "NONE"
    type_name: str | None = None
    type_desc: str | None = None
    type_icon_id: str | None = None


class RoguelikeScrapMoveData(GameDataModel):
    """clz_Torappu_RoguelikeScrapMoveData"""

    count: int = 0
    range: str | None = None
    range_type: str = "RANGE"
    node: list[str] | None = None
    step: int = 0
    is_random_move: bool = False
    node_change_target_type: str = "NONE"
    scrap_id: str | None = None
    scrap_desc: str | None = None
    sell_price: int = 0


class RoguelikeScrapGoodsData(GameDataModel):
    """clz_Torappu_RoguelikeScrapGoodsData"""

    scrap_id: str | None = None
    scrap_desc: str | None = None
    sell_price: int = 0


class RoguelikeScrapPassiveData(GameDataModel):
    """clz_Torappu_RoguelikeScrapPassiveData"""

    node: str = "NONE"
    buff_stack: int = 0
    scrap_id: str | None = None
    scrap_desc: str | None = None
    sell_price: int = 0


class GridPosition(GameDataModel):
    """clz_Torappu_GridPosition"""

    row: int = 0
    col: int = 0


class RangeData(GameDataModel):
    """clz_Torappu_RangeData"""

    id: str | None = None
    direction: str = "UP"
    grids: list[GridPosition] | None = None


class RoguelikeScrapModuleConsts(GameDataModel):
    """clz_Torappu_RoguelikeScrapModuleConsts"""

    identify_scrap_id: str | None = None


class RoguelikeScrapModuleData(GameDataModel):
    """clz_Torappu_RoguelikeScrapModuleData"""

    scrap_item_to_type: dict[str, str] | None = None
    scrap_type_data: dict[str, RoguelikeScrapTypeData] | None = None
    move_scrap_data: dict[str, RoguelikeScrapMoveData] | None = None
    goods_scrap_data: dict[str, RoguelikeScrapGoodsData] | None = None
    passive_scrap_data: dict[str, RoguelikeScrapPassiveData] | None = None
    move_scrap_range_data: dict[str, RangeData] | None = None
    module_consts: RoguelikeScrapModuleConsts | None = None


class RoguelikeModule(GameDataModel):
    """clz_Torappu_RoguelikeModule"""

    module_types: list[str] | None = None
    san_check: RoguelikeSanCheckModuleData | None = None
    dice: RoguelikeDiceModuleData | None = None
    chaos: RoguelikeChaosModuleData | None = None
    totem_buff: RoguelikeTotemBuffModuleData | None = None
    vision: RoguelikeVisionModuleData | None = None
    fragment: RoguelikeFragmentModuleData | None = None
    disaster: RoguelikeDisasterModuleData | None = None
    node_upgrade: RoguelikeNodeUpgradeModuleData | None = None
    copper: RoguelikeCopperModuleData | None = None
    wrath: RoguelikeWrathModuleData | None = None
    candle: RoguelikeCandleModuleData | None = None
    sky: RoguelikeSkyModuleData | None = None
    weather: RoguelikeWeatherModuleData | None = None
    grid_zone: RoguelikeGridZoneModuleData | None = None
    scrap: RoguelikeScrapModuleData | None = None


class RoguelikeTopicDisplayItem(GameDataModel):
    """clz_Torappu_RoguelikeTopicDisplayItem"""

    display_type: str | None = None
    display_num: int = 0
    display_form: str = "ABSOLUTE_VAL"
    token_desc: str | None = None
    sort_id: int = 0


class RoguelikeTopicDev(GameDataModel):
    """clz_Torappu_RoguelikeTopicDev"""

    buff_id: str | None = None
    sort_id: int = 0
    node_type: str = "BRANCH"
    next_node_id: list[str] | None = None
    front_node_id: list[str] | None = None
    token_cost: int = 0
    buff_name: str | None = None
    buff_icon_id: str | None = None
    buff_type_name: str | None = None
    buff_display_info: list[RoguelikeTopicDisplayItem] | None = None


class RoguelikeTopicDevToken(GameDataModel):
    """clz_Torappu_RoguelikeTopicDevToken"""

    sort_id: int = 0
    display_form: str = "ABSOLUTE_VAL"
    token_desc: str | None = None


class RL01EndingText(GameDataModel):
    """clz_Torappu_RL01EndingText"""

    summary_variation: str | None = None
    summary_fusion: str | None = None
    summary_capsule: str | None = None
    summary_actor: str | None = None
    summary_top: str | None = None
    summary_zone: str | None = None
    summary_ending: str | None = None
    summary_difficulty_zone: str | None = None
    summary_difficulty_ending: str | None = None
    summary_mode: str | None = None
    summary_group: str | None = None
    summary_support: str | None = None
    summary_normal_recruit: str | None = None
    summary_direct_recruit: str | None = None
    summary_friend_recruit: str | None = None
    summary_free_recruit: str | None = None
    summary_month_recruit: str | None = None
    summary_upgrade: str | None = None
    summary_complete_ending: str | None = None
    summary_each_zone: str | None = None
    summary_meet_sp_zone: str | None = None
    summary_perfect_battle: str | None = None
    summary_meet_battle: str | None = None
    summary_meet_event: str | None = None
    summary_meet_shop: str | None = None
    summary_meet_treasure: str | None = None
    summary_meet_secretpath: str | None = None
    summary_exchange_relic: str | None = None
    summary_meet_trade: str | None = None
    summary_buy: str | None = None
    summary_buy_with_price_id: str | None = None
    summary_invest: str | None = None
    summary_get: str | None = None
    summary_relic: str | None = None
    summary_safe_house: str | None = None
    summary_fail_end: str | None = None
    summary_stock_recruit_ticket: str | None = None
    summary_duel_win: str | None = None
    summary_duel_tie: str | None = None
    summary_duel_lose: str | None = None
    summary_expedition_go: str | None = None
    summary_expedition_back: str | None = None


class RL01DifficultyExt(GameDataModel):
    """clz_Torappu_RL01DifficultyExt"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    buff_desc: list[str] | None = None


class RL01CustomizeData(GameDataModel):
    """clz_Torappu_RL01CustomizeData"""

    developments: dict[str, RoguelikeTopicDev] | None = None
    development_tokens: dict[str, RoguelikeTopicDevToken] | None = None
    ending_text: RL01EndingText | None = None
    difficulties: list[RL01DifficultyExt] | None = None


class RL02Development(GameDataModel):
    """clz_Torappu_RL02Development"""

    buff_id: str | None = None
    node_type: str = "NONE"
    front_node_id: list[str] | None = None
    next_node_id: list[str] | None = None
    position_p: int = 0
    position_r: int = 0
    token_cost: int = 0
    buff_name: str | None = None
    buff_icon_id: str | None = None
    effect_type: str = "BUFF"
    raw_desc: str | None = None
    buff_display_info: list[RoguelikeTopicDisplayItem] | None = None
    enroll_id: str | None = None


class RL02DevRawTextBuffGroup(GameDataModel):
    """clz_Torappu_RL02DevRawTextBuffGroup"""

    node_id_list: list[str] | None = None
    use_level_mark: bool = False
    group_icon_id: str | None = None
    use_up_break: bool = False
    sort_id: int = 0


class RL02DevelopmentLine(GameDataModel):
    """clz_Torappu_RL02DevelopmentLine"""

    from_node: str | None = None
    to_node: str | None = None
    from_node_p: int = 0
    from_node_r: int = 0
    to_node_p: int = 0
    to_node_r: int = 0
    enroll_id: str | None = None


class RL02EndingText(GameDataModel):
    """clz_Torappu_RL02EndingText"""

    summary_mutation: str | None = None
    summary_dice: str | None = None
    summary_dice_result_good: str | None = None
    summary_dice_result_normal: str | None = None
    summary_dice_result_bad: str | None = None
    summary_dice_result_desc: str | None = None
    summary_commu_desc: str | None = None
    summary_hidden_desc: str | None = None
    summary_knight_desc: str | None = None
    summary_gold_desc: str | None = None
    summary_practice_desc: str | None = None
    summary_commu_empty_desc: str | None = None
    summary_commu_not_empty_desc: str | None = None
    summary_hidden_passed_desc: str | None = None
    summary_hidden_not_passed_desc: str | None = None
    summary_knight_passed_desc: str | None = None
    summary_knight_not_passed_desc: str | None = None
    summary_gold_threshold: int = 0
    summary_gold_high_desc: str | None = None
    summary_gold_low_desc: str | None = None
    summary_practice_threshold: int = 0
    summary_practice_high_desc: str | None = None
    summary_practice_low_desc: str | None = None


class RL02DifficultyExt(GameDataModel):
    """clz_Torappu_RL02DifficultyExt"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    buff_desc: list[str] | None = None


class RL02CustomizeData(GameDataModel):
    """clz_Torappu_RL02CustomizeData"""

    developments: dict[str, RL02Development] | None = None
    development_tokens: dict[str, RoguelikeTopicDevToken] | None = None
    development_raw_text_group: list[RL02DevRawTextBuffGroup] | None = None
    development_lines: list[RL02DevelopmentLine] | None = None
    ending_text: RL02EndingText | None = None
    difficulties: list[RL02DifficultyExt] | None = None


class RL03Development(GameDataModel):
    """clz_Torappu_RL03Development"""

    buff_id: str | None = None
    node_type: str = "NONE"
    front_node_id: list[str] | None = None
    next_node_id: list[str] | None = None
    position_row: int = 0
    position_order: int = 0
    token_cost: int = 0
    buff_name: str | None = None
    buff_icon_id: str | None = None
    effect_type: str = "BUFF"
    raw_desc: list[str] | None = None
    buff_display_info: list[RoguelikeTopicDisplayItem] | None = None
    group_id: str | None = None
    enroll_id: str | None = None


class RL03DevRawTextBuffGroup(GameDataModel):
    """clz_Torappu_RL03DevRawTextBuffGroup"""

    node_id_list: list[str] | None = None
    use_level_mark: bool = False
    group_icon_id: str | None = None
    sort_id: int = 0


class RL03DevDifficultyNodePairInfo(GameDataModel):
    """clz_Torappu_RL03DevDifficultyNodePairInfo"""

    front_node: str | None = None
    next_node: str | None = None


class RL03DevDifficultyNodeInfo(GameDataModel):
    """clz_Torappu_RL03DevDifficultyNodeInfo"""

    buff_id: str | None = None
    node_map: list[RL03DevDifficultyNodePairInfo] | None = None
    enable_grade: int = 0


class RL03EndingText(GameDataModel):
    """clz_Torappu_RL03EndingText"""

    summary_get_totem: str | None = None
    summary_demo_point_up: str | None = None
    summary_demo_point_down: str | None = None
    summary_demo_grade_up: str | None = None
    summary_demo_grade_down: str | None = None
    summary_vision_point_up: str | None = None
    summary_vision_point_down: str | None = None
    summary_vision_grade_up: str | None = None
    summary_vision_grade_down: str | None = None
    summary_fight_win: str | None = None
    summary_fight_fail: str | None = None
    summary_exchange_totem: str | None = None
    summary_use_totem: str | None = None
    summary_vision_grade: str | None = None
    summary_actor: str | None = None
    summary_top: str | None = None
    summary_zone: str | None = None
    summary_ending: str | None = None
    summary_difficulty_zone: str | None = None
    summary_difficulty_ending: str | None = None
    summary_mode: str | None = None
    summary_group: str | None = None
    summary_support: str | None = None
    summary_normal_recruit: str | None = None
    summary_direct_recruit: str | None = None
    summary_friend_recruit: str | None = None
    summary_free_recruit: str | None = None
    summary_month_recruit: str | None = None
    summary_upgrade: str | None = None
    summary_complete_ending: str | None = None
    summary_each_zone: str | None = None
    summary_meet_sp_zone: str | None = None
    summary_perfect_battle: str | None = None
    summary_meet_battle: str | None = None
    summary_meet_event: str | None = None
    summary_meet_shop: str | None = None
    summary_meet_treasure: str | None = None
    summary_meet_secretpath: str | None = None
    summary_exchange_relic: str | None = None
    summary_meet_trade: str | None = None
    summary_buy: str | None = None
    summary_buy_with_price_id: str | None = None
    summary_invest: str | None = None
    summary_get: str | None = None
    summary_relic: str | None = None
    summary_safe_house: str | None = None
    summary_fail_end: str | None = None
    summary_stock_recruit_ticket: str | None = None
    summary_duel_win: str | None = None
    summary_duel_tie: str | None = None
    summary_duel_lose: str | None = None
    summary_expedition_go: str | None = None
    summary_expedition_back: str | None = None


class RL03DifficultyExt(GameDataModel):
    """clz_Torappu_RL03DifficultyExt"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    totem_prob: float = 0.0
    relic_dev_level: str | None = None
    buffs: list[str] | None = None
    buff_desc: list[str] | None = None


class RL03CustomizeData(GameDataModel):
    """clz_Torappu_RL03CustomizeData"""

    developments: dict[str, RL03Development] | None = None
    developments_tokens: dict[str, RoguelikeTopicDevToken] | None = None
    development_raw_text_group: list[RL03DevRawTextBuffGroup] | None = None
    developments_difficulty_node_infos: dict[str, RL03DevDifficultyNodeInfo] | None = (
        None
    )
    ending_text: RL03EndingText | None = None
    difficulties: list[RL03DifficultyExt] | None = None


class RoguelikeCommonDevelopment(GameDataModel):
    """clz_Torappu_RoguelikeCommonDevelopment"""

    buff_id: str | None = None
    node_type: str = "NONE"
    front_node_id: list[str] | None = None
    next_node_id: list[str] | None = None
    position_row: int = 0
    position_order: int = 0
    token_cost: int = 0
    buff_name: str | None = None
    active_icon_id: str | None = None
    inactive_icon_id: str | None = None
    bottom_icon_id: str | None = None
    effect_type: str = "BUFF"
    raw_desc: list[str] | None = None
    buff_display_info: list[RoguelikeTopicDisplayItem] | None = None
    group_id: str | None = None
    enroll_id: str | None = None


class RoguelikeCommonDevRawTextBuffGroup(GameDataModel):
    """clz_Torappu_RoguelikeCommonDevRawTextBuffGroup"""

    node_id_list: list[str] | None = None
    group_icon_id: str | None = None
    sort_id: int = 0


class RoguelikeCommonDevDifficultyNodePairInfo(GameDataModel):
    """clz_Torappu_RoguelikeCommonDevDifficultyNodePairInfo"""

    front_nodes: list[str] | None = None
    next_node: str | None = None


class RoguelikeCommonDevDifficultyNodeInfo(GameDataModel):
    """clz_Torappu_RoguelikeCommonDevDifficultyNodeInfo"""

    buff_id: str | None = None
    node_map: list[RoguelikeCommonDevDifficultyNodePairInfo] | None = None
    enable_grade: int = 0
    enable_desc: str | None = None
    light_id: str | None = None
    deco_id: str | None = None


class RoguelikeCommonDevelopmentData(GameDataModel):
    """clz_Torappu_RoguelikeCommonDevelopmentData"""

    developments: dict[str, RoguelikeCommonDevelopment] | None = None
    developments_tokens: dict[str, RoguelikeTopicDevToken] | None = None
    development_raw_text_group: list[RoguelikeCommonDevRawTextBuffGroup] | None = None
    developments_difficulty_node_infos: (
        dict[str, RoguelikeCommonDevDifficultyNodeInfo] | None
    ) = None


class RL04DifficultyExt(GameDataModel):
    """clz_Torappu_RL04DifficultyExt"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    left_disaster_desc: str | None = None
    left_overweight_desc: str | None = None
    relic_dev_level: str | None = None
    weight_status_limit_desc: str | None = None
    buffs: list[str] | None = None
    buff_desc: list[str] | None = None


class RL04EndingText(GameDataModel):
    """clz_Torappu_RL04EndingText"""

    summary_get_fragment: str | None = None
    summary_use_idea: str | None = None
    summary_use_food: str | None = None
    summary_drop_fragment: str | None = None
    summary_meet_disaster: str | None = None
    summary_leave_disaster: str | None = None
    summary_enter_alchemy: str | None = None
    summary_alchemy_others: str | None = None
    summary_alchemy_fragment: str | None = None
    summary_weight_overweight: str | None = None
    summary_weight_limit: str | None = None
    summary_weight_safe: str | None = None
    summary_perm_upgrade: str | None = None
    summary_temp_upgrade: str | None = None
    summary_sell_fragment: str | None = None
    summary_actor: str | None = None
    summary_top: str | None = None
    summary_zone: str | None = None
    summary_ending: str | None = None
    summary_difficulty_zone: str | None = None
    summary_difficulty_ending: str | None = None
    summary_mode: str | None = None
    summary_support: str | None = None
    summary_group: str | None = None
    summary_normal_recruit: str | None = None
    summary_direct_recruit: str | None = None
    summary_friend_recruit: str | None = None
    summary_free_recruit: str | None = None
    summary_month_recruit: str | None = None
    summary_upgrade: str | None = None
    summary_complete_ending: str | None = None
    summary_each_zone: str | None = None
    summary_meet_sp_zone: str | None = None
    summary_perfect_battle: str | None = None
    summary_meet_battle: str | None = None
    summary_meet_event: str | None = None
    summary_meet_shop: str | None = None
    summary_meet_treasure: str | None = None
    summary_meet_secretpath: str | None = None
    summary_exchange_relic: str | None = None
    summary_meet_trade: str | None = None
    summary_buy: str | None = None
    summary_buy_with_price_id: str | None = None
    summary_invest: str | None = None
    summary_get: str | None = None
    summary_relic: str | None = None
    summary_safe_house: str | None = None
    summary_fail_end: str | None = None
    summary_duel_win: str | None = None
    summary_duel_tie: str | None = None
    summary_duel_lose: str | None = None
    summary_stock_recruit_ticket: str | None = None
    summary_expedition_go: str | None = None
    summary_expedition_back: str | None = None


class RL04CustomizeData(GameDataModel):
    """clz_Torappu_RL04CustomizeData"""

    common_development: RoguelikeCommonDevelopmentData | None = None
    difficulties: list[RL04DifficultyExt] | None = None
    ending_text: RL04EndingText | None = None


class RL05DifficultyExt(GameDataModel):
    """clz_Torappu_RL05DifficultyExt"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    buffs: list[str] | None = None
    buff_desc: list[str] | None = None
    left_wrath_desc: str | None = None
    relic_dev_level: str | None = None
    gild_prob_display: str | None = None
    sky_step_description: str | None = None


class RL05EndingText(GameDataModel):
    """clz_Torappu_RL05EndingText"""

    summary_get_copper: str | None = None
    summary_lost_copper: str | None = None
    summary_draw_copper: str | None = None
    summary_copper_result_good: str | None = None
    summary_copper_result_bad: str | None = None
    summary_copper_result_normal: str | None = None
    summary_copper_check_success: str | None = None
    summary_copper_check_fail: str | None = None
    summary_copper_check_normal: str | None = None
    summary_meet_wrath: str | None = None
    summary_expedition_go_ending_four: str | None = None
    summary_expedition_back_ending_four: str | None = None
    summary_expedition_back_candle: str | None = None
    summary_expedition_go_ending: str | None = None
    summary_expedition_back_ending: str | None = None
    summary_hold_candle: str | None = None
    summary_hold_candle_recruit: str | None = None
    summary_hold_candle_upgrade: str | None = None
    summary_expedition_ending_four_to_five: str | None = None
    summary_exchange_sp_zone_get: str | None = None
    summary_meet_shop_sp_zone: str | None = None
    summary_battle_fail_sp_zone: str | None = None
    summary_meet_event_lock: str | None = None
    summary_treasure_sp_zone: str | None = None
    summary_meet_exchange_sp_zone: str | None = None
    summary_meet_trade_sp_zone: str | None = None
    summary_actor: str | None = None
    summary_top: str | None = None
    summary_zone: str | None = None
    summary_ending: str | None = None
    summary_difficulty_zone: str | None = None
    summary_difficulty_ending: str | None = None
    summary_mode: str | None = None
    summary_support: str | None = None
    summary_group: str | None = None
    summary_normal_recruit: str | None = None
    summary_direct_recruit: str | None = None
    summary_friend_recruit: str | None = None
    summary_free_recruit: str | None = None
    summary_month_recruit: str | None = None
    summary_upgrade: str | None = None
    summary_complete_ending: str | None = None
    summary_each_zone: str | None = None
    summary_meet_sp_zone: str | None = None
    summary_perfect_battle: str | None = None
    summary_meet_battle: str | None = None
    summary_meet_event: str | None = None
    summary_meet_shop: str | None = None
    summary_meet_treasure: str | None = None
    summary_meet_secretpath: str | None = None
    summary_exchange_relic: str | None = None
    summary_meet_trade: str | None = None
    summary_buy: str | None = None
    summary_buy_with_price_id: str | None = None
    summary_invest: str | None = None
    summary_get: str | None = None
    summary_relic: str | None = None
    summary_safe_house: str | None = None
    summary_fail_end: str | None = None
    summary_stock_recruit_ticket: str | None = None
    summary_duel_win: str | None = None
    summary_duel_tie: str | None = None
    summary_duel_lose: str | None = None
    summary_expedition_go: str | None = None
    summary_expedition_back: str | None = None


class RL05CustomizeData(GameDataModel):
    """clz_Torappu_RL05CustomizeData"""

    common_development: RoguelikeCommonDevelopmentData | None = None
    difficulties: list[RL05DifficultyExt] | None = None
    special_shop_dialog: RoguelikeGameShopDialogData | None = None
    ending_text: RL05EndingText | None = None


class RL06DifficultyExt(GameDataModel):
    """clz_Torappu_RL06DifficultyExt"""

    mode_difficulty: str = "NONE"
    grade: int = 0
    buffs: list[str] | None = None
    buff_desc: list[str] | None = None
    left_weather_desc: str | None = None
    relic_dev_level: str | None = None


class RL06EndingText(GameDataModel):
    """clz_Torappu_RL06EndingText"""

    summary_scrap_got: str | None = None
    summary_scrap_sold: str | None = None
    summary_scrap_lost: str | None = None
    summary_scrap_move: str | None = None
    summary_scrap_buff: str | None = None
    summary_scrap_legacy: str | None = None
    summary_meet_weather: str | None = None
    summary_weather_clear: str | None = None
    summary_bubble_bandit: str | None = None
    summary_bubble_treasure: str | None = None
    summary_bubble_event: str | None = None
    summary_savage_camp: str | None = None
    summary_scrap_shop: str | None = None
    summary_scrap_shop_buy: str | None = None
    summary_scrap_shop_identify: str | None = None
    summary_door: str | None = None
    summary_tree_hole: str | None = None
    summary_evacuate: str | None = None
    summary_employ_camp: str | None = None
    summary_employ_recruit: str | None = None
    summary_mercenary_leave: str | None = None
    summary_encounter_battle_win: str | None = None
    summary_encounter_battle_lose: str | None = None
    summary_exchange_scrap: str | None = None
    summary_expedition_go_ending: str | None = None
    summary_expedition_back_ending: str | None = None
    summary_actor: str | None = None
    summary_top: str | None = None
    summary_zone: str | None = None
    summary_ending: str | None = None
    summary_difficulty_zone: str | None = None
    summary_difficulty_ending: str | None = None
    summary_mode: str | None = None
    summary_support: str | None = None
    summary_group: str | None = None
    summary_normal_recruit: str | None = None
    summary_direct_recruit: str | None = None
    summary_friend_recruit: str | None = None
    summary_free_recruit: str | None = None
    summary_month_recruit: str | None = None
    summary_upgrade: str | None = None
    summary_complete_ending: str | None = None
    summary_each_zone: str | None = None
    summary_meet_sp_zone: str | None = None
    summary_perfect_battle: str | None = None
    summary_meet_battle: str | None = None
    summary_meet_event: str | None = None
    summary_meet_shop: str | None = None
    summary_meet_treasure: str | None = None
    summary_meet_secretpath: str | None = None
    summary_exchange_relic: str | None = None
    summary_meet_trade: str | None = None
    summary_buy: str | None = None
    summary_buy_with_price_id: str | None = None
    summary_invest: str | None = None
    summary_get: str | None = None
    summary_relic: str | None = None
    summary_safe_house: str | None = None
    summary_fail_end: str | None = None
    summary_stock_recruit_ticket: str | None = None
    summary_duel_win: str | None = None
    summary_duel_tie: str | None = None
    summary_duel_lose: str | None = None
    summary_expedition_go: str | None = None
    summary_expedition_back: str | None = None


class RL06CustomizeData(GameDataModel):
    """clz_Torappu_RL06CustomizeData"""

    common_development: RoguelikeCommonDevelopmentData | None = None
    difficulties: list[RL06DifficultyExt] | None = None
    ending_text: RL06EndingText | None = None
    scrap_shop_dialog_data: RoguelikeGameShopDialogData | None = None
    employ_shop_dialog_data: RoguelikeGameShopDialogData | None = None


class RoguelikeTopicCustomizeData(GameDataModel):
    """clz_Torappu_RoguelikeTopicCustomizeData"""

    rogue_1: RL01CustomizeData | None = Field(default=None, alias="rogue_1")
    rogue_2: RL02CustomizeData | None = Field(default=None, alias="rogue_2")
    rogue_3: RL03CustomizeData | None = Field(default=None, alias="rogue_3")
    rogue_4: RL04CustomizeData | None = Field(default=None, alias="rogue_4")
    rogue_5: RL05CustomizeData | None = Field(default=None, alias="rogue_5")
    rogue_6: RL06CustomizeData | None = Field(default=None, alias="rogue_6")


class RoguelikeTopicTable(GameDataModel):
    """clz_Torappu_RoguelikeTopicTable"""

    topics: dict[str, RoguelikeTopicBasicData] | None = None
    constant: RoguelikeTopicConst | None = None
    details: dict[str, RoguelikeTopicDetail] | None = None
    modules: dict[str, RoguelikeModule] | None = None
    customize_data: RoguelikeTopicCustomizeData | None = None


# root_type clz_Torappu_RoguelikeTopicTable


RoguelikeTopicBasicDataHomeEntryDisplayData.model_rebuild()
RoguelikeTopicConfig.model_rebuild()
RoguelikeTopicBasicData.model_rebuild()
RoguelikeTopicConstPredefinedChar.model_rebuild()
RoguelikeTopicConst.model_rebuild()
RoguelikeTopicUpdate.model_rebuild()
RoguelikeTopicEnroll.model_rebuild()
RoguelikeTopicBP.model_rebuild()
RoguelikeTopicMilestoneUpdateData.model_rebuild()
ItemBundle.model_rebuild()
RoguelikeTopicBPGrandPrize.model_rebuild()
RoguelikeTopicMonthMission.model_rebuild()
RoguelikeTopicMonthSquadTeamChar.model_rebuild()
RoguelikeTopicMonthSquad.model_rebuild()
RoguelikeTopicChallengeTask.model_rebuild()
RoguelikeTopicChallenge.model_rebuild()
RoguelikeTopicDifficultyRuleDescReplacement.model_rebuild()
RoguelikeTopicDifficulty.model_rebuild()
RoguelikeTopicBankReward.model_rebuild()
ActArchiveRelicItemData.model_rebuild()
ActArchiveRelicData.model_rebuild()
ActArchiveCapsuleItemData.model_rebuild()
ActArchiveCapsuleData.model_rebuild()
ActArchiveTrapItemData.model_rebuild()
ActArchiveTrapData.model_rebuild()
ActArchiveChatItemData.model_rebuild()
ActArchiveChatGroupData.model_rebuild()
ActArchiveChatData.model_rebuild()
ActArchiveEndbookItemData.model_rebuild()
ActArchiveEndbookGroupData.model_rebuild()
ActArchiveEndbookData.model_rebuild()
ActArchiveBuffItemData.model_rebuild()
ActArchiveBuffData.model_rebuild()
ActArchiveTotemItemData.model_rebuild()
ActArchiveTotemData.model_rebuild()
ActArchiveChaosItemData.model_rebuild()
ActArchiveChaosData.model_rebuild()
ActArchiveFragmentItemData.model_rebuild()
ActArchiveFragmentData.model_rebuild()
ActArchiveDisasterItemData.model_rebuild()
ActArchiveDisasterData.model_rebuild()
ActArchiveWrathItemData.model_rebuild()
ActArchiveWrathData.model_rebuild()
ActArchiveCopperItemData.model_rebuild()
ActArchiveCopperTypeData.model_rebuild()
ActArchiveCopperGildData.model_rebuild()
ActArchiveCopperLuckyLevelData.model_rebuild()
ActArchiveCopperData.model_rebuild()
ActArchiveScrapItemData.model_rebuild()
ActArchiveScrapData.model_rebuild()
ActArchiveWeatherItemData.model_rebuild()
ActArchiveWeatherData.model_rebuild()
RoguelikeArchiveComponentData.model_rebuild()
RoguelikeArchiveUnlockCondDesc.model_rebuild()
RoguelikeArchiveEnroll.model_rebuild()
RoguelikeArchiveUnlockCondData.model_rebuild()
RoguelikeTopicDetailConstPlayerLevelData.model_rebuild()
RoguelikeTopicDetailConstCharUpgradeData.model_rebuild()
RoguelikeTopicDetailConstPredefinedPlayerLevelData.model_rebuild()
RoguelikeTopicDetailConst.model_rebuild()
RoguelikeGameInitData.model_rebuild()
RoguelikeGameStageData.model_rebuild()
RoguelikeGameZoneData.model_rebuild()
RoguelikeZoneVariationData.model_rebuild()
RoguelikeGameTrapData.model_rebuild()
RoguelikeGameRecruitTicketData.model_rebuild()
RoguelikeGameUpgradeTicketData.model_rebuild()
RoguelikeGameCustomTicketData.model_rebuild()
RoguelikeGameStashableTicketData.model_rebuild()
BlackboardDataPair.model_rebuild()
RoguelikeBuff.model_rebuild()
RoguelikeGameRelicData.model_rebuild()
RoguelikeGameRelicCheckParam.model_rebuild()
RoguelikeGameRelicParamData.model_rebuild()
RoguelikeGameRecruitGrpData.model_rebuild()
RoguelikeChoiceDisplayData.model_rebuild()
RoguelikeGameChoiceData.model_rebuild()
RoguelikeGameChoiceSceneData.model_rebuild()
RoguelikeGameNodeTypeData.model_rebuild()
RoguelikeGameNodeSubTypeData.model_rebuild()
RoguelikeGameVariationData.model_rebuild()
RoguelikeGameFusionData.model_rebuild()
RoguelikeGameCharBuffData.model_rebuild()
RoguelikeGameSquadBuffData.model_rebuild()
RoguelikeTaskData.model_rebuild()
RoguelikeGameConst.model_rebuild()
RoguelikeGameShopDialogGroupData.model_rebuild()
RoguelikeGameShopDialogTypeData.model_rebuild()
RoguelikeGameShopDialogData.model_rebuild()
RoguelikeTopicCapsule.model_rebuild()
RoguelikeGameEndingDataLevelIcon.model_rebuild()
RoguelikeGameEndingData.model_rebuild()
RoguelikeGameFailEndingData.model_rebuild()
RoguelikeBattleSummeryDescriptionData.model_rebuild()
TipData.model_rebuild()
RoguelikeGameItemData.model_rebuild()
RoguelikeBandRefData.model_rebuild()
RoguelikeEndingDetailText.model_rebuild()
RoguelikeEndingRelicDetailText.model_rebuild()
RoguelikeGameTreasureData.model_rebuild()
RoguelikeDifficultyUpgradeRelicData.model_rebuild()
RoguelikeDifficultyUpgradeRelicGroupData.model_rebuild()
RoguelikePredefinedStyleData.model_rebuild()
RoguelikePredefinedExpStyleConfigData.model_rebuild()
RoguelikePredefinedConstStyleData.model_rebuild()
RoguelikeGameExploreToolData.model_rebuild()
RoguelikeRollNodeGroupData.model_rebuild()
RoguelikeRollNodeData.model_rebuild()
RoguelikeRelicTipsData.model_rebuild()
RoguelikeLegacyItemData.model_rebuild()
RoguelikeActivityBasicData.model_rebuild()
RoguelikeActivitySeedModeDataRoguelikeActivityOfficialSeedData.model_rebuild()
RoguelikeActivitySeedModeDataRoguelikeActivitySeedModeConstData.model_rebuild()
RoguelikeActivitySeedModeData.model_rebuild()
RoguelikeActivityTable.model_rebuild()
RoguelikeActivityData.model_rebuild()
RoguelikeTopicDetail.model_rebuild()
RoguelikeSanRangeData.model_rebuild()
RoguelikeSanCheckConsts.model_rebuild()
RoguelikeSanCheckModuleData.model_rebuild()
RoguelikeDiceData.model_rebuild()
RoguelikeDiceRuleData.model_rebuild()
RoguelikeDiceRuleGroupData.model_rebuild()
RoguelikeDicePredefineData.model_rebuild()
RoguelikeDiceModuleData.model_rebuild()
RoguelikeChaosData.model_rebuild()
RoguelikeChaosRangeData.model_rebuild()
RoguelikeChaosPredefineLevelInfo.model_rebuild()
RoguelikeChaosModuleConsts.model_rebuild()
RoguelikeChaosModuleData.model_rebuild()
RoguelikeTotemLinkedNodeTypeData.model_rebuild()
RoguelikeTotemBuffData.model_rebuild()
RoguelikeTotemSubBuffData.model_rebuild()
RoguelikeTotemModuleConsts.model_rebuild()
RoguelikeTotemBuffModuleData.model_rebuild()
RoguelikeVisionData.model_rebuild()
RoguelikeVisionModuleDataVisionChoiceConfig.model_rebuild()
RoguelikeVisionModuleConsts.model_rebuild()
RoguelikeVisionModuleData.model_rebuild()
RoguelikeFragmentData.model_rebuild()
RoguelikeFragmentTypeData.model_rebuild()
RoguelikeFragmentModuleConsts.model_rebuild()
RoguelikeFragmentBuffData.model_rebuild()
RoguelikeAlchemyData.model_rebuild()
RoguelikeAlchemyFormulationData.model_rebuild()
RoguelikeFragmentLevelRelatedData.model_rebuild()
RoguelikeFragmentModuleData.model_rebuild()
RoguelikeDisasterData.model_rebuild()
RoguelikeDisasterModuleData.model_rebuild()
RoguelikePermNodeUpgradeItemData.model_rebuild()
RoguelikeTempNodeUpgradeItemData.model_rebuild()
RoguelikeNodeUpgradeData.model_rebuild()
RoguelikeNodeUpgradeModuleData.model_rebuild()
RoguelikeCopperData.model_rebuild()
RoguelikeCopperDivineData.model_rebuild()
RoguelikeCopperGildTypeData.model_rebuild()
RoguelikeCopperModuleConsts.model_rebuild()
RoguelikeCopperModuleData.model_rebuild()
RoguelikeWrathData.model_rebuild()
RoguelikeWrathModuleConsts.model_rebuild()
RoguelikeWrathModuleData.model_rebuild()
RoguelikeCandleModuleConsts.model_rebuild()
RoguelikeCandleModuleData.model_rebuild()
RoguelikeSkyNodeData.model_rebuild()
RoguelikeSkyNodeSubTypeData.model_rebuild()
RoguelikeSkyModuleConsts.model_rebuild()
RoguelikeSkyModuleData.model_rebuild()
RoguelikeMainWeatherData.model_rebuild()
RoguelikeSubWeatherData.model_rebuild()
RoguelikeWeatherModuleData.model_rebuild()
RoguelikeGridZoneMissionBannerData.model_rebuild()
RoguelikeGridZoneFocusViewHintData.model_rebuild()
RoguelikeBuoyItemData.model_rebuild()
RoguelikeGridZoneModuleConsts.model_rebuild()
RoguelikeGridZoneModuleData.model_rebuild()
RoguelikeScrapTypeData.model_rebuild()
RoguelikeScrapMoveData.model_rebuild()
RoguelikeScrapGoodsData.model_rebuild()
RoguelikeScrapPassiveData.model_rebuild()
GridPosition.model_rebuild()
RangeData.model_rebuild()
RoguelikeScrapModuleConsts.model_rebuild()
RoguelikeScrapModuleData.model_rebuild()
RoguelikeModule.model_rebuild()
RoguelikeTopicDisplayItem.model_rebuild()
RoguelikeTopicDev.model_rebuild()
RoguelikeTopicDevToken.model_rebuild()
RL01EndingText.model_rebuild()
RL01DifficultyExt.model_rebuild()
RL01CustomizeData.model_rebuild()
RL02Development.model_rebuild()
RL02DevRawTextBuffGroup.model_rebuild()
RL02DevelopmentLine.model_rebuild()
RL02EndingText.model_rebuild()
RL02DifficultyExt.model_rebuild()
RL02CustomizeData.model_rebuild()
RL03Development.model_rebuild()
RL03DevRawTextBuffGroup.model_rebuild()
RL03DevDifficultyNodePairInfo.model_rebuild()
RL03DevDifficultyNodeInfo.model_rebuild()
RL03EndingText.model_rebuild()
RL03DifficultyExt.model_rebuild()
RL03CustomizeData.model_rebuild()
RoguelikeCommonDevelopment.model_rebuild()
RoguelikeCommonDevRawTextBuffGroup.model_rebuild()
RoguelikeCommonDevDifficultyNodePairInfo.model_rebuild()
RoguelikeCommonDevDifficultyNodeInfo.model_rebuild()
RoguelikeCommonDevelopmentData.model_rebuild()
RL04DifficultyExt.model_rebuild()
RL04EndingText.model_rebuild()
RL04CustomizeData.model_rebuild()
RL05DifficultyExt.model_rebuild()
RL05EndingText.model_rebuild()
RL05CustomizeData.model_rebuild()
RL06DifficultyExt.model_rebuild()
RL06EndingText.model_rebuild()
RL06CustomizeData.model_rebuild()
RoguelikeTopicCustomizeData.model_rebuild()
RoguelikeTopicTable.model_rebuild()

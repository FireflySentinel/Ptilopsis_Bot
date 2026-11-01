"""activity_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/activity_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum
from typing import Any

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class ActivityType(IntEnum):
    """enum__Torappu_ActivityType"""

    DEFAULT = 0
    MISSION_ONLY = 1
    CHECKIN_ONLY = 2
    CHECKIN_ALL_PLAYER = 3
    TYPE_ACT3D0 = 4
    TYPE_ACT4D0 = 5
    TYPE_ACT5D0 = 6
    TYPE_ACT5D1 = 7
    COLLECTION = 8
    AVG_ONLY = 9
    TYPE_ACT9D0 = 10
    TYPE_ACT12SIDE = 11
    TYPE_ACT13SIDE = 12
    TYPE_ACT17SIDE = 13
    LOGIN_ONLY = 14
    MINISTORY = 15
    ROGUELIKE = 16
    PRAY_ONLY = 17
    MULTIPLAY = 18
    MULTIPLAY_VERIFY2 = 19
    TYPE_ACT17D7 = 20
    GRID_GACHA = 21
    GRID_GACHA_V2 = 22
    INTERLOCK = 23
    APRIL_FOOL = 24
    BOSS_RUSH = 25
    TYPE_ACT20SIDE = 26
    FLOAT_PARADE = 27
    TYPE_ACT21SIDE = 28
    MAIN_BUFF = 29
    TYPE_ACT24SIDE = 30
    FLIP_ONLY = 31
    TYPE_ACT25SIDE = 32
    CHECKIN_VS = 33
    SWITCH_ONLY = 34
    TYPE_ACT27SIDE = 35
    UNIQUE_ONLY = 36
    MAINLINE_BP = 37
    TYPE_ACT42D0 = 38
    TYPE_ACT29SIDE = 39
    BLESS_ONLY = 40
    CHECKIN_ACCESS = 41
    YEAR_5_GENERAL = 42
    TYPE_ACT35SIDE = 43
    VEC_BREAK = 44
    TYPE_ACT36SIDE = 45
    TYPE_ACT38SIDE = 46
    AUTOCHESS_VERIFY1 = 47
    CHECKIN_VIDEO = 48
    ARCADE = 49
    MULTIPLAY_V3 = 50
    TYPE_MAINSS = 51
    ENEMY_DUEL = 52
    VEC_BREAK_V2 = 53
    TYPE_ACT42SIDE = 54
    TYPE_ACT44SIDE = 55
    HALFIDLE_VERIFY1 = 56
    TYPE_ACT45SIDE = 57
    TEAM_QUEST = 58
    RECRUIT_ONLY = 59
    TYPE_ACT46SIDE = 60
    AUTOCHESS_SEASON = 61
    ARK_HUB = 62
    ACT_FOOTBALL = 63
    TYPE_ACT53SIDE = 64
    TYPE_ACT54SIDE = 65
    ACT_DP = 66
    REWARD_ONLY = 67
    AUTOCHESS = 68
    TYPE_ACT55SIDE = 69
    ENUM = 70


class ActivityDisplayType(IntEnum):
    """enum__Torappu_ActivityDisplayType"""

    NONE = 0
    SIDESTORY = 1
    BRANCHLINE = 2
    MINISTORY = 3


class ActivityCompleteType(IntEnum):
    """enum__Torappu_ActivityCompleteType"""

    SPECIAL = 0
    CAN_COMPLETE = 1
    CANNOT_COMPLETE = 2


class CommonUnlockType(IntEnum):
    """enum__Torappu_CommonUnlockType"""

    STAGECLEAR = 0
    HASCHAR = 1
    NONE = 2


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


class VersusCheckInDataTasteType(IntEnum):
    """enum__Torappu_VersusCheckInData_TasteType"""

    DRAW = 0
    SWEET = 1
    SALT = 2


class Act3D0DataGoodType(IntEnum):
    """enum__Torappu_Act3D0Data_GoodType"""

    NORMAL = 0
    SPECIAL = 1


class Act3D0DataGachaBoxType(IntEnum):
    """enum__Torappu_Act3D0Data_GachaBoxType"""

    LIMITED = 0
    UNLIMITED = 1


class MileStoneInfoGoodType(IntEnum):
    """enum__Torappu_MileStoneInfo_GoodType"""

    NORMAL = 0
    SPECIAL = 1


class Act5D1DataGoodType(IntEnum):
    """enum__Torappu_Act5D1Data_GoodType"""

    NORMAL = 0
    PROGRESS = 1


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


class ActivityCollectionDataJumpType(IntEnum):
    """enum__Torappu_ActivityCollectionData_JumpType"""

    NONE = 0
    ROGUE = 1
    CHAR_REPO = 2


class Act9D0DataActivityNewsLineType(IntEnum):
    """enum__Torappu_Act9D0Data_ActivityNewsLineType"""

    TextContent = 0
    ImageContent = 1


class Act12SideDataActZoneClass(IntEnum):
    """enum__Torappu_Act12SideData_ActZoneClass"""

    NONE = 0
    NORMAL = 1
    HIGHLEVEL = 2
    SUB = 3


class Act12SideDataRecycleDialogType(IntEnum):
    """enum__Torappu_Act12SideData_RecycleDialogType"""

    NONE = 0
    EMPTY = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    GACHA = 5


class Act12SideDataRecycleAnimationState(IntEnum):
    """enum__Torappu_Act12SideData_RecycleAnimationState"""

    NONE = 0
    NORMAL = 1
    SMILE = 2


class Act13SideDataPrestigeRank(IntEnum):
    """enum__Torappu_Act13SideData_PrestigeRank"""

    D = 0
    C = 1
    B = 2
    A = 3
    S = 4


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


class Act13SideDataUnlockCondition(IntEnum):
    """enum__Torappu_Act13SideData_UnlockCondition"""

    NONE = 0
    PRESTIGE = 1
    STAGE = 2


class PlayerBattleRank(IntEnum):
    """enum__Torappu_PlayerBattleRank"""

    FAIL = 1
    PASS = 2
    COMPLETE = 3
    ERR_ZERO = 0


class Act13SideDataActZoneClass(IntEnum):
    """enum__Torappu_Act13SideData_ActZoneClass"""

    NONE = 0
    NORMAL = 1
    HIGHLEVEL = 2
    SUB = 3


class Act17sideDataNodeType(IntEnum):
    """enum__Torappu_Act17sideData_NodeType"""

    LANDMARK = 0
    STORY = 1
    BATTLE = 2
    ENDING = 3
    TREASURE = 4
    EVENT = 5
    TECH = 6
    CHOICE = 7


class Act17sideDataTrackPointType(IntEnum):
    """enum__Torappu_Act17sideData_TrackPointType"""

    NONE = 0
    MAIN = 1
    SUB = 2


class Act17sideDataTreasureType(IntEnum):
    """enum__Torappu_Act17sideData_TreasureType"""

    SMALL = 0
    SPECIAL = 1


class Act17sideDataArchiveItemUnlockCondition(IntEnum):
    """enum__Torappu_Act17sideData_ArchiveItemUnlockCondition"""

    NONE = 0
    STAGE = 1
    NODE = 2


class Act17sideDataArchiveItemStageUnlockParam(IntEnum):
    """enum__Torappu_Act17sideData_ArchiveItemStageUnlockParam"""

    NONE = 0
    PLAYED = 1
    PASS = 2
    COMPLETE = 3


class Act17sideDataChapterIconType(IntEnum):
    """enum__Torappu_Act17sideData_ChapterIconType"""

    NORMAL = 0
    EX = 1
    HARD = 2


class ActivityInterlockDataInterlockStageType(IntEnum):
    """enum__Torappu_ActivityInterlockData_InterlockStageType"""

    NONE = 0
    NORMAL = 1
    INTERLOCK = 2
    FINAL = 3


class ActivityBossRushDataBossRushStageType(IntEnum):
    """enum__Torappu_ActivityBossRushData_BossRushStageType"""

    NONE = 0
    NORMAL = 1
    TEAM = 2
    EX = 3
    SP = 4


class OccPer(IntEnum):
    """enum__Torappu_OccPer"""

    ALWAYS = 0
    ALMOST = 1
    USUAL = 2
    OFTEN = 3
    SOMETIMES = 4
    NEVER = 5
    DEFINITELY_BUFF = 6


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


class Act24SideDataMeldingItemRarityType(IntEnum):
    """enum__Torappu_Act24SideData_MeldingItemRarityType"""

    NONE = 0
    RARITY_1 = 1
    RARITY_2 = 2
    RARITY_3 = 3
    RARITY_4 = 4
    RARITY_5 = 5
    RARITY_6 = 6


class Act24SideDataMeldingGoodDisplayType(IntEnum):
    """enum__Torappu_Act24SideData_MeldingGoodDisplayType"""

    NONE = 0
    RARE_1 = 1
    RARE_2 = 2
    RARE_3 = 3


class Act24SideDataMeldingGoodGachaType(IntEnum):
    """enum__Torappu_Act24SideData_MeldingGoodGachaType"""

    NONE = 0
    LIMITED = 1
    UNLIMITED = 2


class Act24SideDataMissionType(IntEnum):
    """enum__Torappu_Act24SideData_MissionType"""

    NONE = 0
    HUNTING_TASK = 1
    COLLECTION_TASK = 2
    EXPLORATION_TASK = 3
    MONSTER_TASK = 4
    INVATION_TASK = 5


class Act25SideDataAct25SideArchiveItemType(IntEnum):
    """enum__Torappu_Act25SideData_Act25SideArchiveItemType"""

    PIC = 0
    STORY = 1
    BATTLE_PERFORMANCE = 2
    KEY = 3
    ENUM = 4


class Act25SideDataAct25SideArchiveItemUnlockType(IntEnum):
    """enum__Torappu_Act25SideData_Act25SideArchiveItemUnlockType"""

    MISSION = 0
    STAGE = 1
    BUFF = 2


class Act25SideDataAct25sideTechType(IntEnum):
    """enum__Torappu_Act25SideData_Act25sideTechType"""

    TECH_1 = 0
    TECH_2 = 1
    TECH_3 = 2
    TECH_4 = 3
    TECH_NUM = 4


class Act42D0DataAct42D0AreaDifficulty(IntEnum):
    """enum__Torappu_Act42D0Data_Act42D0AreaDifficulty"""

    NONE = 0
    NORMAL = 1
    HARD = 2


class Act29SideDataAct29SideOrcheType(IntEnum):
    """enum__Torappu_Act29SideData_Act29SideOrcheType"""

    ORCHE_1 = 0
    ORCHE_2 = 1
    ORCHE_3 = 2
    ENUM = 3


class Act29SideDataAct29SideProductType(IntEnum):
    """enum__Torappu_Act29SideData_Act29SideProductType"""

    PRODUCT_TYPE_1 = 0
    PRODUCT_TYPE_2 = 1
    PRODUCT_TYPE_3 = 2
    PRODUCT_TYPE_4 = 3
    PRODUCT_TYPE_5 = 4
    ENUM = 5


class Act29SideDataAct29SideInvestType(IntEnum):
    """enum__Torappu_Act29SideData_Act29SideInvestType"""

    MAJOR = 0
    RARE = 1
    NORMAL = 2


class Act35SideDataDialogueType(IntEnum):
    """enum__Torappu_Act35SideData_DialogueType"""

    NONE = 0
    ENTRY = 1
    BONUS = 2
    BUY = 3
    PROCESS = 4


class Act35SideDataDialogueNameBgType(IntEnum):
    """enum__Torappu_Act35SideData_DialogueNameBgType"""

    NONE = 0
    GREEN = 1
    BLUE = 2


class ActVecBreakV2ParticleType(IntEnum):
    """enum__Torappu_ActVecBreakV2ParticleType"""

    NONE = 0
    HARD = 1


class ActVecBreakV2StageOrderType(IntEnum):
    """enum__Torappu_ActVecBreakV2StageOrderType"""

    NONE = 0
    A = 1
    B = 2
    C = 3
    D = 4


class Act38SideDataNpcDialogType(IntEnum):
    """enum__Torappu_Act38SideData_NpcDialogType"""

    NONE = 0
    ENTER_PUZZLE = 1
    PLATE_ERROR = 2
    HINT_SUCC = 3
    HINT_FAIL = 4
    PUZZLE_SOLVED = 5


class ActArcadeDataRank(IntEnum):
    """enum__Torappu_ActArcadeData_Rank"""

    B = 0
    A = 1
    S = 2
    SS = 3
    SSS = 4


class ActArcadeDataSubModeType(IntEnum):
    """enum__Torappu_ActArcadeData_SubModeType"""

    IGNORE = -1
    MINER = 0
    DRAW = 1
    LINE = 2
    CAR = 3
    FISH = 4
    E_NUM = 5


class ActArcadeDataBadgeType(IntEnum):
    """enum__Torappu_ActArcadeData_BadgeType"""

    COMMON = 0
    ZONE = 1
    ULTIMATE = 2


class ActMultiV3PrepareStepType(IntEnum):
    """enum__Torappu_ActMultiV3PrepareStepType"""

    NONE = 0
    STAGE_CHOOSE = 1
    ENTRANCE = 2
    CHAR_PICK = 3
    SYS_ALLOC = 4
    SQUAD_CHECK = 5


class ActMultiV3MapModeType(IntEnum):
    """enum__Torappu_ActMultiV3MapModeType"""

    NONE = 0
    NORMAL = 1
    FOOTBALL = 2
    DEFENCE = 3
    RAFT = 4


class ActMultiV3IdentityType(IntEnum):
    """enum__Torappu_ActMultiV3IdentityType"""

    NONE = 0
    HIGH = 1
    LOW = 2
    TEMPORARY = 3
    ALL = 4


class ActMultiV3MapDiffType(IntEnum):
    """enum__Torappu_ActMultiV3MapDiffType"""

    NONE = 0
    TRAINING = 1
    ORDINARY = 2
    DIFFICULTY = 3
    EXTREMELY = 4


class ActMultiV3MatchPosType(IntEnum):
    """enum__Torappu_ActMultiV3MatchPosType"""

    NORMAL = 0
    COACH = 1
    STUDENT = 2


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


class PlayerAvatarGroupType(IntEnum):
    """enum__Torappu_PlayerAvatarGroupType"""

    NONE = 0
    ASSISTANT = 1
    DEFAULT = 2
    SPECIAL = 3
    ACTIVITY = 4
    DYNAMIC = 5


class ActMultiV3BlockDirType(IntEnum):
    """enum__Torappu_ActMultiV3BlockDirType"""

    NONE = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class ActMultiV3BlockType(IntEnum):
    """enum__Torappu_ActMultiV3BlockType"""

    NONE = 0
    START = 1
    END = 2
    MID = 3


class EnemyDuelModeType(IntEnum):
    """enum__Torappu_EnemyDuelModeType"""

    OPERATION = 0
    STAND = 1


class EnemyDuelBetStrategy(IntEnum):
    """enum__Torappu_EnemyDuelBetStrategy"""

    DEFAULT = 0
    CHOOSE_WIN = 1
    CHOOSE_ODD = 2
    FOLLOW_FEWER = 3
    FOLLOW_MORE = 4
    CHOOSE_ODD_ENEMY_COUNT = 5
    CHOOSE_EVEN_ENEMY_COUNT = 6
    ALWAYS_LEFT = 7


class Act44SideDataInsightType(IntEnum):
    """enum__Torappu_Act44SideData_InsightType"""

    PATIENCE = 0
    ATTENTION = 1
    TRUST = 2


class Act1VHalfIdleGachaPoolType(IntEnum):
    """enum__Torappu_Act1VHalfIdleGachaPoolType"""

    NONE = 0
    GACHA_NORMAL = 1
    GACHA_NEWPLAYER = 2
    GACHA_PAC = 3
    GACHA_DIRECT = 4


class Act1VHalfIdlePlotType(IntEnum):
    """enum__Torappu_Act1VHalfIdlePlotType"""

    NONE = 0
    LANDSCAPE = 1
    ROAD = 2
    ROADSIDE = 3
    SPECIAL = 4


class Act1VHalfIdlePlotCombineType(IntEnum):
    """enum__Torappu_Act1VHalfIdlePlotCombineType"""

    NONE = 0
    SINGLE = 1
    PLUS = 2
    PLUS_OR = 3


class RarityRank(IntEnum):
    """enum__Torappu_RarityRank"""

    TIER_1 = 0
    TIER_2 = 1
    TIER_3 = 2
    TIER_4 = 3
    TIER_5 = 4
    TIER_6 = 5
    E_NUM = 6


class Act1VHalfIdleTechTreeNodeType(IntEnum):
    """enum__Torappu_Act1VHalfIdleTechTreeNodeType"""

    NONE = 0
    NORMAL = 1
    DIFFICULTY = 2


class Act1VHalfIdleBattleItemType(IntEnum):
    """enum__Torappu_Act1VHalfIdleBattleItemType"""

    EQUIP = 0
    TRAP = 1


class Act1VHalfIdleEquipType(IntEnum):
    """enum__Torappu_Act1VHalfIdleEquipType"""

    WEAPON = 0
    ARMOR = 1
    ACCESSORY = 2
    NUM = 3


class HalfIdleTrapBuildableType(IntEnum):
    """enum__Torappu_HalfIdleTrapBuildableType"""

    NONE = 0
    HIGHLAND = 1
    LOWLAND = 2
    IGNORE_TILE_HEIGHT = 3
    LHHE = 4
    LHPLT = 5
    LHRUIN = 6
    LHBOT = 7


class ActAutoChessModeType(IntEnum):
    """enum__Torappu_ActAutoChessModeType"""

    NONE = -1
    LOCAL = 0
    SINGLE = 1
    MULTI = 2


class ActAutoChessModeDifficultyType(IntEnum):
    """enum__Torappu_ActAutoChessModeDifficultyType"""

    NONE = -1
    TRAINING = 0
    FUNNY = 1
    NORMAL = 2
    HARD = 3
    ABYSS = 4
    FAST = 5


class ActAutoChessModeGroupType(IntEnum):
    """enum__Torappu_ActAutoChessModeGroupType"""

    GROUP_MULTI = 0
    GROUP_ROOM = 1
    GROUP_SINGLE = 2
    GROUP_FAST = 3
    GROUP_OFFSEASON = 4


class ActAutoChessMultiModeSubType(IntEnum):
    """enum__Torappu_ActAutoChessMultiModeSubType"""

    NONE = 0
    SOLO = 1
    TEAM = 2


class UITemplateShopTemplateShopDataTShopType(IntEnum):
    """enum__Torappu_UI_TemplateShop_TemplateShopData_TShopType"""

    NORMAL = 0
    SHOP_RARITY_GROUP = 1
    SHOP_PERIOD_UNLOCK = 2
    SHOP_MILESTONE_GROUP = 3
    SHOP_PORTRAIT_GROUP = 4


class UITemplateShopTemplateShopDataGoodType(IntEnum):
    """enum__Torappu_UI_TemplateShop_TemplateShopData_GoodType"""

    NORMAL = 0
    PROGRESS = 1


class AutoChessBandType(IntEnum):
    """enum__Torappu_AutoChessBandType"""

    NONE = 0
    GENERAL = 1
    BONDRELEVANT = 2


class ActAutoChessBondActiveConditionType(IntEnum):
    """enum__Torappu_ActAutoChessBondActiveConditionType"""

    BOARD = 0
    BOARD_AND_DECK = 1
    DECK = 2
    BOARD_ALL_CHESS = 3


class ActAutoChessBondActiveType(IntEnum):
    """enum__Torappu_ActAutoChessBondActiveType"""

    BATTLE = 0
    ALL = 1
    MANI = 2


class ActAutoChessBondPhaseType(IntEnum):
    """enum__Torappu_ActAutoChessBondPhaseType"""

    NONE = 0
    PEOPLE_COUNT = 1
    STACK_COUNT = 2


class AutoChessEffectType(IntEnum):
    """enum__Torappu_AutoChessEffectType"""

    NONE = 0
    BAND_INITIAL = 1
    ENEMY = 2
    ENEMY_TEMPORARY = 3
    ALLY = 4
    EQUIP = 5
    MAGIC = 6
    CHAR_MAP = 7
    BOND = 8
    ENEMY_GAIN = 9
    BUFF_GAIN = 10
    GARRISON = 11
    BAND_SKILL = 12


class AutoChessEffectCounterType(IntEnum):
    """enum__Torappu_AutoChessEffectCounterType"""

    NONE = 0
    TURN_COUNT = 1
    TRIGGER_COUNT = 2
    CHAR_COUNT = 3
    STACK_COUNT = 4
    COIN_JAR = 5


class AutoChessSkillType(IntEnum):
    """enum__Torappu_AutoChessSkillType"""

    NONE = 0
    PASSIVE = 1
    ACTIVE = 2


class AutoChessSkillAvailType(IntEnum):
    """enum__Torappu_AutoChessSkillAvailType"""

    DEFAULT = 0
    ROUND_RESET = 1
    ALL_LIMIT = 2
    COOLDOWN = 3


class AutoChessChessType(IntEnum):
    """enum__Torappu_AutoChessChessType"""

    NORMAL = 0
    DIY = 1
    PRESET = 2


class AutoChessItemType(IntEnum):
    """enum__Torappu_AutoChessItemType"""

    CHAR = 0
    EQUIP = 1
    MAGIC = 2
    TOKEN = 3


class AutoChessEffectChoiceType(IntEnum):
    """enum__Torappu_AutoChessEffectChoiceType"""

    EQUIP_FREE = 0
    EQUIP_PAID = 1
    BOUNTY_HUNT = 2
    BUFF_SELECT = 3
    PERSONAL_CHOOSE = 4
    SKILL_CHANGE = 5


class AutoChessSelectionType(IntEnum):
    """enum__Torappu_AutoChessSelectionType"""

    ROBIN = 0
    SHARED = 1


class AutoChessBondType(IntEnum):
    """enum__Torappu_AutoChessBondType"""

    NONE = 0
    REGULAR = 1
    SEASON = 2


class ArkdexModeType(IntEnum):
    """enum__Torappu_ArkdexModeType"""

    NONE = 0
    ARKDEX_DUEL_SINGLEROUND = 1
    ARKDEX_DUEL_BO3 = 2
    ARKDEX_DUEL_4PLAYER = 3


class ArkDexNpcTileStrategy(IntEnum):
    """enum__Torappu_ArkDexNpcTileStrategy"""

    RANDOM = 0
    PREFER_NEAR_SELF = 1
    PREFER_FAR_SELF = 2
    RANGED_NEAR_MELEE_FAR = 3
    PREFER_MIDDLE = 4
    RANDOM_FROM_ALL = 5


class ArkDexNpcCardStrategy(IntEnum):
    """enum__Torappu_ArkDexNpcCardStrategy"""

    RANDOM = 0
    FIXED_ORDER = 1
    PREFER_ELEMENT_0 = 2
    PREFER_ELEMENT_1 = 3
    PREFER_ELEMENT_2 = 4
    PREFER_RANGED = 5
    PREFER_RARITY = 6
    COUNTER_PLAYER_MAJOR = 7
    COUNTERED_BY_PLAYER_MAJOR = 8
    BAG_MIN_ELEMENT = 9
    BAG_MAX_ELEMENT = 10
    RANDOM_FROM_ALL = 11


class ArkventRangeType(IntEnum):
    """enum__Torappu_ArkventRangeType"""

    NONE = 0
    CIRCLE = 1
    RECT = 2


class ActArkHubModuleType(IntEnum):
    """enum__Torappu_ActArkHubModuleType"""

    NONE = 0
    ARKDEX = 1
    ARKPIXEL = 2


class ActArkHubActorType(IntEnum):
    """enum__Torappu_ActArkHubActorType"""

    FURNI = 0
    LOGIN_REWARDS = 1
    ARKDEX_DUEL = 2
    ARKDEX_PLAYER = 3


class ArkventSpineFaceType(IntEnum):
    """enum__Torappu_ArkventSpineFaceType"""

    RIGHT = 0
    LEFT = 1


class ActArkHubMenuType(IntEnum):
    """enum__Torappu_ActArkHubMenuType"""

    NONE = 0
    INVITE_FRIEND = 1
    MESSAGE = 2
    SETTING = 3
    ARKDEX_CREATURE = 4
    ARKDEX_ITEM = 5
    ARKDEX_ALBUM = 6
    ARKPIXEL = 7
    ARKDEX_TRADE = 8


class SpineFlipMode(IntEnum):
    """enum__Torappu_SpineFlipMode"""

    INPUT = 0
    VELOCITY = 1


class EasingType(IntEnum):
    """enum__Torappu_EasingType"""

    INSTANT = 0
    LINEAR = 1
    EASE_IN = 2
    EASE_OUT = 3
    EASE_IN_OUT = 4
    EXPONENTIAL = 5


class TurningMode(IntEnum):
    """enum__Torappu_TurningMode"""

    INSTANT = 0
    MOMENTUM = 1


class ActArkHubNameCardState(IntEnum):
    """enum__Torappu_ActArkHubNameCardState"""

    NONE = -1
    BATTLE = 0
    CAPTURE = 1
    MATCH = 2
    PIXEL = 3
    INTERACT = 4


class ActArkHubItemType(IntEnum):
    """enum__Torappu_ActArkHubItemType"""

    NONE = 0
    ACTIVITY_COIN = 1
    COIN = 2
    ARKDEX = 3
    PIXEL = 4


class ActivityThemeType(IntEnum):
    """enum__Torappu_ActivityThemeType"""

    NONE = 0
    ACTIVITY = 1
    CRISIS = 2
    MAINLINE = 3
    ROGUELIKE = 4
    CRISISV2 = 5
    SANDBOX_PERM = 6
    ACTIVITY_COMP = 7


class AppearanceStyle(IntEnum):
    """enum__Torappu_AppearanceStyle"""

    MAIN_NORMAL = 0
    MAIN_PREDEFINED = 1
    SUB = 2
    TRAINING = 3
    HIGH_DIFFICULTY = 4
    MIST_OPS = 5
    SPECIAL_STORY = 6


class LevelDataDifficulty(IntEnum):
    """enum__Torappu_LevelData_Difficulty"""

    NONE = 0
    NORMAL = 1
    FOUR_STAR = 2
    EASY = 4
    SIX_STAR = 8
    ALL = 15


class Act4funStageAttributeType(IntEnum):
    """enum__Torappu_Act4funStageAttributeType"""

    POS = 0
    NEG = 1


class Act4funSuperChatType(IntEnum):
    """enum__Torappu_Act4funSuperChatType"""

    ROLLED = 0
    RELATED = 1


class NpcStrategy(IntEnum):
    """enum__Torappu_NpcStrategy"""

    DEFAULT = 0
    CHOOSE_WIN = 1
    CHOOSE_ODD = 2
    FOLLOW_FEWER = 3
    FOLLOW_MORE = 4


class Act6FunAchievementType(IntEnum):
    """enum__Torappu_Act6FunAchievementType"""

    NORMAL = 0
    EX = 1


class CartComponentsCartAccessoryType(IntEnum):
    """enum__Torappu_CartComponents_CartAccessoryType"""

    NONE = 0
    ROOF = 1
    HEADSTOCK = 2
    TRUNK = 3
    CAR_OS = 4


class CartComponentsCartAccessoryPos(IntEnum):
    """enum__Torappu_CartComponents_CartAccessoryPos"""

    NONE = 0
    ROOF = 1
    HEADSTOCK = 2
    TRUNK_01 = 3
    TRUNK_02 = 4
    CAR_OS_01 = 5
    CAR_OS_02 = 6


class SiracusaDataZoneUnlockType(IntEnum):
    """enum__Torappu_SiracusaData_ZoneUnlockType"""

    NONE = 0
    STAGE_UNLOCK = 1
    TASK_UNLOCK = 2


class SiracusaDataCardGainType(IntEnum):
    """enum__Torappu_SiracusaData_CardGainType"""

    NONE = 0
    STAGE_GAIN = 1
    TASK_GAIN = 2


class SiracusaDataTaskRingLogicType(IntEnum):
    """enum__Torappu_SiracusaData_TaskRingLogicType"""

    NONE = 0
    LINEAR = 1
    AND = 2
    OR = 3


class SiracusaDataTaskType(IntEnum):
    """enum__Torappu_SiracusaData_TaskType"""

    NONE = 0
    BATTLE = 1
    AVG = 2


class SiracusaDataNavigationType(IntEnum):
    """enum__Torappu_SiracusaData_NavigationType"""

    NONE = 0
    AVG = 1
    LEVEL = 2
    CHAR_CARD = 3


class FireworkDataFireworkDirectionType(IntEnum):
    """enum__Torappu_FireworkData_FireworkDirectionType"""

    TWO_DIR = 0
    FOUR_DIR = 1


class FireworkDataFireworkType(IntEnum):
    """enum__Torappu_FireworkData_FireworkType"""

    RED = 0
    BLUE = 1
    YELLOW = 2
    GREEN = 3


class Act1VHalfIdleItemType(IntEnum):
    """enum__Torappu_Act1VHalfIdleItemType"""

    NONE = 0
    LEVEL_EXP = 1
    SKILL_EXP = 2
    STRATEGY_POINT = 3
    ASC = 4
    GACHA = 5
    MODEL = 6
    ACTIVITY_ITEM = 7


class PlayerStageState(IntEnum):
    """enum__Torappu_PlayerStageState"""

    UNLOCKED = 0
    PLAYED = 1
    PASS = 2
    COMPLETE = 3


class FifthAnnivExploreValueType(IntEnum):
    """enum__Torappu_FifthAnnivExploreValueType"""

    TEAMVALUE_1 = 0
    TEAMVALUE_2 = 1
    TEAMVALUE_3 = 2


class Anniv7thDisplayNodeType(IntEnum):
    """enum__Torappu_Anniv7thDisplayNodeType"""

    LETTER = 0
    TYPE_WRITER = 1
    RECORD = 2
    SIGN = 3


class AutoChessPeriodType(IntEnum):
    """enum__Torappu_AutoChessPeriodType"""

    SEASON = 0
    OFFSEASON = 1
    SUSPENSION = 2


class AutoChessContentType(IntEnum):
    """enum__Torappu_AutoChessContentType"""

    NONE = 0
    BASIC = 1
    EXPAND = 2


class AutoChessPrepareStepType(IntEnum):
    """enum__Torappu_AutoChessPrepareStepType"""

    NONE = 0
    INFO_CHECK = 1
    BAND_CHECK = 2
    CUSTOM_CHECK = 3
    BATTLE_CHECK = 4


class AutoChessShopTokenDisplayType(IntEnum):
    """enum__Torappu_AutoChessShopTokenDisplayType"""

    DEFAULT = 0
    HIDDEN = 1


class AutoChessSkillTriggerType(IntEnum):
    """enum__Torappu_AutoChessSkillTriggerType"""

    ALWAYS = 0
    ON_TAKE_DAMAGE = 1
    ATTACK_RANGE_ENEMY = 2
    SKILL_RANGE_ENEMY = 3
    CUSTOM_RANGE_ENEMY = 4
    ATTACK_RANGE_ALLY = 5
    SKILL_RANGE_ALLY = 6
    CUSTOM_RANGE_ALLY = 7
    COMBAT_OR_ATTACK = 8
    GLOBAL_RANGE_ENEMY = 9
    AUTO_STOP = 10
    MLYSS_S = 11
    MARCIL_S2 = 12
    APHRIS_S3 = 13
    INVALID_IN_SKILL = 14


class AutoChessBroadcastType(IntEnum):
    """enum__Torappu_AutoChessBroadcastType"""

    NONE = 0
    GOLDEN_CHAR = 1
    SHOP_LEVEL = 2
    BOSS_HIT = 3
    CHAR_DAMAGE = 4
    CHAR_GIFT = 5
    BOND_EFFECT = 6
    GARRISON_EXECUTED = 7
    PERFECT_BATTLE = 8
    SKILL_EXECUTED = 9
    RESTORE_HEALTH = 10
    BAND_SKILL_FAILED = 11


class AutoChessSkinType(IntEnum):
    """enum__Torappu_AutoChessSkinType"""

    ACTIVITY = 0
    SPECIAL = 1


class ItemRarity(IntEnum):
    """enum__Torappu_ItemRarity"""

    TIER_1 = 0
    TIER_2 = 1
    TIER_3 = 2
    TIER_4 = 3
    TIER_5 = 4
    TIER_6 = 5
    E_NUM = 6


class AutoChessSkinVoicePackType(IntEnum):
    """enum__Torappu_AutoChessSkinVoicePackType"""

    NONE = 0
    SINGLE = 1
    MULTI = 2


class CharWordShowType(IntEnum):
    """enum__Torappu_CharWordShowType"""

    HOME_SHOW = 0
    HOME_PLACE = 1
    HOME_WAIT = 2
    GACHA = 3
    EVOLVE_ONE = 4
    EVOLVE_TWO = 5
    FOUR_STAR = 6
    THREE_STAR = 7
    TWO_STAR = 8
    LOSE = 9
    LEVEL_UP = 10
    SQUAD = 11
    SQUAD_FIRST = 12
    BATTLE_START = 13
    BATTLE_FACE_ENEMY = 14
    BATTLE_SELECT = 15
    BATTLE_PLACE = 16
    BATTLE_SKILL_1 = 17
    BATTLE_SKILL_2 = 18
    BATTLE_SKILL_3 = 19
    BATTLE_SKILL_4 = 20
    BUILDING_PLACE = 21
    BUILDING_DRAGGING = 22
    BUILDING_FAVOR_BUBBLE = 23
    BUILDING_TOUCHING = 24
    LOADING_PANEL = 25
    BIRTHDAY = 26
    NEW_YEAR = 27
    VALENT_DAY = 28
    DRAGON_BOAT_FESTIVAL = 29
    HALLOWEEN_DAY = 30
    CHRISMATS_DAY = 31
    GREETING = 32
    ANNIVERSARY = 33
    UNUSED = 34
    AUTOCHESS_GAME_START = 35
    AUTOCHESS_REST_NO_HP_LOSS = 36
    AUTOCHESS_REST_HP_LOSS = 37
    AUTOCHESS_REST_BOSS = 38
    AUTOCHESS_REST_HIDDEN_BOSS = 39
    AUTOCHESS_SAME_OPERATOR = 40
    AUTOCHESS_BUY_OPERATOR_LOW = 41
    AUTOCHESS_BUY_OPERATOR_HIGH = 42
    AUTOCHESS_SHOP_UPGRADE = 43
    AUTOCHESS_COUNTDOWN = 44
    AUTOCHESS_MERGE_TRIPLE = 45
    AUTOCHESS_ALLIANCE_LEVEL = 46
    AUTOCHESS_FREEZE = 47
    E_ALL = 48


class TemplateMissionBigRewardType(IntEnum):
    """enum__Torappu_TemplateMissionBigRewardType"""

    NONE = 0
    ILLUST_CHAR_REWARD = 1
    CUSTOM = 2
    PIC_REWARD = 3
    SKIN_REWARD = 4
    POINT_REWARD_LIST = 5


class TemplateMissionTitleType(IntEnum):
    """enum__Torappu_TemplateMissionTitleType"""

    COMMON = 0
    CUSTOM = 1


class TemplateMissionCoinInfoType(IntEnum):
    """enum__Torappu_TemplateMissionCoinInfoType"""

    COMMON = 0
    CUSTOM = 1


class StageUnlockParam(GameDataModel):
    """clz_Torappu_StageUnlockParam"""

    stage_id: str | None = None


class CharUnlockParam(GameDataModel):
    """clz_Torappu_CharUnlockParam"""

    char_id: str | None = None


class CommonAvailCheck(GameDataModel):
    """clz_Torappu_CommonAvailCheck"""

    start_ts: int = 0
    end_ts: int = 0
    type: str = "STAGECLEAR"
    rate: float = 0.0
    stage_unlock_param: StageUnlockParam | None = None
    char_unlock_param: CharUnlockParam | None = None


class ActivityTablePicGroup(GameDataModel):
    """clz_Torappu_ActivityTable_PicGroup"""

    sort_index: int = 0
    pic_id: str | None = None
    avail_check: CommonAvailCheck | None = None


class ActivityTableBasicData(GameDataModel):
    """clz_Torappu_ActivityTable_BasicData"""

    id: str | None = None
    type: str = "DEFAULT"
    display_type: str = "NONE"
    name: str | None = None
    start_time: int = 0
    end_time: int = 0
    reward_end_time: int = 0
    display_on_home: bool = False
    has_stage: bool = False
    template_shop_id: str | None = None
    medal_group_id: str | None = None
    ungrouped_medal_ids: list[str] | None = None
    is_replicate: bool = False
    need_fixed_sync: bool = False
    trap_domain_id: str | None = None
    rec_type: str = "SPECIAL"
    is_page_entry: bool = False
    is_magnify: bool = False
    pic_group: list[ActivityTablePicGroup] | None = None
    use_pic_group: bool = False


class ActivityTableHomeActivityConfig(GameDataModel):
    """clz_Torappu_ActivityTable_HomeActivityConfig"""

    act_id: str | None = None
    is_popup_after_checkin: bool = False
    show_top_bar_menu: bool = False
    act_top_bar_color: str | None = None
    act_top_bar_text: str | None = None


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


class DefaultZoneData(GameDataModel):
    """clz_Torappu_DefaultZoneData"""

    zone_id: str | None = None
    zone_index: str | None = None
    zone_name: str | None = None
    zone_desc: str | None = None
    item_drop_list: list[str] | None = None


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class DefaultShopData(GameDataModel):
    """clz_Torappu_DefaultShopData"""

    good_id: str | None = None
    slot_id: int = 0
    price: int = 0
    avail_count: int = 0
    override_name: str | None = None
    item: ItemBundle | None = None


class DefaultFirstData(GameDataModel):
    """clz_Torappu_DefaultFirstData"""

    zone_list: list[DefaultZoneData] | None = None
    shop_list: list[DefaultShopData] | None = None


class DefaultCheckInDataCheckInDailyInfo(GameDataModel):
    """clz_Torappu_DefaultCheckInData_CheckInDailyInfo"""

    item_list: list[ItemBundle] | None = None
    order: int = 0
    color: int = 0
    key_item: int = 0
    show_item_order: int = 0
    is_dyn_item: bool = False


class DefaultCheckInDataDynCheckInDailyInfo(GameDataModel):
    """clz_Torappu_DefaultCheckInData_DynCheckInDailyInfo"""

    question_desc: str | None = None
    pre_option: str | None = None
    option_list: list[str] | None = None
    show_day: int = 0
    sp_order_icon_id: str | None = None
    sp_order_desc: str | None = None
    sp_order_complete_desc: str | None = None


class DefaultCheckInDataOptionInfo(GameDataModel):
    """clz_Torappu_DefaultCheckInData_OptionInfo"""

    option_desc: str | None = None
    show_image_id_1: str | None = None
    show_image_id_2: str | None = None
    option_complete_desc: str | None = None
    is_start: bool = False


class DefaultCheckInDataDynamicCheckInConsts(GameDataModel):
    """clz_Torappu_DefaultCheckInData_DynamicCheckInConsts"""

    first_question_desc: str | None = None
    first_question_tips_desc: str | None = None
    expiration_desc: str | None = None
    first_question_confirm_desc: str | None = None


class DefaultCheckInDataDynamicCheckInData(GameDataModel):
    """clz_Torappu_DefaultCheckInData_DynamicCheckInData"""

    dyn_check_in_dict: dict[str, DefaultCheckInDataDynCheckInDailyInfo] | None = None
    dyn_option_dict: dict[str, DefaultCheckInDataOptionInfo] | None = None
    dyn_item_dict: dict[str, list[ItemBundle]] | None = None
    const_data: DefaultCheckInDataDynamicCheckInConsts | None = None
    init_option: str | None = None


class DefaultCheckInDataExtraCheckinDailyInfo(GameDataModel):
    """clz_Torappu_DefaultCheckInData_ExtraCheckinDailyInfo"""

    order: int = 0
    blessing: str | None = None
    absolut_data: int = 0
    ad_tip: str | None = None
    relative_data: int = 0
    item_list: list[ItemBundle] | None = None


class DefaultCheckInData(GameDataModel):
    """clz_Torappu_DefaultCheckInData"""

    check_in_list: dict[int, DefaultCheckInDataCheckInDailyInfo] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    dyn_check_in_data: DefaultCheckInDataDynamicCheckInData | None = None
    extra_checkin_list: list[DefaultCheckInDataExtraCheckinDailyInfo] | None = None


class AllPlayerCheckinDataDailyInfo(GameDataModel):
    """clz_Torappu_AllPlayerCheckinData_DailyInfo"""

    item_list: list[ItemBundle] | None = None
    order: int = 0
    key_item: bool = False
    show_item_order: int = 0


class AllPlayerCheckinDataPublicBehaviour(GameDataModel):
    """clz_Torappu_AllPlayerCheckinData_PublicBehaviour"""

    sort_id: int = 0
    all_behavior_id: str | None = None
    display_order: int = 0
    all_behavior_desc: str | None = None
    requiring_value: int = 0
    require_repeat_completion: bool = False
    reward_received_desc: str | None = None
    rewards: list[ItemBundle] | None = None


class AllPlayerCheckinDataPersonalBehaviour(GameDataModel):
    """clz_Torappu_AllPlayerCheckinData_PersonalBehaviour"""

    sort_id: int = 0
    personal_behavior_id: str | None = None
    display_order: int = 0
    require_repeat_completion: bool = False
    desc: str | None = None


class AllPlayerCheckinDataConstData(GameDataModel):
    """clz_Torappu_AllPlayerCheckinData_ConstData"""

    character_name: str | None = None
    skin_name: str | None = None


class AllPlayerCheckinData(GameDataModel):
    """clz_Torappu_AllPlayerCheckinData"""

    check_in_list: dict[int, AllPlayerCheckinDataDailyInfo] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    pub_bhvs: dict[str, AllPlayerCheckinDataPublicBehaviour] | None = None
    personal_bhvs: dict[str, AllPlayerCheckinDataPersonalBehaviour] | None = None
    const_data: AllPlayerCheckinDataConstData | None = None


class VersusCheckInDataDailyInfo(GameDataModel):
    """clz_Torappu_VersusCheckInData_DailyInfo"""

    reward_list: list[ItemBundle] | None = None
    order: int = 0


class VersusCheckInDataVoteData(GameDataModel):
    """clz_Torappu_VersusCheckInData_VoteData"""

    pl_sweet_num: int = 0
    pl_salty_num: int = 0
    pl_taste: int = 0


class VersusCheckInDataTasteInfoData(GameDataModel):
    """clz_Torappu_VersusCheckInData_TasteInfoData"""

    pl_taste: int = 0
    taste_type: str = "DRAW"
    taste_text: str | None = None


class VersusCheckInDataTasteRewardData(GameDataModel):
    """clz_Torappu_VersusCheckInData_TasteRewardData"""

    taste_type: str = "DRAW"
    reward_item: ItemBundle | None = None


class VersusCheckInData(GameDataModel):
    """clz_Torappu_VersusCheckInData"""

    check_in_dict: dict[int, VersusCheckInDataDailyInfo] | None = None
    vote_taste_list: list[VersusCheckInDataVoteData] | None = None
    taste_info_dict: dict[int, VersusCheckInDataTasteInfoData] | None = None
    taste_reward_dict: dict[str, VersusCheckInDataTasteRewardData] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    versus_total_days: int = 0
    rule_text: str | None = None


class Act3D0DataCampBasicInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_CampBasicInfo"""

    camp_id: str | None = None
    camp_name: str | None = None
    camp_desc: str | None = None
    reward_desc: str | None = None


class Act3D0DataLimitedPoolDetailInfoPoolItemInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_LimitedPoolDetailInfo_PoolItemInfo"""

    good_id: str | None = None
    item_info: ItemBundle | None = None
    good_type: str = "NORMAL"
    per_count: int = 0
    total_count: int = 0
    weight: int = 0
    type: str | None = None
    order_id: int = 0


class Act3D0DataLimitedPoolDetailInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_LimitedPoolDetailInfo"""

    pool_id: str | None = None
    pool_item_info: list[Act3D0DataLimitedPoolDetailInfoPoolItemInfo] | None = None


class Act3D0DataInfinitePoolDetailInfoPoolItemInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_InfinitePoolDetailInfo_PoolItemInfo"""

    good_id: str | None = None
    good_type: str = "NORMAL"
    item_info: ItemBundle | None = None
    per_count: int = 0
    weight: int = 0
    type: str | None = None
    order_id: int = 0


class Act3D0DataInfinitePoolDetailInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_InfinitePoolDetailInfo"""

    pool_id: str | None = None
    pool_item_info: list[Act3D0DataInfinitePoolDetailInfoPoolItemInfo] | None = None


class Act3D0DataInfinitePoolPercent(GameDataModel):
    """clz_Torappu_Act3D0Data_InfinitePoolPercent"""

    percent_dict: dict[str, int] | None = None


class Act3D0DataCampItemMapInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_CampItemMapInfo"""

    good_id: str | None = None
    item_dict: dict[str, ItemBundle] | None = None


class Act3D0DataClueInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_ClueInfo"""

    item_id: str | None = None
    camp_id: str | None = None
    order_id: int = 0
    image_id: str | None = None


class Act3D0DataMileStoneInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_MileStoneInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    mile_stone_type: str = "NORMAL"
    normal_item: ItemBundle | None = None
    special_item_dict: dict[str, ItemBundle] | None = None
    token_num: int = 0


class Act3D0DataGachaBoxInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_GachaBoxInfo"""

    gacha_box_id: str | None = None
    box_type: str = "LIMITED"
    key_good_id: str | None = None
    token_id: ItemBundle | None = None
    token_num_once: int = 0
    unlock_img: str | None = None
    next_gacha_box_info_id: str | None = None


class Act3D0DataCampInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_CampInfo"""

    camp_id: str | None = None
    camp_chinese_name: str | None = None


class Act3D0DataZoneDescInfo(GameDataModel):
    """clz_Torappu_Act3D0Data_ZoneDescInfo"""

    zone_id: str | None = None
    locked_text: str | None = None


class CommonFavorUpInfo(GameDataModel):
    """clz_Torappu_CommonFavorUpInfo"""

    char_id: str | None = None
    display_start_time: int = 0
    display_end_time: int = 0


class Act3D0Data(GameDataModel):
    """clz_Torappu_Act3D0Data"""

    camp_basic_info: dict[str, Act3D0DataCampBasicInfo] | None = None
    limited_pool_list: dict[str, Act3D0DataLimitedPoolDetailInfo] | None = None
    infinite_pool_list: dict[str, Act3D0DataInfinitePoolDetailInfo] | None = None
    infinite_percent: dict[str, Act3D0DataInfinitePoolPercent] | None = None
    camp_item_map_info: dict[str, Act3D0DataCampItemMapInfo] | None = None
    clue_info: dict[str, Act3D0DataClueInfo] | None = None
    mile_stone_info: list[Act3D0DataMileStoneInfo] | None = None
    mile_stone_token_id: str | None = None
    coin_token_id: str | None = None
    et_token_id: str | None = None
    gacha_box_info: list[Act3D0DataGachaBoxInfo] | None = None
    camp_info: dict[str, Act3D0DataCampInfo] | None = None
    zone_desc: dict[str, Act3D0DataZoneDescInfo] | None = None
    favor_up_list: dict[str, CommonFavorUpInfo] | None = None


class Act4D0DataMileStoneItemInfo(GameDataModel):
    """clz_Torappu_Act4D0Data_MileStoneItemInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    item: ItemBundle | None = None


class Act4D0DataMileStoneStoryInfo(GameDataModel):
    """clz_Torappu_Act4D0Data_MileStoneStoryInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    story_key: str | None = None
    desc: str | None = None


class Act4D0DataStoryInfo(GameDataModel):
    """clz_Torappu_Act4D0Data_StoryInfo"""

    story_key: str | None = None
    story_id: str | None = None
    story_sort: str | None = None
    story_name: str | None = None
    lock_desc: str | None = None
    story_desc: str | None = None


class Act4D0DataStageJumpInfo(GameDataModel):
    """clz_Torappu_Act4D0Data_StageJumpInfo"""

    stage_key: str | None = None
    zone_id: str | None = None
    stage_id: str | None = None
    unlock_desc: str | None = None
    lock_desc: str | None = None


class Act4D0Data(GameDataModel):
    """clz_Torappu_Act4D0Data"""

    mile_stone_item_list: list[Act4D0DataMileStoneItemInfo] | None = None
    mile_stone_story_list: list[Act4D0DataMileStoneStoryInfo] | None = None
    story_info_list: list[Act4D0DataStoryInfo] | None = None
    stage_info: list[Act4D0DataStageJumpInfo] | None = None
    token_item: ItemBundle | None = None
    char_stone_id: str | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    extra_drop_zones: list[str] | None = None


class MileStoneInfo(GameDataModel):
    """clz_Torappu_MileStoneInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    mile_stone_type: str = "NORMAL"
    normal_item: ItemBundle | None = None
    is_bonus: int = Field(default=0, alias="IsBonus")


class Act5D0DataZoneDescInfo(GameDataModel):
    """clz_Torappu_Act5D0Data_ZoneDescInfo"""

    zone_id: str | None = None
    locked_text: str | None = None


class Act5D0DataMissionExtraInfo(GameDataModel):
    """clz_Torappu_Act5D0Data_MissionExtraInfo"""

    difficult_level: int = 0
    level_desc: str | None = None
    sort_id: int = 0


class Act5D0Data(GameDataModel):
    """clz_Torappu_Act5D0Data"""

    mile_stone_info: list[MileStoneInfo] | None = None
    mile_stone_token_id: str | None = None
    zone_desc: dict[str, Act5D0DataZoneDescInfo] | None = None
    mission_extra_list: dict[str, Act5D0DataMissionExtraInfo] | None = None
    sp_reward: str | None = None


class Act5D1DataRuneStageData(GameDataModel):
    """clz_Torappu_Act5D1Data_RuneStageData"""

    stage_id: str | None = None
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None
    description: str | None = None
    pic_id: str | None = None


class Act5D1DataRuneRecurrentStateData(GameDataModel):
    """clz_Torappu_Act5D1Data_RuneRecurrentStateData"""

    rune_re_id: str | None = None
    stage_id: str | None = None
    slot_id: int = 0
    start_time: int = 0
    end_time: int = 0
    rune_list: list[str] | None = None
    is_avail: bool = False
    warning_point: int = 0


class Act5D1DataRuneUnlockData(GameDataModel):
    """clz_Torappu_Act5D1Data_RuneUnlockData"""

    rune_id: str | None = None
    price_item: ItemBundle | None = None
    rune_name: str | None = None
    bg_pic: str | None = None
    rune_desc: str | None = None
    sort_id: int = 0
    icon_id: str | None = None


class Act5D1DataRuneReleaseData(GameDataModel):
    """clz_Torappu_Act5D1Data_RuneReleaseData"""

    rune_id: str | None = None
    stage_id: str | None = None
    release_time: int = 0


class Act5D1DataShopGood(GameDataModel):
    """clz_Torappu_Act5D1Data_ShopGood"""

    good_id: str | None = None
    slot_id: int = 0
    price: int = 0
    avail_count: int = 0
    item: ItemBundle | None = None
    progress_good_id: str | None = None
    good_type: str = "NORMAL"
    rarity: str | None = None


class Act5D1DataProgessGoodItem(GameDataModel):
    """clz_Torappu_Act5D1Data_ProgessGoodItem"""

    order: int = 0
    price: int = 0
    display_name: str | None = None
    item: ItemBundle | None = None


class Act5D1DataShopData(GameDataModel):
    """clz_Torappu_Act5D1Data_ShopData"""

    shop_goods: dict[str, Act5D1DataShopGood] | None = None
    progress_goods: dict[str, list[Act5D1DataProgessGoodItem]] | None = None


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


class RuneTablePackedRuneData(GameDataModel):
    """clz_Torappu_RuneTable_PackedRuneData"""

    id: str | None = None
    points: float = 0.0
    mutex_group_key: str | None = None
    description: str | None = None
    runes: list[RuneData] | None = None


class RuneTableRuneStageExtraData(GameDataModel):
    """clz_Torappu_RuneTable_RuneStageExtraData"""

    stage_id: str | None = None
    runes: list[RuneTablePackedRuneData] | None = None


class Act5D1Data(GameDataModel):
    """clz_Torappu_Act5D1Data"""

    stage_common_data: list[Act5D1DataRuneStageData] | None = None
    rune_stage_data: list[Act5D1DataRuneRecurrentStateData] | None = None
    rune_unlock_dict: dict[str, list[Act5D1DataRuneUnlockData]] | None = None
    rune_release_data: list[Act5D1DataRuneReleaseData] | None = None
    mission_data: list[MissionData] | None = None
    mission_group: list[MissionGroup] | None = None
    use_benefit_mission_dict: dict[str, bool] | None = None
    shop_data: Act5D1DataShopData | None = None
    coin_item_id: str | None = None
    pt_item_id: str | None = None
    stage_rune: list[RuneTableRuneStageExtraData] | None = None
    show_rune_mission_list: list[str] | None = None


class ActivityCollectionDataCollectionInfo(GameDataModel):
    """clz_Torappu_ActivityCollectionData_CollectionInfo"""

    id: int = 0
    item_type: str = "NONE"
    item_id: str | None = None
    item_cnt: int = 0
    point_id: str | None = None
    point_cnt: int = 0
    is_bonus: bool = False
    png_name: str | None = None
    png_sort: int = 0
    is_show: bool = False
    show_in_list: bool = False
    show_icon_bg: bool = Field(default=False, alias="showIconBG")
    is_bonus_show: bool = False


class ActivityCollectionDataConsts(GameDataModel):
    """clz_Torappu_ActivityCollectionData_Consts"""

    show_jump_btn: bool = False
    jump_btn_type: str = "NONE"
    jump_btn_param_1: str | None = None
    jump_btn_param_2: str | None = None
    daily_task_disabled: bool = False
    daily_task_start_time: int = 0
    is_simple_mode: bool = False


class ActivityCollectionData(GameDataModel):
    """clz_Torappu_ActivityCollectionData"""

    collections: list[ActivityCollectionDataCollectionInfo] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    consts: ActivityCollectionDataConsts | None = None


class Act9D0DataZoneDescInfo(GameDataModel):
    """clz_Torappu_Act9D0Data_ZoneDescInfo"""

    zone_id: str | None = None
    unlock_text: str | None = None
    display_start_time: int = 0


class Act9D0DataFavorUpInfo(GameDataModel):
    """clz_Torappu_Act9D0Data_FavorUpInfo"""

    char_id: str | None = None
    display_start_time: int = 0
    display_end_time: int = 0


class Act9D0DataSubMissionInfo(GameDataModel):
    """clz_Torappu_Act9D0Data_SubMissionInfo"""

    mission_id: str | None = None
    mission_title: str | None = None
    sort_id: int = 0
    mission_index: str | None = None


class Act9D0DataActivityNewsStyleInfo(GameDataModel):
    """clz_Torappu_Act9D0Data_ActivityNewsStyleInfo"""

    type_id: str | None = None
    type_name: str | None = None
    type_logo: str | None = None
    type_main_logo: str | None = None


class Act9D0DataActivityNewsLine(GameDataModel):
    """clz_Torappu_Act9D0Data_ActivityNewsLine"""

    line_type: str = "TextContent"
    content: str | None = None


class Act9D0DataActivityNewsInfo(GameDataModel):
    """clz_Torappu_Act9D0Data_ActivityNewsInfo"""

    news_id: str | None = None
    news_sort_id: int = 0
    style_info: Act9D0DataActivityNewsStyleInfo | None = None
    preposed_stage: str | None = None
    title_pic: str | None = None
    news_title: str | None = None
    news_inf_show: int = 0
    news_from: str | None = None
    news_text: str | None = None
    news_param_1: int = 0
    news_param_2: int = 0
    news_param_3: float = 0.0
    news_lines: list[Act9D0DataActivityNewsLine] | None = None


class Act9D0DataActivityNewsServerInfo(GameDataModel):
    """clz_Torappu_Act9D0Data_ActivityNewsServerInfo"""

    news_id: str | None = None
    preposed_stage: str | None = None


class Act9D0DataAct9D0ConstData(GameDataModel):
    """clz_Torappu_Act9D0Data_Act9D0ConstData"""

    campaign_enemy_cnt: int = 0
    campaign_stage_id: str | None = None


class Act9D0Data(GameDataModel):
    """clz_Torappu_Act9D0Data"""

    token_item_id: str | None = None
    zone_desc_list: dict[str, Act9D0DataZoneDescInfo] | None = None
    favor_up_list: dict[str, Act9D0DataFavorUpInfo] | None = None
    sub_mission_info: dict[str, Act9D0DataSubMissionInfo] | None = None
    has_sub_mission: bool = False
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    news_info_list: dict[str, Act9D0DataActivityNewsInfo] | None = None
    news_server_info_list: dict[str, Act9D0DataActivityNewsServerInfo] | None = None
    misc_hub: dict[str, str] | None = None
    const_data: Act9D0DataAct9D0ConstData | None = None


class Act12SideDataConstData(GameDataModel):
    """clz_Torappu_Act12SideData_ConstData"""

    recycle_reward_threshold: int = 0
    charm_repo_unlock_stage_id: str | None = None
    recycle_low_threshold: int = 0
    recycle_medium_threshold: int = 0
    recycle_high_threshold: int = 0
    auto_get_charm_id: str | None = None
    fog_stage_id: str | None = None
    fog_unlock_stage_id: str | None = None
    fog_unlock_ts: int = 0
    fog_unlock_desc: str | None = None


class Act12SideDataZoneAdditionData(GameDataModel):
    """clz_Torappu_Act12SideData_ZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None
    zone_class: str = "NONE"


class Act12SideDataMissionDescInfo(GameDataModel):
    """clz_Torappu_Act12SideData_MissionDescInfo"""

    zone_class: str = "NONE"
    special_mission_desc: str | None = None
    need_lock: bool = False
    unlock_hint: str | None = None
    unlock_stage: str | None = None


class Act12SideDataMileStoneInfo(GameDataModel):
    """clz_Torappu_Act12SideData_MileStoneInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    item: ItemBundle | None = None
    is_precious: bool = False
    mile_stone_stage: int = 0


class Act12SideDataPhotoInfo(GameDataModel):
    """clz_Torappu_Act12SideData_PhotoInfo"""

    pic_id: str | None = None
    pic_name: str | None = None
    mile_stone_id: str | None = None
    pic_desc: str | None = None
    jump_stage_id: str | None = None


class Act12SideDataRecycleDialogData(GameDataModel):
    """clz_Torappu_Act12SideData_RecycleDialogData"""

    dialog_type: str = "NONE"
    dialog: str | None = None
    dialog_express: str = "NONE"


class Act12SideData(GameDataModel):
    """clz_Torappu_Act12SideData"""

    const_data: Act12SideDataConstData | None = None
    zone_addition_data_list: list[Act12SideDataZoneAdditionData] | None = None
    mission_desc_list: dict[str, Act12SideDataMissionDescInfo] | None = None
    mile_stone_info_list: list[Act12SideDataMileStoneInfo] | None = None
    photo_list: dict[str, Act12SideDataPhotoInfo] | None = None
    recycle_dialog_dict: dict[str, list[Act12SideDataRecycleDialogData]] | None = None


class Act13SideDataConstData(GameDataModel):
    """clz_Torappu_Act13SideData_ConstData"""

    prestige_desc_list: list[str] | None = None
    daily_random_count: list[list[int]] | None = None
    daily_weight_initial: int = 0
    daily_weight_complete: int = 0
    agenda_recover: int = 0
    agenda_max: int = 0
    agenda_hint: int = 0
    mission_pool_max: int = 0
    mission_board_max: int = 0
    item_random_list: list[ItemBundle] | None = None
    unlock_prestige_cond: str | None = None
    hot_spot_show_flag: int = 0


class Act13SideDataPrestigeData(GameDataModel):
    """clz_Torappu_Act13SideData_PrestigeData"""

    rank: str = "D"
    threshold: int = 0
    reward: ItemBundle | None = None
    news_count: int = 0
    archive_count: int = 0
    avg_count: int = 0


class Act13SideDataLongTermMissionGroupData(GameDataModel):
    """clz_Torappu_Act13SideData_LongTermMissionGroupData"""

    group_id: str | None = None
    group_name: str | None = None
    org_id: str | None = None
    mission_list: list[str] | None = None


class Act13SideDataOrgSectionData(GameDataModel):
    """clz_Torappu_Act13SideData_OrgSectionData"""

    section_name: str | None = None
    sort_id: int = 0
    group_data: Act13SideDataLongTermMissionGroupData | None = None


class Act13SideDataOrgData(GameDataModel):
    """clz_Torappu_Act13SideData_OrgData"""

    org_id: str | None = None
    org_name: str | None = None
    org_en_name: str | None = None
    open_time: int = 0
    principal_id_list: list[str] | None = None
    prestige_list: list[Act13SideDataPrestigeData] | None = None
    agenda_count_2_prestige_item_map: dict[int, ItemBundle] | None = None
    org_section_list: list[Act13SideDataOrgSectionData] | None = None
    prestige_item: ItemBundle | None = None


class Act13SideDataPrincipalData(GameDataModel):
    """clz_Torappu_Act13SideData_PrincipalData"""

    principal_id: str | None = None
    principal_name: str | None = None
    principal_en_name: str | None = None
    avg_char_id: str | None = None
    principal_desc_list: list[str] | None = None


class Act13SideDataLongTermMissionData(GameDataModel):
    """clz_Torappu_Act13SideData_LongTermMissionData"""

    mission_name: str | None = None
    group_id: str | None = None
    principal_id: str | None = None
    finished_desc: str | None = None
    section_sort_id: int = 0
    have_stage_btn: bool = False
    jump_stage_id: str | None = None


class Act13SideDataDailyMissionData(GameDataModel):
    """clz_Torappu_Act13SideData_DailyMissionData"""

    id: str | None = None
    sort_id: int = 0
    description: str | None = None
    mission_name: str | None = None
    template: str | None = None
    template_type: str | None = None
    param: list[str] | None = None
    rewards: list[MissionDisplayRewards] | None = None
    org_pool: list[str] | None = None
    reward_pool: list[str] | None = None
    jump_stage_id: str | None = None
    agenda_count: int = 0


class Act13SideDataDailyMissionRewardGroupData(GameDataModel):
    """clz_Torappu_Act13SideData_DailyMissionRewardGroupData"""

    group_id: str | None = None
    rewards: list[ItemBundle] | None = None


class Act13SideDataArchiveItemUnlockData(GameDataModel):
    """clz_Torappu_Act13SideData_ArchiveItemUnlockData"""

    item_id: str | None = None
    item_type: str = "NONE"
    unlock_condition: str = "NONE"
    param_1: str | None = None
    param_2: str | None = None


class ActivityTableActHiddenAreaPreposeStageData(GameDataModel):
    """clz_Torappu_ActivityTable_ActHiddenAreaPreposeStageData"""

    stage_id: str | None = None
    unlock_rank: str = "ERR_ZERO"


class ActivityTableActivityHiddenAreaData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityHiddenAreaData"""

    name: str | None = None
    desc: str | None = None
    preposed_stage: list[ActivityTableActHiddenAreaPreposeStageData] | None = None
    preposed_time: int = 0


class Act13SideDataZoneAdditionData(GameDataModel):
    """clz_Torappu_Act13SideData_ZoneAdditionData"""

    unlock_text: str | None = None
    zone_class: str = "NONE"


class Act13SideData(GameDataModel):
    """clz_Torappu_Act13SideData"""

    const_data: Act13SideDataConstData | None = None
    org_data_map: dict[str, Act13SideDataOrgData] | None = None
    principal_data_map: dict[str, Act13SideDataPrincipalData] | None = None
    long_term_mission_data_map: dict[str, Act13SideDataLongTermMissionData] | None = (
        None
    )
    daily_mission_data_list: list[Act13SideDataDailyMissionData] | None = None
    daily_reward_group_data_map: (
        dict[str, Act13SideDataDailyMissionRewardGroupData] | None
    ) = None
    archive_item_unlock_data: dict[str, Act13SideDataArchiveItemUnlockData] | None = (
        None
    )
    hidden_area_data: dict[str, ActivityTableActivityHiddenAreaData] | None = None
    zone_addtion_data_map: dict[str, Act13SideDataZoneAdditionData] | None = None


class Act17sideDataPlaceData(GameDataModel):
    """clz_Torappu_Act17sideData_PlaceData"""

    place_id: str | None = None
    place_desc: str | None = None
    lock_event_id: str | None = None
    zone_id: str | None = None
    visible_cond_type: str | None = None
    visible_params: list[str] | None = None


class Act17sideDataNodeInfoData(GameDataModel):
    """clz_Torappu_Act17sideData_NodeInfoData"""

    node_id: str | None = None
    node_type: str = "LANDMARK"
    sort_id: int = 0
    place_id: str | None = None
    is_point_place: bool = False
    chapter_id: str | None = None
    track_point_type: str = "NONE"
    unlock_cond_type: str | None = None
    unlock_params: list[str] | None = None


class Act17sideDataLandmarkNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_LandmarkNodeData"""

    node_id: str | None = None
    landmark_id: str | None = None
    landmark_name: str | None = None
    landmark_pic: str | None = None
    landmark_special_pic: str | None = None
    landmark_des_list: list[str] | None = None


class Act17sideDataStoryNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_StoryNodeData"""

    node_id: str | None = None
    story_id: str | None = None
    story_key: str | None = None
    story_name: str | None = None
    story_pic: str | None = None
    confirm_des: str | None = None
    story_des_list: list[str] | None = None


class Act17sideDataBattleNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_BattleNodeData"""

    node_id: str | None = None
    stage_id: str | None = None


class Act17sideDataTreasureNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_TreasureNodeData"""

    node_id: str | None = None
    treasure_id: str | None = None
    treasure_name: str | None = None
    treasure_pic: str | None = None
    treasure_special_pic: str | None = None
    end_event_id: str | None = None
    confirm_des: str | None = None
    treasure_des_list: list[str] | None = None
    mission_id_list: list[str] | None = None
    reward_list: list[ItemBundle] | None = None
    treasure_type: str = "SMALL"


class Act17sideDataEventNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_EventNodeData"""

    node_id: str | None = None
    event_id: str | None = None
    end_event_id: str | None = None


class Act17sideDataTechNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_TechNodeData"""

    node_id: str | None = None
    tech_tree_id: str | None = None
    tech_tree_name: str | None = None
    tech_pic: str | None = None
    tech_special_pic: str | None = None
    end_event_id: str | None = None
    confirm_des: str | None = None
    tech_des_list: list[str] | None = None
    mission_id_list: list[str] | None = None


class Act17sideDataChoiceNodeOptionData(GameDataModel):
    """clz_Torappu_Act17sideData_ChoiceNodeOptionData"""

    can_repeat: bool = False
    event_id: str | None = None
    des: str | None = None
    unlock_des: str | None = None
    unlock_cond_type: str | None = None
    unlock_params: list[str] | None = None


class Act17sideDataChoiceNodeData(GameDataModel):
    """clz_Torappu_Act17sideData_ChoiceNodeData"""

    node_id: str | None = None
    choice_pic: str | None = None
    is_disposable: bool = False
    choice_special_pic: str | None = None
    choice_name: str | None = None
    choice_des_list: list[str] | None = None
    cancel_des: str | None = None
    choice_num: int = 0
    option_list: list[Act17sideDataChoiceNodeOptionData] | None = None


class Act17sideDataEventData(GameDataModel):
    """clz_Torappu_Act17sideData_EventData"""

    event_id: str | None = None
    event_pic: str | None = None
    event_special_pic: str | None = None
    event_title: str | None = None
    event_des_list: list[str] | None = None


class Act17sideDataArchiveItemUnlockData(GameDataModel):
    """clz_Torappu_Act17sideData_ArchiveItemUnlockData"""

    item_id: str | None = None
    item_type: str = "NONE"
    unlock_condition: str = "NONE"
    node_id: str | None = None
    stage_param: str = "NONE"
    chapter_id: str | None = None


class Act17sideDataTechTreeData(GameDataModel):
    """clz_Torappu_Act17sideData_TechTreeData"""

    tech_tree_id: str | None = None
    sort_id: int = 0
    tech_tree_name: str | None = None
    default_branch_id: str | None = None
    lock_des: str | None = None


class Act17sideDataTechTreeBranchData(GameDataModel):
    """clz_Torappu_Act17sideData_TechTreeBranchData"""

    tech_tree_branch_id: str | None = None
    tech_tree_id: str | None = None
    tech_tree_branch_name: str | None = None
    tech_tree_branch_icon: str | None = None
    tech_tree_branch_desc: str | None = None
    rune_data: RuneTablePackedRuneData | None = None


class Act17sideDataMainlineChapterData(GameDataModel):
    """clz_Torappu_Act17sideData_MainlineChapterData"""

    chapter_id: str | None = None
    chapter_des: str | None = None
    chapter_icon: str = "NORMAL"
    unlock_des: str | None = None
    id: str | None = None


class Act17sideDataMainlineData(GameDataModel):
    """clz_Torappu_Act17sideData_MainlineData"""

    mainline_id: str | None = None
    node_id: str | None = None
    sort_id: int = 0
    mission_sort: str | None = None
    zone_id: str | None = None
    mainline_des: str | None = None
    focus_node_id: str | None = None


class Act17sideDataZoneData(GameDataModel):
    """clz_Torappu_Act17sideData_ZoneData"""

    zone_id: str | None = None
    unlock_place_id: str | None = None
    unlock_text: str | None = None


class Act17sideDataConstData(GameDataModel):
    """clz_Torappu_Act17sideData_ConstData"""

    tech_tree_unlock_event_id: str | None = None


class Act17sideData(GameDataModel):
    """clz_Torappu_Act17sideData"""

    place_data_map: dict[str, Act17sideDataPlaceData] | None = None
    node_info_data_map: dict[str, Act17sideDataNodeInfoData] | None = None
    landmark_node_data_map: dict[str, Act17sideDataLandmarkNodeData] | None = None
    story_node_data_map: dict[str, Act17sideDataStoryNodeData] | None = None
    battle_node_data_map: dict[str, Act17sideDataBattleNodeData] | None = None
    treasure_node_data_map: dict[str, Act17sideDataTreasureNodeData] | None = None
    event_node_data_map: dict[str, Act17sideDataEventNodeData] | None = None
    tech_node_data_map: dict[str, Act17sideDataTechNodeData] | None = None
    choice_node_data_map: dict[str, Act17sideDataChoiceNodeData] | None = None
    event_data_map: dict[str, Act17sideDataEventData] | None = None
    archive_item_unlock_data_map: (
        dict[str, Act17sideDataArchiveItemUnlockData] | None
    ) = None
    tech_tree_data_map: dict[str, Act17sideDataTechTreeData] | None = None
    tech_tree_branch_data_map: dict[str, Act17sideDataTechTreeBranchData] | None = None
    mainline_chapter_data_map: dict[str, Act17sideDataMainlineChapterData] | None = None
    mainline_data_map: dict[str, Act17sideDataMainlineData] | None = None
    zone_data_list: list[Act17sideDataZoneData] | None = None
    const_data: Act17sideDataConstData | None = None


class Act20SideDataResidentCartData(GameDataModel):
    """clz_Torappu_Act20SideData_ResidentCartData"""

    resident_pic: str | None = None


class Act20SideData(GameDataModel):
    """clz_Torappu_Act20SideData"""

    zone_addition_data_map: dict[str, str] | None = None
    resident_cart_datas: dict[str, Act20SideDataResidentCartData] | None = None


class Act21SideDataZoneAddtionData(GameDataModel):
    """clz_Torappu_Act21SideData_ZoneAddtionData"""

    zone_id: str | None = None
    unlock_text: str | None = None
    stage_unlock_text: str | None = None
    entry_id: str | None = None


class Act21SideDataConstData(GameDataModel):
    """clz_Torappu_Act21SideData_ConstData"""

    line_connect_zone: str | None = None


class Act21SideData(GameDataModel):
    """clz_Torappu_Act21SideData"""

    zone_addition_data_map: dict[str, Act21SideDataZoneAddtionData] | None = None
    const_data: Act21SideDataConstData | None = None


class ActivityLoginData(GameDataModel):
    """clz_Torappu_ActivityLoginData"""

    description: str | None = None
    item_list: list[ItemBundle] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None


class ActivitySwitchCheckinConstData(GameDataModel):
    """clz_Torappu_ActivitySwitchCheckinConstData"""

    activity_time: str | None = None
    activity_rule: str | None = None


class ActivitySwitchCheckinRewardItemShowData(GameDataModel):
    """clz_Torappu_ActivitySwitchCheckinRewardItemShowData"""

    item_bundle: ItemBundle | None = None
    is_main_reward: bool = False


class ActivitySwitchCheckinMainRewardShowData(GameDataModel):
    """clz_Torappu_ActivitySwitchCheckinMainRewardShowData"""

    main_reward_pic_id: str | None = None
    main_reward_name: str | None = None
    main_reward_count: int = 0
    has_tip: bool = False
    tip_item_bundle: ItemBundle | None = None


class ActivitySwitchCheckinRewardShowData(GameDataModel):
    """clz_Torappu_ActivitySwitchCheckinRewardShowData"""

    checkin_id: str | None = None
    rewards_title: str | None = None
    reward_show_item_datas: list[ActivitySwitchCheckinRewardItemShowData] | None = None
    main_reward_show_data: ActivitySwitchCheckinMainRewardShowData | None = None


class ActivitySwitchCheckinData(GameDataModel):
    """clz_Torappu_ActivitySwitchCheckinData"""

    const_data: ActivitySwitchCheckinConstData | None = None
    rewards: dict[str, list[ItemBundle]] | None = None
    reward_show_datas: dict[str, ActivitySwitchCheckinRewardShowData] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    sort_id_dict: dict[str, int] | None = None


class ActivityMiniStoryDataZoneDescInfo(GameDataModel):
    """clz_Torappu_ActivityMiniStoryData_ZoneDescInfo"""

    zone_id: str | None = None
    unlock_text: str | None = None


class ActivityMiniStoryDataFavorUpInfo(GameDataModel):
    """clz_Torappu_ActivityMiniStoryData_FavorUpInfo"""

    char_id: str | None = None
    display_start_time: int = 0
    display_end_time: int = 0


class ActivityMiniStoryData(GameDataModel):
    """clz_Torappu_ActivityMiniStoryData"""

    token_item_id: str | None = None
    zone_desc_list: dict[str, ActivityMiniStoryDataZoneDescInfo] | None = None
    favor_up_list: dict[str, ActivityMiniStoryDataFavorUpInfo] | None = None
    extra_drop_zone_list: list[str] | None = None


class ActivityRoguelikeDataOuterBuffUnlockInfo(GameDataModel):
    """clz_Torappu_ActivityRoguelikeData_OuterBuffUnlockInfo"""

    buff_level: int = 0
    name: str | None = None
    icon_id: str | None = None
    description: str | None = None
    usage: str | None = None
    item_id: str | None = None
    item_type: str = "NONE"
    cost: int = 0


class ActivityRoguelikeDataOuterBuffUnlockInfoData(GameDataModel):
    """clz_Torappu_ActivityRoguelikeData_OuterBuffUnlockInfoData"""

    buff_id: str | None = None
    buff_unlock_infos: dict[int, ActivityRoguelikeDataOuterBuffUnlockInfo] | None = None


class ActivityRoguelikeDataMileStoneItemInfo(GameDataModel):
    """clz_Torappu_ActivityRoguelikeData_MileStoneItemInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    item: ItemBundle | None = None


class ActivityTableCustomUnlockCond(GameDataModel):
    """clz_Torappu_ActivityTable_CustomUnlockCond"""

    act_id: str | None = None
    stage_id: str | None = None


class ActivityRoguelikeData(GameDataModel):
    """clz_Torappu_ActivityRoguelikeData"""

    out_buff_infos: dict[str, ActivityRoguelikeDataOuterBuffUnlockInfoData] | None = (
        None
    )
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    outer_buff_token: str | None = None
    shop_token: str | None = None
    relic_unlock_time: int = 0
    milestone_token_ratio: float = 0.0
    outer_buff_token_ratio: float = 0.0
    relic_token_ratio: float = 0.0
    relic_outer_buff_token_ratio: float = 0.0
    re_open_cool_down: int = 0
    token_item: ItemBundle | None = None
    char_stone_id: str | None = None
    milestone: list[ActivityRoguelikeDataMileStoneItemInfo] | None = None
    unlock_conds: list[ActivityTableCustomUnlockCond] | None = None


class ActivityInterlockDataStageAdditionData(GameDataModel):
    """clz_Torappu_ActivityInterlockData_StageAdditionData"""

    stage_id: str | None = None
    stage_type: str = "NONE"
    lock_stage_key: str | None = None
    lock_sort_index: int = 0


class ActivityInterlockDataTreasureMonsterData(GameDataModel):
    """clz_Torappu_ActivityInterlockData_TreasureMonsterData"""

    lock_stage_key: str | None = None
    enemy_id: str | None = None
    enemy_name: str | None = None
    enemy_icon: str | None = None
    enemy_description: str | None = None


class SharedCharDataSharedCharSkillData(GameDataModel):
    """clz_Torappu_SharedCharData_SharedCharSkillData"""

    skill_id: str | None = None
    specialize_level: int = 0


class SharedCharDataCharEquipInfo(GameDataModel):
    """clz_Torappu_SharedCharData_CharEquipInfo"""

    locked: bool = False
    level: int = 0


class SharedCharDataTmplData(GameDataModel):
    """clz_Torappu_SharedCharData_TmplData"""

    skill_index: int = 0
    skin_id: str | None = None
    skills: list[SharedCharDataSharedCharSkillData] | None = None
    current_equip: str | None = None
    equip: dict[str, SharedCharDataCharEquipInfo] | None = None


class SharedCharData(GameDataModel):
    """clz_Torappu_SharedCharData"""

    char_id: str | None = None
    potential_rank: int = 0
    skill_index: int = 0
    skin_id: str | None = None
    skills: list[SharedCharDataSharedCharSkillData] | None = None
    current_equip: str | None = None
    equip: dict[str, SharedCharDataCharEquipInfo] | None = None
    main_skill_lvl: int = 0
    evolve_phase: int = 0
    level: int = 0
    favor_point: int = 0
    crisis_record: dict[str, int] | None = None
    crisis_v2_record: dict[str, int] | None = None
    current_tmpl: str | None = None
    tmpl: dict[str, SharedCharDataTmplData] | None = None


class ActivityInterlockDataMileStoneItemInfo(GameDataModel):
    """clz_Torappu_ActivityInterlockData_MileStoneItemInfo"""

    mile_stone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    item: ItemBundle | None = None


class ActivityInterlockDataFinalStageProgressData(GameDataModel):
    """clz_Torappu_ActivityInterlockData_FinalStageProgressData"""

    stage_id: str | None = None
    kill_cnt: int = 0
    ap_cost: int = 0
    favor: int = 0
    exp: int = 0
    gold: int = 0


class ActivityInterlockData(GameDataModel):
    """clz_Torappu_ActivityInterlockData"""

    stage_addition_info_map: (
        dict[str, ActivityInterlockDataStageAdditionData] | None
    ) = None
    treasure_monster_map: dict[str, ActivityInterlockDataTreasureMonsterData] | None = (
        None
    )
    special_assist_data: SharedCharData | None = None
    mile_stone_item_list: list[ActivityInterlockDataMileStoneItemInfo] | None = None
    final_stage_progress_map: (
        dict[str, list[ActivityInterlockDataFinalStageProgressData]] | None
    ) = None


class ActivityBossRushDataZoneAdditionData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_ZoneAdditionData"""

    unlock_text: str | None = None
    display_start_time: int = 0


class ActivityBossRushDataBossRushStageGroupData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_BossRushStageGroupData"""

    stage_group_id: str | None = None
    sort_id: int = 0
    stage_group_name: str | None = None
    stage_id_map: dict[str, str] | None = None
    wave_boss_info: list[list[str]] | None = None
    normal_stage_count: int = 0
    is_hard_stage_group: bool = False
    unlock_condtion: str | None = None


class ActivityBossRushDataBossRushStageAdditionData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_BossRushStageAdditionData"""

    stage_id: str | None = None
    stage_type: str = "NONE"
    stage_group_id: str | None = None
    team_id_list: list[str] | None = None
    unlock_text: str | None = None


class ActivityBossRushDataDisplayDetailRewards(GameDataModel):
    """clz_Torappu_ActivityBossRushData_DisplayDetailRewards"""

    occ_percent: str = "ALWAYS"
    drop_count: int = 0
    type: str = "NONE"
    id: str | None = None
    drop_type: str = "NONE"


class ActivityBossRushDataBossRushDropInfo(GameDataModel):
    """clz_Torappu_ActivityBossRushData_BossRushDropInfo"""

    clear_wave_count: int = 0
    display_detail_rewards: list[ActivityBossRushDataDisplayDetailRewards] | None = None
    first_pass_rewards: list[ItemBundle] | None = None
    pass_rewards: list[ItemBundle] | None = None


class ActivityBossRushDataBossRushMissionAdditionData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_BossRushMissionAdditionData"""

    mission_id: str | None = None
    is_relic_task: bool = False


class ActivityBossRushDataBossRushTeamData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_BossRushTeamData"""

    team_id: str | None = None
    team_name: str | None = None
    char_id_list: list[str] | None = None
    team_buff_name: str | None = None
    team_buff_des: str | None = None
    team_buff_id: str | None = None
    max_char_num: int = 0
    rune_data: RuneTablePackedRuneData | None = None


class ActivityBossRushDataRelicData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_RelicData"""

    relic_id: str | None = None
    sort_id: int = 0
    name: str | None = None
    icon: str | None = None
    relic_task_id: str | None = None


class ActivityBossRushDataRelicLevelInfo(GameDataModel):
    """clz_Torappu_ActivityBossRushData_RelicLevelInfo"""

    level: int = 0
    effect_desc: str | None = None
    rune_data: RuneTablePackedRuneData | None = None
    need_item_count: int = 0


class ActivityBossRushDataRelicLevelInfoData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_RelicLevelInfoData"""

    relic_id: str | None = None
    level_infos: dict[int, ActivityBossRushDataRelicLevelInfo] | None = None


class ActivityBossRushDataBossRushMileStoneData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_BossRushMileStoneData"""

    mile_stone_id: str | None = None
    mile_stone_lvl: int = 0
    need_point_cnt: int = 0
    reward_item: ItemBundle | None = None


class ActivityBossRushDataConstData(GameDataModel):
    """clz_Torappu_ActivityBossRushData_ConstData"""

    max_provided_char_num: int = 0
    text_milestone_item_level_desc: str | None = None
    milestone_point_id: str | None = None
    relic_upgrade_item_id: str | None = None
    default_relict_list: list[str] | None = None
    reward_skin_id: str | None = None


class ActivityBossRushData(GameDataModel):
    """clz_Torappu_ActivityBossRushData"""

    zone_addition_data_map: dict[str, ActivityBossRushDataZoneAdditionData] | None = (
        None
    )
    stage_group_map: dict[str, ActivityBossRushDataBossRushStageGroupData] | None = None
    stage_addition_data_map: (
        dict[str, ActivityBossRushDataBossRushStageAdditionData] | None
    ) = None
    stage_drop_data_map: (
        dict[str, dict[int, ActivityBossRushDataBossRushDropInfo]] | None
    ) = None
    mission_addition_data_map: (
        dict[str, ActivityBossRushDataBossRushMissionAdditionData] | None
    ) = None
    team_data_map: dict[str, ActivityBossRushDataBossRushTeamData] | None = None
    relic_list: list[ActivityBossRushDataRelicData] | None = None
    relic_level_info_data_map: (
        dict[str, ActivityBossRushDataRelicLevelInfoData] | None
    ) = None
    mile_stone_list: list[ActivityBossRushDataBossRushMileStoneData] | None = None
    best_wave_rune_list: list[RuneTablePackedRuneData] | None = None
    const_data: ActivityBossRushDataConstData | None = None


class ActivityFloatParadeDataConstData(GameDataModel):
    """clz_Torappu_ActivityFloatParadeData_ConstData"""

    city_name: str | None = None
    city_name_pic: str | None = None
    low_standard: float = 0.0
    variation_title: str | None = None
    rule_desc: str | None = None


class ActivityFloatParadeDataDailyData(GameDataModel):
    """clz_Torappu_ActivityFloatParadeData_DailyData"""

    day_index: int = 0
    date_name: str | None = None
    place_name: str | None = None
    place_en_name: str | None = None
    place_pic: str | None = None
    event_group_id: str | None = None
    ext_reward: ItemBundle | None = None


class ActivityFloatParadeDataRewardPool(GameDataModel):
    """clz_Torappu_ActivityFloatParadeData_RewardPool"""

    grp_id: str | None = None
    id: str | None = None
    type: str | None = None
    name: str | None = None
    desc: str | None = None
    reward: ItemBundle | None = None


class ActivityFloatParadeDataTactic(GameDataModel):
    """clz_Torappu_ActivityFloatParadeData_Tactic"""

    id: int = 0
    name: str | None = None
    pack_name: str | None = None
    brief_name: str | None = None
    reward_var: dict[str, float] | None = None


class ActivityFloatParadeDataGroupData(GameDataModel):
    """clz_Torappu_ActivityFloatParadeData_GroupData"""

    group_id: str | None = None
    name: str | None = None
    start_day: int = 0
    end_day: int = 0
    ext_reward_day: int = 0
    ext_reward_count: int = 0


class ActivityFloatParadeData(GameDataModel):
    """clz_Torappu_ActivityFloatParadeData"""

    const_data: ActivityFloatParadeDataConstData | None = None
    daily_data_dic: list[ActivityFloatParadeDataDailyData] | None = None
    reward_pools: dict[str, dict[str, ActivityFloatParadeDataRewardPool]] | None = None
    tactic_list: list[ActivityFloatParadeDataTactic] | None = None
    group_infos: dict[str, ActivityFloatParadeDataGroupData] | None = None


class ActivityMainlineBuffDataMissionGroupData(GameDataModel):
    """clz_Torappu_ActivityMainlineBuffData_MissionGroupData"""

    id: str | None = None
    bind_banner: str | None = None
    sort_id: int = 0
    zone_id: str | None = None
    mission_id_list: list[str] | None = None


class ActivityMainlineBuffDataPeriodDataStepData(GameDataModel):
    """clz_Torappu_ActivityMainlineBuffData_PeriodData_StepData"""

    is_block: bool = False
    favor_up_desc: str | None = None
    unlock_desc: str | None = None
    bind_stage_id: str | None = None
    block_desc: str | None = None


class ActivityMainlineBuffDataPeriodData(GameDataModel):
    """clz_Torappu_ActivityMainlineBuffData_PeriodData"""

    id: str | None = None
    start_time: int = 0
    end_time: int = 0
    favor_up_char_desc: str | None = None
    favor_up_img_name: str | None = None
    new_chapter_img_name: str | None = None
    new_chapter_zone_id: str | None = None
    step_data_list: list[ActivityMainlineBuffDataPeriodDataStepData] | None = None


class ActivityMainlineBuffDataConstData(GameDataModel):
    """clz_Torappu_ActivityMainlineBuffData_ConstData"""

    favor_up_stage_range: str | None = None


class ActivityMainlineBuffData(GameDataModel):
    """clz_Torappu_ActivityMainlineBuffData"""

    mission_group_list: dict[str, ActivityMainlineBuffDataMissionGroupData] | None = (
        None
    )
    period_data_list: list[ActivityMainlineBuffDataPeriodData] | None = None
    ap_supply_out_of_date_dict: dict[str, int] | None = None
    const_data: ActivityMainlineBuffDataConstData | None = None


class Act24SideDataToolData(GameDataModel):
    """clz_Torappu_Act24SideData_ToolData"""

    tool_id: str | None = None
    sort_id: int = 0
    tool_name: str | None = None
    tool_desc: str | None = None
    tool_icon_1: str | None = None
    tool_icon_2: str | None = None
    tool_unlock_desc: str | None = None
    tool_buff_id: str | None = None
    rune_data: RuneTablePackedRuneData | None = None
    tool_stage_id: str | None = None


class Act24SideDataMealData(GameDataModel):
    """clz_Torappu_Act24SideData_MealData"""

    meal_id: str | None = None
    sort_id: int = 0
    meal_name: str | None = None
    meal_effect_desc: str | None = None
    meal_desc: str | None = None
    meal_icon: str | None = None
    meal_cost: int = 0
    meal_reward_ap: int = Field(default=0, alias="mealRewardAP")
    meal_reward_item_info: ItemBundle | None = None


class Act24SideDataMeldingItemData(GameDataModel):
    """clz_Torappu_Act24SideData_MeldingItemData"""

    melding_id: str | None = None
    bg_id: str | None = None
    sort_id: int = 0
    melding_price: int = 0
    rarity: str = "NONE"


class Act24SideDataMeldingGachaBoxData(GameDataModel):
    """clz_Torappu_Act24SideData_MeldingGachaBoxData"""

    gacha_box_id: str | None = None
    gacha_sort_id: int = 0
    gacha_icon: str | None = None
    gacha_box_name: str | None = None
    gacha_cost: int = 0
    gacha_times_limit: int = 0
    theme_color: str | None = None
    remain_item_bg_color: str | None = None


class Act24SideDataMeldingGachaBoxGoodData(GameDataModel):
    """clz_Torappu_Act24SideData_MeldingGachaBoxGoodData"""

    good_id: str | None = None
    gacha_box_id: str | None = None
    order_id: int = 0
    item_id: str | None = None
    item_type: str = "NONE"
    display_type: str = "NONE"
    per_count: int = 0
    total_count: int = 0
    gacha_type: str = "NONE"
    weight: int = 0
    gacha_order_id: int = 0
    gacha_num: int = 0


class Act24SideDataZoneAdditionData(GameDataModel):
    """clz_Torappu_Act24SideData_ZoneAdditionData"""

    zone_id: str | None = None
    zone_icon: str | None = None
    unlock_text: str | None = None
    display_time: str | None = None


class QuestStageData(GameDataModel):
    """clz_Torappu_QuestStageData"""

    stage_id: str | None = None
    stage_rank: int = 0
    sort_id: int = 0
    is_urgent_stage: bool = False
    is_dragon_stage: bool = False


class Act24SideDataMissionExtraData(GameDataModel):
    """clz_Torappu_Act24SideData_MissionExtraData"""

    task_type_name: str | None = None
    task_type_icon: str | None = None
    task_type: str = "NONE"
    task_title: str | None = None
    task_client: str | None = None
    task_client_desc: str | None = None


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


class Act24SideDataHuntDatabaseData(GameDataModel):
    """clz_Torappu_Act24SideData_HuntDatabaseData"""

    id: str | None = None
    name: str | None = None
    sort_id: int = 0
    level: int = 0
    is_boss: bool = False
    boss_pic_id: str | None = None
    icon_small_id: str | None = None
    icon_large_id: str | None = None
    basic_desc: str | None = None
    ride_icon: str | None = None
    ride_desc: str | None = None
    secret_task_id: str | None = None
    secret_task_item_id: str | None = None
    secret_task_desc: str | None = None
    secret_content: str | None = None


class Act24SideDataConstData(GameDataModel):
    """clz_Torappu_Act24SideData_ConstData"""

    stage_unlock_tool_desc: str | None = None
    meal_lack_money: str | None = None
    meal_day_times_limit: int = 0
    tool_maximum: int = 0
    stage_can_not_use_to_tool: list[str] | None = None
    hunter_guide_reward_item_id: str | None = None
    hunter_guide_reward_item_type: str | None = None
    hunter_guide_reward_item_count: int = 0
    hunter_guide_detail_tab_position: int = 0
    task_reward_item_no_icon_display_id: str | None = None
    special_level_unlock_task_id: str | None = None
    mission_progress_format: str | None = None
    gacha_default_prob: float = 0.0
    gacha_extra_prob: float = 0.0


class Act24SideData(GameDataModel):
    """clz_Torappu_Act24SideData"""

    tool_data_list: dict[str, Act24SideDataToolData] | None = None
    meal_data_list: dict[str, Act24SideDataMealData] | None = None
    melding_dict: dict[str, Act24SideDataMeldingItemData] | None = None
    melding_gacha_box_data_list: dict[str, Act24SideDataMeldingGachaBoxData] | None = (
        None
    )
    melding_gacha_box_good_data_map: (
        dict[str, list[Act24SideDataMeldingGachaBoxGoodData]] | None
    ) = None
    meal_welcome_txt_data_map: dict[str, str] | None = None
    zone_addition_data_map: dict[str, Act24SideDataZoneAdditionData] | None = None
    quest_stage_list: list[QuestStageData] | None = None
    mission_data_list: dict[str, Act24SideDataMissionExtraData] | None = None
    melding_drop_dict: dict[str, StageDataStageDropInfo] | None = None
    stage_map_preview_dict: dict[str, list[str]] | None = None
    hunt_database_dict: dict[str, Act24SideDataHuntDatabaseData] | None = None
    stage_id_to_unlock_item_id_dict: dict[str, str] | None = None
    const_data: Act24SideDataConstData | None = None


class Act25SideDataConstData(GameDataModel):
    """clz_Torappu_Act25SideData_ConstData"""

    get_daily_count: int = 0
    cost_name: str | None = None
    cost_desc: str | None = None
    cost_limit: int = 0
    reward_limit: int = 0
    research_unlock_text: str | None = None
    harvest_reward: ItemBundle | None = None
    cost_count: int = 0
    cost_count_limit: int = 0
    basic_progress: int = 0
    harvest_desc: str | None = None


class Act25SideDataZoneDescInfo(GameDataModel):
    """clz_Torappu_Act25SideData_ZoneDescInfo"""

    zone_id: str | None = None
    unlock_text: str | None = None
    display_start_time: int = 0


class Act25SideDataArchiveItemData(GameDataModel):
    """clz_Torappu_Act25SideData_ArchiveItemData"""

    item_id: str | None = None
    item_type: str = "PIC"
    item_unlock_type: str = "MISSION"
    item_unlock_param: str | None = None
    unlock_desc: str | None = None
    icon_id: str | None = None
    item_name: str | None = None


class Act25SideDataArchiveMapInfoData(GameDataModel):
    """clz_Torappu_Act25SideData_ArchiveMapInfoData"""

    object_id: str | None = None
    type: str = "PIC"
    number_id: str | None = None
    area_id: str | None = None
    sort_id: int = 0
    position: int = 0
    has_dot: bool = False


class Act25SideDataAreaInfoData(GameDataModel):
    """clz_Torappu_Act25SideData_AreaInfoData"""

    area_id: str | None = None
    sort_id: int = 0
    area_icon: str | None = None
    area_name: str | None = None
    unlock_text: str | None = None
    preposed_stage: str | None = None
    area_initial_desc: str | None = None
    area_ending_desc: str | None = None
    area_ending_aud: str | None = None
    reward: ItemBundle | None = None
    final_id: str | None = None
    area_new_icon: bool = False


class Act25SideDataAreaMissionData(GameDataModel):
    """clz_Torappu_Act25SideData_AreaMissionData"""

    id: str | None = None
    area_id: str | None = None
    preposed_mission_id: str | None = None
    sort_id: int = 0
    is_zone: bool = False
    stage_id: str | None = None
    cost_count: int = 0
    transform: int = 0
    progress: int = 0
    progress_pic_id: str | None = None
    template: str | None = None
    template_type: int = 0
    desc: str | None = None
    param: list[str] | None = None
    rewards: list[ItemBundle] | None = None
    archive_items: list[str] | None = None


class Act25SideDataBattlePerformanceData(GameDataModel):
    """clz_Torappu_Act25SideData_BattlePerformanceData"""

    item_id: str | None = None
    sort_id: int = 0
    item_name: str | None = None
    item_icon: str | None = None
    item_desc: str | None = None
    item_tech_type: str = "TECH_1"
    rune_data: RuneTablePackedRuneData | None = None


class Act25SideDataKeyData(GameDataModel):
    """clz_Torappu_Act25SideData_KeyData"""

    key_id: str | None = None
    key_name: str | None = None
    key_icon: str | None = None
    toast_text: str | None = None


class Act25SideDataFogUnlockData(GameDataModel):
    """clz_Torappu_Act25SideData_FogUnlockData"""

    lock_id: str | None = None
    locked_collection_icon_id: str | None = None
    unlocked_collection_icon_id: str | None = None


class Act25SideDataDailyFarmData(GameDataModel):
    """clz_Torappu_Act25SideData_DailyFarmData"""

    transform: int = 0
    unit_time: int = 0


class Act25SideData(GameDataModel):
    """clz_Torappu_Act25SideData"""

    token_item_id: str | None = None
    const_data: Act25SideDataConstData | None = None
    zone_desc_list: dict[str, Act25SideDataZoneDescInfo] | None = None
    archive_item_data: dict[str, Act25SideDataArchiveItemData] | None = None
    arc_map_info_data: dict[str, Act25SideDataArchiveMapInfoData] | None = None
    area_info_data: dict[str, Act25SideDataAreaInfoData] | None = None
    area_mission_data: dict[str, Act25SideDataAreaMissionData] | None = None
    battle_performance_data: dict[str, Act25SideDataBattlePerformanceData] | None = None
    key_data: dict[str, Act25SideDataKeyData] | None = None
    fog_unlock_data: dict[str, Act25SideDataFogUnlockData] | None = None
    farm_list: list[Act25SideDataDailyFarmData] | None = None


class Act27SideDataAct27SideGoodData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideGoodData"""

    id: str | None = None
    name: str | None = None
    type_desc: str | None = None
    icon_id: str | None = None
    launch_icon_id: str | None = None
    purchase_price: list[int] | None = None
    selling_price_list: list[int] | None = None
    sell_shop_list: list[str] | None = None
    is_permanent: bool = False


class Act27SideDataAct27SideMileStoneData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideMileStoneData"""

    mile_stone_id: str | None = None
    mile_stone_lvl: int = 0
    need_point_cnt: int = 0
    reward_item: ItemBundle | None = None


class Act27SideDataAct27SideGoodLaunchData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideGoodLaunchData"""

    group_id: str | None = None
    start_time: int = 0
    stage_id: str | None = None
    code: str | None = None
    drink_id: str | None = None
    food_id: str | None = None
    souvenir_id: str | None = None


class Act27SideDataAct27SideShopData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideShopData"""

    shop_id: str | None = None
    sort_id: int = 0
    name: str | None = None
    icon_id: str | None = None


class Act27SideDataAct27SideInquireData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideInquireData"""

    mile_stone_pt: int = 0
    inquire_count: int = 0


class Act27SideDataAct27SideDynEntrySwitchData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideDynEntrySwitchData"""

    entry_id: str | None = None
    start_hour: int = 0
    signal_id: str | None = None


class Act27SideDataAct27sideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27sideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None
    display_time: str | None = None


class Act27SideDataAct27SideMileStoneFurniRewardData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideMileStoneFurniRewardData"""

    furni_id: str | None = None
    point_num: int = 0


class Act27SideDataAct27SideConstData(GameDataModel):
    """clz_Torappu_Act27SideData_Act27SideConstData"""

    stage_id: str | None = None
    stage_code: str | None = None
    purchase_price_name: list[str] | None = None
    furni_reward_list: list[Act27SideDataAct27SideMileStoneFurniRewardData] | None = (
        None
    )
    prize_text: str | None = None
    player_shop_id: str | None = None
    milestone_point_name: str | None = None
    inquire_panel_title: str | None = None
    inquire_panel_desc: str | None = None
    gain_123: list[float] | None = None
    gain_113: list[float] | None = None
    gain_122: list[float] | None = None
    gain_111: list[float] | None = None
    gain_11_none: list[float] | None = None
    gain_12_none: list[float] | None = None
    campaign_enemy_cnt: int = 0


class Act27SideData(GameDataModel):
    """clz_Torappu_Act27SideData"""

    good_data_map: dict[str, Act27SideDataAct27SideGoodData] | None = None
    mile_stone_list: list[Act27SideDataAct27SideMileStoneData] | None = None
    good_launch_data_list: list[Act27SideDataAct27SideGoodLaunchData] | None = None
    shop_data_map: dict[str, Act27SideDataAct27SideShopData] | None = None
    inquire_data_list: list[Act27SideDataAct27SideInquireData] | None = None
    dyn_entry_switch_data: list[Act27SideDataAct27SideDynEntrySwitchData] | None = None
    zone_addition_data_map: dict[str, Act27SideDataAct27sideZoneAdditionData] | None = (
        None
    )
    const_data: Act27SideDataAct27SideConstData | None = None


class Act42D0DataAct42D0AreaInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0AreaInfoData"""

    area_id: str | None = None
    sort_id: int = 0
    area_code: str | None = None
    area_name: str | None = None
    difficulty: str = "NONE"
    area_desc: str | None = None
    cost_limit: int = 0
    boss_icon: str | None = None
    boss_id: str | None = None
    next_area_stage: str | None = None


class Act42D0DataAct42D0StageInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0StageInfoData"""

    stage_id: str | None = None
    area_id: str | None = None
    stage_code: str | None = None
    sort_id: int = 0
    stage_desc: list[str] | None = None
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None


class Act42D0DataAct42D0EffectGroupInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0EffectGroupInfoData"""

    effect_group_id: str | None = None
    sort_id: int = 0
    effect_group_name: str | None = None


class Act42D0DataAct42D0EffectInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0EffectInfoData"""

    effect_id: str | None = None
    effect_group_id: str | None = None
    row: int = 0
    col: int = 0
    effect_name: str | None = None
    effect_icon: str | None = None
    cost: int = 0
    effect_desc: str | None = None
    unlock_time: int = 0
    rune_data: RuneTablePackedRuneData | None = None


class Act42D0DataAct42D0ChallengeMissionData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0ChallengeMissionData"""

    mission_id: str | None = None
    sort_id: int = 0
    stage_id: str | None = None
    mission_desc: str | None = None
    milestone_count: int = 0


class Act42D0DataAct42D0ChallengeInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0ChallengeInfoData"""

    stage_id: str | None = None
    stage_desc: str | None = None
    start_ts: int = 0
    end_ts: int = 0
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    loading_pic_id: str | None = None
    challenge_mission_data: list[Act42D0DataAct42D0ChallengeMissionData] | None = None


class Act42D0DataAct42D0RatingInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0RatingInfoData"""

    rating_level: int = 0
    cost_up_limit: int = 0
    achivement: str | None = None
    icon: str | None = None
    milestone_count: int = 0


class Act42D0DataAct42D0StageRatingInfoData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0StageRatingInfoData"""

    stage_id: str | None = None
    area_id: str | None = None
    milestone_data: list[Act42D0DataAct42D0RatingInfoData] | None = None


class Act42D0DataAct42D0MilestoneData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0MilestoneData"""

    milestone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    item: ItemBundle | None = None


class Act42D0DataAct42D0ConstData(GameDataModel):
    """clz_Torappu_Act42D0Data_Act42D0ConstData"""

    milestone_id: str | None = None
    strife_name: str | None = None
    strife_desc: str | None = None
    unlock_desc: str | None = None
    reward_desc: str | None = None
    trauma_desc: str | None = None
    milestone_area_name: str | None = None
    trauma_name: str | None = None


class Act42D0Data(GameDataModel):
    """clz_Torappu_Act42D0Data"""

    area_info_data: dict[str, Act42D0DataAct42D0AreaInfoData] | None = None
    stage_info_data: dict[str, Act42D0DataAct42D0StageInfoData] | None = None
    effect_group_info_data: dict[str, Act42D0DataAct42D0EffectGroupInfoData] | None = (
        None
    )
    effect_info_data: dict[str, Act42D0DataAct42D0EffectInfoData] | None = None
    challenge_info_data: dict[str, Act42D0DataAct42D0ChallengeInfoData] | None = None
    stage_rating_info_data: dict[str, Act42D0DataAct42D0StageRatingInfoData] | None = (
        None
    )
    milestone_data: list[Act42D0DataAct42D0MilestoneData] | None = None
    const_data: Act42D0DataAct42D0ConstData | None = None
    track_point_period_data: list[int] | None = None


class Act29SideDataAct29SideFragData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideFragData"""

    frag_id: str | None = None
    sort_id: int = 0
    frag_name: str | None = None
    frag_icon: str | None = None
    frag_store_icon: str | None = None


class Act29SideDataAct29SideOrcheData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideOrcheData"""

    id: str | None = None
    name: str | None = None
    desc: str | None = None
    icon: str | None = None
    sort_id: int = 0
    orche_type: str = "ORCHE_1"


class Act29SideDataAct29SideProductGroupData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideProductGroupData"""

    group_id: str | None = None
    group_name: str | None = None
    group_icon: str | None = None
    group_desc: str | None = None
    default_bgm_signal: str | None = None
    product_list: list[str] | None = None
    group_eng_name: str | None = None
    group_small_name: str | None = None
    group_type_icon: str | None = None
    group_store_icon_id: str | None = None
    group_type_base_pic: str | None = None
    group_type_eye_icon: str | None = None
    group_sort_id: int = 0
    form_list: list[str] | None = None
    sheet_id: str | None = None
    sheet_num: int = 0
    sheet_rotate_spd: float = 0.0
    product_type: str = "PRODUCT_TYPE_1"
    product_desc_color: str | None = None
    play_tint_color: str | None = None
    confirm_tint_color: str | None = None
    confirm_desc_color: str | None = None
    bag_theme_color: str | None = None


class Act29SideDataAct29SideProductData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideProductData"""

    id: str | None = None
    orche_id: str | None = None
    group_id: str | None = None
    form_id: str | None = None
    music_id: str | None = None


class Act29SideDataAct29SideFormData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideFormData"""

    form_id: str | None = None
    frag_id_list: list[str] | None = None
    form_desc: str | None = None
    product_id_dict: dict[str, str] | None = None
    without_orche_product_id: str | None = None
    group_id: str | None = None
    form_sort_id: int = 0


class Act29SideDataAct29SideInvestResultData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideInvestResultData"""

    result_id: str | None = None
    result_title: str | None = None
    result_desc_1: str | None = None
    result_desc_2: str | None = None


class Act29SideDataAct29SideInvestData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideInvestData"""

    invest_id: str | None = None
    invest_type: str = "MAJOR"
    invest_npc_name: str | None = None
    story_id: str | None = None
    invest_npc_pic: str | None = None
    invest_npc_avatar_pic: str | None = None
    major_npc_pic: str | None = None
    major_npc_black_pic: str | None = None
    reward: ItemBundle | None = None
    invest_suc_result_id: str | None = None
    invest_fail_result_id: str | None = None
    invest_rare_result_id: str | None = None


class Act29SideDataAct29SideConstData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideConstData"""

    major_invest_unlock_item_name: str | None = None
    wrong_tips_trigger_time: int = 0
    major_invest_complete_img_id: str | None = None
    major_invest_unknown_avatar_id: str | None = None
    major_invest_detail_desc_1: str | None = None
    major_invest_detail_desc_2: str | None = None
    major_invest_detail_desc_3: str | None = None
    major_invest_detail_desc_4: str | None = None
    hidden_invest_img_id: str | None = None
    hidden_invest_head_img_id: str | None = None
    hidden_invest_npc_name: str | None = None
    unlock_level_id: str | None = None
    invest_result_hint: str | None = None
    invest_unlock_text: str | None = None
    no_orche_desc: str | None = None
    invest_track_id: str | None = None


class Act29SideDataAct29SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act29SideDataAct29SideMusicData(GameDataModel):
    """clz_Torappu_Act29SideData_Act29SideMusicData"""

    group_id: str | None = None
    orche_id: str | None = None
    music_id: str | None = None


class Act29SideData(GameDataModel):
    """clz_Torappu_Act29SideData"""

    frag_data_map: dict[str, Act29SideDataAct29SideFragData] | None = None
    orche_data_map: dict[str, Act29SideDataAct29SideOrcheData] | None = None
    product_group_data_map: dict[str, Act29SideDataAct29SideProductGroupData] | None = (
        None
    )
    product_data_map: dict[str, Act29SideDataAct29SideProductData] | None = None
    form_data_map: dict[str, Act29SideDataAct29SideFormData] | None = None
    invest_result_data_map: dict[str, Act29SideDataAct29SideInvestResultData] | None = (
        None
    )
    invest_data_map: dict[str, Act29SideDataAct29SideInvestData] | None = None
    major_invest_id_list: list[str] | None = None
    rare_invest_id_list: list[str] | None = None
    const_data: Act29SideDataAct29SideConstData | None = None
    zone_addition_data_map: dict[str, Act29SideDataAct29SideZoneAdditionData] | None = (
        None
    )
    music_data_map: list[Act29SideDataAct29SideMusicData] | None = None


class ActivityYear5GeneralConstData(GameDataModel):
    """clz_Torappu_ActivityYear5GeneralConstData"""

    rew_point: int = 0
    rew_main_desc: str | None = None
    rew_ap_desc: str | None = None
    rew_end_desc: str | None = None
    act_primary_desc: str | None = None
    act_entry_desc: str | None = None
    act_secondary_desc: str | None = None
    act_reward_desc: str | None = None
    mission_archive_topic_id: str | None = None
    mission_archive_unlock_desc: str | None = None


class ActivityYear5GeneralUnlimitedApRewardData(GameDataModel):
    """clz_Torappu_ActivityYear5GeneralUnlimitedApRewardData"""

    reward_index: int = 0
    reward_item: ItemBundle | None = None


class ActivityYear5GeneralData(GameDataModel):
    """clz_Torappu_ActivityYear5GeneralData"""

    const_data: ActivityYear5GeneralConstData | None = None
    unlimited_ap_rewards: list[ActivityYear5GeneralUnlimitedApRewardData] | None = None


class Act35SideDataAct35SideChallengeData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideChallengeData"""

    challenge_id: str | None = None
    challenge_name: str | None = None
    challenge_desc: str | None = None
    sort_id: int = 0
    challenge_pic_id: str | None = None
    challenge_icon_id: str | None = None
    open_time: int = 0
    preposed_challenge_id: str | None = None
    pass_round: int = 0
    pass_round_score: int = 0
    round_id_list: list[str] | None = None


class Act35SideDataAct35SideRoundData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideRoundData"""

    round_id: str | None = None
    challenge_id: str | None = None
    round: int = 0
    round_pass_rating: int = 0
    is_material_random: bool = False
    fixed_material_list: dict[str, int] | None = None
    pass_round_coin: int = 0


class Act35SideDataAct35SideChallengeTaskData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideChallengeTaskData"""

    task_id: str | None = None
    task_desc: str | None = None
    material_id: str | None = None
    material_num: int = 0
    pass_task_coin: int = 0


class Act35SideDataAct35sideCardMaterialData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35sideCardMaterialData"""

    material_id: str | None = None
    count: int = 0


class Act35SideDataAct35SideCardLevelData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideCardLevelData"""

    card_level: int = 0
    card_name: str | None = None
    card_desc: str | None = None
    input_material_list: list[Act35SideDataAct35sideCardMaterialData] | None = None
    output_material_list: list[Act35SideDataAct35sideCardMaterialData] | None = None


class Act35SideDataAct35SideCardData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideCardData"""

    card_id: str | None = None
    sort_id: int = 0
    rank: int = 0
    card_face: str | None = None
    card_pic: str | None = None
    level_data_list: list[Act35SideDataAct35SideCardLevelData] | None = None


class Act35SideDataAct35SideMaterialData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideMaterialData"""

    material_id: str | None = None
    sort_id: int = 0
    material_icon: str | None = None
    material_name: str | None = None
    material_rating: int = 0


class Act35SideDataAct35SideDialogueData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideDialogueData"""

    sort_id: int = 0
    icon_id: str | None = None
    name: str | None = None
    content: str | None = None
    bg_type: str = "NONE"


class Act35SideDataAct35SideDialogueGroupData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideDialogueGroupData"""

    type: str = "NONE"
    dialog_data_list: list[Act35SideDataAct35SideDialogueData] | None = None


class Act35SideDataAct35SideMileStoneGrandRewardInfo(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideMileStoneGrandRewardInfo"""

    item_name: str | None = None
    level: int = 0


class Act35SideDataAct35SideConstData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideConstData"""

    campaign_stage_id: str | None = None
    campaign_enemy_cnt: int = 0
    milestone_grand_reward_info_list: (
        list[Act35SideDataAct35SideMileStoneGrandRewardInfo] | None
    ) = None
    unlock_level_id: str | None = None
    bird_spine_low_rate: float = 0.0
    bird_spine_high_rate: float = 0.0
    card_max_level: int = 0
    max_slot_cnt: int = 0
    card_refresh_num: int = 0
    init_slot_cnt: int = 0
    bonus_material_id: str | None = None
    intro_round_id_list: list[str] | None = None
    challenge_unlock_text: str | None = None
    slot_unlock_text: str | None = None
    estimate_ratio: int = 0
    carving_unlock_toast_text: str | None = None


class Act35SideDataAct35SideMileStoneData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideMileStoneData"""

    mile_stone_id: str | None = None
    mile_stone_lvl: int = 0
    need_point_cnt: int = 0
    reward_item: ItemBundle | None = None


class Act35SideDataAct35SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act35SideData_Act35SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act35SideData(GameDataModel):
    """clz_Torappu_Act35SideData"""

    challenge_data_map: dict[str, Act35SideDataAct35SideChallengeData] | None = None
    round_data_map: dict[str, Act35SideDataAct35SideRoundData] | None = None
    task_data_map: dict[str, Act35SideDataAct35SideChallengeTaskData] | None = None
    card_data_map: dict[str, Act35SideDataAct35SideCardData] | None = None
    material_data_map: dict[str, Act35SideDataAct35SideMaterialData] | None = None
    dialogue_group_data_map: (
        dict[str, Act35SideDataAct35SideDialogueGroupData] | None
    ) = None
    const_data: Act35SideDataAct35SideConstData | None = None
    mile_stone_list: list[Act35SideDataAct35SideMileStoneData] | None = None
    zone_addition_data_map: dict[str, Act35SideDataAct35SideZoneAdditionData] | None = (
        None
    )


class ActVecBreakV2BossData(GameDataModel):
    """clz_Torappu_ActVecBreakV2BossData"""

    enemy_id: str | None = None
    name: str | None = None
    desc: str | None = None
    level: int = 0
    icon_id: str | None = None
    level_deco_figure_id: str | None = None
    level_deco_sign_id: str | None = None
    deco_id: str | None = None


class ActVecBreakV2OffenseStageData(GameDataModel):
    """clz_Torappu_ActVecBreakV2OffenseStageData"""

    stage_id: str | None = None
    level: int = 0
    level_layout: str | None = None
    story_desc: str | None = None
    particle_type: str = "NONE"
    boss_data: ActVecBreakV2BossData | None = None


class ActVecBreakV2HardStageData(GameDataModel):
    """clz_Torappu_ActVecBreakV2HardStageData"""

    stage_id: str | None = None
    order_type: str = "NONE"
    story_desc: str | None = None
    boss_data: ActVecBreakV2BossData | None = None


class ActVecBreakV2DefenseBasicData(GameDataModel):
    """clz_Torappu_ActVecBreakV2DefenseBasicData"""

    stage_id: str | None = None
    group_id: str | None = None
    sort_id: int = 0
    start_ts: int = 0


class ActVecBreakV2DefenseDetailData(GameDataModel):
    """clz_Torappu_ActVecBreakV2DefenseDetailData"""

    stage_id: str | None = None
    buff_id: str | None = None
    defense_char_limit: int = 0
    boss_icon_id: str | None = None


class ActVecBreakV2ZoneData(GameDataModel):
    """clz_Torappu_ActVecBreakV2ZoneData"""

    zone_id: str | None = None
    stage_lock_hint: str | None = None


class ActVecBreakV2DefenseGroupData(GameDataModel):
    """clz_Torappu_ActVecBreakV2DefenseGroupData"""

    group_id: str | None = None
    sort_id: int = 0
    ordered_stage_list: list[str] | None = None


class ActVecBreakV2BattleBuffData(GameDataModel):
    """clz_Torappu_ActVecBreakV2BattleBuffData"""

    buff_id: str | None = None
    name: str | None = None
    desc: str | None = None
    icon_id: str | None = None
    rune_data: RuneTablePackedRuneData | None = None


class ActVecBreakV2MilestoneItemData(GameDataModel):
    """clz_Torappu_ActVecBreakV2MilestoneItemData"""

    milestone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    reward: ItemBundle | None = None
    avail_time: int = 0


class ActVecBreakV2StageRewardDataLimitedRewardData(GameDataModel):
    """clz_Torappu_ActVecBreakV2StageRewardData_LimitedRewardData"""

    start_ts: int = 0
    end_ts: int = 0
    reward_cnt: int = 0


class ActVecBreakV2StageRewardData(GameDataModel):
    """clz_Torappu_ActVecBreakV2StageRewardData"""

    stage_id: str | None = None
    complete_reward_cnt: int = 0
    normal_reward_cnt: int = 0
    limit_reward: ActVecBreakV2StageRewardDataLimitedRewardData | None = None


class ActVecBreakV2ConstData(GameDataModel):
    """clz_Torappu_ActVecBreakV2ConstData"""

    defense_desc: str | None = None
    defense_overview_name: str | None = None
    milestone_name: str | None = None
    milestone_item_id: str | None = None
    boss_desc_title: str | None = None
    defense_unlock_require_stage_id: str | None = None
    offense_nav_lock_toast_stage_id: str | None = None
    offense_nav_lock_toast_str: str | None = None
    offense_hard_unlock_toast: str | None = None
    hard_unlock_stage_id: str | None = None
    defense_retreat_single_text: str | None = None
    defense_retreat_multiple_text: str | None = None
    defense_replace_text: str | None = None
    defense_equip_buff_limit: int = 0
    display_medal_id: str | None = None
    defense_add_buff_toast: str | None = None
    defense_remove_buff_toast: str | None = None
    defense_replace_buff_toast: str | None = None
    defense_buff_exceed_toast: str | None = None
    defend_same_group_hint: str | None = None
    defend_other_hint: str | None = None
    defense_buff_lock_toast: str | None = None
    offense_buff_select_unsave_hint: str | None = None
    defence_battle_finish_equip_text: str | None = None
    defence_battle_finish_activate_text: str | None = None
    defence_battle_finish_squad_text: str | None = None
    milestone_track_id: str | None = None
    theme_color: str | None = None
    sub_title_name: str | None = None


class ActVecBreakV2ScheduleBlockData(GameDataModel):
    """clz_Torappu_ActVecBreakV2ScheduleBlockData"""

    start_ts: int = 0
    end_ts: int = 0


class ActVecBreakV2Data(GameDataModel):
    """clz_Torappu_ActVecBreakV2Data"""

    offense_stage_dict: dict[str, ActVecBreakV2OffenseStageData] | None = None
    hard_stage_dict: dict[str, ActVecBreakV2HardStageData] | None = None
    defense_basic_dict: dict[str, ActVecBreakV2DefenseBasicData] | None = None
    defense_detail_dict: dict[str, ActVecBreakV2DefenseDetailData] | None = None
    zone_dict: dict[str, ActVecBreakV2ZoneData] | None = None
    defense_group_dict: dict[str, ActVecBreakV2DefenseGroupData] | None = None
    battle_buff_dict: dict[str, ActVecBreakV2BattleBuffData] | None = None
    milestone_list: list[ActVecBreakV2MilestoneItemData] | None = None
    stage_reward_dict: dict[str, ActVecBreakV2StageRewardData] | None = None
    const_data: ActVecBreakV2ConstData | None = None
    squad_buff_avail_stage_list: list[str] | None = None
    schedule_block_list: list[ActVecBreakV2ScheduleBlockData] | None = None
    defense_zone_id: str | None = None
    offense_zone_id: str | None = None
    hard_zone_id: str | None = None
    first_defense_stage_id: str | None = None


class Act36SideDataAct36SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act36SideData_Act36SideZoneAdditionData"""

    zone_id: str | None = None
    zone_icon_id: str | None = None
    unlock_text: str | None = None
    display_time: int = 0


class Act36SideDataAct36SideEnemyHandbookData(GameDataModel):
    """clz_Torappu_Act36SideData_Act36SideEnemyHandbookData"""

    enemy_handbook_id: str | None = None
    sprite_id: str | None = None
    sort_id: int = 0
    food_type_id: str | None = None
    food_amount_id: str | None = None


class Act36SideDataAct36SideTokenHandbookData(GameDataModel):
    """clz_Torappu_Act36SideData_Act36SideTokenHandbookData"""

    token_handbook_id: str | None = None
    sprite_id: str | None = None
    sort_id: int = 0
    token_ability: str | None = None
    token_descrption: str | None = None


class Act36SideDataAct36SideConstData(GameDataModel):
    """clz_Torappu_Act36SideData_Act36SideConstData"""

    reward_failed: str | None = None
    reward_receive_number: int = 0


class Act36SideData(GameDataModel):
    """clz_Torappu_Act36SideData"""

    zone_addition_data: dict[str, Act36SideDataAct36SideZoneAdditionData] | None = None
    enemy_handbook_data: dict[str, Act36SideDataAct36SideEnemyHandbookData] | None = (
        None
    )
    token_handbook_data: dict[str, Act36SideDataAct36SideTokenHandbookData] | None = (
        None
    )
    const_data: Act36SideDataAct36SideConstData | None = None


class Act38SideDataAct38SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act38SideData_Act38SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act38SideDataAct38SidePuzzleInfo(GameDataModel):
    """clz_Torappu_Act38SideData_Act38SidePuzzleInfo"""

    puzzle_id: str | None = None
    sort_id: int = 0
    start_time: int = 0
    puzzle_group_id: str | None = None


class Act38SideDataAct38SideNpcDialogData(GameDataModel):
    """clz_Torappu_Act38SideData_Act38SideNpcDialogData"""

    desc: str | None = None
    dialog_type: str = "NONE"
    emo_spine_name: str | None = None


class Act38SideDataConstData(GameDataModel):
    """clz_Torappu_Act38SideData_ConstData"""

    npc_idle_spine_name: str | None = None
    puzzle_map_anim_group_id: str | None = None
    puzzle_cross_day_track_id: str | None = None
    puzzle_list_text: str | None = None
    puzzle_reward_num: int = 0


class Act38SideDataAct38SidePuzzleGroupFocusData(GameDataModel):
    """clz_Torappu_Act38SideData_Act38SidePuzzleGroupFocusData"""

    puzzle_group_id: str | None = None
    x_axis_focus_pos: float = 0.0


class Act38SideData(GameDataModel):
    """clz_Torappu_Act38SideData"""

    zone_addition_data_map: dict[str, Act38SideDataAct38SideZoneAdditionData] | None = (
        None
    )
    puzzle_info_map: dict[str, Act38SideDataAct38SidePuzzleInfo] | None = None
    npc_dialog_list: list[Act38SideDataAct38SideNpcDialogData] | None = None
    const_data: Act38SideDataConstData | None = None
    puzzle_group_focus_data_map: (
        dict[str, Act38SideDataAct38SidePuzzleGroupFocusData] | None
    ) = None


class ActArcadeDataArcadeStageRankRewardLevelData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeStageRankRewardLevelData"""

    rank: str = "B"
    rank_score: int = 0
    coin_cnt: int = 0


class ActArcadeDataArcadeStageRankRewardData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeStageRankRewardData"""

    stage_id: str | None = None
    max_reward_rank: str = "B"
    rank_reward_level_datas: (
        list[ActArcadeDataArcadeStageRankRewardLevelData] | None
    ) = None


class ActArcadeDataArcadeStageAdditionalData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeStageAdditionalData"""

    stage_id: str | None = None
    zone_id: str | None = None
    mech_description: str | None = None
    sort_id: int = 0
    max_slot: int = 0
    rank_reward_data: ActArcadeDataArcadeStageRankRewardData | None = None


class ActArcadeDataArcadeZoneAdditionalData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeZoneAdditionalData"""

    zone_id: str | None = None
    sort_id: int = 0
    zone_name: str | None = None
    start_ts: int = 0
    end_ts: int = 0
    stages: list[str] | None = None
    sub_mode_type: str = "MINER"
    zone_desc: str | None = None


class ActArcadeDataArcadeBadgeTierData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeBadgeTierData"""

    badge_tier_id: str | None = None
    sort_id: int = 0
    badge_tier_icon_id: str | None = None
    badge_tier_share_icon_id: str | None = None
    badge_tier_effect_id: str | None = None
    title: str | None = None
    desc: str | None = None
    buff_id: str | None = None
    unlock_desc: str | None = None
    rune_data: RuneTablePackedRuneData | None = None


class ActArcadeDataArcadeBadgeData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeBadgeData"""

    badge_id: str | None = None
    badge_type: str = "COMMON"
    sort_id: int = 0
    badge_name: str | None = None
    buff_range_desc: str | None = None
    has_score: bool = False
    score_zone: str | None = None
    tiers: dict[str, ActArcadeDataArcadeBadgeTierData] | None = None


class ActArcadeDataArcadeBadgeTypeData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeBadgeTypeData"""

    badge_type: str = "COMMON"
    badge_type_name: str | None = None
    sort_id: int = 0
    buff_range_desc: str | None = None


class ActArcadeDataArcadeMilestoneItemData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeMilestoneItemData"""

    mile_stone_id: str | None = None
    mile_stone_lvl: int = 0
    need_point_cnt: int = 0
    reward: ItemBundle | None = None


class ActArcadeDataArcadeConstData(GameDataModel):
    """clz_Torappu_ActArcadeData_ArcadeConstData"""

    milestone_name: str | None = None
    milestone_name_en: str | None = Field(default=None, alias="milestoneNameEN")
    milestone_item_id: str | None = None
    reward_home_theme_id: str | None = None
    reward_home_theme_text: str | None = None
    reward_avatar_id: str | None = None
    reward_avatar_text: str | None = None
    reward_background_id: str | None = None
    reward_background_text: str | None = None
    badge_collection_name: str | None = None
    collection_entry_related_badge: str | None = None
    zone_entry_unlock_toast: str | None = None
    zone_entry_end_text: str | None = None
    zone_entry_end_toast: str | None = None
    rank_unlock_next_stage: str | None = None
    stage_score_display_limit: int = 0
    zone_ulti_score_display_limit: int = 0
    enemy_hud_score: list[str] | None = None
    trap_not_buildable_in_rest: list[str] | None = None


class ActArcadeData(GameDataModel):
    """clz_Torappu_ActArcadeData"""

    stage_addition_data_dict: (
        dict[str, ActArcadeDataArcadeStageAdditionalData] | None
    ) = None
    zone_additional_data_dict: (
        dict[str, ActArcadeDataArcadeZoneAdditionalData] | None
    ) = None
    badge_data_dict: dict[str, ActArcadeDataArcadeBadgeData] | None = None
    tire_badge_id_dict: dict[str, str] | None = None
    badge_type_data_dict: dict[str, ActArcadeDataArcadeBadgeTypeData] | None = None
    milestone_list: list[ActArcadeDataArcadeMilestoneItemData] | None = None
    const_data: ActArcadeDataArcadeConstData | None = None


class ActMultiV3SelectStepData(GameDataModel):
    """clz_Torappu_ActMultiV3SelectStepData"""

    step_type: str = "NONE"
    sort_id: int = 0
    time: int = 0
    hint_time: int = 0
    title: str | None = None
    desc: str | None = None


class ActMultiV3SquadInfoData(GameDataModel):
    """clz_Torappu_ActMultiV3SquadInfoData"""

    id: str | None = None
    sort_id: int = 0
    name: str | None = None
    mode_type: str = "NONE"


class ActMultiV3IdentityData(GameDataModel):
    """clz_Torappu_ActMultiV3IdentityData"""

    id: str | None = None
    sort_id: int = 0
    pic_id: str | None = None
    type: str = "NONE"
    max_num: int = 0
    color: str | None = None


class ActMultiV3SquadEffectDataToken(GameDataModel):
    """clz_Torappu_ActMultiV3SquadEffectData_Token"""

    name: str | None = None
    desc: str | None = None
    icon_id: str | None = None


class ActMultiV3SquadEffectData(GameDataModel):
    """clz_Torappu_ActMultiV3SquadEffectData"""

    id: str | None = None
    icon_id: str | None = None
    sort_id: int = 0
    name: str | None = None
    theme_color: str | None = None
    buff_desc: str | None = None
    debuff_desc: str | None = None
    token: ActMultiV3SquadEffectDataToken | None = None
    rune_data: RuneTablePackedRuneData | None = None
    is_initial: bool = False


class ActMultiV3TargetMissionData(GameDataModel):
    """clz_Torappu_ActMultiV3TargetMissionData"""

    id: str | None = None
    sort_id: int = 0
    title: str | None = None
    battle_desc: str | None = None
    description: str | None = None


class ActMultiV3MapTypeData(GameDataModel):
    """clz_Torappu_ActMultiV3MapTypeData"""

    mode_id: str | None = None
    mode: str = "NONE"
    difficulty: str = "NONE"
    is_default_select_in_quick_match: bool = False
    squad_max: int = 0
    match_unlock_mode_id: str | None = None
    match_unlock_param: int = 0
    stage_id_in_mode_list: list[str] | None = None
    unlock_hint: str | None = None


class ActMultiV3MapData(GameDataModel):
    """clz_Torappu_ActMultiV3MapData"""

    stage_id: str | None = None
    mode_id: str | None = None
    sort_id: int = 0
    mission_id_list: list[str] | None = None
    display_enemy_id_list: list[str] | None = None
    preview_icon_id: str | None = None


class ActMultiV3MapModeData(GameDataModel):
    """clz_Torappu_ActMultiV3MapModeData"""

    mode_type: str = "NONE"
    name: str | None = None
    icon_id: str | None = None
    color: str | None = None
    quick_match_sort_id: int = 0
    stage_overview_sort_id: int = 0
    unlock_ts: int = 0
    unlock_page_title: str | None = None
    unlock_page_desc: str | None = None


class ActMultiV3MapDiffData(GameDataModel):
    """clz_Torappu_ActMultiV3MapDiffData"""

    diff_type: str = "NONE"
    name: str | None = None


class ActMultiV3TitleData(GameDataModel):
    """clz_Torappu_ActMultiV3TitleData"""

    order: int = 0
    title_desc: str | None = None
    is_back: bool = False


class ActMultiV3PhotoSlotData(GameDataModel):
    """clz_Torappu_ActMultiV3PhotoSlotData"""

    slot_pos_x: float = 0.0
    slot_pos_y: float = 0.0
    slot_rot_z: int = 0
    slot_scale: float = 0.0
    slot_anim_name: str | None = None


class ActMultiV3PhotoTypeData(GameDataModel):
    """clz_Torappu_ActMultiV3PhotoTypeData"""

    photo_type_name: str | None = None
    sort_id: int = 0
    background: str | None = None
    photo_desc: str | None = None
    slots: list[ActMultiV3PhotoSlotData] | None = None


class ActMultiV3WeeklyPhotoRewardData(GameDataModel):
    """clz_Torappu_ActMultiV3WeeklyPhotoRewardData"""

    order: int = 0
    title_desc: str | None = None
    unlock_time: int = 0
    rewards: list[ItemBundle] | None = None


class ActMultiV3MatchPosUnlockCond(GameDataModel):
    """clz_Torappu_ActMultiV3MatchPosUnlockCond"""

    diff: str = "NONE"
    complete_map_count: int = 0
    require_map_star: int = 0
    unlock_hint: str | None = None


class ActMultiV3MatchPosData(GameDataModel):
    """clz_Torappu_ActMultiV3MatchPosData"""

    match_pos: str = "NORMAL"
    sort_id: int = 0
    name: str | None = None
    desc: str | None = None
    pos_toast: str | None = None
    match_desc: str | None = None
    unlock_cond: ActMultiV3MatchPosUnlockCond | None = None


class ActMultiV3StarRewardData(GameDataModel):
    """clz_Torappu_ActMultiV3StarRewardData"""

    star_num: int = 0
    rewards: list[ItemBundle] | None = None
    daily_mission_point: int = 0


class ActMultiV3DiffStarRewardData(GameDataModel):
    """clz_Torappu_ActMultiV3DiffStarRewardData"""

    diff_type: str = "NONE"
    star_reward_datas: list[ActMultiV3StarRewardData] | None = None


class ActMultiV3MilestoneData(GameDataModel):
    """clz_Torappu_ActMultiV3MilestoneData"""

    id: str | None = None
    level: int = 0
    need_point_cnt: int = 0
    reward_item: ItemBundle | None = None
    avail_time: int = 0


class ActMultiV3TipsData(GameDataModel):
    """clz_Torappu_ActMultiV3TipsData"""

    id: str | None = None
    txt: str | None = None
    weight: int = 0


class CommonReportPlayerData(GameDataModel):
    """clz_Torappu_CommonReportPlayerData"""

    id: str | None = None
    sort_id: int = 0
    txt: str | None = None
    desc: str | None = None


class ActMultiV3TempCharData(GameDataModel):
    """clz_Torappu_ActMultiV3TempCharData"""

    char_id: str | None = None
    level: int = 0
    evolve_phase: str = "PHASE_0"
    main_skill_level: int = 0
    specialize_level: int = 0
    potential_rank: int = 0
    favor_point: int = 0
    skin_id: str | None = None


class ActMultiV3ConstToastData(GameDataModel):
    """clz_Torappu_ActMultiV3ConstToastData"""

    no_room: str | None = None
    full_room: str | None = None
    room_id_format_error: str | None = None
    room_id_copy_success: str | None = None
    banned: str | None = None
    server_overload: str | None = None
    match_alive_failed: str | None = None
    create_room_alive_failed: str | None = None
    join_room_alive_failed: str | None = None
    room_owner_revise_map: str | None = None
    room_collaborator_revise_map: str | None = None
    room_collaborator_join_room: str | None = None
    room_collaborator_exit_room: str | None = None
    room_owner_revise_mode: str | None = None
    room_collaborator_revise_mode: str | None = None
    continuous_clicks: str | None = None
    match_no_project: str | None = None
    other_mode_training_lock: str | None = None
    team_lock: str | None = None
    mentor_lock_tips: str | None = None
    unlock_mentor_in_match: str | None = None
    unlock_inverse_mode: str | None = None
    unlock_new_map_type: str | None = None
    team_full_low: str | None = None
    team_full_high: str | None = None
    difficult_unlock: str | None = None
    weekly_album_time_unlock: str | None = None
    weekly_album_commit_unlock: str | None = None
    squad_lock_hint: str | None = None
    squad_effect_edit_hint: str | None = None
    inverse_mode_unlock_hint: str | None = None
    no_photo_in_template_hint: str | None = None
    cannot_resubmit_hint: str | None = None
    cannot_save_title_change: str | None = None
    match_prepare_room_close: str | None = None
    stage_list_view_time_lock_toast: str | None = None


class ActMultiV3ConstDataPingCond(GameDataModel):
    """clz_Torappu_ActMultiV3ConstData_PingCond"""

    cond: int = 0
    txt: str | None = None


class ActMultiV3InverseUnlockCond(GameDataModel):
    """clz_Torappu_ActMultiV3InverseUnlockCond"""

    diff: str = "NONE"
    require_star_cnt: int = 0


class ActMultiV3ConstData(GameDataModel):
    """clz_Torappu_ActMultiV3ConstData"""

    milestone_id: str | None = None
    room_num_copy_desc: str | None = None
    no_map_room_num_copy_desc: str | None = None
    random_map_room_num_copy_desc: str | None = None
    target_cd: int = 0
    squad_min_num: int = 0
    squad_max_num: int = 0
    defense_tra_max: int = 0
    defense_ord_max: int = 0
    defense_dif_max: int = 0
    stage_choose_anim_random_stage_id_list: list[str] | None = None
    require_stars_per_buff_key: int = 0
    max_unlock_num: int = 0
    map_unlock_desc_1: str | None = None
    map_unlock_desc_2: str | None = None
    map_unlock_desc_3: str | None = None
    map_unlock_desc_4: str | None = None
    map_unlock_desc_5: str | None = None
    map_unlock_desc_6: str | None = None
    map_unlock_desc_7: str | None = None
    dif_unlock_cond: int = 0
    ord_reward_stage_id: str | None = None
    dif_reward_stage_id: str | None = None
    max_match_time: int = 0
    tips_switch_time: int = 0
    ping_conds: list[ActMultiV3ConstDataPingCond] | None = None
    chat_cd: int = 0
    chat_time: int = 0
    mark_cd: int = 0
    mark_cond_1: int = 0
    mark_cond_2: int = 0
    daily_mission_param: int = 0
    daily_mission_name: str | None = None
    daily_mission_desc: str | None = None
    daily_mission_rule: str | None = None
    mission_desc: str | None = None
    daily_mission_reward_item: ItemBundle | None = None
    normal_great_voice_star: int = 0
    football_great_voice_num: int = 0
    defence_great_voice_wave: int = 0
    report_max_num: int = 0
    reward_1_id: str | None = None
    reward_1_text: str | None = None
    reward_2_id: str | None = None
    reward_2_text: str | None = None
    max_retry_time_in_team_room: int = 0
    max_retry_time_in_match_room: int = 0
    max_retry_time_in_battle: int = 0
    max_operator_delay: float = 0.0
    max_play_speed: int = 0
    delay_time_need_tip: int = 0
    settle_retry_time: int = 0
    player_display_time_max: float = 0.0
    is_match_default_inverse: bool = False
    inverse_unlock_cond: ActMultiV3InverseUnlockCond | None = None
    inverse_mode_hint: str | None = None
    team_unlock_stage_id: str | None = None
    team_unlock_param: int = 0
    train_partner_char_id: str | None = None
    train_partner_char_skin_id: str | None = None
    train_partner_player_name: str | None = None
    train_partner_player_level: int = 0
    train_partner_buff_id: str | None = None
    train_partner_avatar_group_type: str = "NONE"
    train_partner_avatar_id: str | None = None
    train_partner_title_list: list[str] | None = None
    train_partner_name_card_skin_id: str | None = None
    train_partner_name_card_skin_tmpl: int = 0
    max_photo_per_type: int = 0
    check_friend_state_time: int = 0
    photo_character_default_act: str | None = None
    training_stage_confirm_desc: str | None = None
    join_room_long_time_threshold: float = 0.0
    invitation_send_cd: int = 0
    boat_map_reachable_size: int = 0
    boat_map_size_max: int = 0
    boat_exit_map_offset: int = 0
    boat_enter_tran_offset: int = 0
    boat_collision_loss_speed_factor: float = 0.0
    boat_air_factor: float = 0.0
    boat_friction_factor: float = 0.0
    boat_force_interval: float = 0.0
    boat_exchange_damage_max: int = 0
    boat_exchange_damage_min: int = 0
    boat_exchange_force_max: int = 0
    boat_exchange_force_min: int = 0
    water_speed_factor: float = 0.0


class ActMultiV3SailBoatLevelPoolData(GameDataModel):
    """clz_Torappu_ActMultiV3SailBoatLevelPoolData"""

    stage_id: str | None = None
    start_block_pool: str | None = None
    mid_block_pool: str | None = None
    end_block_pool: str | None = None


class ActMultiV3SailBoatBlockPoolData(GameDataModel):
    """clz_Torappu_ActMultiV3SailBoatBlockPoolData"""

    block_pool: str | None = None
    block_id: str | None = None
    start_dir_type: str = "NONE"
    end_dir_type: str = "NONE"
    weight: int = 0


class ActMultiV3SailBoatBlockInfoData(GameDataModel):
    """clz_Torappu_ActMultiV3SailBoatBlockInfoData"""

    block_id: str | None = None
    block_level_id: str | None = None
    start_dir_type: str = "NONE"
    end_dir_type: str = "NONE"
    block_type: str = "NONE"


class ActMultiV3Data(GameDataModel):
    """clz_Torappu_ActMultiV3Data"""

    select_step_data_list: list[ActMultiV3SelectStepData] | None = None
    squad_info_list: list[ActMultiV3SquadInfoData] | None = None
    identity_data_list: list[ActMultiV3IdentityData] | None = None
    squad_effect_list: list[ActMultiV3SquadEffectData] | None = None
    target_mission_data_dict: dict[str, ActMultiV3TargetMissionData] | None = None
    map_type_data_dict: dict[str, ActMultiV3MapTypeData] | None = None
    map_data_dict: dict[str, ActMultiV3MapData] | None = None
    map_mode_data_dict: dict[str, ActMultiV3MapModeData] | None = None
    map_diff_data_dict: dict[str, ActMultiV3MapDiffData] | None = None
    mission_title_dict: dict[str, str] | None = None
    title_data_dict: dict[str, ActMultiV3TitleData] | None = None
    photo_type_data_dict: dict[str, ActMultiV3PhotoTypeData] | None = None
    photo_weekly_reward_data_dict: dict[str, ActMultiV3WeeklyPhotoRewardData] | None = (
        None
    )
    match_pos_data_dict: dict[str, ActMultiV3MatchPosData] | None = None
    enabled_emoticon_theme_id_list: list[str] | None = None
    diff_star_reward_dict: dict[str, ActMultiV3DiffStarRewardData] | None = None
    milestone_list: list[ActMultiV3MilestoneData] | None = None
    tips_data_list: list[ActMultiV3TipsData] | None = None
    report_data_list: list[CommonReportPlayerData] | None = None
    temp_char_data_list: list[ActMultiV3TempCharData] | None = None
    const_toast_data: ActMultiV3ConstToastData | None = None
    const_data: ActMultiV3ConstData | None = None
    sail_boat_level_pool_dict: dict[str, ActMultiV3SailBoatLevelPoolData] | None = None
    sail_boat_block_pool_dict: (
        dict[str, list[ActMultiV3SailBoatBlockPoolData]] | None
    ) = None
    sail_boat_block_info_list: dict[str, ActMultiV3SailBoatBlockInfoData] | None = None


class ActMainSSZoneAdditionData(GameDataModel):
    """clz_Torappu_ActMainSSZoneAdditionData"""

    unlock_tip: str | None = None
    unlock_tip_after_retro: str | None = None


class ActMainSSData(GameDataModel):
    """clz_Torappu_ActMainSSData"""

    zone_addition_data_map: dict[str, ActMainSSZoneAdditionData] | None = None


class ActivityEnemyDuelMilestoneItemData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelMilestoneItemData"""

    milestone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    reward: ItemBundle | None = None
    avail_time: int = 0


class ActivityEnemyDuelModeData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelModeData"""

    mode_id: str | None = None
    is_multi_player: bool = False
    is_room: bool = False
    mode_type: str = "OPERATION"
    stage_ids: list[str] | None = None
    page_id: int = 0
    inner_sort_id: int = 0
    mode_name: str | None = None
    mode_short_name: str | None = None
    mode_en_name: str | None = None
    max_player: int = 0
    preposed_mode: str | None = None
    start_ts: int = 0
    end_ts: int = 0
    entry_pic_id: str | None = None
    title_pics: list[str] | None = None
    mode_target: str | None = None
    mode_desc: str | None = None
    mode_record_desc: str | None = None
    extra_tag: bool = False
    mode_avatar_pic_id: str | None = None
    mode_avatar_name: str | None = None
    mode_avatar_text: str | None = None
    has_unlock_toast: bool = False


class ActivityEnemyDuelRoundData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelRoundData"""

    round_id: str | None = None
    mode_id: str | None = None
    guess_time: int = 0
    round: int = 0
    enemy_predefined: bool = False
    round_score: int = 0
    enemy_score: float = 0.0
    enemy_score_random: float = 0.0
    enemy_side_min_left: int = 0
    enemy_side_max_left: int = 0
    enemy_side_min_right: int = 0
    enemy_side_max_right: int = 0
    enemy_pool_left: str | None = None
    enemy_pool_right: str | None = None
    can_skip: bool = False
    can_all_in: bool = False


class ActivityEnemyDuelPoolData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelPoolData"""

    enemy_id: str | None = None
    pool_normal: float = 0.0
    pool_small_enemy: float = 0.0
    pool_boss: float = 0.0
    pool_music: float = 0.0
    pool_no_surprise_enemy: float = 0.0
    pool_giant_boss: float = 0.0
    pool_anti_giant_boss: float = 0.0


class ActivityEnemyDuelNpcData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelNpcData"""

    npc_id: str | None = None
    avatar_id: str | None = None
    name: str | None = None
    priority: float = 0.0
    special_strategy: str = "DEFAULT"
    npc_prob: float = 0.0
    default_enemy_score: float = 0.0
    allin_prob: float = 0.0


class ActivityEnemyDuelNpcSelectorData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelNpcSelectorData"""

    enemy_id: str | None = None
    score: float = 0.0


class ActivityEnemyDuelNpcSelectorGroupData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelNpcSelectorGroupData"""

    npc_id: str | None = None
    data: list[ActivityEnemyDuelNpcSelectorData] | None = None


class ActivityEnemyDuelEnemyData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelEnemyData"""

    enemy_id: str | None = None
    original_enemy_id: str | None = None
    tag_type: str | None = None


class ActivityEnemyDuelExtraScoreData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelExtraScoreData"""

    rank_min: int = 0
    rank_max: int = 0
    token_num: int = 0


class ActivityEnemyDuelExtraScoreGroupData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelExtraScoreGroupData"""

    mode_id: str | None = None
    data: list[ActivityEnemyDuelExtraScoreData] | None = None


class ActivityEnemyDuelAnnounceData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelAnnounceData"""

    start_ts: int = 0
    end_ts: int = 0
    announce_text: str | None = None
    show_new: bool = False


class ActivityEnemyDuelSingleCommentData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelSingleCommentData"""

    comment_id: str | None = None
    priority: int = 0
    template: str | None = None
    param: list[str] | None = None
    comment_text: str | None = None


class ActivityEnemyDuelConstDataPingCond(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelConstData_PingCond"""

    cond: int = 0
    txt: str | None = None


class ActivityEnemyDuelConstData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelConstData"""

    max_loading_time: float = 0.0
    max_retry_time_in_battle: float = 0.0
    max_match_time: float = 0.0
    max_room_time: float = 0.0
    max_retry_time_in_team_room: float = 0.0
    room_reserve_time: float = 0.0
    min_room_num: int = 0
    room_finish_waiting_time: int = 0
    room_master_restart_waiting_time: int = 0
    ping_conds: list[ActivityEnemyDuelConstDataPingCond] | None = None
    chat_cd: float = 0.0
    chat_time: float = 0.0
    daily_mission_param: int = 0
    daily_mission_reward: ItemBundle | None = None
    daily_mission_name: str | None = None
    daily_mission_desc: str | None = None
    max_operator_delay: float = 0.0
    max_play_speed: float = 0.0
    delay_time_need_tip: float = 0.0
    net_block_time_need_tip: float = 0.0
    stage_time_max: float = 0.0
    npc_correct_prob: float = 0.0
    win_streak_round_num: int = 0
    settlement_pic_num: int = 0
    time_before_select_after_round_begin: int = 0
    npc_max_correct_count_in_stand: int = 0
    battle_phase_time_max: int = 0
    battle_finish_to_settle_time_max: int = 0
    min_bet_cd: float = 0.0
    default_emoticon_item_id: str | None = None
    default_emoticon_pic_id: str | None = None
    default_enemy_tag: str | None = None
    mode_operation_round_number: int = 0
    mode_operation_initial_score: int = 0
    mode_operation_max_score: int = 0
    mode_operation_select_time: int = 0
    mode_operation_select_time_last: int = 0
    mode_operation_skip_param: float = 0.0
    mode_operation_bet_param: float = 0.0
    mode_operation_allin_param: float = 0.0
    mode_operation_top_rank: int = 0
    mode_operation_rank_time: int = 0
    mode_solo_operation_rank_time: int = 0
    mode_operation_reward_multiplier: int = 0
    mode_operation_reward_multiplier_allin: int = 0
    mode_operation_hot_round_number: int = 0
    mode_solo_operation_select_time: int = 0
    mode_stand_round_number: int = 0
    mode_stand_shield_turn: int = 0
    mode_stand_select_time: int = 0
    mode_stand_select_time_last: int = 0
    mode_stand_allin_param: float = 0.0
    mode_stand_top_rank: int = 0
    mode_stand_rank_time: int = 0
    mode_stand_hot_round_number: int = 0
    milestone_name: str | None = None
    milestone_item_id: str | None = None
    milestone_item_name: str | None = None
    milestone_item_text: str | None = None
    milestone_track_id: str | None = None
    entry_video_id: str | None = None
    entry_tab_text: str | None = None
    match_tab_text: str | None = None
    mode_operation_id: str | None = None
    mode_stand_id: str | None = None
    multi_preposed_mode_id: str | None = None
    entry_music_name: str | None = None
    milestone_plan_name: str | None = None
    mode_cond_lock_text: str | None = None
    mode_time_lock_text: str | None = None
    title_pic_rotate_time: float = 0.0
    title_pic_id: str | None = None


class ActivityEnemyDuelConstToastData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelConstToastData"""

    create_room_alive_failed: str | None = None
    join_room_alive_failed: str | None = None
    room_id_format_error: str | None = None
    empty_room_id: str | None = None
    no_room: str | None = None
    continuous_clicks: str | None = None
    match_alive_failed: str | None = None
    server_overloaded: str | None = None
    match_timeout: str | None = None
    unlock_multi_mode: str | None = None
    unlock_room_mode: str | None = None
    add_friend_in_room: str | None = None
    room_id_copy_success: str | None = None
    entry_mode_lock: str | None = None


class ActivityEnemyDuelTipsData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelTipsData"""

    id: str | None = None
    txt: str | None = None
    weight: int = 0
    mode_ids: list[str] | None = None


class ActivityEnemyDuelData(GameDataModel):
    """clz_Torappu_ActivityEnemyDuelData"""

    milestone_list: list[ActivityEnemyDuelMilestoneItemData] | None = None
    mode_data: dict[str, ActivityEnemyDuelModeData] | None = None
    round_data: dict[str, ActivityEnemyDuelRoundData] | None = None
    pool_data: dict[str, ActivityEnemyDuelPoolData] | None = None
    npc_data: dict[str, ActivityEnemyDuelNpcData] | None = None
    npc_selector_data: dict[str, ActivityEnemyDuelNpcSelectorGroupData] | None = None
    enemy_data: dict[str, ActivityEnemyDuelEnemyData] | None = None
    extra_score_data: dict[str, ActivityEnemyDuelExtraScoreGroupData] | None = None
    basic_scores: list[int] | None = None
    announce_data: list[ActivityEnemyDuelAnnounceData] | None = None
    comment_data: dict[str, dict[str, ActivityEnemyDuelSingleCommentData]] | None = None
    const_data: ActivityEnemyDuelConstData | None = None
    const_toast_data: ActivityEnemyDuelConstToastData | None = None
    tips_data: list[ActivityEnemyDuelTipsData] | None = None
    enabled_emoticon_theme_id_list: list[str] | None = None


class Act42SideDataAct42SideTrustorData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideTrustorData"""

    trustor_id: str | None = None
    sort_id: int = 0
    trustor_name: str | None = None
    trustor_icon_small: str | None = None
    trustor_icon_large: str | None = None
    gun_id: str | None = None
    task_list: list[str] | None = None


class Act42SideDataAct42SideTaskData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideTaskData"""

    task_id: str | None = None
    preposed_task_id: str | None = None
    trustor_id: str | None = None
    trustor_name: str | None = None
    sort_id: int = 0
    task_name: str | None = None
    task_content: str | None = None
    after_task_content: str | None = None
    before_task_item_icon: str | None = None
    after_task_item_icon: str | None = None
    stage_id: str | None = None
    task_desc: str | None = None
    rewards: list[ItemBundle] | None = None


class Act42SideDataAct42SideGunData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideGunData"""

    gun_id: str | None = None
    gun_name: str | None = None
    trustor_name: str | None = None
    gun_content: str | None = None
    gun_small_icon: str | None = None
    gun_white_icon: str | None = None
    gun_color_icon: str | None = None


class Act42SideDataAct42SideFileData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideFileData"""

    content_id: str | None = None
    sort_id: int = 0


class Act42SideDataAct42SideDailyRewardData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideDailyRewardData"""

    completed_cnt: int = 0
    reward: ItemBundle | None = None


class Act42SideDataAct42SideConstData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideConstData"""

    coffee_name: str | None = None
    daily_coffee: int = 0
    coffee_limit: int = 0
    coffee_content: str | None = None
    min_gun_task_display: str | None = None
    unlock_stage_id: str | None = None
    toast_gun_task_completed: str | None = None
    toast_gun_task_locked: str | None = None
    toast_stage_block: str | None = None
    toast_entry_locked: str | None = None
    toast_file_locked: str | None = None
    toast_gun_locked: str | None = None
    toast_no_coffee: str | None = None
    toast_outer_unlock: str | None = None


class Act42SideDataAct42SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act42SideData_Act42SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act42SideData(GameDataModel):
    """clz_Torappu_Act42SideData"""

    trustor_data: dict[str, Act42SideDataAct42SideTrustorData] | None = None
    task_data: dict[str, Act42SideDataAct42SideTaskData] | None = None
    gun_data: dict[str, Act42SideDataAct42SideGunData] | None = None
    file_data: dict[str, Act42SideDataAct42SideFileData] | None = None
    daily_reward_list: list[Act42SideDataAct42SideDailyRewardData] | None = None
    const_data: Act42SideDataAct42SideConstData | None = None
    zone_addition_data_map: dict[str, Act42SideDataAct42SideZoneAdditionData] | None = (
        None
    )


class Act44SideDataAct44SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act44SideDataAct44SideCustomerData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideCustomerData"""

    id: str | None = None
    name: str | None = None
    img_id: str | None = None
    icon_id: str | None = None
    is_sp: bool = False
    description: str | None = None


class Act44SideDataAct44SideTagData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideTagData"""

    id: str | None = None
    name: str | None = None
    is_sp: bool = False
    description: str | None = None


class Act44SideDataAct44SideChoiceData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideChoiceData"""

    id: str | None = None
    img_id: str | None = None
    attention_arrow: int = 0
    trust_arrow: int = 0
    attention_value: int = 0
    trust_value: int = 0
    patience_value: int = 0


class Act44SideDataAct44SideNewsData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideNewsData"""

    id: str | None = None
    title: str | None = None
    desc_1: str | None = None
    desc_2: str | None = None
    img_id: str | None = None


class Act44SideDataAct44SideInsightData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideInsightData"""

    type: str = "PATIENCE"
    lower_desc: str | None = None
    recommend_desc: str | None = None
    max_desc: str | None = None


class Act44SideDataAct44SideMileStoneData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideMileStoneData"""

    mile_stone_id: str | None = None
    mile_stone_lvl: int = 0
    need_point_cnt: int = 0
    reward_item: ItemBundle | None = None


class Act44SideDataAct44SideMilestoneSpecialRewardInfo(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideMilestoneSpecialRewardInfo"""

    item_name: str | None = None
    point: int = 0


class Act44SideDataAct44SideConstData(GameDataModel):
    """clz_Torappu_Act44SideData_Act44SideConstData"""

    informant_unlock_stage_id: str | None = None
    informant_item_id: str | None = None
    informant_item_type: str = "NONE"
    informant_item_count: int = 0
    milestone_item_id: str | None = None
    attention_max: int = 0
    trust_max: int = 0
    attention_min: int = 0
    trust_min: int = 0
    patience_rc_round_num: int = Field(default=0, alias="patienceRCRoundNum")
    beginner_patience_rc_round_num: int = Field(
        default=0, alias="beginnerPatienceRCRoundNum"
    )
    special_customer_list_id: list[str] | None = None
    milestone_reward_list: (
        list[Act44SideDataAct44SideMilestoneSpecialRewardInfo] | None
    ) = None
    for_count_big_success: int = 0
    outer_open_unlock: str | None = None
    customer_tag_format: str | None = None


class Act44SideData(GameDataModel):
    """clz_Torappu_Act44SideData"""

    zone_addition_data_map: dict[str, Act44SideDataAct44SideZoneAdditionData] | None = (
        None
    )
    customer_data_map: dict[str, Act44SideDataAct44SideCustomerData] | None = None
    tag_data_map: dict[str, Act44SideDataAct44SideTagData] | None = None
    choice_data_map: dict[str, Act44SideDataAct44SideChoiceData] | None = None
    customer_dialog_map: dict[str, str] | None = None
    keeper_dialog_map: dict[str, str] | None = None
    news_data_map: dict[str, Act44SideDataAct44SideNewsData] | None = None
    insight_desc_map: dict[str, Act44SideDataAct44SideInsightData] | None = None
    mile_stone_list: list[Act44SideDataAct44SideMileStoneData] | None = None
    const_data: Act44SideDataAct44SideConstData | None = None


class Act1VHalfIdleGachaPoolDataConsumeData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleGachaPoolData_ConsumeData"""

    gacha_times: int = 0
    consume: int = 0


class Act1VHalfIdleGachaPoolData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleGachaPoolData"""

    pool_id: str | None = None
    item_id: str | None = None
    pool_type: str = "NONE"
    sort_id: int = 0
    name: str | None = None
    char_data: list[str] | None = None
    consume_data: list[Act1VHalfIdleGachaPoolDataConsumeData] | None = None


class Act1VHalfIdleGachaCharData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleGachaCharData"""

    char_id: str | None = None
    is_linkage_char: bool = False


class Act1VHalfIdlePlotTypeData(GameDataModel):
    """clz_Torappu_Act1VHalfIdlePlotTypeData"""

    plot_type: str = "NONE"
    type_name: str | None = None
    plot_squad_limit: dict[str, list[int]] | None = None


class Act1VHalfIdlePlotDataItemDropData(GameDataModel):
    """clz_Torappu_Act1VHalfIdlePlotData_ItemDropData"""

    item_id: str | None = None
    item_drop_desc: str | None = None


class Act1VHalfIdlePlotDataPlotCombineDataCombineItemData(GameDataModel):
    """clz_Torappu_Act1VHalfIdlePlotData_PlotCombineData_CombineItemData"""

    plot_id: str | None = None
    plot_count: int = 0


class Act1VHalfIdlePlotDataPlotCombineData(GameDataModel):
    """clz_Torappu_Act1VHalfIdlePlotData_PlotCombineData"""

    combine_type: str = "NONE"
    plots: list[Act1VHalfIdlePlotDataPlotCombineDataCombineItemData] | None = None


class Act1VHalfIdlePlotData(GameDataModel):
    """clz_Torappu_Act1VHalfIdlePlotData"""

    plot_id: str | None = None
    plot_name: str | None = None
    plot_type: str = "NONE"
    trap_id: str | None = None
    init_unlock: bool = False
    rarity: int = 0
    sort_id: int = 0
    is_base_plot: bool = False
    icon_id: str | None = None
    func_desc: str | None = None
    flavor_desc: str | None = None
    enemy_ids: list[str] | None = None
    enemy_desc: str | None = None
    item_id_shown: str | None = None
    item_drop_data: list[Act1VHalfIdlePlotDataItemDropData] | None = None
    prev_combine_data: Act1VHalfIdlePlotDataPlotCombineData | None = None
    derived_plots: list[str] | None = None


class Act1VHalfIdleStageProductionDataItemProductionData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleStageProductionData_ItemProductionData"""

    item_id: str | None = None
    efficiency_max: int = 0
    is_fixed: bool = False
    max_drop_value: int = 0


class Act1VHalfIdleStageProductionData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleStageProductionData"""

    stage_id: str | None = None
    fixed_production: list[str] | None = None
    production_data: (
        dict[str, Act1VHalfIdleStageProductionDataItemProductionData] | None
    ) = None


class Act1VHalfIdleCharRankDataCharRankData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharRankData_CharRankData"""

    level: int = 0
    accumulated_exp: int = 0
    exp: int = 0


class Act1VHalfIdleCharRankData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharRankData"""

    evolve_phase: str = "PHASE_0"
    exp_data: list[Act1VHalfIdleCharRankDataCharRankData] | None = None


class Act1VHalfIdleCharEvolveDataEvolveData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharEvolveData_EvolveData"""

    evolve_phase: str = "PHASE_0"
    item_id: str | None = None
    item_count: int = 0
    rebate_item_id: str | None = None
    rebate_item_count: int = 0


class Act1VHalfIdleCharEvolveDataProfessionCharEvolveData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharEvolveData_ProfessionCharEvolveData"""

    profession: str = "NONE"
    evolve_data: dict[str, Act1VHalfIdleCharEvolveDataEvolveData] | None = None


class Act1VHalfIdleCharEvolveData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharEvolveData"""

    rarity: str = "TIER_1"
    profession_evolve_data: (
        dict[str, Act1VHalfIdleCharEvolveDataProfessionCharEvolveData] | None
    ) = None


class Act1VHalfIdleCharMaxRankDataMaxRankData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharMaxRankData_MaxRankData"""

    evolve_phase: str = "PHASE_0"
    max_level: int = 0
    max_skill_rank: int = 0


class Act1VHalfIdleCharMaxRankData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharMaxRankData"""

    rarity: str = "TIER_1"
    max_rank_data: dict[str, Act1VHalfIdleCharMaxRankDataMaxRankData] | None = None
    max_evolve_phase: str = "PHASE_0"


class Act1VHalfIdleCharSkillRankDataSkillRankData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharSkillRankData_SkillRankData"""

    skill_level: int = 0
    cost: int = 0
    accumulated_cost: int = 0


class Act1VHalfIdleCharSkillRankData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharSkillRankData"""

    rarity: str = "TIER_1"
    skill_rank_data: list[Act1VHalfIdleCharSkillRankDataSkillRankData] | None = None


class Act1VHalfIdleTechTreeDataEffect(GameDataModel):
    """clz_Torappu_Act1VHalfIdleTechTreeData_Effect"""

    desc: str | None = None
    title: str | None = None
    icon_id: str | None = None
    rune_datas: list[RuneTablePackedRuneData] | None = None


class Act1VHalfIdleTechTreeData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleTechTreeData"""

    node_id: str | None = None
    node_type: str = "NONE"
    prev_node_id: list[str] | None = None
    token_cost: int = 0
    name: str | None = None
    icon_id: str | None = None
    show_prev_lock_tips: bool = False
    effect: list[Act1VHalfIdleTechTreeDataEffect] | None = None


class Act1VHalfIdleCharBuffInfo(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharBuffInfo"""

    id: str | None = None
    level: int = 0
    char_count: int = 0
    desc: str | None = None
    rune_data: RuneTablePackedRuneData | None = None


class Act1VHalfIdleCharBuffData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleCharBuffData"""

    prof: str = "NONE"
    buff_infos: list[Act1VHalfIdleCharBuffInfo] | None = None


class Act1VHalfIdleMilestoneItemData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleMilestoneItemData"""

    milestone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    reward: ItemBundle | None = None
    avail_time: int = 0


class Act1VHalfIdleGachaPoolTypeData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleGachaPoolTypeData"""

    pool_type: str = "NONE"
    type_name: str | None = None
    desc: str | None = None
    sort_id: int = 0


class Act1VHalfIdleEnemyPreloadMeta(GameDataModel):
    """clz_Torappu_Act1VHalfIdleEnemyPreloadMeta"""

    enemy_id: str | None = None
    level: int = 0


class Act1VHalfIdleConstDataProfessionDesc(GameDataModel):
    """clz_Torappu_Act1VHalfIdleConstData_ProfessionDesc"""

    profession: str = "NONE"
    desc: str | None = None


class Act1VHalfIdleConstData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleConstData"""

    income_production_items: list[str] | None = None
    milestone_id: str | None = None
    discount: list[int] | None = None
    skill_levels: list[int] | None = None
    level_exp_item_id: str | None = None
    skill_exp_item_id: str | None = None
    normal_stage_ids: list[str] | None = None
    hard_stage_ids: list[str] | None = None
    tech_cost_item_id: str | None = None
    assist_base_num: int = 0
    preload_enemy: list[Act1VHalfIdleEnemyPreloadMeta] | None = None
    preload_trap: list[str] | None = None
    default_max_discount_skill_level: int = 0
    npc_max_discount_skill_level: int = 0
    forbidden_assist_char_ids: list[str] | None = None
    max_evolve_phase: int = 0
    max_safe_enemy_duration: int = 0
    overload_lose_life_point: int = 0
    trap_modify_boss_trigger_time: int = 0
    normal_enemy_overload_cnt: int = 0
    elite_enemy_overload_cnt: int = 0
    boss_enemy_overload_cnt: int = 0
    max_equip_num_in_bag: int = 0
    boss_branch_name: str | None = None
    boss_preview_branch_name: str | None = None
    enemy_capacity_id_white_list: list[str] | None = None
    unlock_stage_id: str | None = None
    profession_desc: list[Act1VHalfIdleConstDataProfessionDesc] | None = None
    product_max_efficiency_dict: dict[str, int] | None = None
    efficiency_duration_max: int = 0
    produce_cd: int = 0
    harvest_hint_threshold_time: int = 0
    const_rune_datas: list[RuneTablePackedRuneData] | None = None
    milestone_track_id: str | None = None
    max_deck_card_num: int = 0
    tutorial_stage_id: str | None = None
    predefined_plot_ids: list[str] | None = None
    predefined_char_ids: list[str] | None = None
    enemy_overload_warning_ratio: float = 0.0
    battle_finish_warning_time: int = 0
    gacha_num_max: int = 0
    battle_custom_tile_highlight_color: str | None = None
    battle_custom_tile_emission_color: str | None = None
    battle_equip_level_colors: list[str] | None = None
    battle_fail_hint_str: list[str] | None = None
    trap_drop_weight_step: int = 0
    unlock_special_plot: list[str] | None = None
    boss_enter_bgm_key: str | None = None


class UnityEngineVector2(GameDataModel):
    """clz_UnityEngine_Vector2"""

    x: float = 0.0
    y: float = 0.0


class Act1VHalfIdleDiagramDataPointPosData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleDiagramData_PointPosData"""

    pos: UnityEngineVector2 | None = None


class Act1VHalfIdleDiagramDataLinePosData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleDiagramData_LinePosData"""

    start_pos: UnityEngineVector2 | None = None
    end_pos: UnityEngineVector2 | None = None


class Act1VHalfIdleDiagramDataLineRelationData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleDiagramData_LineRelationData"""

    start_point_list: list[str] | None = None
    end_point_list: list[str] | None = None


class Act1VHalfIdleDiagramDataNodePointData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleDiagramData_NodePointData"""

    node_id: str | None = None


class Act1VHalfIdleDiagramData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleDiagramData"""

    width: float = 0.0
    height: float = 0.0
    point_pos_data_map: dict[str, Act1VHalfIdleDiagramDataPointPosData] | None = None
    line_pos_data_map: dict[str, Act1VHalfIdleDiagramDataLinePosData] | None = None
    line_relation_data_map: (
        dict[str, Act1VHalfIdleDiagramDataLineRelationData] | None
    ) = None
    node_point_data_map: dict[str, Act1VHalfIdleDiagramDataNodePointData] | None = None


class Act1VHalfIdleEnemyDropBundle(GameDataModel):
    """clz_Torappu_Act1VHalfIdleEnemyDropBundle"""

    exp: int = 0
    mile_stone_cnt: int = 0
    battle_item_drop_pool: str | None = None
    resource_item_drop_pool: str | None = None


class Act1VWeightedBattleItemPool(GameDataModel):
    """clz_Torappu_Act1VWeightedBattleItemPool"""

    pool_key: str | None = None
    type: str = "EQUIP"
    weight: float = 0.0


class Act1VBattleItemDropSlot(GameDataModel):
    """clz_Torappu_Act1VBattleItemDropSlot"""

    prob: float = 0.0
    item_pools: list[Act1VWeightedBattleItemPool] | None = None


class Act1VWeightedResItemBundle(GameDataModel):
    """clz_Torappu_Act1VWeightedResItemBundle"""

    weight: float = 0.0
    resources: dict[str, int] | None = None


class Act1VHalfIdleWeightedBattleEquip(GameDataModel):
    """clz_Torappu_Act1VHalfIdleWeightedBattleEquip"""

    weight: float = 0.0
    equip_id: str | None = None
    level: int = 0
    alias: str | None = None


class Act1VHalfIdleEquipData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleEquipData"""

    equip_id: str | None = None
    alias: str | None = None
    icon_id: str | None = None
    name: str | None = None
    level: int = 0
    equip_type: str = "WEAPON"
    rune_data: RuneTablePackedRuneData | None = None


class Act1VHalfIdleTrapMeta(GameDataModel):
    """clz_Torappu_Act1VHalfIdleTrapMeta"""

    trap_type: str = "NONE"
    build_type: str = "NONE"
    skill_index: int = 0
    drop_weight: float = 0.0
    default_plot_id: str | None = None


class Act1VHalfIdleData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleData"""

    gacha_pool_data: dict[str, Act1VHalfIdleGachaPoolData] | None = None
    gacha_char_data: dict[str, Act1VHalfIdleGachaCharData] | None = None
    plot_type_data: dict[str, Act1VHalfIdlePlotTypeData] | None = None
    plot_data: dict[str, Act1VHalfIdlePlotData] | None = None
    stage_production_data: dict[str, Act1VHalfIdleStageProductionData] | None = None
    char_rank_data: dict[str, Act1VHalfIdleCharRankData] | None = None
    char_evolve_data: dict[str, Act1VHalfIdleCharEvolveData] | None = None
    char_max_rank_data: dict[str, Act1VHalfIdleCharMaxRankData] | None = None
    char_skill_rank_data: dict[str, Act1VHalfIdleCharSkillRankData] | None = None
    tech_tree_data: dict[str, Act1VHalfIdleTechTreeData] | None = None
    char_buff_data: list[Act1VHalfIdleCharBuffData] | None = None
    milestone_list: list[Act1VHalfIdleMilestoneItemData] | None = None
    pool_type_data: list[Act1VHalfIdleGachaPoolTypeData] | None = None
    stage_ids: list[str] | None = None
    zone_id: str | None = None
    const_data: Act1VHalfIdleConstData | None = None
    diagram_list: list[Act1VHalfIdleDiagramData] | None = None
    enemy_item_drop_pool_dict: dict[str, Act1VHalfIdleEnemyDropBundle] | None = None
    battle_item_pool_dict: dict[str, list[Act1VBattleItemDropSlot]] | None = None
    resource_item_pool_dict: dict[str, list[Act1VWeightedResItemBundle]] | None = None
    equip_item_pool_dict: dict[str, list[Act1VHalfIdleWeightedBattleEquip]] | None = (
        None
    )
    trap_item_pool_dict: dict[str, list[str]] | None = None
    equip_item_data: dict[str, dict[int, list[Act1VHalfIdleEquipData]]] | None = None
    trap_meta_dict: dict[str, Act1VHalfIdleTrapMeta] | None = None
    plot_show_combine_highlight_dict: dict[str, list[str]] | None = None


class Act45SideDataAct45SideCharData(GameDataModel):
    """clz_Torappu_Act45SideData_Act45SideCharData"""

    char_id: str | None = None
    sort_id: int = 0
    char_illust_id: str | None = None
    char_card_id: str | None = None
    char_name: str | None = None
    unlock_stage_id: str | None = None


class Act45SideDataAct45SideMailData(GameDataModel):
    """clz_Torappu_Act45SideData_Act45SideMailData"""

    mail_id: str | None = None
    sort_id: int = 0
    char_name: str | None = None
    pic_id: str | None = None
    mail_title: str | None = None
    mail_content: str | None = None
    send_time: int = 0
    rewards: list[ItemBundle] | None = None


class Act45SideDataAct45SideConstData(GameDataModel):
    """clz_Torappu_Act45SideData_Act45SideConstData"""

    entry_stage_id: str | None = None
    toast_char_unlock: str | None = None
    toast_live_page_unlock: str | None = None
    toast_live_page_locked: str | None = None
    text_char_locked: str | None = None
    text_mail_time: str | None = None
    text_btn_mail_time: str | None = None
    game_tv_size_music_id: str | None = Field(default=None, alias="gameTVSizeMusicId")
    game_full_size_music_id: str | None = None
    entry_music_id: str | None = None


class Act45SideDataAct45SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act45SideData_Act45SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act45SideData(GameDataModel):
    """clz_Torappu_Act45SideData"""

    char_data: dict[str, Act45SideDataAct45SideCharData] | None = None
    mail_data: dict[str, Act45SideDataAct45SideMailData] | None = None
    const_data: Act45SideDataAct45SideConstData | None = None
    zone_addition_data_map: dict[str, Act45SideDataAct45SideZoneAdditionData] | None = (
        None
    )


class ActRecruitOnlyDataRecruitOnlyItemData(GameDataModel):
    """clz_Torappu_ActRecruitOnlyData_RecruitOnlyItemData"""

    id: str | None = None
    phase_num: int = 0
    tag_id: int = 0
    tag_times: int = 0
    start_time: int = 0
    end_time: int = 0
    start_time_desc: str | None = None
    end_time_desc: str | None = None
    desc_1: str | None = None
    desc_2: str | None = None


class ActRecruitOnlyData(GameDataModel):
    """clz_Torappu_ActRecruitOnlyData"""

    recruit_data: ActRecruitOnlyDataRecruitOnlyItemData | None = None
    preview_data: ActRecruitOnlyDataRecruitOnlyItemData | None = None


class Act46SideDataAct46SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act46SideData_Act46SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act46SideDataAct46SideMonopolyStageData(GameDataModel):
    """clz_Torappu_Act46SideData_Act46SideMonopolyStageData"""

    stage_id: str | None = None
    sort_id: int = 0
    start_ts: int = 0
    stage_name: str | None = None
    stage_desc: str | None = None
    task_required_amount: int = 0
    reward_list: list[ItemBundle] | None = None
    buff_id_list: list[str] | None = None
    bg_sprite_id: str | None = None
    max_turn: int = 0
    node_icon_style_index_list: list[int] | None = None
    valid_resource_id_list: list[str] | None = None


class Act46SideDataAct46SideMonopolyBuffData(GameDataModel):
    """clz_Torappu_Act46SideData_Act46SideMonopolyBuffData"""

    buff_id: str | None = None
    buff_icon_id: str | None = None
    buff_name: str | None = None
    buff_desc: str | None = None


class Act46SideDataAct46SideSettleDialogData(GameDataModel):
    """clz_Torappu_Act46SideData_Act46SideSettleDialogData"""

    character_avatar_id: str | None = None
    dialog_text: str | None = None


class Act46SideDataAct46SideConstData(GameDataModel):
    """clz_Torappu_Act46SideData_Act46SideConstData"""

    training_stage_id: str | None = None
    excellent_rate: list[int] | None = None
    entry_requirement: str | None = None
    business_unlock_text: str | None = None
    map_node_start_icon: str | None = None
    combo_task_progress_count: int = 0


class Act46SideDataAct46SideMonopolyResourceItemData(GameDataModel):
    """clz_Torappu_Act46SideData_Act46SideMonopolyResourceItemData"""

    resource_id: str | None = None
    sort_id: int = 0


class Act46SideData(GameDataModel):
    """clz_Torappu_Act46SideData"""

    zone_addition_data_map: dict[str, Act46SideDataAct46SideZoneAdditionData] | None = (
        None
    )
    monopoly_stage_data_map: (
        dict[str, Act46SideDataAct46SideMonopolyStageData] | None
    ) = None
    buff_data_map: dict[str, Act46SideDataAct46SideMonopolyBuffData] | None = None
    settle_dialog_data_map: (
        dict[str, dict[str, list[Act46SideDataAct46SideSettleDialogData]]] | None
    ) = None
    const_data: Act46SideDataAct46SideConstData | None = None
    resource_item_data_map: (
        dict[str, Act46SideDataAct46SideMonopolyResourceItemData] | None
    ) = None


class ActAutoChessDataActAutoChessModeData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessModeData"""

    mode_id: str | None = None
    name: str | None = None
    code: str | None = None
    sort_id: int = 0
    background_id: str | None = None
    desc: str | None = None
    difficulty: int = 0
    factor: float = 0.0
    difficulty_desc: str | None = None
    trophy_desc: str | None = None
    event_ids: list[str] | None = None
    unlock_text: str | None = None
    loading_pic_id: str | None = None
    mode_type: str = "LOCAL"
    mode_difficulty: str = "TRAINING"
    mode_icon_id: str | None = None
    mode_color: str | None = None
    special_phase_time: int = 0
    active_bond_id_list: list[str] | None = None
    inactive_bond_id_list: list[str] | None = None
    inactive_enemy_key: list[str] | None = None
    start_time: int = 0
    unlock_diffierent_mode_id: str | None = None
    group_list: list[str] | None = None


class ActAutoChessDataActAutoChessModeGroupData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessModeGroupData"""

    group_type: str = "GROUP_MULTI"
    mode_type: str = "NONE"
    will_expand: bool = False
    mode_ids: list[str] | None = None


class ActAutoChessDataActAutoChessShopLevelDisplayData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessShopLevelDisplayData"""

    shop_level: int = 0
    level_tag_bg_color: str | None = None
    is_level_char_chess_empty: bool = False
    is_level_trap_chess_empty: bool = False
    char_chess_diy_slot_id_list: list[str] | None = None


class ActAutoChessDataActAutoChessStageData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessStageData"""

    stage_id: str | None = None
    mode: list[str] | None = None
    weight: int = 0


class ActAutoChessDataActAutochessSpecialEnemyTypeEntry(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutochessSpecialEnemyTypeEntry"""

    count: int = 0
    count_single: int = 0
    weight: int = 0
    show_enemy_id: str | None = None


class ActivityCommonMilestoneData(GameDataModel):
    """clz_Torappu_ActivityCommonMilestoneData"""

    milestone_id: str | None = None
    milestone_lvl: int = 0
    token_num: int = 0
    reward_item: ItemBundle | None = None
    available_time: int = 0


class ActivityPeriodicalRewardConf(GameDataModel):
    """clz_Torappu_ActivityPeriodicalRewardConf"""

    id: str | None = None
    periodical_point_cost: int = 0
    sort_index: int = 0
    rewards: list[MissionDisplayRewards] | None = None


class ActAutoChessDataActAutoChessPlayerTitleData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessPlayerTitleData"""

    id: str | None = None
    type: str | None = None
    point: int = 0
    rank: int = 0
    pic_id: str | None = None
    txt: str | None = None


class ActAutoChessDataActAutoChessShopCharChessInfoData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessShopCharChessInfoData"""

    chess_level: int = 0
    is_golden: bool = False
    evolve_phase: str = "PHASE_0"
    char_level: int = 0
    skill_level: int = 0
    favor_point: int = 0
    equip_level: int = 0
    purchase_price: int = 0
    chess_sold_price: int = 0
    elite_icon_id: str | None = None


class ActAutoChessDataActAutoChessConstData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessConstData"""

    shop_refresh_price: int = 0
    max_deck_chess_cnt: int = 0
    max_deck_equipment_chess_cnt: int = 0
    max_battle_chess_cnt: int = 0
    fallback_bond_id: str | None = None
    store_cnt_max: int = 0
    cost_player_hp_limit: int = 0
    borrow_count: int = 0
    milestone_id: str | None = None
    daily_mission_param: int = 0
    daily_mission_name: str | None = None
    daily_mission_rule: str | None = None
    milestone_track_id: str | None = None
    escaped_battle_template_map_single_player: str | None = None
    escaped_battle_template_map_multi_player: str | None = None
    web_bus_type: str | None = None
    web_update_log_bus_type: str | None = None
    item_max_count: int = 0
    diy_char_limit_for_levels: dict[int, int] | None = None
    perm_shop_logo_id: str | None = None
    content_update_time: int = 0
    system_custom_char: list[str] | None = None
    boss_icon_id: str | None = None
    mode_warning_diff: int = 0
    perfect_battle_voice_round: int = 0
    lose_hp_voice_round: int = 0
    bond_voice_layers: list[int] | None = None
    shop_tag_warm_up_id: str | None = None


class UITemplateShopTemplateShopDataShopGood(GameDataModel):
    """clz_Torappu_UI_TemplateShop_TemplateShopData_ShopGood"""

    good_id: str | None = None
    display_name: str | None = None
    sort_id: int = 0
    good_type: str = "NORMAL"
    item: ItemBundle | None = None
    progress_good_id: str | None = None
    price: int = 0
    avail_count: int = 0


class UITemplateShopTemplateShopDataProgessGoodItem(GameDataModel):
    """clz_Torappu_UI_TemplateShop_TemplateShopData_ProgessGoodItem"""

    order: int = 0
    price: int = 0
    display_name: str | None = None
    item: ItemBundle | None = None


class UITemplateShopTemplateShopDataTShopGroup(GameDataModel):
    """clz_Torappu_UI_TemplateShop_TemplateShopData_TShopGroup"""

    shop_group_id: str | None = None
    sort_id: int = 0
    pre_group: str | None = None
    bkg_icon_id: str | None = None
    lock_desc: str | None = None
    shop_good: dict[str, UITemplateShopTemplateShopDataShopGood] | None = None
    progress_goods: (
        dict[str, list[UITemplateShopTemplateShopDataProgessGoodItem]] | None
    ) = None


class UITemplateShopTemplateShopDataGroupShopExtraData(GameDataModel):
    """clz_Torappu_UI_TemplateShop_TemplateShopData_GroupShopExtraData"""

    in_time_text: str | None = None
    all_end_text: str | None = None


class UITemplateShopTemplateShopDataShopAccumulativePrizeItem(GameDataModel):
    """clz_Torappu_UI_TemplateShop_TemplateShopData_ShopAccumulativePrizeItem"""

    prize_id: str | None = None
    sort_id: int = 0
    pic_id: str | None = None
    item_id: str | None = None
    item_type: str = "NONE"
    count: int = 0
    cost_total: int = 0
    acquire_title: str | None = None
    display_name: str | None = None
    display_discription: str | None = None


class UITemplateShopTemplateShopData(GameDataModel):
    """clz_Torappu_UI_TemplateShop_TemplateShopData"""

    shop_id: str | None = None
    shop_name: str | None = None
    type: str = "NORMAL"
    price: ItemBundle | None = None
    shop_group: dict[str, UITemplateShopTemplateShopDataTShopGroup] | None = None
    icon_color_codes: str | None = None
    button_color_codes: str | None = None
    start_time: int = 0
    end_time: int = 0
    group_extra_data: UITemplateShopTemplateShopDataGroupShopExtraData | None = None
    accumulative_prize_goods: (
        dict[str, UITemplateShopTemplateShopDataShopAccumulativePrizeItem] | None
    ) = None


class ActAutoChessDataActAutoChessBandData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessBandData"""

    band_id: str | None = None
    sort_id: int = 0
    band_type: str = "NONE"
    inactive_mode_id_list: list[str] | None = None
    band_desc: str | None = None
    total_hp: int = 0
    effect_id: str | None = None
    victor_count: int = 0
    master_victor_count: int = 0
    band_reward_modulus: float = 0.0
    offseason_priority: int = 0
    relate_bond_list: list[str] | None = None


class ActAutoChessDataActAutoChessBondInfo(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessBondInfo"""

    bond_id: str | None = None
    name: str | None = None
    desc: str | None = None
    icon_id: str | None = None
    active_count: int = 0
    active_condition: str = "BOARD"
    active_condition_template: str | None = None
    active_param_list: list[str] | None = None
    effect_id: str | None = None
    active_type: str = "BATTLE"
    identifier: int = 0
    weight: int = 0
    is_active_in_deck: bool = False
    max_inactive_bond_count: int = 0
    no_stack: bool = False
    no_select: bool = False
    chess_id_list: list[str] | None = None


class ActAutoChessDataActAutoChessGarrisonData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessGarrisonData"""

    garrison_desc: str | None = None
    event_type: str | None = None
    event_type_desc: str | None = None
    event_type_icon: str | None = None
    event_type_small_icon: str | None = None
    event_effect: str | None = None
    effect_type: str | None = None
    char_level: int = 0
    battle_rune_key: str | None = None
    blackboard: list[BlackboardDataPair] | None = None
    description: str | None = None


class ActAutoChessDataActAutoChessEffectDescParamInfo(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessEffectDescParamInfo"""

    desc_param_base: str | None = None
    desc_param_per_stack: str | None = None
    desc_param_max: float = 0.0


class ActAutoChessDataActAutoChessEffectDescParamData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessEffectDescParamData"""

    desc_param_infos: list[ActAutoChessDataActAutoChessEffectDescParamInfo] | None = (
        None
    )
    phase_type: str = "NONE"
    bond_phase_count_list: list[int] | None = None


class ActAutoChessDataActAutoChessEffectInfoData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessEffectInfoData"""

    effect_id: str | None = None
    effect_type: str = "NONE"
    effect_counter_type: str = "NONE"
    continued_round: int = 0
    effect_name: str | None = None
    effect_desc: str | None = None
    effect_deco_icon_id: str | None = None
    enemy_price: int = 0
    show_tag: str | None = None
    display_in_hud: bool = Field(default=False, alias="displayInHUD")


class ActAutoChessDataActAutoChessSkillInfoData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessSkillInfoData"""

    effect_id: str | None = None
    skill_desc: str | None = None
    skill_type: str = "NONE"
    skill_cost: int = 0
    skill_avail_type: str = "DEFAULT"
    skill_avail_count: int = 0
    unlock_type: str | None = None
    unlock_param: list[str] | None = None
    minor_unlock: bool = False
    unlock_effect_id: str | None = None
    target_type: str | None = None
    target_filter_type: str | None = None
    target_tip: str | None = None
    is_unusable_at_special_recruit: bool = False
    band_id: str | None = None


class ActAutoChessDataActAutoChessBuffInfoData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessBuffInfoData"""

    key: str | None = None
    blackboard: list[BlackboardDataPair] | None = None


class ActAutoChessDataActAutoChessShopLevelData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessShopLevelData"""

    shop_level: int = 0
    initial_upgrade_price: int = 0
    char_chess_count: int = 0
    item_count: int = 0
    level_tag_bg_color: str | None = None


class ActAutoChessDataActAutoChessCharChessStatusData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessCharChessStatusData"""

    evolve_phase: str = "PHASE_0"
    char_level: int = 0
    skill_level: int = 0
    favor_point: int = 0
    equip_level: int = 0


class ActAutoChessDataActAutoChessCharChessData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessCharChessData"""

    chess_id: str | None = None
    identifier: int = 0
    is_golden: bool = False
    status: ActAutoChessDataActAutoChessCharChessStatusData | None = None
    upgrade_chess_id: str | None = None
    upgrade_num: int = 0
    equip_slot_num: int = 0
    show_tag: str | None = None
    bond_ids: list[str] | None = None
    garrison_ids: list[str] | None = None
    desc: str | None = None


class ActAutoChessDataActAutoChessCharShopChessData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessCharShopChessData"""

    chess_id: str | None = None
    golden_chess_id: str | None = None
    chess_level: int = 0
    shop_level_sort_id: int = 0
    chess_type: str = "NORMAL"
    char_id: str | None = None
    tmpl_id: str | None = None
    default_skill_index: int = 0
    default_uni_equip_id: str | None = None
    backup_char_id: str | None = None
    backup_tmpl_id: str | None = None
    backup_char_skill_index: int = 0
    backup_char_uni_equip_id: str | None = None
    backup_char_pot_rank: int = 0
    is_hidden: bool = False


class ActAutoChessDataAutoChessTrapChessStatusData(GameDataModel):
    """clz_Torappu_ActAutoChessData_AutoChessTrapChessStatusData"""

    evolve_phase: str = "PHASE_0"
    trap_level: int = 0
    skill_index: int = 0
    skill_level: int = 0


class ActAutoChessDataActAutoChessTrapChessData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessTrapChessData"""

    chess_id: str | None = None
    identifier: int = 0
    char_id: str | None = None
    is_golden: bool = False
    purchase_price: int = 0
    status: ActAutoChessDataAutoChessTrapChessStatusData | None = None
    upgrade_chess_id: str | None = None
    upgrade_num: int = 0
    trap_duration: int = 0
    effect_id: str | None = None
    give_bond_id: str | None = None
    can_give_bond: bool = False
    can_fuse: bool = False
    fuse_with: str | None = None
    fuse_result: str | None = None
    item_type: str = "CHAR"


class ActAutoChessDataActAutoChessTrapShopChessData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessTrapShopChessData"""

    item_id: str | None = None
    golden_item_id: str | None = None
    hide_in_shop: bool = False
    item_level: int = 0
    icon_level: int = 0
    shop_level_sort_id: int = 0
    item_type: str = "CHAR"
    trap_id: str | None = None


class ActAutoChessDataActAutoChessEffectChoiceInfoData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessEffectChoiceInfoData"""

    choice_event_id: str | None = None
    choice_type: str = "EQUIP_FREE"
    effect_type: str = "NONE"
    selection_type: str = "ROBIN"
    name: str | None = None
    desc: str | None = None


class ActAutoChessDataActAutoChessBattleData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessBattleData"""

    boss_id: str | None = None
    level_id: str | None = None
    is_sp_prepare: bool = False


class ActAutoChessDataActAutochessBossEntry(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutochessBossEntry"""

    boss_id: str | None = None
    sort_id: int = 0
    weight: int = 0
    blood_data_dict: dict[str, int] | None = None
    is_hiding_boss: bool = False


class ActAutoChessDataActAutochessSpecialEnemyEntry(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutochessSpecialEnemyEntry"""

    type: str | None = None
    special_enemy_key: str | None = None
    random_weight: int = 0
    is_in_first_half: bool = False
    attached_normal_enemy_keys: list[str] | None = None
    attached_elite_enemy_keys: list[str] | None = None


class ActAutoChessDataActAutoChessTrainingNpcData(GameDataModel):
    """clz_Torappu_ActAutoChessData_ActAutoChessTrainingNpcData"""

    npc_id: str | None = None
    char_id: str | None = None
    name_card_skin_id: str | None = None
    medal_count: int = 0
    band_id: str | None = None


class AutoChessDataAutoChessBandData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessBandData"""

    band_id: str | None = None
    band_name: str | None = None
    band_icon_id: str | None = None
    unlock_desc: str | None = None


class AutoChessDataAutoChessBondInfoData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessBondInfoData"""

    bond_id: str | None = None
    bond_type: str = "NONE"
    power_id_list: list[str] | None = None
    name: str | None = None
    icon: str | None = None
    is_power: bool = False
    bond_order: int = 0
    is_hidden_char_list: bool = False


class AutoChessDataAutoChessBossInfoData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessBossInfoData"""

    boss_id: str | None = None
    enemy_id: str | None = None
    handbook_enemy_id: str | None = None


class AutoChessDataAutoChessRandomEnemyAttributeData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessRandomEnemyAttributeData"""

    enemy_key: str | None = None
    level: int = 0
    extra_enemy_identifier: int = 0
    extra_enemy_key_list: list[str] | None = None
    is_fly_enemy: bool = False
    enemy_battle_effectiveness_factor: float = 0.0


class ActAutoChessTrainingDataAutoChessTrainingData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_AutoChessTrainingData"""

    band_data_dict: dict[str, AutoChessDataAutoChessBandData] | None = None
    bond_data_dict: dict[str, AutoChessDataAutoChessBondInfoData] | None = None
    boss_info_dict: dict[str, AutoChessDataAutoChessBossInfoData] | None = None
    random_enemy_attribute_dict: (
        dict[str, AutoChessDataAutoChessRandomEnemyAttributeData] | None
    ) = None


class ActAutoChessTrainingDataTrainingConstData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_TrainingConstData"""

    trstage_band_id: str | None = None
    trstage_boss_id: str | None = None
    tr_stage_id: str | None = None
    training_mode_id: str | None = None
    tr_special_enemy_types: list[str] | None = None
    tr_bond_ids: list[str] | None = None
    tr_banned_bond_ids: list[str] | None = None
    tr_stage_boss_hp: int = Field(default=0, alias="trStageBossHP")
    tr_in_game_diy_chess_id: str | None = None
    tr_in_game_ban_diy_chess_id: str | None = None


class ActAutoChessTrainingDataTrainingShopSlotData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_TrainingShopSlotData"""

    slot: int = 0
    chess_ids: list[str] | None = None


class ActAutoChessTrainingDataTrainingRoundInfoData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_TrainingRoundInfoData"""

    round: int = 0
    is_boss_turn: bool = False
    base_gold_cnt: int = 0


class ActAutoChessTrainingDataTrainingSpecialChoiceData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_TrainingSpecialChoiceData"""

    choice_event_id: str | None = None
    round: int = 0
    slot: int = 0
    equip_id: str | None = None
    training_npc_id: str | None = None


class ActAutoChessTrainingDataTrainingNpcDeployData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_TrainingNpcDeployData"""

    round: int = 0
    training_npc_id: str | None = None
    chess_id: str | None = None
    position: UnityEngineVector2 | None = None
    direction: int = 0
    equip_chess_ids: list[str] | None = None
    garrison_layer: int = 0


class ActAutoChessTrainingDataTrainingDiyChessData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData_TrainingDiyChessData"""

    chess_id: str | None = None
    char_id: str | None = None
    tmpl_id: str | None = None
    skin_id: str | None = None
    skill_index: int = 0
    uni_equip_id: str | None = None
    potential_rank: int = 0


class ActAutoChessTrainingData(GameDataModel):
    """clz_Torappu_ActAutoChessTrainingData"""

    override_auto_chess_data: ActAutoChessTrainingDataAutoChessTrainingData | None = (
        None
    )
    band_data_list_dict: dict[str, ActAutoChessDataActAutoChessBandData] | None = None
    bond_info_dict: dict[str, ActAutoChessDataActAutoChessBondInfo] | None = None
    garrison_data_dict: dict[str, ActAutoChessDataActAutoChessGarrisonData] | None = (
        None
    )
    effect_info_data_dict: (
        dict[str, ActAutoChessDataActAutoChessEffectInfoData] | None
    ) = None
    effect_desc_param_data_dict: (
        dict[str, ActAutoChessDataActAutoChessEffectDescParamData] | None
    ) = None
    skill_info_data_dict: (
        dict[str, ActAutoChessDataActAutoChessSkillInfoData] | None
    ) = None
    effect_buff_info_data_dict: (
        dict[str, list[ActAutoChessDataActAutoChessBuffInfoData]] | None
    ) = None
    shop_level_data_dict: (
        dict[str, dict[int, ActAutoChessDataActAutoChessShopLevelData]] | None
    ) = None
    char_chess_data_dict: (
        dict[str, ActAutoChessDataActAutoChessCharChessData] | None
    ) = None
    char_shop_chess_datas: (
        dict[str, ActAutoChessDataActAutoChessCharShopChessData] | None
    ) = None
    trap_chess_data_dict: (
        dict[str, ActAutoChessDataActAutoChessTrapChessData] | None
    ) = None
    trap_shop_chess_datas: (
        dict[str, ActAutoChessDataActAutoChessTrapShopChessData] | None
    ) = None
    chess_normal_id_lookup_dict: dict[str, str] | None = None
    effect_choice_info_dict: (
        dict[str, ActAutoChessDataActAutoChessEffectChoiceInfoData] | None
    ) = None
    battle_data_dict: (
        dict[str, dict[int, list[ActAutoChessDataActAutoChessBattleData]]] | None
    ) = None
    boss_info_dict: dict[str, ActAutoChessDataActAutochessBossEntry] | None = None
    special_enemy_info_dict: (
        dict[str, ActAutoChessDataActAutochessSpecialEnemyEntry] | None
    ) = None
    training_npc_list: list[ActAutoChessDataActAutoChessTrainingNpcData] | None = None
    const_data: ActAutoChessDataActAutoChessConstData | None = None
    training_const_data: ActAutoChessTrainingDataTrainingConstData | None = None
    training_shop_dict: (
        dict[int, list[ActAutoChessTrainingDataTrainingShopSlotData]] | None
    ) = None
    training_round_info_dict: (
        dict[int, ActAutoChessTrainingDataTrainingRoundInfoData] | None
    ) = None
    training_special_choice_dict: (
        dict[str, list[ActAutoChessTrainingDataTrainingSpecialChoiceData]] | None
    ) = None
    training_npc_deploy_dict: (
        dict[int, list[ActAutoChessTrainingDataTrainingNpcDeployData]] | None
    ) = None
    training_diy_chess_dict: (
        dict[str, ActAutoChessTrainingDataTrainingDiyChessData] | None
    ) = None
    special_enemy_random_type_dict: (
        dict[str, ActAutoChessDataActAutochessSpecialEnemyTypeEntry] | None
    ) = None


class ActAutoChessData(GameDataModel):
    """clz_Torappu_ActAutoChessData"""

    mode_data_dict: dict[str, ActAutoChessDataActAutoChessModeData] | None = None
    mode_group_data_dict: (
        dict[str, ActAutoChessDataActAutoChessModeGroupData] | None
    ) = None
    chess_normal_id_lookup_dict: dict[str, str] | None = None
    diy_chess_dict: dict[str, str] | None = None
    diy_chess_info_dict: dict[str, list[str]] | None = None
    shop_level_display_data_dict: (
        dict[int, ActAutoChessDataActAutoChessShopLevelDisplayData] | None
    ) = None
    stage_datas_dict: dict[str, ActAutoChessDataActAutoChessStageData] | None = None
    enemy_info_dict: dict[str, list[str]] | None = None
    special_enemy_random_type_dict: (
        dict[str, ActAutoChessDataActAutochessSpecialEnemyTypeEntry] | None
    ) = None
    enemy_reward_type_dict: dict[str, str] | None = None
    enemy_reward_text_format_dict: dict[str, str] | None = None
    milestone_list: list[ActivityCommonMilestoneData] | None = None
    periodical_rewards: dict[str, ActivityPeriodicalRewardConf] | None = None
    mode_factor_info: dict[str, float] | None = None
    difficulty_factor_info: dict[str, float] | None = None
    player_title_data_dict: (
        dict[str, ActAutoChessDataActAutoChessPlayerTitleData] | None
    ) = None
    shop_char_chess_info_data: (
        dict[int, list[ActAutoChessDataActAutoChessShopCharChessInfoData]] | None
    ) = None
    const_data: ActAutoChessDataActAutoChessConstData | None = None
    season_shop: UITemplateShopTemplateShopData | None = None
    band_data_list_dict: dict[str, ActAutoChessDataActAutoChessBandData] | None = None
    bond_info_dict: dict[str, ActAutoChessDataActAutoChessBondInfo] | None = None
    garrison_data_dict: dict[str, ActAutoChessDataActAutoChessGarrisonData] | None = (
        None
    )
    effect_desc_param_data_dict: (
        dict[str, ActAutoChessDataActAutoChessEffectDescParamData] | None
    ) = None
    effect_info_data_dict: (
        dict[str, ActAutoChessDataActAutoChessEffectInfoData] | None
    ) = None
    skill_info_data_dict: (
        dict[str, ActAutoChessDataActAutoChessSkillInfoData] | None
    ) = None
    effect_buff_info_data_dict: (
        dict[str, list[ActAutoChessDataActAutoChessBuffInfoData]] | None
    ) = None
    shop_level_data_dict: (
        dict[str, dict[int, ActAutoChessDataActAutoChessShopLevelData]] | None
    ) = None
    char_chess_data_dict: (
        dict[str, ActAutoChessDataActAutoChessCharChessData] | None
    ) = None
    char_shop_chess_datas: (
        dict[str, ActAutoChessDataActAutoChessCharShopChessData] | None
    ) = None
    trap_chess_data_dict: (
        dict[str, ActAutoChessDataActAutoChessTrapChessData] | None
    ) = None
    trap_shop_chess_datas: (
        dict[str, ActAutoChessDataActAutoChessTrapShopChessData] | None
    ) = None
    effect_choice_info_dict: (
        dict[str, ActAutoChessDataActAutoChessEffectChoiceInfoData] | None
    ) = None
    battle_data_dict: (
        dict[str, dict[int, list[ActAutoChessDataActAutoChessBattleData]]] | None
    ) = None
    boss_info_dict: dict[str, ActAutoChessDataActAutochessBossEntry] | None = None
    special_enemy_info_dict: (
        dict[str, ActAutoChessDataActAutochessSpecialEnemyEntry] | None
    ) = None
    training_npc_list: list[ActAutoChessDataActAutoChessTrainingNpcData] | None = None
    training_data: ActAutoChessTrainingData | None = None


class ActFootballDataActFootballZoneAdditionData(GameDataModel):
    """clz_Torappu_ActFootballData_ActFootballZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class ActFootballDataActFootballStageAdditionData(GameDataModel):
    """clz_Torappu_ActFootballData_ActFootballStageAdditionData"""

    stage_id: str | None = None
    self_team_icon: str | None = None
    self_team_name: str | None = None
    enemy_team_icon: str | None = None
    enemy_team_name: str | None = None
    unlock_buff_id: str | None = None
    unlock_buff_icon: str | None = None
    unlock_buff_name: str | None = None
    unlock_buff_desc: str | None = None
    first_complete_point: int = 0
    complete_point: int = 0


class ActFootballDataActFootballMilestoneItemData(GameDataModel):
    """clz_Torappu_ActFootballData_ActFootballMilestoneItemData"""

    milestone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    reward: ItemBundle | None = None
    avail_time: int = 0


class ActFootballDataActFootballNPCCharData(GameDataModel):
    """clz_Torappu_ActFootballData_ActFootballNPCCharData"""

    inst_id: int = 0
    char_id: str | None = None
    level: int = 0
    evolve_phase: str = "PHASE_0"
    main_skill_level: int = 0
    specialize_level: int = 0
    potential_rank: int = 0
    favor_point: int = 0
    skin_id: str | None = None
    get_time: int = 0


class ActFootballDataActFootballConstData(GameDataModel):
    """clz_Torappu_ActFootballData_ActFootballConstData"""

    milestone_point_id: str | None = None
    milestone_track_id: str | None = None


class ActFootballData(GameDataModel):
    """clz_Torappu_ActFootballData"""

    zone_addition_data_map: (
        dict[str, ActFootballDataActFootballZoneAdditionData] | None
    ) = None
    stage_addition_data_map: (
        dict[str, ActFootballDataActFootballStageAdditionData] | None
    ) = None
    milestone_list: list[ActFootballDataActFootballMilestoneItemData] | None = None
    npc_char_data_dict: dict[int, ActFootballDataActFootballNPCCharData] | None = None
    const_data: ActFootballDataActFootballConstData | None = None


class ArkdexModeData(GameDataModel):
    """clz_Torappu_ArkdexModeData"""

    mode_id: str | None = None
    mode_num_id: int = 0
    is_multiplayer: bool = False
    num_max: int = 0
    battle_npc_count: int = 0
    is_matching: bool = False
    max_round_number: int = 0
    stage_time_max: int = 0
    character_limit: int = 0
    mode_type: str = "NONE"
    stage_ids: list[str] | None = None
    mode_name: str | None = None
    mode_hint: str | None = None
    matching_icon_id: str | None = None


class ArkdexCreatureData(GameDataModel):
    """clz_Torappu_ArkdexCreatureData"""

    creature_num_id: int = 0
    enemy_id: str | None = None
    deployed_enemy_id: str | None = None
    trap_id: str | None = None
    ui_display_scale: float = 0.0
    follow_scale: float = 0.0
    anim_speed_follow: float = 0.0
    rarity: int = 0
    special_rarity: bool = False
    sort_id: int = 0
    order_id: str | None = None
    name: str | None = None
    creature_icon: str | None = None
    world_entity_id: str | None = None
    alter_num_id: int = 0
    up_weight_tag_is_show: bool = False
    advantage_type: str | None = None
    description: str | None = None
    abilities: list[str] | None = None
    obtain_approach: str | None = None
    hp: float = 0.0
    atk: float = 0.0
    def_: float = Field(default=0.0, alias="def")
    mag: float = 0.0
    move_speed: float = 0.0
    atk_speed: float = 0.0
    hp_pct: int = 0
    atk_pct: int = 0
    def_pct: int = 0
    mag_pct: int = 0
    move_speed_pct: int = 0
    atk_speed_pct: int = 0


class ArkdexAdvantageTypeData(GameDataModel):
    """clz_Torappu_ArkdexAdvantageTypeData"""

    advantage_type: str | None = None
    sort_id: int = 0
    name: str | None = None
    type_icon: str | None = None
    entry_effect_key: str | None = None
    damage_scale_map: dict[str, float] | None = None


class ArkdexNpcInfoData(GameDataModel):
    """clz_Torappu_ArkdexNpcInfoData"""

    npc_id: int = 0
    strategy_group_id: str | None = None
    name: str | None = None
    avatar_id: str | None = None
    npc_prob: int = 0
    avatar_type: str = "NONE"
    name_card_skin_id: str | None = None
    name_card_skin_tmpl_id: int = 0


class ArkdexNpcDuelCreatureData(GameDataModel):
    """clz_Torappu_ArkdexNpcDuelCreatureData"""

    creature_num_id: int = 0
    trait_mask: int = 0


class ArkdexNpcDuelStrategyData(GameDataModel):
    """clz_Torappu_ArkdexNpcDuelStrategyData"""

    strategy_group_id: str | None = None
    strategy_id: str | None = None
    tile_strategy: str = "RANDOM"
    card_strategy: str = "RANDOM"
    creature_data: list[ArkdexNpcDuelCreatureData] | None = None
    weight: int = 0


class ArkdexItemEffectData(GameDataModel):
    """clz_Torappu_ArkdexItemEffectData"""

    item_num_id: int = 0
    buff: str | None = None
    active_desc: str | None = None
    blackboard: list[BlackboardDataPair] | None = None


class ArkdexTraitData(GameDataModel):
    """clz_Torappu_ArkdexTraitData"""

    sort_id: int = 0
    trait_mask: int = 0
    trait_id: str | None = None
    name: str | None = None
    icon: str | None = None
    description: str | None = None
    color: str | None = None
    buff: list[BlackboardDataPair] | None = None


class ArkdexNpcBattleParamData(GameDataModel):
    """clz_Torappu_ArkdexNpcBattleParamData"""

    npc_battle_id: int = 0
    mode_id: str | None = None


class ArkdexNpcPixelData(GameDataModel):
    """clz_Torappu_ArkdexNpcPixelData"""

    npc_pixel_id: str | None = None
    npc_pixel_icon: str | None = None
    npc_pixel_name: str | None = None
    npc_locked_toast: str | None = None


class ArkdexCaptureAreaData(GameDataModel):
    """clz_Torappu_ArkdexCaptureAreaData"""

    area_id: int = 0


class PingCond(GameDataModel):
    """clz_Torappu_PingCond"""

    cond: int = 0
    txt: str | None = None


class UnityEngineVector3(GameDataModel):
    """clz_UnityEngine_Vector3"""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


class ArkventRangeData(GameDataModel):
    """clz_Torappu_ArkventRangeData"""

    type: str = "NONE"
    position: UnityEngineVector3 | None = None
    bounds: UnityEngineVector3 | None = None


class ArkdexConstData(GameDataModel):
    """clz_Torappu_ArkdexConstData"""

    arkdex_creature_bag_max_num: int = 0
    arkdex_creature_bag_alert_num: int = 0
    operator_team_size: int = 0
    total_squad_cnt: int = 0
    team_slots: int = 0
    team_size: int = 0
    max_team_rarity_count: int = 0
    solo_character_limit: int = 0
    brawl_character_limit: int = 0
    build_entry_max_time: float = 0.0
    battle_entry_max_time: float = 0.0
    settle_max_time: float = 0.0
    ping_conds: list[PingCond] | None = None
    max_loading_time: int = 0
    deploy_phase_time: int = 0
    deploy_phase_hint_time: int = 0
    battle_phase_time_max: int = 0
    mode_operation_rank_time: int = 0
    pet_follow_panel_scale: float = 0.0
    trade_request_time: int = 0
    creatured_disappear_alert: float = 0.0
    creature_interact_range: ArkventRangeData | None = None
    creature_interact_style_id: str | None = None
    creature_display_name_id: str | None = None
    creature_head_up_style_id: str | None = None


class ArkdexModuleData(GameDataModel):
    """clz_Torappu_ArkdexModuleData"""

    mode_data: dict[str, ArkdexModeData] | None = None
    creature_data: dict[int, ArkdexCreatureData] | None = None
    advantage_type_data: dict[str, ArkdexAdvantageTypeData] | None = None
    advantage_counter_map: dict[str, list[str]] | None = None
    npc_info_data: dict[int, ArkdexNpcInfoData] | None = None
    npc_duel_strategy_data: dict[str, dict[str, ArkdexNpcDuelStrategyData]] | None = (
        None
    )
    item_effect_data: dict[int, ArkdexItemEffectData] | None = None
    trait_data: dict[int, ArkdexTraitData] | None = None
    scene_type_map: dict[int, str] | None = None
    npc_battle_param_data: dict[int, ArkdexNpcBattleParamData] | None = None
    npc_pixel_data: dict[str, ArkdexNpcPixelData] | None = None
    capture_area_data: dict[int, ArkdexCaptureAreaData] | None = None
    dex_const_data: ArkdexConstData | None = None


class ArkpixelConstData(GameDataModel):
    """clz_Torappu_ArkpixelConstData"""

    arkpixel_bag_num: int = 0
    arkpixel_other_player_bag_num: int = 0
    max_release_times_per_stage: int = 0
    pixel_param_id: str | None = None
    hidden_creator_name: str | None = None
    scene_pixel_display_radius: float = 0.0
    pixel_show_limit_config_list: list[int] | None = None
    show_collect_icon_count: int = 0
    max_collected_count: int = 0
    max_collected_display_text: str | None = None


class ArkpixelReleaseStageData(GameDataModel):
    """clz_Torappu_ArkpixelReleaseStageData"""

    arkpixel_stage: str | None = None
    start_time: int = 0
    arkpixel_release_times: int = 0


class ArkpixelModuleData(GameDataModel):
    """clz_Torappu_ArkpixelModuleData"""

    pixel_const_data: ArkpixelConstData | None = None
    release_stage_data: dict[str, ArkpixelReleaseStageData] | None = None


class ActArkHubModuleData(GameDataModel):
    """clz_Torappu_ActArkHubModuleData"""

    arkdex_module: ArkdexModuleData | None = None
    arkpixel_module: ArkpixelModuleData | None = None
    module_types: list[str] | None = None


class ActArkHubInteractiveUnitData(GameDataModel):
    """clz_Torappu_ActArkHubInteractiveUnitData"""

    editor_actor_id: int = 0
    actor_interact_point_count: int = 0
    display_name_id: str | None = None
    unit_id: str | None = None
    asset_id: str | None = None
    actor_type: str = "FURNI"
    actor_param: str | None = None
    avg_id: str | None = None
    interaction_requirements: list[str] | None = None
    position: UnityEngineVector3 | None = None
    yaw: float = 0.0
    block_range: ArkventRangeData | None = None
    interact_range: ArkventRangeData | None = None
    trigger_camera_config: str | None = None
    interact_camera_config: str | None = None
    interact_btn_style_id: str | None = None
    head_up_style_id: str | None = None
    scene_id: int = 0
    override_anim_config: dict[str, str] | None = None
    spine_face: str = "RIGHT"
    has_safe_pos: bool = False
    safe_pos: UnityEngineVector3 | None = None


class ActArkHubMenuData(GameDataModel):
    """clz_Torappu_ActArkHubMenuData"""

    type: str = "NONE"
    name: str | None = None
    icon_id: str | None = None
    is_permanent: bool = False
    sort_id: int = 0
    unlock_toast: str | None = None
    banned_toast: str | None = None


class ActArkHubConstData(GameDataModel):
    """clz_Torappu_ActArkHubConstData"""

    max_channel_player_limit: int = 0
    emoji_cd: float = Field(default=0.0, alias="emojiCD")
    emoji_time: float = 0.0
    run_max_stable_move_speed: float = 0.0
    walk_max_stable_move_speed: float = 0.0
    stable_movement_sharpness: float = 0.0
    default_alpha: float = 0.0
    run_configured_anim_scale: float = 0.0
    walk_configured_anim_scale: float = 0.0
    min_anim_scale: float = 0.0
    max_anim_scale: float = 0.0
    default_move_preset: str | None = None
    default_spine_flip: str = "INPUT"
    default_slide_stop_threshold: float = 0.0
    report_max_num: int = 0
    invitation_send_cd: int = 0
    invitation_validity_period: int = 0
    story_machine_camera_config_id: str | None = None
    ping_conds: list[PingCond] | None = None
    btn_cancel_interact_style_id: str | None = None
    npc_default_fx: str | None = None
    npc_selected_fx: str | None = None
    enter_lobby_fx: str | None = None
    interact_selected_fx: str | None = None
    spray_summon_fx: str | None = None
    spray_fade_fx: str | None = None
    pet_summon_fx: str | None = None
    follow_distance: float = 0.0
    stop_distance: float = 0.0
    move_speed: float = 0.0
    follow_offset: float = 0.0
    color_spine_outline: str | None = None
    high_quality_pet_spine_count: int = 0
    low_quality_pet_spine_count: int = 0
    mid_quality_pet_spine_count: int = 0


class ActArkHubMoveFixData(GameDataModel):
    """clz_Torappu_ActArkHubMoveFixData"""

    skin_id: str | None = None
    run_max_stable_move_speed: float = 0.0
    walk_max_stable_move_speed: float = 0.0
    alpha: float = 0.0
    run_configured_anim_scale: float = 0.0
    walk_configured_anim_scale: float = 0.0
    slide_stop_threshold: float = 0.0
    spine_flip: str = "INPUT"


class ArkventMovePresetData(GameDataModel):
    """clz_Torappu_ArkventMovePresetData"""

    preset_id: str | None = None
    accel_easing_type: str = "INSTANT"
    accel_duration: float = 0.0
    acc_power: float = 0.0
    dec_easing_type: str = "INSTANT"
    dec_duration: float = 0.0
    dec_power: float = 0.0
    turning_mode: str = "INSTANT"
    momentum_turn_speed: float = 0.0
    momentum_turn_speed_low: float = 0.0


class ActArkHubPlayerStateInfoData(GameDataModel):
    """clz_Torappu_ActArkHubPlayerStateInfoData"""

    state: str = "BATTLE"
    icon_id: str | None = None
    name: str | None = None


class ActArkHubRewardItem(GameDataModel):
    """clz_Torappu_ActArkHubRewardItem"""

    item_id: str | None = None
    count: int = 0
    item_type: str = "NONE"


class ActArkHubRewardData(GameDataModel):
    """clz_Torappu_ActArkHubRewardData"""

    reward_id: str | None = None
    item_list: list[ActArkHubRewardItem] | None = None


class ActArkhubLoadingTipData(GameDataModel):
    """clz_Torappu_ActArkhubLoadingTipData"""

    tip: str | None = None
    weight: int = 0


class ActArkHubData(GameDataModel):
    """clz_Torappu_ActArkHubData"""

    module_data: ActArkHubModuleData | None = None
    interactive_unit_data: dict[int, ActArkHubInteractiveUnitData] | None = None
    enabled_emoticon_theme_id_list: list[str] | None = None
    report_player_data_list: list[CommonReportPlayerData] | None = None
    menu_data: dict[str, ActArkHubMenuData] | None = None
    const_data: ActArkHubConstData | None = None
    move_fix_data: dict[str, ActArkHubMoveFixData] | None = None
    move_preset_data: dict[str, ArkventMovePresetData] | None = None
    skin_preset_dict: dict[str, str] | None = None
    player_state_info_data: dict[str, ActArkHubPlayerStateInfoData] | None = None
    reward_data_dict: dict[str, ActArkHubRewardData] | None = None
    spawn_fx_duration_dict: dict[str, float] | None = None
    loading_tip_list: list[ActArkhubLoadingTipData] | None = None


class Act53SideDataAct53SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act53SideData_Act53SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act53SideDataAct53SideConstData(GameDataModel):
    """clz_Torappu_Act53SideData_Act53SideConstData"""

    ark_odc_topic_id: str | None = None
    ark_odc_unlock_stage_id: str | None = None
    ark_odc_unlock_text: str | None = None
    ark_odc_update_text: str | None = None
    campaign_stage_id: str | None = None
    campaign_enemy_cnt: int = 0
    coin_item_id: str | None = None


class Act53SideData(GameDataModel):
    """clz_Torappu_Act53SideData"""

    zone_addition_data_map: dict[str, Act53SideDataAct53SideZoneAdditionData] | None = (
        None
    )
    act_odc_stage_id_list: list[str] | None = None
    const_data: Act53SideDataAct53SideConstData | None = None


class Act54SideDataAct54SideCardData(GameDataModel):
    """clz_Torappu_Act54SideData_Act54SideCardData"""

    card_id: str | None = None
    sort_id: int = 0
    name: str | None = None
    char_name: str | None = None
    desc_upright: str | None = None
    desc_reverse: str | None = None
    unlock_stage_id: str | None = None


class Act54SideDataAct54SideSpreadItemInfo(GameDataModel):
    """clz_Torappu_Act54SideData_Act54SideSpreadItemInfo"""

    sort_id: int = 0
    name: str | None = None
    name_english: str | None = None


class Act54SideDataAct54SideSpreadData(GameDataModel):
    """clz_Torappu_Act54SideData_Act54SideSpreadData"""

    spread_id: str | None = None
    sort_id: int = 0
    avail_times_divination: int = 0
    unlock_stage_id: str | None = None
    unlock_spread_id: str | None = None
    spreads_to_unlock: list[str] | None = None
    name: str | None = None
    name_english: str | None = None
    spread_info_list: list[Act54SideDataAct54SideSpreadItemInfo] | None = None
    rewards: list[ItemBundle] | None = None


class Act54SideDataAct54SideSpecialZoneStageInfo(GameDataModel):
    """clz_Torappu_Act54SideData_Act54SideSpecialZoneStageInfo"""

    stage_id: str | None = None
    sort_id: int = 0
    has_urgent_stage: bool = False


class Act54SideDataAct54SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act54SideData_Act54SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act54SideDataAct54SideConstData(GameDataModel):
    """clz_Torappu_Act54SideData_Act54SideConstData"""

    divination_unlock_stage_id: str | None = None
    final_reward: ItemBundle | None = None
    activity_item_id: str | None = None
    divination_enter_delay: float = 0.0


class Act54SideData(GameDataModel):
    """clz_Torappu_Act54SideData"""

    cards: dict[str, Act54SideDataAct54SideCardData] | None = None
    spreads: dict[str, Act54SideDataAct54SideSpreadData] | None = None
    special_zone_stage_infos: (
        list[Act54SideDataAct54SideSpecialZoneStageInfo] | None
    ) = None
    zone_addition_data_map: dict[str, Act54SideDataAct54SideZoneAdditionData] | None = (
        None
    )
    const_data: Act54SideDataAct54SideConstData | None = None


class ActVasebreakerDataActVasebreakerZoneAdditionData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class ActVasebreakerDataActVasebreakerStageAdditionData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerStageAdditionData"""

    stage_id: str | None = None
    first_cost: int = 0
    formation_most_num: int = 0
    formation_least_num: int = 0


class ActVasebreakerDataActVasebreakerStageUnlockToastData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerStageUnlockToastData"""

    stage_id: str | None = None
    unlock_toast: str | None = None


class ActVasebreakerDataActVasebreakerStageDropData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerStageDropData"""

    stage_id: str | None = None
    item_type: str = "NONE"
    item_id: str | None = None
    retry_count: int = 0
    first_count: int = 0
    complete_count: int = 0
    once_complete_count: int = 0
    is_display: bool = False


class ActVasebreakerDataActVasebreakerMilestoneItemData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerMilestoneItemData"""

    milestone_id: str | None = None
    order_id: int = 0
    token_num: int = 0
    reward: ItemBundle | None = None
    avail_time: int = 0


class ActVasebreakerDataActVasebreakerStickerData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerStickerData"""

    sticker_id: str | None = None
    sticker_icon: str | None = None
    template: str | None = None
    sticker_name: str | None = None
    param: list[str] | None = None


class ActVasebreakerDataActVasebreakerConstData(GameDataModel):
    """clz_Torappu_ActVasebreakerData_ActVasebreakerConstData"""

    milestone_point_id: str | None = None
    milestone_track_id: str | None = None
    level_entrance_text: str | None = None
    reward_furniture_id: str | None = None
    reward_furniture_text: str | None = None
    reward_avatar_id: str | None = None
    reward_avatar_text: str | None = None


class ActVasebreakerData(GameDataModel):
    """clz_Torappu_ActVasebreakerData"""

    zone_addition_data_map: (
        dict[str, ActVasebreakerDataActVasebreakerZoneAdditionData] | None
    ) = None
    stage_addition_data_map: (
        dict[str, ActVasebreakerDataActVasebreakerStageAdditionData] | None
    ) = None
    stage_unlock_toast_map: (
        dict[str, ActVasebreakerDataActVasebreakerStageUnlockToastData] | None
    ) = None
    stage_drop_data_map: (
        dict[str, ActVasebreakerDataActVasebreakerStageDropData] | None
    ) = None
    milestone_list: list[ActVasebreakerDataActVasebreakerMilestoneItemData] | None = (
        None
    )
    sticker_list: list[ActVasebreakerDataActVasebreakerStickerData] | None = None
    const_data: ActVasebreakerDataActVasebreakerConstData | None = None


class Act55SideDataAct55SideZoneAdditionData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideZoneAdditionData"""

    zone_id: str | None = None
    unlock_text: str | None = None


class Act55SideDataAct55SideNewspaperData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideNewspaperData"""

    stage_id: str | None = None
    sort_id: int = 0
    stage_name: str | None = None
    stage_desc: str | None = None
    bg_pic: str | None = None
    unlock_stage_id: str | None = None
    unlock_ts: int = 0
    base_reward_list: list[ItemBundle] | None = None
    advanced_reward_list: list[ItemBundle] | None = None
    basic_target_desc: str | None = None
    advanced_target_desc: str | None = None
    advanced_target_param: int = 0
    init_card_id_list: list[str] | None = None
    rating_score_list: list[int] | None = None
    max_score: int = 0
    pic_id: str | None = None
    init_empty_slot: int = 0
    fixed_report_id_list: list[str] | None = None


class Act55SideDataAct55SideFixedReportData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideFixedReportData"""

    fixed_report_id: str | None = None
    fixed_report_tag: str | None = None


class Act55SideDataAct55SideHandReportData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideHandReportData"""

    hand_report_id: str | None = None
    hand_report_pic_1: str | None = Field(default=None, alias="handReportPic_1")
    hand_report_pic_2: str | None = Field(default=None, alias="handReportPic_2")
    hand_report_title_id: str | None = None
    hand_report_sub_title_id: str | None = None
    hand_report_positive_tag_list: list[str] | None = None
    hand_report_negative_tag_list: list[str] | None = None
    sort_id: int = 0


class Act55SideDataAct55SideHandReportColorData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideHandReportColorData"""

    hand_report_pic_1: str | None = Field(default=None, alias="handReportPic_1")
    hand_report_title_color: str | None = None
    hand_report_sub_title_color: str | None = None


class Act55SideDataAct55SideBattleItemLevelData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideBattleItemLevelData"""

    level: int = 0
    score: int = 0


class Act55SideDataAct55SideConstData(GameDataModel):
    """clz_Torappu_Act55SideData_Act55SideConstData"""

    price_item_id: str | None = None
    price_item_type: str | None = None
    entry_requirement: str | None = None
    business_unlock_text: str | None = None
    stage_unlock_text: str | None = None
    hand_basic_score: int = 0
    hand_positive_score: int = 0
    hand_negative_score: int = 0


class Act55SideData(GameDataModel):
    """clz_Torappu_Act55SideData"""

    zone_addition_data_map: dict[str, Act55SideDataAct55SideZoneAdditionData] | None = (
        None
    )
    newspaper_data_map: dict[str, Act55SideDataAct55SideNewspaperData] | None = None
    fixed_report_data_map: dict[str, Act55SideDataAct55SideFixedReportData] | None = (
        None
    )
    hand_report_data_map: dict[str, Act55SideDataAct55SideHandReportData] | None = None
    hand_report_color_data_map: (
        dict[str, Act55SideDataAct55SideHandReportColorData] | None
    ) = None
    report_tag_list: list[str] | None = None
    battle_item_level_data_list: (
        list[Act55SideDataAct55SideBattleItemLevelData] | None
    ) = None
    const_data: Act55SideDataAct55SideConstData | None = None


class ActivityTableActivityDetailTable(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityDetailTable"""

    default: dict[str, DefaultFirstData] | None = Field(default=None, alias="DEFAULT")
    checkin_only: dict[str, DefaultCheckInData] | None = Field(
        default=None, alias="CHECKIN_ONLY"
    )
    checkin_all_player: dict[str, AllPlayerCheckinData] | None = Field(
        default=None, alias="CHECKIN_ALL_PLAYER"
    )
    checkin_vs: dict[str, VersusCheckInData] | None = Field(
        default=None, alias="CHECKIN_VS"
    )
    type_act3_d0: dict[str, Act3D0Data] | None = Field(
        default=None, alias="TYPE_ACT3D0"
    )
    type_act4_d0: dict[str, Act4D0Data] | None = Field(
        default=None, alias="TYPE_ACT4D0"
    )
    type_act5_d0: dict[str, Act5D0Data] | None = Field(
        default=None, alias="TYPE_ACT5D0"
    )
    type_act5_d1: dict[str, Act5D1Data] | None = Field(
        default=None, alias="TYPE_ACT5D1"
    )
    collection: dict[str, ActivityCollectionData] | None = Field(
        default=None, alias="COLLECTION"
    )
    type_act9_d0: dict[str, Act9D0Data] | None = Field(
        default=None, alias="TYPE_ACT9D0"
    )
    type_act12_side: dict[str, Act12SideData] | None = Field(
        default=None, alias="TYPE_ACT12SIDE"
    )
    type_act13_side: dict[str, Act13SideData] | None = Field(
        default=None, alias="TYPE_ACT13SIDE"
    )
    type_act17_side: dict[str, Act17sideData] | None = Field(
        default=None, alias="TYPE_ACT17SIDE"
    )
    type_act20_side: dict[str, Act20SideData] | None = Field(
        default=None, alias="TYPE_ACT20SIDE"
    )
    type_act21_side: dict[str, Act21SideData] | None = Field(
        default=None, alias="TYPE_ACT21SIDE"
    )
    login_only: dict[str, ActivityLoginData] | None = Field(
        default=None, alias="LOGIN_ONLY"
    )
    switch_only: dict[str, ActivitySwitchCheckinData] | None = Field(
        default=None, alias="SWITCH_ONLY"
    )
    ministory: dict[str, ActivityMiniStoryData] | None = Field(
        default=None, alias="MINISTORY"
    )
    roguelike: dict[str, ActivityRoguelikeData] | None = Field(
        default=None, alias="ROGUELIKE"
    )
    interlock: dict[str, ActivityInterlockData] | None = Field(
        default=None, alias="INTERLOCK"
    )
    boss_rush: dict[str, ActivityBossRushData] | None = Field(
        default=None, alias="BOSS_RUSH"
    )
    float_parade: dict[str, ActivityFloatParadeData] | None = Field(
        default=None, alias="FLOAT_PARADE"
    )
    main_buff: dict[str, ActivityMainlineBuffData] | None = Field(
        default=None, alias="MAIN_BUFF"
    )
    type_act24_side: dict[str, Act24SideData] | None = Field(
        default=None, alias="TYPE_ACT24SIDE"
    )
    type_act25_side: dict[str, Act25SideData] | None = Field(
        default=None, alias="TYPE_ACT25SIDE"
    )
    type_act27_side: dict[str, Act27SideData] | None = Field(
        default=None, alias="TYPE_ACT27SIDE"
    )
    type_act42_d0: dict[str, Act42D0Data] | None = Field(
        default=None, alias="TYPE_ACT42D0"
    )
    type_act29_side: dict[str, Act29SideData] | None = Field(
        default=None, alias="TYPE_ACT29SIDE"
    )
    year_5_general: dict[str, ActivityYear5GeneralData] | None = Field(
        default=None, alias="YEAR_5_GENERAL"
    )
    type_act35_side: dict[str, Act35SideData] | None = Field(
        default=None, alias="TYPE_ACT35SIDE"
    )
    vec_break_v2: dict[str, ActVecBreakV2Data] | None = Field(
        default=None, alias="VEC_BREAK_V2"
    )
    type_act36_side: dict[str, Act36SideData] | None = Field(
        default=None, alias="TYPE_ACT36SIDE"
    )
    type_act38_side: dict[str, Act38SideData] | None = Field(
        default=None, alias="TYPE_ACT38SIDE"
    )
    arcade: dict[str, ActArcadeData] | None = Field(default=None, alias="ARCADE")
    multiplay_v3: dict[str, ActMultiV3Data] | None = Field(
        default=None, alias="MULTIPLAY_V3"
    )
    type_mainss: dict[str, ActMainSSData] | None = Field(
        default=None, alias="TYPE_MAINSS"
    )
    enemy_duel: dict[str, ActivityEnemyDuelData] | None = Field(
        default=None, alias="ENEMY_DUEL"
    )
    type_act42_side: dict[str, Act42SideData] | None = Field(
        default=None, alias="TYPE_ACT42SIDE"
    )
    type_act44_side: dict[str, Act44SideData] | None = Field(
        default=None, alias="TYPE_ACT44SIDE"
    )
    halfidle_verify1: dict[str, Act1VHalfIdleData] | None = Field(
        default=None, alias="HALFIDLE_VERIFY1"
    )
    type_act45_side: dict[str, Act45SideData] | None = Field(
        default=None, alias="TYPE_ACT45SIDE"
    )
    recruit_only: dict[str, ActRecruitOnlyData] | None = Field(
        default=None, alias="RECRUIT_ONLY"
    )
    type_act46_side: dict[str, Act46SideData] | None = Field(
        default=None, alias="TYPE_ACT46SIDE"
    )
    autochess: dict[str, dict[str, ActAutoChessData]] | None = Field(
        default=None, alias="AUTOCHESS"
    )
    act_football: dict[str, ActFootballData] | None = Field(
        default=None, alias="ACT_FOOTBALL"
    )
    ark_hub: dict[str, ActArkHubData] | None = Field(default=None, alias="ARK_HUB")
    type_act53_side: dict[str, Act53SideData] | None = Field(
        default=None, alias="TYPE_ACT53SIDE"
    )
    type_act54_side: dict[str, Act54SideData] | None = Field(
        default=None, alias="TYPE_ACT54SIDE"
    )
    act_dp: dict[str, ActVasebreakerData] | None = Field(default=None, alias="ACT_DP")
    type_act55_side: dict[str, Act55SideData] | None = Field(
        default=None, alias="TYPE_ACT55SIDE"
    )


class ActMainlineBpExtraDataActMainlineBpExtraPeriodData(GameDataModel):
    """clz_Torappu_ActMainlineBpExtraData_ActMainlineBpExtraPeriodData"""

    period_id: str | None = None
    start_ts: int = 0
    end_ts: int = 0


class ActMainlineBpExtraData(GameDataModel):
    """clz_Torappu_ActMainlineBpExtraData"""

    period_data_list: (
        list[ActMainlineBpExtraDataActMainlineBpExtraPeriodData] | None
    ) = None


class ActivityTableActivityExtraData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityExtraData"""

    mainline_bp: dict[str, ActMainlineBpExtraData] | None = Field(
        default=None, alias="MAINLINE_BP"
    )


class HgInternalJObject(GameDataModel):
    """hg__internal__JObject"""

    base_64: str | None = None


class ActivityStageRewardData(GameDataModel):
    """clz_Torappu_ActivityStageRewardData"""

    stage_rewards_dict: dict[str, list[StageDataDisplayDetailRewards]] | None = None


class ActivityThemeDataTimeNode(GameDataModel):
    """clz_Torappu_ActivityThemeData_TimeNode"""

    title: str | None = None
    ts: int = 0


class ActivityThemeDataPicGroup(GameDataModel):
    """clz_Torappu_ActivityThemeData_PicGroup"""

    sort_index: int = 0
    pic_id: str | None = None
    avail_check: CommonAvailCheck | None = None


class ActivityThemeData(GameDataModel):
    """clz_Torappu_ActivityThemeData"""

    id: str | None = None
    type: str = "NONE"
    func_id: str | None = None
    end_ts: int = 0
    sort_id: int = 0
    item_id: str | None = None
    time_nodes: list[ActivityThemeDataTimeNode] | None = None
    pic_groups: list[ActivityThemeDataPicGroup] | None = None
    start_ts: int = 0


class StageDataConditionDesc(GameDataModel):
    """clz_Torappu_StageData_ConditionDesc"""

    stage_id: str | None = None
    complete_state: str = "ERR_ZERO"


class AprilFoolStageData(GameDataModel):
    """clz_Torappu_AprilFoolStageData"""

    stage_id: str | None = None
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    appearance_style: str = "MAIN_NORMAL"
    loading_pic_id: str | None = None
    difficulty: str = "NONE"
    unlock_condition: list[StageDataConditionDesc] | None = None
    stage_drop_info: list[ItemBundle] | None = None


class AprilFoolScoreData(GameDataModel):
    """clz_Torappu_AprilFoolScoreData"""

    stage_id: str | None = None
    sort_id: int = 0
    player_name: str | None = None
    player_score: int = 0


class AprilFoolConst(GameDataModel):
    """clz_Torappu_AprilFoolConst"""

    battle_finish_lose_des: str | None = None
    kill_enemy_des: str | None = None
    kill_boss_des: str | None = None
    total_time: str | None = None


class Act4funPerformGroupInfo(GameDataModel):
    """clz_Torappu_Act4funPerformGroupInfo"""

    perform_group_id: str | None = None
    perform_ids: list[str] | None = None


class Act4funPerformWordData(GameDataModel):
    """clz_Torappu_Act4funPerformWordData"""

    text: str | None = None
    pic_id: str | None = None
    background_id: str | None = None


class Act4funPerformInfo(GameDataModel):
    """clz_Torappu_Act4funPerformInfo"""

    perform_id: str | None = None
    perform_finished_pic_id: str | None = None
    fixed_cmp_group: str | None = None
    cmp_groups: list[str] | None = None
    words: list[Act4funPerformWordData] | None = None


class Act4funLiveMatEffectInfo(GameDataModel):
    """clz_Torappu_Act4funLiveMatEffectInfo"""

    live_mat_effect_id: str | None = None
    value_id: str | None = None
    perform_group: str | None = None


class Act4funLiveMatInfoData(GameDataModel):
    """clz_Torappu_Act4funLiveMatInfoData"""

    live_mat_id: str | None = None
    stage_id: str | None = None
    name: str | None = None
    pic_id: str | None = None
    tag_txt: str | None = None
    emoji_icon: str | None = None
    selected_perform_id: str | None = None
    effect_infos: dict[str, Act4funLiveMatEffectInfo] | None = None


class Act4funSpLiveMatInfoData(GameDataModel):
    """clz_Torappu_Act4funSpLiveMatInfoData"""

    sp_live_mat_id: str | None = None
    sp_live_eve_id: str | None = None
    stage_id: str | None = None
    name: str | None = None
    pic_id: str | None = None
    tag_txt: str | None = None
    emoji_icon: str | None = None
    according_perform_id: str | None = None
    selected_perform_id: str | None = None
    value_effect_id: str | None = None
    according_super_chat_id: str | None = None


class Act4funValueEffectInfoData(GameDataModel):
    """clz_Torappu_Act4funValueEffectInfoData"""

    value_effect_id: str | None = None
    effect_params: dict[str, int] | None = None


class Act4funLiveValueInfoData(GameDataModel):
    """clz_Torappu_Act4funLiveValueInfoData"""

    live_value_id: str | None = None
    name: str | None = None
    stage_id: str | None = None
    icon_id: str | None = None
    high_ending_id: str | None = None
    low_ending_id: str | None = None
    increase_toast_txt: str | None = None
    decrease_toast_txt: str | None = None


class Act4funSuperChatInfo(GameDataModel):
    """clz_Torappu_Act4funSuperChatInfo"""

    super_chat_id: str | None = None
    chat_type: str = "ROLLED"
    user_name: str | None = None
    icon_id: str | None = None
    value_effect_id: str | None = None
    perform_id: str | None = None
    super_chat_txt: str | None = None


class Act4funCmtInfo(GameDataModel):
    """clz_Torappu_Act4funCmtInfo"""

    icon_id: str | None = None
    name: str | None = None
    cmt_txt: str | None = None


class Act4funCmtGroupInfo(GameDataModel):
    """clz_Torappu_Act4funCmtGroupInfo"""

    cmt_group_id: str | None = None
    cmt_list: list[Act4funCmtInfo] | None = None


class Act4funEndingInfo(GameDataModel):
    """clz_Torappu_Act4funEndingInfo"""

    ending_id: str | None = None
    ending_avg: str | None = None
    ending_desc: str | None = None
    stage_id: str | None = None
    is_good_ending: bool = False


class Act4funTokenInfoData(GameDataModel):
    """clz_Torappu_Act4funTokenInfoData"""

    token_level_id: str | None = None
    level_desc: str | None = None
    skill_desc: str | None = None
    token_level_num: int = 0
    level_icon_id: str | None = None


class Act4funMissionData(GameDataModel):
    """clz_Torappu_Act4funMissionData"""

    mission_id: str | None = None
    sort_id: str | None = None
    mission_des: str | None = None
    reward_icon_ids: list[str] | None = None
    rewards: list[ItemBundle] | None = None


class Act4funConst(GameDataModel):
    """clz_Torappu_Act4funConst"""

    live_mat_amt_lower_limit: int = 0
    live_turn_upper_limit: int = 0
    super_chat_count_down_num: int = 0
    bad_ending_perform_effect_title: str | None = None
    perform_effect_title: str | None = None
    default_perform_pic_id: str | None = None
    default_txt_background: str | None = None
    opening_perform_group: str | None = None
    forget_perform_group: str | None = None
    run_perform_group: str | None = None
    live_mat_default_user_icon: str | None = None
    live_mat_attribute_icon: str | None = None
    live_mat_attrib_icon_diff_num: int = 0
    live_value_abs_limit: int = 0
    cmt_appear_time_lower_limit: float = 0.0
    cmt_appear_time_upper_limit: float = 0.0
    subtitle_interval_time: float = 0.0
    main_page_event_des: str | None = None
    sp_stage_ending_tip: str | None = None
    no_live_ending_tip: str | None = None
    not_enough_ending_tip: str | None = None
    enough_ending_tip: str | None = None
    main_page_personal: str | None = None
    main_page_job_des: str | None = None
    ending_page_confirm_txt: str | None = None
    run_confirm_txt: str | None = None
    main_page_diamond_mission_id: str | None = None
    reconnect_confirm_txt: str | None = None
    study_stage_id: str | None = None
    good_ending_toast_txt: str | None = None
    token_level_up_toast_txt: str | None = None
    study_stage_toast_txt: str | None = None
    mat_not_enough_toast_txt: str | None = None
    formal_level_unlock_toast_txt: str | None = None


class Act4funStageExtraData(GameDataModel):
    """clz_Torappu_Act4funStageExtraData"""

    description: str | None = None
    value_icon_id: str | None = None


class Act4funData(GameDataModel):
    """clz_Torappu_Act4funData"""

    perform_group_info_dict: dict[str, Act4funPerformGroupInfo] | None = None
    perform_info_dict: dict[str, Act4funPerformInfo] | None = None
    normal_mat_dict: dict[str, Act4funLiveMatInfoData] | None = None
    sp_mat_dict: dict[str, Act4funSpLiveMatInfoData] | None = None
    value_effect_info_dict: dict[str, Act4funValueEffectInfoData] | None = None
    live_value_info_dict: dict[str, Act4funLiveValueInfoData] | None = None
    super_chat_info_dict: dict[str, Act4funSuperChatInfo] | None = None
    cmt_group_info_dict: dict[str, Act4funCmtGroupInfo] | None = None
    cmt_users: list[str] | None = None
    ending_dict: dict[str, Act4funEndingInfo] | None = None
    token_level_infos: dict[str, Act4funTokenInfoData] | None = None
    mission_datas: dict[str, Act4funMissionData] | None = None
    constant: Act4funConst | None = None
    stage_extra_datas: dict[str, Act4funStageExtraData] | None = None
    random_msg_text: list[str] | None = None
    random_user_icon_id: list[str] | None = None


class Act5funConst(GameDataModel):
    """clz_Torappu_Act5funConst"""

    story_stage_id: str | None = None
    bet_stage_id: str | None = None
    story_roundnumber: int = 0
    bet_roundnumber: int = 0
    initial_fund_story: int = 0
    initial_fund_bet: int = 0
    min_fund_drop: int = 0
    max_fund: int = 0
    select_time: float = 0.0
    npc_count_in_round: int = 0
    select_description: str | None = None
    select_left_description: str | None = None
    select_right_description: str | None = None
    fund_description: str | None = None
    confirm_description: str | None = None
    loading_description: str | None = None


class Act5FunRoundData(GameDataModel):
    """clz_Torappu_Act5FunRoundData"""

    round_id: str | None = None
    stage_id: str | None = None
    enemy_predefined: bool = False
    round: int = 0
    enemy_point: float = 0.0
    enemy_score_random: float = 0.0
    min_type: int = 0
    max_type: int = 0
    choice_count: int = 0
    choice_id_1: str | None = None
    choice_id_2: str | None = None
    choice_id_3: str | None = None
    choice_id_4: str | None = None
    enable_side_target: bool = False


class Act5FunNpcData(GameDataModel):
    """clz_Torappu_Act5FunNpcData"""

    npc_id: str | None = None
    avatar_id: str | None = None
    name: str | None = None
    priority: float = 0.0
    special_strategy: str = "DEFAULT"
    npc_prob: float = 0.0
    default_enemy_score: float = 0.0


class Act5FunNpcSelectorData(GameDataModel):
    """clz_Torappu_Act5FunNpcSelectorData"""

    npc_id: str | None = None
    enemy_id: str | None = None
    score: float = 0.0


class Act5FunChoiceRewardData(GameDataModel):
    """clz_Torappu_Act5FunChoiceRewardData"""

    choice_id: str | None = None
    name: str | None = None
    percentage: float = 0.0
    is_special_style: bool = False


class Act5FunEnemyIdMappingData(GameDataModel):
    """clz_Torappu_Act5FunEnemyIdMappingData"""

    enemy_id: str | None = None
    original_enemy_id: str | None = None


class Act5FunDataBattleData(GameDataModel):
    """clz_Torappu_Act5FunData_BattleData"""

    battle_const_data: Act5funConst | None = None
    round_data: dict[str, Act5FunRoundData] | None = None
    npc_data: dict[str, Act5FunNpcData] | None = None
    npc_selector_data: list[Act5FunNpcSelectorData] | None = None
    choice_reward_data: dict[str, Act5FunChoiceRewardData] | None = None
    enemy_id_mapping_data: dict[str, Act5FunEnemyIdMappingData] | None = None
    battle_streak: list[float] | None = None


class Act5funBasicConst(GameDataModel):
    """clz_Torappu_Act5funBasicConst"""

    story_stage_id: str | None = None
    bet_stage_id: str | None = None
    story_round_number: int = 0
    bet_round_number: int = 0
    min_fund_drop: int = 0
    max_fund: int = 0


class Act5FunBasicNpcData(GameDataModel):
    """clz_Torappu_Act5FunBasicNpcData"""

    npc_id: str | None = None
    avatar_id: str | None = None
    name: str | None = None


class Act5FunSettleRatingData(GameDataModel):
    """clz_Torappu_Act5FunSettleRatingData"""

    min_rating: int = 0
    max_rating: int = 0
    rating_desc: str | None = None


class Act5FunSettleStreakData(GameDataModel):
    """clz_Torappu_Act5FunSettleStreakData"""

    count: int = 0
    desc: str | None = None


class Act5FunSettleSuccessData(GameDataModel):
    """clz_Torappu_Act5FunSettleSuccessData"""

    count: int = 0
    desc: str | None = None


class Act5FunData(GameDataModel):
    """clz_Torappu_Act5FunData"""

    battle_data: Act5FunDataBattleData | None = None
    const_data: Act5funBasicConst | None = None
    npc_data: dict[str, Act5FunBasicNpcData] | None = None
    rating_data: list[Act5FunSettleRatingData] | None = None
    streak_data: list[Act5FunSettleStreakData] | None = None
    success_data: list[Act5FunSettleSuccessData] | None = None


class Act6FunStageAdditionData(GameDataModel):
    """clz_Torappu_Act6FunStageAdditionData"""

    description: str | None = None
    npc_dialog_text: str | None = None
    preview_char_pic_id: str | None = None
    fever_coin_num: int = 0
    is_hidden_stage: bool = False


class Act6FunAchievementData(GameDataModel):
    """clz_Torappu_Act6FunAchievementData"""

    achievement_id: str | None = None
    sort_id: int = 0
    achievement_type: str = "NORMAL"
    description: str | None = None
    cover_desc: str | None = None


class Act6FunAchievementRewardData(GameDataModel):
    """clz_Torappu_Act6FunAchievementRewardData"""

    reward: ItemBundle | None = None
    sort_id: int = 0
    achievement_count: int = 0


class Act6FunConst(GameDataModel):
    """clz_Torappu_Act6FunConst"""

    default_stage: str | None = None
    achievement_max_number: int = 0
    special_number: int = 0
    character_tip_toast: str | None = None
    function_toast_list: list[str] | None = None


class Act6FunData(GameDataModel):
    """clz_Torappu_Act6FunData"""

    stage_addition_map: dict[str, Act6FunStageAdditionData] | None = None
    stage_achievement_map: dict[str, list[Act6FunAchievementData]] | None = None
    achievement_reward_list: dict[str, Act6FunAchievementRewardData] | None = None
    const_data: Act6FunConst | None = None


class Act7FunStageAdditionData(GameDataModel):
    """clz_Torappu_Act7FunStageAdditionData"""

    homepage_spine_group_id: str | None = None
    battle_spine_group_id: str | None = None
    settle_win_spine_group_id: str | None = None
    settle_lose_spine_group_id: str | None = None
    trap_max_num: int = 0
    trap_target_num: int = 0


class Act7FunEasterEggData(GameDataModel):
    """clz_Torappu_Act7FunEasterEggData"""

    easteregg_id: str | None = None
    char_id: str | None = None
    news_desc: str | None = None


class Act7FunSpineHolderData(GameDataModel):
    """clz_Torappu_Act7FunSpineHolderData"""

    holder_id: int = 0
    char_id: str | None = None
    direction: bool = False


class Act7FunSpineGroupData(GameDataModel):
    """clz_Torappu_Act7FunSpineGroupData"""

    spine_group_id: str | None = None
    holder_data: list[Act7FunSpineHolderData] | None = None


class Act7FunCharAnimData(GameDataModel):
    """clz_Torappu_Act7FunCharAnimData"""

    char_id: str | None = None
    fail_anim_id: str | None = None
    normal_anim_ids: list[str] | None = None


class Act7FunConstData(GameDataModel):
    """clz_Torappu_Act7FunConstData"""

    default_stage: str | None = None
    homepage_switch_stage_id: str | None = None


class Act7FunData(GameDataModel):
    """clz_Torappu_Act7FunData"""

    stage_addition_map: dict[str, Act7FunStageAdditionData] | None = None
    easter_egg_data: dict[str, Act7FunEasterEggData] | None = None
    spine_group_data: dict[str, Act7FunSpineGroupData] | None = None
    char_anim_data: dict[str, Act7FunCharAnimData] | None = None
    stage_reward_list: list[str] | None = None
    const_data: Act7FunConstData | None = None


class AprilFoolTable(GameDataModel):
    """clz_Torappu_AprilFoolTable"""

    stages: dict[str, AprilFoolStageData] | None = None
    score_dict: dict[str, list[AprilFoolScoreData]] | None = None
    constant: AprilFoolConst | None = None
    act_4_fun_data: Act4funData | None = None
    act_5_fun_data: Act5FunData | None = None
    act_6_fun_data: Act6FunData | None = None
    act_7_fun_data: Act7FunData | None = None


class CartComponents(GameDataModel):
    """clz_Torappu_CartComponents"""

    comp_id: str | None = None
    sort_id: int = 0
    type: str = "NONE"
    pos_list: list[str] | None = None
    pos_id_dict: dict[str, list[str]] | None = None
    name: str | None = None
    icon: str | None = None
    show_scores: int = 0
    item_usage: str | None = None
    item_desc: str | None = None
    item_obtain: str | None = None
    rarity: int = 0
    detail_desc: str | None = None
    price: int = 0
    special_obtain: str | None = None
    obtain_in_random: bool = False
    additive_color: str | None = None


class CartDataCartConstData(GameDataModel):
    """clz_Torappu_CartData_CartConstData"""

    car_item_unlock_stage_id: str | None = None
    car_item_unlock_desc: str | None = None
    sp_level_unlock_item_cnt: int = 0
    mile_stone_base_interval: int = 0
    sp_stage_ids: list[str] | None = None
    car_frame_default_color: str | None = None


class CartData(GameDataModel):
    """clz_Torappu_CartData"""

    car_dict: dict[str, CartComponents] | None = None
    rune_data_dict: dict[str, RuneTablePackedRuneData] | None = None
    cart_stages: list[str] | None = None
    const_data: CartDataCartConstData | None = None


class SiracusaDataAreaData(GameDataModel):
    """clz_Torappu_SiracusaData_AreaData"""

    area_id: str | None = None
    area_name: str | None = None
    area_sub_name: str | None = None
    unlock_type: str = "NONE"
    unlock_stage: str | None = None
    area_icon_id: str | None = None
    point_list: list[str] | None = None


class SiracusaDataPointData(GameDataModel):
    """clz_Torappu_SiracusaData_PointData"""

    point_id: str | None = None
    area_id: str | None = None
    point_name: str | None = None
    point_desc: str | None = None
    point_icon_id: str | None = None
    point_ita_name: str | None = None


class SiracusaDataCharCardData(GameDataModel):
    """clz_Torappu_SiracusaData_CharCardData"""

    char_card_id: str | None = None
    sort_index: int = 0
    avg_char: str | None = None
    avg_char_offset_y: float = 0.0
    char_card_name: str | None = None
    char_card_ita_name: str | None = None
    char_card_title: str | None = None
    char_card_desc: str | None = None
    full_complete_des: str | None = None
    gain_desc: str | None = None
    theme_color: str | None = None
    task_ring_list: list[str] | None = None
    opera_item_id: str | None = None
    gain_type: str = "NONE"
    gain_param_list: list[str] | None = None


class SiracusaDataTaskRingData(GameDataModel):
    """clz_Torappu_SiracusaData_TaskRingData"""

    task_ring_id: str | None = None
    sort_index: int = 0
    char_card_id: str | None = None
    logic_type: str = "NONE"
    ring_text: str | None = None
    item: ItemBundle | None = None
    is_precious: bool = False
    task_id_list: list[str] | None = None


class SiracusaDataTaskBasicInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_TaskBasicInfoData"""

    task_id: str | None = None
    task_ring_id: str | None = None
    sort_index: int = 0
    place_id: str | None = None
    npc_id: str | None = None
    task_type: str = "NONE"


class SiracusaDataBattleTaskData(GameDataModel):
    """clz_Torappu_SiracusaData_BattleTaskData"""

    task_id: str | None = None
    stage_id: str | None = None
    battle_task_desc: str | None = None
    target_type: str | None = None
    target_template: str | None = None
    target_param_list: list[str] | None = None


class SiracusaDataAVGTaskData(GameDataModel):
    """clz_Torappu_SiracusaData_AVGTaskData"""

    task_id: str | None = None
    task_avg: str | None = None


class SiracusaDataItemInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_ItemInfoData"""

    item_id: str | None = None
    item_name: str | None = None
    item_italy_name: str | None = None
    item_desc: str | None = None
    item_icon: str | None = None


class SiracusaDataItemCardInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_ItemCardInfoData"""

    card_id: str | None = None
    card_name: str | None = None
    card_desc: str | None = None
    option_script: str | None = None


class SiracusaDataNavigationInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_NavigationInfoData"""

    entry_id: str | None = None
    navigation_type: str = "NONE"
    entry_icon: str | None = None
    entry_name: str | None = None
    entry_sub_name: str | None = None


class SiracusaDataOptionInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_OptionInfoData"""

    option_id: str | None = None
    option_desc: str | None = None
    option_script: str | None = None
    option_go_to_script: str | None = None
    is_leave_option: bool = False
    need_comment_like: bool = False
    require_card_id: str | None = None


class SiracusaDataStagePointInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_StagePointInfoData"""

    stage_id: str | None = None
    point_id: str | None = None
    sort_id: int = 0
    is_task_stage: bool = False


class SiracusaDataStoryBriefInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_StoryBriefInfoData"""

    story_id: str | None = None
    stage_id: str | None = None
    story_info: str | None = None


class SiracusaDataOperaInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_OperaInfoData"""

    opera_id: str | None = None
    sort_id: int = 0
    opera_name: str | None = None
    opera_sub_name: str | None = None
    opera_score: str | None = None
    unlock_time: int = 0


class SiracusaDataOperaCommentInfoData(GameDataModel):
    """clz_Torappu_SiracusaData_OperaCommentInfoData"""

    comment_id: str | None = None
    reference_opera_id: str | None = None
    column_index: int = 0
    column_sort_id: int = 0
    comment_title: str | None = None
    score: str | None = None
    comment_content: str | None = None
    comment_char_id: str | None = None


class SiracusaDataConstData(GameDataModel):
    """clz_Torappu_SiracusaData_ConstData"""

    opera_daily_num: int = 0
    opera_all_unlock_time: int = 0
    default_focus_area: str | None = None


class SiracusaData(GameDataModel):
    """clz_Torappu_SiracusaData"""

    area_data_map: dict[str, SiracusaDataAreaData] | None = None
    point_data_map: dict[str, SiracusaDataPointData] | None = None
    char_card_map: dict[str, SiracusaDataCharCardData] | None = None
    task_ring_map: dict[str, SiracusaDataTaskRingData] | None = None
    task_info_map: dict[str, SiracusaDataTaskBasicInfoData] | None = None
    battle_task_map: dict[str, SiracusaDataBattleTaskData] | None = None
    avg_task_map: dict[str, SiracusaDataAVGTaskData] | None = None
    item_info_map: dict[str, SiracusaDataItemInfoData] | None = None
    item_card_info_map: dict[str, SiracusaDataItemCardInfoData] | None = None
    navigation_info_map: dict[str, SiracusaDataNavigationInfoData] | None = None
    option_info_map: dict[str, SiracusaDataOptionInfoData] | None = None
    stage_point_list: list[SiracusaDataStagePointInfoData] | None = None
    story_brief_info_data_map: dict[str, SiracusaDataStoryBriefInfoData] | None = None
    opera_info_map: dict[str, SiracusaDataOperaInfoData] | None = None
    opera_comment_info_map: dict[str, SiracusaDataOperaCommentInfoData] | None = None
    const_data: SiracusaDataConstData | None = None


class GridPosition(GameDataModel):
    """clz_Torappu_GridPosition"""

    row: int = 0
    col: int = 0


class FireworkDataPlateContent(GameDataModel):
    """clz_Torappu_FireworkData_PlateContent"""

    plate_content: list[GridPosition] | None = None


class FireworkDataPlateData(GameDataModel):
    """clz_Torappu_FireworkData_PlateData"""

    plate_id: str | None = None
    sort_id: int = 0
    direction_type: str = "TWO_DIR"
    unlock_level: str | None = None
    plate_rank: int = 0
    plate_contents: list[FireworkDataPlateContent] | None = None
    is_craft: bool = False


class FireworkDataAnimalData(GameDataModel):
    """clz_Torappu_FireworkData_AnimalData"""

    animal_id: str | None = None
    sort_id: int = 0
    animal_name: str | None = None
    animal_buff_desc_1: str | None = None
    animal_buff_desc_2: str | None = None
    unlock_level: str | None = None
    type: str = "RED"
    none_outline_unselect_icon_id: list[str] | None = None
    outline_icon_id: list[str] | None = None
    none_outline_select_icon_id: list[str] | None = None
    unlock_toast: str | None = None
    unlock_toast_icon_id: str | None = None
    changed_toast: str | None = None
    firework_animal_name_icon_id: str | None = None


class FireworkDataLevelData(GameDataModel):
    """clz_Torappu_FireworkData_LevelData"""

    level_id: str | None = None
    sort_id: int = 0
    trap_pos_x: int = 0
    trap_pos_y: int = 0
    is_sp_level: bool = Field(default=False, alias="isSPLevel")


class FireworkDataConstData(GameDataModel):
    """clz_Torappu_FireworkData_ConstData"""

    max_firework_num: int = 0
    max_firework_plate_row_count: int = 0
    unlock_stage_code: str | None = None
    dont_display_firework_plugin_stage_list: list[str] | None = None


class FireworkData(GameDataModel):
    """clz_Torappu_FireworkData"""

    plate_data: dict[str, FireworkDataPlateData] | None = None
    animal_data: dict[str, FireworkDataAnimalData] | None = None
    level_data: dict[str, FireworkDataLevelData] | None = None
    const_data: FireworkDataConstData | None = None


class Act1VHalfIdleItemData(GameDataModel):
    """clz_Torappu_Act1VHalfIdleItemData"""

    act_id: str | None = None
    item_id: str | None = None
    item_type: str = "NONE"
    item_name: str | None = None
    sort_id: int = 0
    icon_id: str | None = None
    func_desc: str | None = None
    flavor_desc: str | None = None
    obtain_approach: str | None = None
    show_in_inventory: bool = False


class HalfIdleData(GameDataModel):
    """clz_Torappu_HalfIdleData"""

    item_data: dict[str, Act1VHalfIdleItemData] | None = None


class ArkNewsDataArkNewsBuffItemData(GameDataModel):
    """clz_Torappu_ArkNewsData_ArkNewsBuffItemData"""

    level: int = 0
    desc: str | None = None
    template_trap_id: str | None = None


class ArkNewsData(GameDataModel):
    """clz_Torappu_ArkNewsData"""

    battle_item_level_data_list: list[ArkNewsDataArkNewsBuffItemData] | None = None


class KVSwitchInfo(GameDataModel):
    """clz_Torappu_KVSwitchInfo"""

    is_default: bool = False
    display_time: int = 0
    stage_id: str | None = None
    pass_state: str = "UNLOCKED"


class ActivityKVSwitchData(GameDataModel):
    """clz_Torappu_ActivityKVSwitchData"""

    kv_switch_info: dict[str, KVSwitchInfo] | None = None


class DynEntrySwitchInfo(GameDataModel):
    """clz_Torappu_DynEntrySwitchInfo"""

    entry_id: str | None = None
    sort_id: int = 0
    stage_id: str | None = None
    signal_id: str | None = None


class DynEntryAnimationInfo(GameDataModel):
    """clz_Torappu_DynEntryAnimationInfo"""

    animation_id: str | None = None
    sort_id: int = 0
    is_default_animation: bool = False
    stage_id: str | None = None
    signal_id: str | None = None


class ActivityDynEntrySwitchData(GameDataModel):
    """clz_Torappu_ActivityDynEntrySwitchData"""

    entry_switch_info: dict[str, DynEntrySwitchInfo] | None = None
    random_entry_switch_info: dict[str, DynEntrySwitchInfo] | None = None
    entry_animation_info: dict[str, DynEntryAnimationInfo] | None = None


class ActivityTableActivityHiddenStageUnlockConditionData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityHiddenStageUnlockConditionData"""

    unlock_stage_id: str | None = None
    unlock_template: str | None = None
    unlock_params: list[str] | None = None
    mission_stage_id: str | None = None
    unlocked_name: str | None = None
    locked_name: str | None = None
    lock_code: str | None = None
    unlocked_des: str | None = None
    template_desc: str | None = None
    desc: str | None = None
    riddle: str | None = None


class ActivityTableActivityHiddenStageData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityHiddenStageData"""

    stage_id: str | None = None
    encoded_name: str | None = None
    show_stage_id: str | None = None
    reward_diamond: bool = False
    missions: list[ActivityTableActivityHiddenStageUnlockConditionData] | None = None


class MissionArchiveVoiceClipData(GameDataModel):
    """clz_Torappu_MissionArchiveVoiceClipData"""

    char_id: str | None = None
    voice_id: str | None = None
    index: int = 0


class MissionArchiveNodeData(GameDataModel):
    """clz_Torappu_MissionArchiveNodeData"""

    node_id: str | None = None
    title: str | None = None
    unlock_desc: str | None = None
    clips: list[MissionArchiveVoiceClipData] | None = None


class MissionArchiveData(GameDataModel):
    """clz_Torappu_MissionArchiveData"""

    topic_id: str | None = None
    zones: list[str] | None = None
    nodes: list[MissionArchiveNodeData] | None = None
    hidden_clips: list[MissionArchiveVoiceClipData] | None = None
    unlock_desc: str | None = None


class FifthAnnivExploreGroupData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreGroupData"""

    id: str | None = None
    name: str | None = None
    desc: str | None = None
    code: str | None = None
    icon_id: str | None = None
    initial_values: dict[str, int] | None = None
    heritage_value_type: str = "TEAMVALUE_1"


class FifthAnnivExploreStageData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreStageData"""

    id: str | None = None
    name: str | None = None
    desc: str | None = None
    next_stage_id: str | None = None
    event_count: int = 0
    prev_node_count: int = 0
    stage_num: int = 0
    stage_event_num: int = 0
    stage_display_num: str | None = None
    stage_failure_description: str | None = None


class FifthAnnivExploreTargetData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreTargetData"""

    id: str | None = None
    link_stage_id: str | None = None
    target_values: dict[str, int] | None = None
    require_event_id: str | None = None
    locked_level_id: str | None = None
    is_end: bool = False
    name: str | None = None
    end_name: str | None = None
    desc: str | None = None
    success_desc: str | None = None
    success_icon_id: str | None = None


class FifthAnnivExploreEventData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreEventData"""

    id: str | None = None
    name: str | None = None
    type_name: str | None = None
    icon_id: str | None = None
    desc: str | None = None
    choice_ids: list[str] | None = None


class FifthAnnivExploreEventChoiceData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreEventChoiceData"""

    id: str | None = None
    event_id: str | None = None
    name: str | None = None
    desc: str | None = None
    success_desc: str | None = None
    failure_desc: str | None = None


class FifthAnnivExploreBroadcastData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreBroadcastData"""

    id: str | None = None
    event_count: int = 0
    stage_id: str | None = None
    content: str | None = None


class FifthAnnivExploreConst(GameDataModel):
    """clz_Torappu_FifthAnnivExploreConst"""

    prev_record_num: int = 0
    max_board: int = 0
    value_min: int = 0
    value_max: int = 0
    target_stuck_desc: str | None = None
    stage_stuck_desc: str | None = None
    mission_name: str | None = None
    mission_desc: str | None = None
    choice_value_order: list[str] | None = None
    team_pass_targe_desc: str | None = None
    team_pass_end_desc: str | None = None


class FifthAnnivExploreMissionData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreMissionData"""

    progress_up_limit: int = 0
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


class FifthAnnivExploreData(GameDataModel):
    """clz_Torappu_FifthAnnivExploreData"""

    explore_group_data: dict[str, FifthAnnivExploreGroupData] | None = None
    explore_stage_data: dict[str, FifthAnnivExploreStageData] | None = None
    explore_target_data: dict[str, FifthAnnivExploreTargetData] | None = None
    explore_event_data: dict[str, FifthAnnivExploreEventData] | None = None
    explore_choice_data: dict[str, FifthAnnivExploreEventChoiceData] | None = None
    broadcast_data: dict[str, FifthAnnivExploreBroadcastData] | None = None
    explore_const: FifthAnnivExploreConst | None = None
    mission_data: dict[str, FifthAnnivExploreMissionData] | None = None


class Anniv7thClueGroupData(GameDataModel):
    """clz_Torappu_Anniv7thClueGroupData"""

    clue_group_id: str | None = None
    sort_id: int = 0
    clue_group_name: str | None = None
    clue_group_sub_name: str | None = None
    clue_group_bg: str | None = None


class Anniv7thClueData(GameDataModel):
    """clz_Torappu_Anniv7thClueData"""

    clue_id: str | None = None
    clue_group_id: str | None = None
    sort_id: int = 0
    clue_link: list[str] | None = None
    clue_name: str | None = None
    clue_owner: str | None = None
    clue_desc: str | None = None
    unlock_desc: str | None = None
    clue_owner_pic: str | None = None
    page_res: str | None = None


class Anniv7thClueRewardData(GameDataModel):
    """clz_Torappu_Anniv7thClueRewardData"""

    clue_record_id: str | None = None
    clue_record: int = 0
    clue_record_desc: str | None = None
    rewards: list[ItemBundle] | None = None


class Anniv7thDisplayData(GameDataModel):
    """clz_Torappu_Anniv7thDisplayData"""

    sort_id: int = 0
    char_id: str | None = None
    voice_id: str | None = None


class Anniv7thDisplayNodeData(GameDataModel):
    """clz_Torappu_Anniv7thDisplayNodeData"""

    node_type: str = "LETTER"
    display_data: list[Anniv7thDisplayData] | None = None


class Anniv7thClueConstData(GameDataModel):
    """clz_Torappu_Anniv7thClueConstData"""

    unlock_stage_id: str | None = None
    unlock_toast: str | None = None


class Anniv7thMainlineData(GameDataModel):
    """clz_Torappu_Anniv7thMainlineData"""

    clue_group_data: dict[str, Anniv7thClueGroupData] | None = None
    clue_data: dict[str, Anniv7thClueData] | None = None
    clue_reward_data: list[Anniv7thClueRewardData] | None = None
    display_node_data: list[Anniv7thDisplayNodeData] | None = None
    const_data: Anniv7thClueConstData | None = None


class AutoChessDataAutoChessVersionInfoData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessVersionInfoData"""

    version_id: str | None = None
    activity_id: str | None = None
    enroll_id: str | None = None
    period_type: str = "SEASON"
    content_type: str = "NONE"
    is_content_updated: bool = False
    is_shop_updated: bool = False
    season_name: str | None = None
    season_year: str | None = None
    is_activity_item_max: bool = False
    is_activity_task_max: bool = False
    is_offseason: bool = False
    sort_id: int = 0
    expire_version: int = 0
    start_time: int = 0
    end_time: int = 0


class AutoChessDataAutoChessWarmupScheduleData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessWarmupScheduleData"""

    warmup_id: str | None = None
    version_id: str | None = None
    start_time: int = 0
    end_time: int = 0
    is_main_page_used: bool = False


class AutoChessDataAutoChessStagePageDisplayData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessStagePageDisplayData"""

    display_id: str | None = None
    version_id: str | None = None
    main_disappear_time: int = 0
    stage_page_disappear_time: int = 0


class AutoChessDataAutoChessCultivateRelationData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessCultivateRelationData"""

    cultivate_num: int = 0
    effect_id: str | None = None
    evolve_phase: str = "PHASE_0"
    char_level: int = 0
    atk_per: int = 0
    def_per: int = 0
    hp_per: int = 0


class AutoChessDataAutoChessEffectTypeData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessEffectTypeData"""

    description: str | None = None


class AutoChessDataAutoChessEnemyTypeData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessEnemyTypeData"""

    type: str | None = None
    sort_id: int = 0
    name: str | None = None
    description: str | None = None
    icon: str | None = None
    type_identifier: int = 0
    involve_random: bool = False


class AutoChessDataAutoChessEnterStepData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessEnterStepData"""

    step_type: str = "NONE"
    sort_id: int = 0
    time: int = 0
    hint_time: int = 0
    title: str | None = None
    desc: str | None = None


class AutoChessDataAutoChessShopStateTokenData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessShopStateTokenData"""

    token_id: str | None = None
    token_display_type: str = "DEFAULT"


class AutoChessDataAutoChessSkillTriggerData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessSkillTriggerData"""

    profession: str = "NONE"
    sub_profession_id: str | None = None
    char_id: str | None = None
    skill_index: int = 0
    skill_trigger_types: list[str] | None = None


class AutoChessDataAutoChessPrepareStateData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessPrepareStateData"""

    effect_id: str | None = None
    buff: str | None = None
    black_board: list[BlackboardDataPair] | None = None


class AutoChessDataAutoChessGameTipData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessGameTipData"""

    tip: str | None = None
    weight: int = 0


class AutoChessDataAutoChessMedalData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessMedalData"""

    medal_count: int = 0
    medal_icon_id: str | None = None


class AutoChessDataAutoChessTurnInfoData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessTurnInfoData"""

    round: int = 0
    normal_phase_time: int = 0
    is_boss_turn: bool = False
    boss_turn_hp_reduce_time: int = 0


class AutoChessDataAutoChessRoundScoreData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessRoundScoreData"""

    round: int = 0
    score: int = 0


class AutoChessDataAutoChessBroadcastData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessBroadcastData"""

    id: str | None = None
    id_code: int = 0
    desc: str | None = None
    priority: int = 0
    comment_icon: str | None = None
    type: str = "NONE"
    param_list: list[str] | None = None


class AutoChessDataAutoChessBossDamageStatsStyleData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessBossDamageStatsStyleData"""

    damage_threshold: int = 0
    style_status_id: str | None = None


class AutoChessDataAutoChessConstData(GameDataModel):
    """clz_Torappu_AutoChessData_AutoChessConstData"""

    ping_conds: list[PingCond] | None = None
    matching_tip_rotate_interval: float = 0.0
    min_replaced_enemy_count: int = 0
    max_replaced_enemy_count: int = 0
    template_enemy_normal: str | None = None
    template_enemy_elite: str | None = None
    template_enemy_special: str | None = None
    template_enemy_normal_fly: str | None = None
    template_enemy_elite_fly: str | None = None
    template_enemy_special_fly: str | None = None
    template_enemy_token: str | None = None
    template_enemy_token_fly: str | None = None
    max_level_cnt: int = 0
    special_enemy_num: int = 0
    special_enemy_num_single: int = 0
    enemy_type_identifier_to_fill_random: int = 0
    enemy_max_hp_factor: float = 0.0
    enemy_atk_factor: float = 0.0
    enemy_def_factor: float = 0.0
    enemy_magic_resistance_factor: float = 0.0
    special_phase_stay_time: int = 0
    hint_time_special_phase: int = 0
    hint_time_normal_phase: int = 0
    hint_time_fight_phase: int = 0
    invitation_send_cd: int = 0
    discount_color: str | None = None
    premium_color: str | None = None
    normal_color: str | None = None
    report_max_num: int = 0
    chat_cd: float = Field(default=0.0, alias="chatCD")
    chat_time: float = 0.0
    broadcast_begin_delay: float = 0.0
    no_money_tips_band: list[str] | None = None
    no_skill_tips_band: list[str] | None = None
    boss_trailer_start_round: int = 0
    single_closure_stay_time: float = 0.0
    match_time_max: float = 0.0
    enemy_data_level_id: str | None = None
    player_avatar_win_streak_thresholds: list[int] | None = None
    player_avatar_boss_damage_thresholds: list[float] | None = None
    boss_damage_stats_show_delay_time: float = 0.0


class AutoChessSkinTimeLimitInfo(GameDataModel):
    """clz_Torappu_AutoChessSkinTimeLimitInfo"""

    limit_id: str | None = None
    id: str | None = None
    avail_start_time: int = 0
    avail_end_time: int = 0


class AutoChessSkinData(GameDataModel):
    """clz_Torappu_AutoChessSkinData"""

    id: str | None = None
    name: str | None = None
    type: str = "ACTIVITY"
    skin_trap_id: str | None = None
    rarity: str = "TIER_1"
    sort_id: int = 0
    is_time_limit: bool = False
    thumbnail_pic_id: str | None = None
    preview_pic_id: str | None = None
    background_preview_pic_id: str | None = None
    voice_pack_type: str = "NONE"
    voice_cv: str | None = None
    skin_start_time: int = 0
    skin_desc: str | None = None
    usage_desc: str | None = None
    skin_approach: str | None = None
    time_limit_info_list: dict[str, AutoChessSkinTimeLimitInfo] | None = None


class AutoChessSkinColorData(GameDataModel):
    """clz_Torappu_AutoChessSkinColorData"""

    autochess_skin_id: str | None = None
    garrison_icon_color_1: str | None = None
    garrison_icon_color_2: str | None = None
    garrison_icon_color_3: str | None = None
    bond_color: str | None = None
    bond_icon_color: str | None = None
    chess_name_color: str | None = None
    sale_color_1: str | None = None
    sale_color_2: str | None = None
    destroy_color_1: str | None = None
    destroy_color_2: str | None = None
    countdown_hint_color: str | None = None
    ob_icon_color: str | None = None
    skin_dark_color: str | None = None
    skin_light_color: str | None = None


class AutoChessSkinVoiceTriggerData(GameDataModel):
    """clz_Torappu_AutoChessSkinVoiceTriggerData"""

    trigger: str = "HOME_SHOW"
    probability: float = 0.0
    cd: int = 0
    priority: int = 0


class AutoChessSkinEffectPreviewData(GameDataModel):
    """clz_Torappu_AutoChessSkinEffectPreviewData"""

    effect_id: str | None = None
    sort_id: int = 0
    title: str | None = None
    icon_id: str | None = None
    desc: str | None = None


class AutoChessSkinSoundPreviewData(GameDataModel):
    """clz_Torappu_AutoChessSkinSoundPreviewData"""

    sound_id: str | None = None
    sort_id: int = 0
    title: str | None = None
    voice_use: str | None = None
    voice_id: str | None = None
    place_type: str = "HOME_SHOW"
    sfx_module: str | None = None
    sfx_play_signal: str | None = None
    sfx_sub_signal: str | None = None


class AutoChessSkinConsts(GameDataModel):
    """clz_Torappu_AutoChessSkinConsts"""

    default_auto_chess_skin_id: str | None = None


class OffseasonConstData(GameDataModel):
    """clz_Torappu_OffseasonConstData"""

    off_season_band_frequency: int = 0


class OffseasonData(GameDataModel):
    """clz_Torappu_OffseasonData"""

    offseason_id: str | None = None
    version_id: str | None = None
    offseason_const_data: OffseasonConstData | None = None


class AutoChessData(GameDataModel):
    """clz_Torappu_AutoChessData"""

    version_info_dict: dict[str, AutoChessDataAutoChessVersionInfoData] | None = None
    warmup_schedule_dict: dict[str, AutoChessDataAutoChessWarmupScheduleData] | None = (
        None
    )
    stage_page_display_dict: (
        dict[str, AutoChessDataAutoChessStagePageDisplayData] | None
    ) = None
    band_data_dict: dict[str, AutoChessDataAutoChessBandData] | None = None
    cultivate_effect_list: list[AutoChessDataAutoChessCultivateRelationData] | None = (
        None
    )
    effect_type_data_dict: dict[str, AutoChessDataAutoChessEffectTypeData] | None = None
    bond_info_dict: dict[str, AutoChessDataAutoChessBondInfoData] | None = None
    boss_info_dict: dict[str, AutoChessDataAutoChessBossInfoData] | None = None
    enemy_type_datas: dict[str, AutoChessDataAutoChessEnemyTypeData] | None = None
    enter_step_list: list[AutoChessDataAutoChessEnterStepData] | None = None
    shop_state_token_dict: (
        dict[str, AutoChessDataAutoChessShopStateTokenData] | None
    ) = None
    skill_trigger_data_list: list[AutoChessDataAutoChessSkillTriggerData] | None = None
    skill_range_dict: dict[str, str] | None = None
    prepare_state_dict: dict[str, AutoChessDataAutoChessPrepareStateData] | None = None
    random_enemy_attribute_dict: (
        dict[str, AutoChessDataAutoChessRandomEnemyAttributeData] | None
    ) = None
    enabled_emoticon_theme_id_list: list[str] | None = None
    game_tips_list: list[AutoChessDataAutoChessGameTipData] | None = None
    prize_shop_relation_dict: dict[str, str] | None = None
    medal_data_list: list[AutoChessDataAutoChessMedalData] | None = None
    turn_info_data_dict: (
        dict[str, dict[int, AutoChessDataAutoChessTurnInfoData]] | None
    ) = None
    round_score_data_list: list[AutoChessDataAutoChessRoundScoreData] | None = None
    report_player_data_list: list[CommonReportPlayerData] | None = None
    broadcast_list: list[AutoChessDataAutoChessBroadcastData] | None = None
    boss_damage_stats_style_list: (
        list[AutoChessDataAutoChessBossDamageStatsStyleData] | None
    ) = None
    const_data: AutoChessDataAutoChessConstData | None = None
    skin_data_dict: dict[str, AutoChessSkinData] | None = None
    skin_color_data_dict: dict[str, AutoChessSkinColorData] | None = None
    skin_voice_trigger_data_dict: dict[str, AutoChessSkinVoiceTriggerData] | None = None
    skin_effect_preview_dict: dict[str, list[AutoChessSkinEffectPreviewData]] | None = (
        None
    )
    skin_sound_preview_dict: dict[str, list[AutoChessSkinSoundPreviewData]] | None = (
        None
    )
    skin_voice_anim_dict: dict[str, dict[str, str]] | None = None
    skin_consts: AutoChessSkinConsts | None = None
    offseason_data_dict: dict[str, dict[str, OffseasonData]] | None = None
    perm_shop_id: str | None = None


class ActArkHubItemData(GameDataModel):
    """clz_Torappu_ActArkHubItemData"""

    item_id: str | None = None
    item_num_id: int = 0
    item_type: str = "NONE"
    item_name: str | None = None
    item_usage: str | None = None
    item_desc: str | None = None
    obtain_approach: str | None = None
    stack_limit: int = 0
    max_effect_count: int = 0
    rarity: str = "TIER_1"
    item_sort_id: int = 0
    is_usable: bool = False
    is_show: bool = False
    accumulate_desc: str | None = None


class ArkhubData(GameDataModel):
    """clz_Torappu_ArkhubData"""

    item_data: dict[str, ActArkHubItemData] | None = None


class ActivityTableTemplateTrapData(GameDataModel):
    """clz_Torappu_ActivityTable_TemplateTrapData"""

    trap_id: str | None = None
    sort_id: int = 0
    trap_name: str | None = None
    trap_desc: str | None = None
    trap_text: str | None = None
    trap_icon_1: str | None = None
    trap_icon_2: str | None = None
    trap_task_id: str | None = None
    trap_unlock_desc: str | None = None
    trap_buff_id: str | None = None
    available_count: int = 0


class ActivityTableActivityTrapConstData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityTrapConstData"""

    stage_unlock_trap_desc: str | None = None
    trap_maximum: int = 0
    stage_can_not_use_trap: list[str] | None = None
    must_select_trap: bool = False
    system_unlock_toast: str | None = None
    squad_save_success_toast: str | None = None
    locked_toast: str | None = None
    show_btn_back: bool = False
    use_special_toast: bool = False


class ActivityTableActivityTrapsData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityTrapsData"""

    template_traps: dict[str, ActivityTableTemplateTrapData] | None = None
    trap_const_data: ActivityTableActivityTrapConstData | None = None


class ActivityTableTrapMissionData(GameDataModel):
    """clz_Torappu_ActivityTable_TrapMissionData"""

    id: str | None = None
    description: str | None = None
    type: str = "UNKNOWN"
    rewards: list[MissionDisplayRewards] | None = None


class ActivityTableActivityTrapMissionsData(GameDataModel):
    """clz_Torappu_ActivityTable_ActivityTrapMissionsData"""

    trap_missions: dict[str, ActivityTableTrapMissionData] | None = None


class TemplateMissionStyleData(GameDataModel):
    """clz_Torappu_TemplateMissionStyleData"""

    is_mission_bg_custom_type: bool = False
    big_reward_type: str = "NONE"
    big_reward_param_list: list[str] | None = None
    is_mission_list_common_type: bool = False
    is_mission_item_common_type: bool = False
    mission_item_main_color: str | None = None
    is_mission_item_complete_use_main_color: bool = False
    mission_item_complete_color: str | None = None
    is_mission_reward_item_common_type: bool = False
    is_claim_all_btn_common_type: bool = False
    claim_all_btn_main_color: str | None = None
    claim_all_btn_tips: str | None = None
    title_type: str = "COMMON"
    coin_type: str = "COMMON"
    coin_back_color: str | None = None


class CrossDayTrackData(GameDataModel):
    """clz_Torappu_CrossDayTrackData"""

    update_end_ts: int = 0
    id: str | None = None


class CrossDayTrackTypeData(GameDataModel):
    """clz_Torappu_CrossDayTrackTypeData"""

    type: str | None = None
    start_ts: int = 0
    expire_ts: int = 0
    data_dict: dict[str, CrossDayTrackData] | None = None


class StoryReadTipsData(GameDataModel):
    """clz_Torappu_StoryReadTipsData"""

    key: str | None = None
    pic_id: str | None = None
    main_text: str | None = None
    confirm_text: str | None = None
    is_all: bool = False
    stage_id_list: list[str] | None = None


class ActivityTable(GameDataModel):
    """clz_Torappu_ActivityTable"""

    basic_info: dict[str, ActivityTableBasicData] | None = None
    home_act_config: dict[str, ActivityTableHomeActivityConfig] | None = None
    zone_to_activity: dict[str, str] | None = None
    act_time_track_point: dict[str, int] | None = None
    mission_data: list[MissionData] | None = None
    mission_group: list[MissionGroup] | None = None
    replicate_missions: dict[str, str] | None = None
    activity: ActivityTableActivityDetailTable | None = None
    extra_data: ActivityTableActivityExtraData | None = None
    activity_items: dict[str, list[str]] | None = None
    sync_points: dict[str, list[int]] | None = None
    dyn_acts: dict[str, Any] | None = None
    stage_rewards_data: dict[str, ActivityStageRewardData] | None = None
    act_themes: list[ActivityThemeData] | None = None
    act_fun_data: AprilFoolTable | None = None
    car_data: CartData | None = None
    siracusa_data: SiracusaData | None = None
    firework_data: FireworkData | None = None
    half_idle_data: HalfIdleData | None = None
    ark_news_data: ArkNewsData | None = None
    kv_switch_data: dict[str, ActivityKVSwitchData] | None = None
    dyn_entry_switch_data: dict[str, ActivityDynEntrySwitchData] | None = None
    hidden_stage_data: list[ActivityTableActivityHiddenStageData] | None = None
    mission_archives: dict[str, MissionArchiveData] | None = None
    fifth_anniv_explore_data: FifthAnnivExploreData | None = None
    anniv_7th_data: Anniv7thMainlineData | None = Field(
        default=None, alias="anniv7thData"
    )
    auto_chess_data: AutoChessData | None = None
    arkhub_data: ArkhubData | None = None
    string_res: dict[str, dict[str, str]] | None = None
    activity_traps: dict[str, ActivityTableActivityTrapsData] | None = None
    activity_trap_missions: dict[str, ActivityTableActivityTrapMissionsData] | None = (
        None
    )
    trap_rune_data_dict: dict[str, RuneTablePackedRuneData] | None = None
    activity_template_mission_styles: dict[str, TemplateMissionStyleData] | None = None
    activity_cross_day_track_type_data_dict: dict[str, CrossDayTrackTypeData] | None = (
        None
    )
    activity_cross_day_track_type_map: dict[str, list[str]] | None = None
    activity_story_read_tips_datas: dict[str, StoryReadTipsData] | None = None
    stages_force_play_act_entry_on_first_read: dict[str, list[str]] | None = None


# root_type clz_Torappu_ActivityTable


StageUnlockParam.model_rebuild()
CharUnlockParam.model_rebuild()
CommonAvailCheck.model_rebuild()
ActivityTablePicGroup.model_rebuild()
ActivityTableBasicData.model_rebuild()
ActivityTableHomeActivityConfig.model_rebuild()
MissionDisplayRewards.model_rebuild()
MissionData.model_rebuild()
MissionGroup.model_rebuild()
DefaultZoneData.model_rebuild()
ItemBundle.model_rebuild()
DefaultShopData.model_rebuild()
DefaultFirstData.model_rebuild()
DefaultCheckInDataCheckInDailyInfo.model_rebuild()
DefaultCheckInDataDynCheckInDailyInfo.model_rebuild()
DefaultCheckInDataOptionInfo.model_rebuild()
DefaultCheckInDataDynamicCheckInConsts.model_rebuild()
DefaultCheckInDataDynamicCheckInData.model_rebuild()
DefaultCheckInDataExtraCheckinDailyInfo.model_rebuild()
DefaultCheckInData.model_rebuild()
AllPlayerCheckinDataDailyInfo.model_rebuild()
AllPlayerCheckinDataPublicBehaviour.model_rebuild()
AllPlayerCheckinDataPersonalBehaviour.model_rebuild()
AllPlayerCheckinDataConstData.model_rebuild()
AllPlayerCheckinData.model_rebuild()
VersusCheckInDataDailyInfo.model_rebuild()
VersusCheckInDataVoteData.model_rebuild()
VersusCheckInDataTasteInfoData.model_rebuild()
VersusCheckInDataTasteRewardData.model_rebuild()
VersusCheckInData.model_rebuild()
Act3D0DataCampBasicInfo.model_rebuild()
Act3D0DataLimitedPoolDetailInfoPoolItemInfo.model_rebuild()
Act3D0DataLimitedPoolDetailInfo.model_rebuild()
Act3D0DataInfinitePoolDetailInfoPoolItemInfo.model_rebuild()
Act3D0DataInfinitePoolDetailInfo.model_rebuild()
Act3D0DataInfinitePoolPercent.model_rebuild()
Act3D0DataCampItemMapInfo.model_rebuild()
Act3D0DataClueInfo.model_rebuild()
Act3D0DataMileStoneInfo.model_rebuild()
Act3D0DataGachaBoxInfo.model_rebuild()
Act3D0DataCampInfo.model_rebuild()
Act3D0DataZoneDescInfo.model_rebuild()
CommonFavorUpInfo.model_rebuild()
Act3D0Data.model_rebuild()
Act4D0DataMileStoneItemInfo.model_rebuild()
Act4D0DataMileStoneStoryInfo.model_rebuild()
Act4D0DataStoryInfo.model_rebuild()
Act4D0DataStageJumpInfo.model_rebuild()
Act4D0Data.model_rebuild()
MileStoneInfo.model_rebuild()
Act5D0DataZoneDescInfo.model_rebuild()
Act5D0DataMissionExtraInfo.model_rebuild()
Act5D0Data.model_rebuild()
Act5D1DataRuneStageData.model_rebuild()
Act5D1DataRuneRecurrentStateData.model_rebuild()
Act5D1DataRuneUnlockData.model_rebuild()
Act5D1DataRuneReleaseData.model_rebuild()
Act5D1DataShopGood.model_rebuild()
Act5D1DataProgessGoodItem.model_rebuild()
Act5D1DataShopData.model_rebuild()
RuneDataSelector.model_rebuild()
BlackboardDataPair.model_rebuild()
RuneData.model_rebuild()
RuneTablePackedRuneData.model_rebuild()
RuneTableRuneStageExtraData.model_rebuild()
Act5D1Data.model_rebuild()
ActivityCollectionDataCollectionInfo.model_rebuild()
ActivityCollectionDataConsts.model_rebuild()
ActivityCollectionData.model_rebuild()
Act9D0DataZoneDescInfo.model_rebuild()
Act9D0DataFavorUpInfo.model_rebuild()
Act9D0DataSubMissionInfo.model_rebuild()
Act9D0DataActivityNewsStyleInfo.model_rebuild()
Act9D0DataActivityNewsLine.model_rebuild()
Act9D0DataActivityNewsInfo.model_rebuild()
Act9D0DataActivityNewsServerInfo.model_rebuild()
Act9D0DataAct9D0ConstData.model_rebuild()
Act9D0Data.model_rebuild()
Act12SideDataConstData.model_rebuild()
Act12SideDataZoneAdditionData.model_rebuild()
Act12SideDataMissionDescInfo.model_rebuild()
Act12SideDataMileStoneInfo.model_rebuild()
Act12SideDataPhotoInfo.model_rebuild()
Act12SideDataRecycleDialogData.model_rebuild()
Act12SideData.model_rebuild()
Act13SideDataConstData.model_rebuild()
Act13SideDataPrestigeData.model_rebuild()
Act13SideDataLongTermMissionGroupData.model_rebuild()
Act13SideDataOrgSectionData.model_rebuild()
Act13SideDataOrgData.model_rebuild()
Act13SideDataPrincipalData.model_rebuild()
Act13SideDataLongTermMissionData.model_rebuild()
Act13SideDataDailyMissionData.model_rebuild()
Act13SideDataDailyMissionRewardGroupData.model_rebuild()
Act13SideDataArchiveItemUnlockData.model_rebuild()
ActivityTableActHiddenAreaPreposeStageData.model_rebuild()
ActivityTableActivityHiddenAreaData.model_rebuild()
Act13SideDataZoneAdditionData.model_rebuild()
Act13SideData.model_rebuild()
Act17sideDataPlaceData.model_rebuild()
Act17sideDataNodeInfoData.model_rebuild()
Act17sideDataLandmarkNodeData.model_rebuild()
Act17sideDataStoryNodeData.model_rebuild()
Act17sideDataBattleNodeData.model_rebuild()
Act17sideDataTreasureNodeData.model_rebuild()
Act17sideDataEventNodeData.model_rebuild()
Act17sideDataTechNodeData.model_rebuild()
Act17sideDataChoiceNodeOptionData.model_rebuild()
Act17sideDataChoiceNodeData.model_rebuild()
Act17sideDataEventData.model_rebuild()
Act17sideDataArchiveItemUnlockData.model_rebuild()
Act17sideDataTechTreeData.model_rebuild()
Act17sideDataTechTreeBranchData.model_rebuild()
Act17sideDataMainlineChapterData.model_rebuild()
Act17sideDataMainlineData.model_rebuild()
Act17sideDataZoneData.model_rebuild()
Act17sideDataConstData.model_rebuild()
Act17sideData.model_rebuild()
Act20SideDataResidentCartData.model_rebuild()
Act20SideData.model_rebuild()
Act21SideDataZoneAddtionData.model_rebuild()
Act21SideDataConstData.model_rebuild()
Act21SideData.model_rebuild()
ActivityLoginData.model_rebuild()
ActivitySwitchCheckinConstData.model_rebuild()
ActivitySwitchCheckinRewardItemShowData.model_rebuild()
ActivitySwitchCheckinMainRewardShowData.model_rebuild()
ActivitySwitchCheckinRewardShowData.model_rebuild()
ActivitySwitchCheckinData.model_rebuild()
ActivityMiniStoryDataZoneDescInfo.model_rebuild()
ActivityMiniStoryDataFavorUpInfo.model_rebuild()
ActivityMiniStoryData.model_rebuild()
ActivityRoguelikeDataOuterBuffUnlockInfo.model_rebuild()
ActivityRoguelikeDataOuterBuffUnlockInfoData.model_rebuild()
ActivityRoguelikeDataMileStoneItemInfo.model_rebuild()
ActivityTableCustomUnlockCond.model_rebuild()
ActivityRoguelikeData.model_rebuild()
ActivityInterlockDataStageAdditionData.model_rebuild()
ActivityInterlockDataTreasureMonsterData.model_rebuild()
SharedCharDataSharedCharSkillData.model_rebuild()
SharedCharDataCharEquipInfo.model_rebuild()
SharedCharDataTmplData.model_rebuild()
SharedCharData.model_rebuild()
ActivityInterlockDataMileStoneItemInfo.model_rebuild()
ActivityInterlockDataFinalStageProgressData.model_rebuild()
ActivityInterlockData.model_rebuild()
ActivityBossRushDataZoneAdditionData.model_rebuild()
ActivityBossRushDataBossRushStageGroupData.model_rebuild()
ActivityBossRushDataBossRushStageAdditionData.model_rebuild()
ActivityBossRushDataDisplayDetailRewards.model_rebuild()
ActivityBossRushDataBossRushDropInfo.model_rebuild()
ActivityBossRushDataBossRushMissionAdditionData.model_rebuild()
ActivityBossRushDataBossRushTeamData.model_rebuild()
ActivityBossRushDataRelicData.model_rebuild()
ActivityBossRushDataRelicLevelInfo.model_rebuild()
ActivityBossRushDataRelicLevelInfoData.model_rebuild()
ActivityBossRushDataBossRushMileStoneData.model_rebuild()
ActivityBossRushDataConstData.model_rebuild()
ActivityBossRushData.model_rebuild()
ActivityFloatParadeDataConstData.model_rebuild()
ActivityFloatParadeDataDailyData.model_rebuild()
ActivityFloatParadeDataRewardPool.model_rebuild()
ActivityFloatParadeDataTactic.model_rebuild()
ActivityFloatParadeDataGroupData.model_rebuild()
ActivityFloatParadeData.model_rebuild()
ActivityMainlineBuffDataMissionGroupData.model_rebuild()
ActivityMainlineBuffDataPeriodDataStepData.model_rebuild()
ActivityMainlineBuffDataPeriodData.model_rebuild()
ActivityMainlineBuffDataConstData.model_rebuild()
ActivityMainlineBuffData.model_rebuild()
Act24SideDataToolData.model_rebuild()
Act24SideDataMealData.model_rebuild()
Act24SideDataMeldingItemData.model_rebuild()
Act24SideDataMeldingGachaBoxData.model_rebuild()
Act24SideDataMeldingGachaBoxGoodData.model_rebuild()
Act24SideDataZoneAdditionData.model_rebuild()
QuestStageData.model_rebuild()
Act24SideDataMissionExtraData.model_rebuild()
WeightItemBundle.model_rebuild()
StageDataDisplayRewards.model_rebuild()
StageDataDisplayDetailRewards.model_rebuild()
StageDataStageDropInfo.model_rebuild()
Act24SideDataHuntDatabaseData.model_rebuild()
Act24SideDataConstData.model_rebuild()
Act24SideData.model_rebuild()
Act25SideDataConstData.model_rebuild()
Act25SideDataZoneDescInfo.model_rebuild()
Act25SideDataArchiveItemData.model_rebuild()
Act25SideDataArchiveMapInfoData.model_rebuild()
Act25SideDataAreaInfoData.model_rebuild()
Act25SideDataAreaMissionData.model_rebuild()
Act25SideDataBattlePerformanceData.model_rebuild()
Act25SideDataKeyData.model_rebuild()
Act25SideDataFogUnlockData.model_rebuild()
Act25SideDataDailyFarmData.model_rebuild()
Act25SideData.model_rebuild()
Act27SideDataAct27SideGoodData.model_rebuild()
Act27SideDataAct27SideMileStoneData.model_rebuild()
Act27SideDataAct27SideGoodLaunchData.model_rebuild()
Act27SideDataAct27SideShopData.model_rebuild()
Act27SideDataAct27SideInquireData.model_rebuild()
Act27SideDataAct27SideDynEntrySwitchData.model_rebuild()
Act27SideDataAct27sideZoneAdditionData.model_rebuild()
Act27SideDataAct27SideMileStoneFurniRewardData.model_rebuild()
Act27SideDataAct27SideConstData.model_rebuild()
Act27SideData.model_rebuild()
Act42D0DataAct42D0AreaInfoData.model_rebuild()
Act42D0DataAct42D0StageInfoData.model_rebuild()
Act42D0DataAct42D0EffectGroupInfoData.model_rebuild()
Act42D0DataAct42D0EffectInfoData.model_rebuild()
Act42D0DataAct42D0ChallengeMissionData.model_rebuild()
Act42D0DataAct42D0ChallengeInfoData.model_rebuild()
Act42D0DataAct42D0RatingInfoData.model_rebuild()
Act42D0DataAct42D0StageRatingInfoData.model_rebuild()
Act42D0DataAct42D0MilestoneData.model_rebuild()
Act42D0DataAct42D0ConstData.model_rebuild()
Act42D0Data.model_rebuild()
Act29SideDataAct29SideFragData.model_rebuild()
Act29SideDataAct29SideOrcheData.model_rebuild()
Act29SideDataAct29SideProductGroupData.model_rebuild()
Act29SideDataAct29SideProductData.model_rebuild()
Act29SideDataAct29SideFormData.model_rebuild()
Act29SideDataAct29SideInvestResultData.model_rebuild()
Act29SideDataAct29SideInvestData.model_rebuild()
Act29SideDataAct29SideConstData.model_rebuild()
Act29SideDataAct29SideZoneAdditionData.model_rebuild()
Act29SideDataAct29SideMusicData.model_rebuild()
Act29SideData.model_rebuild()
ActivityYear5GeneralConstData.model_rebuild()
ActivityYear5GeneralUnlimitedApRewardData.model_rebuild()
ActivityYear5GeneralData.model_rebuild()
Act35SideDataAct35SideChallengeData.model_rebuild()
Act35SideDataAct35SideRoundData.model_rebuild()
Act35SideDataAct35SideChallengeTaskData.model_rebuild()
Act35SideDataAct35sideCardMaterialData.model_rebuild()
Act35SideDataAct35SideCardLevelData.model_rebuild()
Act35SideDataAct35SideCardData.model_rebuild()
Act35SideDataAct35SideMaterialData.model_rebuild()
Act35SideDataAct35SideDialogueData.model_rebuild()
Act35SideDataAct35SideDialogueGroupData.model_rebuild()
Act35SideDataAct35SideMileStoneGrandRewardInfo.model_rebuild()
Act35SideDataAct35SideConstData.model_rebuild()
Act35SideDataAct35SideMileStoneData.model_rebuild()
Act35SideDataAct35SideZoneAdditionData.model_rebuild()
Act35SideData.model_rebuild()
ActVecBreakV2BossData.model_rebuild()
ActVecBreakV2OffenseStageData.model_rebuild()
ActVecBreakV2HardStageData.model_rebuild()
ActVecBreakV2DefenseBasicData.model_rebuild()
ActVecBreakV2DefenseDetailData.model_rebuild()
ActVecBreakV2ZoneData.model_rebuild()
ActVecBreakV2DefenseGroupData.model_rebuild()
ActVecBreakV2BattleBuffData.model_rebuild()
ActVecBreakV2MilestoneItemData.model_rebuild()
ActVecBreakV2StageRewardDataLimitedRewardData.model_rebuild()
ActVecBreakV2StageRewardData.model_rebuild()
ActVecBreakV2ConstData.model_rebuild()
ActVecBreakV2ScheduleBlockData.model_rebuild()
ActVecBreakV2Data.model_rebuild()
Act36SideDataAct36SideZoneAdditionData.model_rebuild()
Act36SideDataAct36SideEnemyHandbookData.model_rebuild()
Act36SideDataAct36SideTokenHandbookData.model_rebuild()
Act36SideDataAct36SideConstData.model_rebuild()
Act36SideData.model_rebuild()
Act38SideDataAct38SideZoneAdditionData.model_rebuild()
Act38SideDataAct38SidePuzzleInfo.model_rebuild()
Act38SideDataAct38SideNpcDialogData.model_rebuild()
Act38SideDataConstData.model_rebuild()
Act38SideDataAct38SidePuzzleGroupFocusData.model_rebuild()
Act38SideData.model_rebuild()
ActArcadeDataArcadeStageRankRewardLevelData.model_rebuild()
ActArcadeDataArcadeStageRankRewardData.model_rebuild()
ActArcadeDataArcadeStageAdditionalData.model_rebuild()
ActArcadeDataArcadeZoneAdditionalData.model_rebuild()
ActArcadeDataArcadeBadgeTierData.model_rebuild()
ActArcadeDataArcadeBadgeData.model_rebuild()
ActArcadeDataArcadeBadgeTypeData.model_rebuild()
ActArcadeDataArcadeMilestoneItemData.model_rebuild()
ActArcadeDataArcadeConstData.model_rebuild()
ActArcadeData.model_rebuild()
ActMultiV3SelectStepData.model_rebuild()
ActMultiV3SquadInfoData.model_rebuild()
ActMultiV3IdentityData.model_rebuild()
ActMultiV3SquadEffectDataToken.model_rebuild()
ActMultiV3SquadEffectData.model_rebuild()
ActMultiV3TargetMissionData.model_rebuild()
ActMultiV3MapTypeData.model_rebuild()
ActMultiV3MapData.model_rebuild()
ActMultiV3MapModeData.model_rebuild()
ActMultiV3MapDiffData.model_rebuild()
ActMultiV3TitleData.model_rebuild()
ActMultiV3PhotoSlotData.model_rebuild()
ActMultiV3PhotoTypeData.model_rebuild()
ActMultiV3WeeklyPhotoRewardData.model_rebuild()
ActMultiV3MatchPosUnlockCond.model_rebuild()
ActMultiV3MatchPosData.model_rebuild()
ActMultiV3StarRewardData.model_rebuild()
ActMultiV3DiffStarRewardData.model_rebuild()
ActMultiV3MilestoneData.model_rebuild()
ActMultiV3TipsData.model_rebuild()
CommonReportPlayerData.model_rebuild()
ActMultiV3TempCharData.model_rebuild()
ActMultiV3ConstToastData.model_rebuild()
ActMultiV3ConstDataPingCond.model_rebuild()
ActMultiV3InverseUnlockCond.model_rebuild()
ActMultiV3ConstData.model_rebuild()
ActMultiV3SailBoatLevelPoolData.model_rebuild()
ActMultiV3SailBoatBlockPoolData.model_rebuild()
ActMultiV3SailBoatBlockInfoData.model_rebuild()
ActMultiV3Data.model_rebuild()
ActMainSSZoneAdditionData.model_rebuild()
ActMainSSData.model_rebuild()
ActivityEnemyDuelMilestoneItemData.model_rebuild()
ActivityEnemyDuelModeData.model_rebuild()
ActivityEnemyDuelRoundData.model_rebuild()
ActivityEnemyDuelPoolData.model_rebuild()
ActivityEnemyDuelNpcData.model_rebuild()
ActivityEnemyDuelNpcSelectorData.model_rebuild()
ActivityEnemyDuelNpcSelectorGroupData.model_rebuild()
ActivityEnemyDuelEnemyData.model_rebuild()
ActivityEnemyDuelExtraScoreData.model_rebuild()
ActivityEnemyDuelExtraScoreGroupData.model_rebuild()
ActivityEnemyDuelAnnounceData.model_rebuild()
ActivityEnemyDuelSingleCommentData.model_rebuild()
ActivityEnemyDuelConstDataPingCond.model_rebuild()
ActivityEnemyDuelConstData.model_rebuild()
ActivityEnemyDuelConstToastData.model_rebuild()
ActivityEnemyDuelTipsData.model_rebuild()
ActivityEnemyDuelData.model_rebuild()
Act42SideDataAct42SideTrustorData.model_rebuild()
Act42SideDataAct42SideTaskData.model_rebuild()
Act42SideDataAct42SideGunData.model_rebuild()
Act42SideDataAct42SideFileData.model_rebuild()
Act42SideDataAct42SideDailyRewardData.model_rebuild()
Act42SideDataAct42SideConstData.model_rebuild()
Act42SideDataAct42SideZoneAdditionData.model_rebuild()
Act42SideData.model_rebuild()
Act44SideDataAct44SideZoneAdditionData.model_rebuild()
Act44SideDataAct44SideCustomerData.model_rebuild()
Act44SideDataAct44SideTagData.model_rebuild()
Act44SideDataAct44SideChoiceData.model_rebuild()
Act44SideDataAct44SideNewsData.model_rebuild()
Act44SideDataAct44SideInsightData.model_rebuild()
Act44SideDataAct44SideMileStoneData.model_rebuild()
Act44SideDataAct44SideMilestoneSpecialRewardInfo.model_rebuild()
Act44SideDataAct44SideConstData.model_rebuild()
Act44SideData.model_rebuild()
Act1VHalfIdleGachaPoolDataConsumeData.model_rebuild()
Act1VHalfIdleGachaPoolData.model_rebuild()
Act1VHalfIdleGachaCharData.model_rebuild()
Act1VHalfIdlePlotTypeData.model_rebuild()
Act1VHalfIdlePlotDataItemDropData.model_rebuild()
Act1VHalfIdlePlotDataPlotCombineDataCombineItemData.model_rebuild()
Act1VHalfIdlePlotDataPlotCombineData.model_rebuild()
Act1VHalfIdlePlotData.model_rebuild()
Act1VHalfIdleStageProductionDataItemProductionData.model_rebuild()
Act1VHalfIdleStageProductionData.model_rebuild()
Act1VHalfIdleCharRankDataCharRankData.model_rebuild()
Act1VHalfIdleCharRankData.model_rebuild()
Act1VHalfIdleCharEvolveDataEvolveData.model_rebuild()
Act1VHalfIdleCharEvolveDataProfessionCharEvolveData.model_rebuild()
Act1VHalfIdleCharEvolveData.model_rebuild()
Act1VHalfIdleCharMaxRankDataMaxRankData.model_rebuild()
Act1VHalfIdleCharMaxRankData.model_rebuild()
Act1VHalfIdleCharSkillRankDataSkillRankData.model_rebuild()
Act1VHalfIdleCharSkillRankData.model_rebuild()
Act1VHalfIdleTechTreeDataEffect.model_rebuild()
Act1VHalfIdleTechTreeData.model_rebuild()
Act1VHalfIdleCharBuffInfo.model_rebuild()
Act1VHalfIdleCharBuffData.model_rebuild()
Act1VHalfIdleMilestoneItemData.model_rebuild()
Act1VHalfIdleGachaPoolTypeData.model_rebuild()
Act1VHalfIdleEnemyPreloadMeta.model_rebuild()
Act1VHalfIdleConstDataProfessionDesc.model_rebuild()
Act1VHalfIdleConstData.model_rebuild()
UnityEngineVector2.model_rebuild()
Act1VHalfIdleDiagramDataPointPosData.model_rebuild()
Act1VHalfIdleDiagramDataLinePosData.model_rebuild()
Act1VHalfIdleDiagramDataLineRelationData.model_rebuild()
Act1VHalfIdleDiagramDataNodePointData.model_rebuild()
Act1VHalfIdleDiagramData.model_rebuild()
Act1VHalfIdleEnemyDropBundle.model_rebuild()
Act1VWeightedBattleItemPool.model_rebuild()
Act1VBattleItemDropSlot.model_rebuild()
Act1VWeightedResItemBundle.model_rebuild()
Act1VHalfIdleWeightedBattleEquip.model_rebuild()
Act1VHalfIdleEquipData.model_rebuild()
Act1VHalfIdleTrapMeta.model_rebuild()
Act1VHalfIdleData.model_rebuild()
Act45SideDataAct45SideCharData.model_rebuild()
Act45SideDataAct45SideMailData.model_rebuild()
Act45SideDataAct45SideConstData.model_rebuild()
Act45SideDataAct45SideZoneAdditionData.model_rebuild()
Act45SideData.model_rebuild()
ActRecruitOnlyDataRecruitOnlyItemData.model_rebuild()
ActRecruitOnlyData.model_rebuild()
Act46SideDataAct46SideZoneAdditionData.model_rebuild()
Act46SideDataAct46SideMonopolyStageData.model_rebuild()
Act46SideDataAct46SideMonopolyBuffData.model_rebuild()
Act46SideDataAct46SideSettleDialogData.model_rebuild()
Act46SideDataAct46SideConstData.model_rebuild()
Act46SideDataAct46SideMonopolyResourceItemData.model_rebuild()
Act46SideData.model_rebuild()
ActAutoChessDataActAutoChessModeData.model_rebuild()
ActAutoChessDataActAutoChessModeGroupData.model_rebuild()
ActAutoChessDataActAutoChessShopLevelDisplayData.model_rebuild()
ActAutoChessDataActAutoChessStageData.model_rebuild()
ActAutoChessDataActAutochessSpecialEnemyTypeEntry.model_rebuild()
ActivityCommonMilestoneData.model_rebuild()
ActivityPeriodicalRewardConf.model_rebuild()
ActAutoChessDataActAutoChessPlayerTitleData.model_rebuild()
ActAutoChessDataActAutoChessShopCharChessInfoData.model_rebuild()
ActAutoChessDataActAutoChessConstData.model_rebuild()
UITemplateShopTemplateShopDataShopGood.model_rebuild()
UITemplateShopTemplateShopDataProgessGoodItem.model_rebuild()
UITemplateShopTemplateShopDataTShopGroup.model_rebuild()
UITemplateShopTemplateShopDataGroupShopExtraData.model_rebuild()
UITemplateShopTemplateShopDataShopAccumulativePrizeItem.model_rebuild()
UITemplateShopTemplateShopData.model_rebuild()
ActAutoChessDataActAutoChessBandData.model_rebuild()
ActAutoChessDataActAutoChessBondInfo.model_rebuild()
ActAutoChessDataActAutoChessGarrisonData.model_rebuild()
ActAutoChessDataActAutoChessEffectDescParamInfo.model_rebuild()
ActAutoChessDataActAutoChessEffectDescParamData.model_rebuild()
ActAutoChessDataActAutoChessEffectInfoData.model_rebuild()
ActAutoChessDataActAutoChessSkillInfoData.model_rebuild()
ActAutoChessDataActAutoChessBuffInfoData.model_rebuild()
ActAutoChessDataActAutoChessShopLevelData.model_rebuild()
ActAutoChessDataActAutoChessCharChessStatusData.model_rebuild()
ActAutoChessDataActAutoChessCharChessData.model_rebuild()
ActAutoChessDataActAutoChessCharShopChessData.model_rebuild()
ActAutoChessDataAutoChessTrapChessStatusData.model_rebuild()
ActAutoChessDataActAutoChessTrapChessData.model_rebuild()
ActAutoChessDataActAutoChessTrapShopChessData.model_rebuild()
ActAutoChessDataActAutoChessEffectChoiceInfoData.model_rebuild()
ActAutoChessDataActAutoChessBattleData.model_rebuild()
ActAutoChessDataActAutochessBossEntry.model_rebuild()
ActAutoChessDataActAutochessSpecialEnemyEntry.model_rebuild()
ActAutoChessDataActAutoChessTrainingNpcData.model_rebuild()
AutoChessDataAutoChessBandData.model_rebuild()
AutoChessDataAutoChessBondInfoData.model_rebuild()
AutoChessDataAutoChessBossInfoData.model_rebuild()
AutoChessDataAutoChessRandomEnemyAttributeData.model_rebuild()
ActAutoChessTrainingDataAutoChessTrainingData.model_rebuild()
ActAutoChessTrainingDataTrainingConstData.model_rebuild()
ActAutoChessTrainingDataTrainingShopSlotData.model_rebuild()
ActAutoChessTrainingDataTrainingRoundInfoData.model_rebuild()
ActAutoChessTrainingDataTrainingSpecialChoiceData.model_rebuild()
ActAutoChessTrainingDataTrainingNpcDeployData.model_rebuild()
ActAutoChessTrainingDataTrainingDiyChessData.model_rebuild()
ActAutoChessTrainingData.model_rebuild()
ActAutoChessData.model_rebuild()
ActFootballDataActFootballZoneAdditionData.model_rebuild()
ActFootballDataActFootballStageAdditionData.model_rebuild()
ActFootballDataActFootballMilestoneItemData.model_rebuild()
ActFootballDataActFootballNPCCharData.model_rebuild()
ActFootballDataActFootballConstData.model_rebuild()
ActFootballData.model_rebuild()
ArkdexModeData.model_rebuild()
ArkdexCreatureData.model_rebuild()
ArkdexAdvantageTypeData.model_rebuild()
ArkdexNpcInfoData.model_rebuild()
ArkdexNpcDuelCreatureData.model_rebuild()
ArkdexNpcDuelStrategyData.model_rebuild()
ArkdexItemEffectData.model_rebuild()
ArkdexTraitData.model_rebuild()
ArkdexNpcBattleParamData.model_rebuild()
ArkdexNpcPixelData.model_rebuild()
ArkdexCaptureAreaData.model_rebuild()
PingCond.model_rebuild()
UnityEngineVector3.model_rebuild()
ArkventRangeData.model_rebuild()
ArkdexConstData.model_rebuild()
ArkdexModuleData.model_rebuild()
ArkpixelConstData.model_rebuild()
ArkpixelReleaseStageData.model_rebuild()
ArkpixelModuleData.model_rebuild()
ActArkHubModuleData.model_rebuild()
ActArkHubInteractiveUnitData.model_rebuild()
ActArkHubMenuData.model_rebuild()
ActArkHubConstData.model_rebuild()
ActArkHubMoveFixData.model_rebuild()
ArkventMovePresetData.model_rebuild()
ActArkHubPlayerStateInfoData.model_rebuild()
ActArkHubRewardItem.model_rebuild()
ActArkHubRewardData.model_rebuild()
ActArkhubLoadingTipData.model_rebuild()
ActArkHubData.model_rebuild()
Act53SideDataAct53SideZoneAdditionData.model_rebuild()
Act53SideDataAct53SideConstData.model_rebuild()
Act53SideData.model_rebuild()
Act54SideDataAct54SideCardData.model_rebuild()
Act54SideDataAct54SideSpreadItemInfo.model_rebuild()
Act54SideDataAct54SideSpreadData.model_rebuild()
Act54SideDataAct54SideSpecialZoneStageInfo.model_rebuild()
Act54SideDataAct54SideZoneAdditionData.model_rebuild()
Act54SideDataAct54SideConstData.model_rebuild()
Act54SideData.model_rebuild()
ActVasebreakerDataActVasebreakerZoneAdditionData.model_rebuild()
ActVasebreakerDataActVasebreakerStageAdditionData.model_rebuild()
ActVasebreakerDataActVasebreakerStageUnlockToastData.model_rebuild()
ActVasebreakerDataActVasebreakerStageDropData.model_rebuild()
ActVasebreakerDataActVasebreakerMilestoneItemData.model_rebuild()
ActVasebreakerDataActVasebreakerStickerData.model_rebuild()
ActVasebreakerDataActVasebreakerConstData.model_rebuild()
ActVasebreakerData.model_rebuild()
Act55SideDataAct55SideZoneAdditionData.model_rebuild()
Act55SideDataAct55SideNewspaperData.model_rebuild()
Act55SideDataAct55SideFixedReportData.model_rebuild()
Act55SideDataAct55SideHandReportData.model_rebuild()
Act55SideDataAct55SideHandReportColorData.model_rebuild()
Act55SideDataAct55SideBattleItemLevelData.model_rebuild()
Act55SideDataAct55SideConstData.model_rebuild()
Act55SideData.model_rebuild()
ActivityTableActivityDetailTable.model_rebuild()
ActMainlineBpExtraDataActMainlineBpExtraPeriodData.model_rebuild()
ActMainlineBpExtraData.model_rebuild()
ActivityTableActivityExtraData.model_rebuild()
HgInternalJObject.model_rebuild()
ActivityStageRewardData.model_rebuild()
ActivityThemeDataTimeNode.model_rebuild()
ActivityThemeDataPicGroup.model_rebuild()
ActivityThemeData.model_rebuild()
StageDataConditionDesc.model_rebuild()
AprilFoolStageData.model_rebuild()
AprilFoolScoreData.model_rebuild()
AprilFoolConst.model_rebuild()
Act4funPerformGroupInfo.model_rebuild()
Act4funPerformWordData.model_rebuild()
Act4funPerformInfo.model_rebuild()
Act4funLiveMatEffectInfo.model_rebuild()
Act4funLiveMatInfoData.model_rebuild()
Act4funSpLiveMatInfoData.model_rebuild()
Act4funValueEffectInfoData.model_rebuild()
Act4funLiveValueInfoData.model_rebuild()
Act4funSuperChatInfo.model_rebuild()
Act4funCmtInfo.model_rebuild()
Act4funCmtGroupInfo.model_rebuild()
Act4funEndingInfo.model_rebuild()
Act4funTokenInfoData.model_rebuild()
Act4funMissionData.model_rebuild()
Act4funConst.model_rebuild()
Act4funStageExtraData.model_rebuild()
Act4funData.model_rebuild()
Act5funConst.model_rebuild()
Act5FunRoundData.model_rebuild()
Act5FunNpcData.model_rebuild()
Act5FunNpcSelectorData.model_rebuild()
Act5FunChoiceRewardData.model_rebuild()
Act5FunEnemyIdMappingData.model_rebuild()
Act5FunDataBattleData.model_rebuild()
Act5funBasicConst.model_rebuild()
Act5FunBasicNpcData.model_rebuild()
Act5FunSettleRatingData.model_rebuild()
Act5FunSettleStreakData.model_rebuild()
Act5FunSettleSuccessData.model_rebuild()
Act5FunData.model_rebuild()
Act6FunStageAdditionData.model_rebuild()
Act6FunAchievementData.model_rebuild()
Act6FunAchievementRewardData.model_rebuild()
Act6FunConst.model_rebuild()
Act6FunData.model_rebuild()
Act7FunStageAdditionData.model_rebuild()
Act7FunEasterEggData.model_rebuild()
Act7FunSpineHolderData.model_rebuild()
Act7FunSpineGroupData.model_rebuild()
Act7FunCharAnimData.model_rebuild()
Act7FunConstData.model_rebuild()
Act7FunData.model_rebuild()
AprilFoolTable.model_rebuild()
CartComponents.model_rebuild()
CartDataCartConstData.model_rebuild()
CartData.model_rebuild()
SiracusaDataAreaData.model_rebuild()
SiracusaDataPointData.model_rebuild()
SiracusaDataCharCardData.model_rebuild()
SiracusaDataTaskRingData.model_rebuild()
SiracusaDataTaskBasicInfoData.model_rebuild()
SiracusaDataBattleTaskData.model_rebuild()
SiracusaDataAVGTaskData.model_rebuild()
SiracusaDataItemInfoData.model_rebuild()
SiracusaDataItemCardInfoData.model_rebuild()
SiracusaDataNavigationInfoData.model_rebuild()
SiracusaDataOptionInfoData.model_rebuild()
SiracusaDataStagePointInfoData.model_rebuild()
SiracusaDataStoryBriefInfoData.model_rebuild()
SiracusaDataOperaInfoData.model_rebuild()
SiracusaDataOperaCommentInfoData.model_rebuild()
SiracusaDataConstData.model_rebuild()
SiracusaData.model_rebuild()
GridPosition.model_rebuild()
FireworkDataPlateContent.model_rebuild()
FireworkDataPlateData.model_rebuild()
FireworkDataAnimalData.model_rebuild()
FireworkDataLevelData.model_rebuild()
FireworkDataConstData.model_rebuild()
FireworkData.model_rebuild()
Act1VHalfIdleItemData.model_rebuild()
HalfIdleData.model_rebuild()
ArkNewsDataArkNewsBuffItemData.model_rebuild()
ArkNewsData.model_rebuild()
KVSwitchInfo.model_rebuild()
ActivityKVSwitchData.model_rebuild()
DynEntrySwitchInfo.model_rebuild()
DynEntryAnimationInfo.model_rebuild()
ActivityDynEntrySwitchData.model_rebuild()
ActivityTableActivityHiddenStageUnlockConditionData.model_rebuild()
ActivityTableActivityHiddenStageData.model_rebuild()
MissionArchiveVoiceClipData.model_rebuild()
MissionArchiveNodeData.model_rebuild()
MissionArchiveData.model_rebuild()
FifthAnnivExploreGroupData.model_rebuild()
FifthAnnivExploreStageData.model_rebuild()
FifthAnnivExploreTargetData.model_rebuild()
FifthAnnivExploreEventData.model_rebuild()
FifthAnnivExploreEventChoiceData.model_rebuild()
FifthAnnivExploreBroadcastData.model_rebuild()
FifthAnnivExploreConst.model_rebuild()
FifthAnnivExploreMissionData.model_rebuild()
FifthAnnivExploreData.model_rebuild()
Anniv7thClueGroupData.model_rebuild()
Anniv7thClueData.model_rebuild()
Anniv7thClueRewardData.model_rebuild()
Anniv7thDisplayData.model_rebuild()
Anniv7thDisplayNodeData.model_rebuild()
Anniv7thClueConstData.model_rebuild()
Anniv7thMainlineData.model_rebuild()
AutoChessDataAutoChessVersionInfoData.model_rebuild()
AutoChessDataAutoChessWarmupScheduleData.model_rebuild()
AutoChessDataAutoChessStagePageDisplayData.model_rebuild()
AutoChessDataAutoChessCultivateRelationData.model_rebuild()
AutoChessDataAutoChessEffectTypeData.model_rebuild()
AutoChessDataAutoChessEnemyTypeData.model_rebuild()
AutoChessDataAutoChessEnterStepData.model_rebuild()
AutoChessDataAutoChessShopStateTokenData.model_rebuild()
AutoChessDataAutoChessSkillTriggerData.model_rebuild()
AutoChessDataAutoChessPrepareStateData.model_rebuild()
AutoChessDataAutoChessGameTipData.model_rebuild()
AutoChessDataAutoChessMedalData.model_rebuild()
AutoChessDataAutoChessTurnInfoData.model_rebuild()
AutoChessDataAutoChessRoundScoreData.model_rebuild()
AutoChessDataAutoChessBroadcastData.model_rebuild()
AutoChessDataAutoChessBossDamageStatsStyleData.model_rebuild()
AutoChessDataAutoChessConstData.model_rebuild()
AutoChessSkinTimeLimitInfo.model_rebuild()
AutoChessSkinData.model_rebuild()
AutoChessSkinColorData.model_rebuild()
AutoChessSkinVoiceTriggerData.model_rebuild()
AutoChessSkinEffectPreviewData.model_rebuild()
AutoChessSkinSoundPreviewData.model_rebuild()
AutoChessSkinConsts.model_rebuild()
OffseasonConstData.model_rebuild()
OffseasonData.model_rebuild()
AutoChessData.model_rebuild()
ActArkHubItemData.model_rebuild()
ArkhubData.model_rebuild()
ActivityTableTemplateTrapData.model_rebuild()
ActivityTableActivityTrapConstData.model_rebuild()
ActivityTableActivityTrapsData.model_rebuild()
ActivityTableTrapMissionData.model_rebuild()
ActivityTableActivityTrapMissionsData.model_rebuild()
TemplateMissionStyleData.model_rebuild()
CrossDayTrackData.model_rebuild()
CrossDayTrackTypeData.model_rebuild()
StoryReadTipsData.model_rebuild()
ActivityTable.model_rebuild()

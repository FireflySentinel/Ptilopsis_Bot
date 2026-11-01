"""sandbox_perm_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/sandbox_perm_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class SandboxPermTemplateType(IntEnum):
    """enum__Torappu_SandboxPermTemplateType"""

    NONE = 0
    SANDBOX_V2 = 1
    SANDBOX_V3 = 2


class SandboxV2TrapItemType(IntEnum):
    """enum__Torappu_SandboxV2TrapItemType"""

    NONE = 0
    BATTLE = 1
    TACTICAL = 2
    FUNCTION = 3
    ANIMAL = 4


class SandboxV2ItemTrapTag(IntEnum):
    """enum__Torappu_SandboxV2ItemTrapTag"""

    OUTPUT = 0
    COLLECTION = 1
    IMPAIR = 2
    ENHANCE = 3
    EXPLORE = 4
    SPECTACLE = 5
    DECORATE = 6
    DEFEND = 7
    SCOUT = 8


class SandboxV2CraftItemType(IntEnum):
    """enum__Torappu_SandboxV2CraftItemType"""

    BASE_BUILDING = 0
    TACTICAL = 1
    COMBAT_BUILDING = 2


class SandboxPermItemType(IntEnum):
    """enum__Torappu_SandboxPermItemType"""

    NONE = 0
    TACTICAL = 1
    BUILDING = 2
    BUILDINGMAT = 3
    FOOD = 4
    FOODMAT = 5
    SPECIALMAT = 6
    COIN = 9
    CRAFT = 10
    PLACEHOLDER = 11
    STAMINAPOT = 12
    ANIMAL = 13
    INSECT = 14
    SLUGITEM = 15
    RELIC = 16
    RECIPE = 17
    PRODUCT = 18
    TOOLKIT = 19
    RANDRELIC = 20
    RANDRECIPE = 21
    CURRENCY = 22
    COOKBOOK = 23
    BASEBUILDING = 24
    BASECOIN = 25
    BASEANIMAL = 26
    BASETACTICAL = 27
    TECHPOINT = 28


class SandboxFoodMatType(IntEnum):
    """enum__Torappu_SandboxFoodMatType"""

    MAIN = 0
    SUB = 1


class SandboxFoodAttribute(IntEnum):
    """enum__Torappu_SandboxFoodAttribute"""

    NONE = 0
    SURVIVE = 1
    COST = 2
    ATTACK = 3
    COOLDOWN = 4
    SKILL_POINT = 5
    SPECIAL = 6
    ENHANCED = 7
    FUNCTION = 8


class SandboxFoodVariantType(IntEnum):
    """enum__Torappu_SandboxFoodVariantType"""

    NONE = 0
    ALPHA = 1
    BETA = 2
    GAMMA = 3


class SandboxV2NodeType(IntEnum):
    """enum__Torappu_SandboxV2NodeType"""

    NONE = 0
    HOME = 1
    HOME_OUTPOST = 2
    BATTLE = 3
    NEST = 4
    COLLECT = 5
    HUNT = 6
    CAVE = 7
    MINE = 8
    ENCOUNTER = 9
    EXPEDITION = 10
    SHOP = 11
    GATE = 12
    MARKET = 13
    HOME_PORTABLE = 14
    HOME_PORTABLE_RIFT = 15
    SELECTION = 16
    RACING = 17


class SandboxV2WeatherType(IntEnum):
    """enum__Torappu_SandboxV2WeatherType"""

    NORMAL = 0
    RAINFOREST = 1
    VOLCANO = 2
    DESERT = 3


class SandboxV2EnemyRushType(IntEnum):
    """enum__Torappu_SandboxV2EnemyRushType"""

    NORMAL = 0
    ELITE = 1
    BOSS = 2
    BANDIT = 3
    RALLY = 4
    THIEF = 5
    MESSENGER = 6
    INSECT = 7


class SandboxV2SeasonType(IntEnum):
    """enum__Torappu_SandboxV2SeasonType"""

    NONE = 0
    DRY = 1
    RAINY = 2
    CHALLENGE = 3


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


class TipDataCategory(IntEnum):
    """enum__Torappu_TipData_Category"""

    NONE = 0
    BATTLE = 1
    UI = 2
    BUILDING = 4
    GACHA = 8
    MISC = 16
    ALL = 31


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


class LevelDataDifficulty(IntEnum):
    """enum__Torappu_LevelData_Difficulty"""

    NONE = 0
    NORMAL = 1
    FOUR_STAR = 2
    EASY = 4
    SIX_STAR = 8
    ALL = 15


class SandboxV2QuestRouteType(IntEnum):
    """enum__Torappu_SandboxV2QuestRouteType"""

    NONE = 0
    ENEMY_RUSH = 1
    EVENT = 2
    NODE = 3
    NPC = 4


class SandboxV2QuestLineType(IntEnum):
    """enum__Torappu_SandboxV2QuestLineType"""

    NONE = 0
    MAIN = 1
    SIDE = 2
    GUIDE = 3
    TRAINING = 4


class SandboxV2NpcType(IntEnum):
    """enum__Torappu_SandboxV2NpcType"""

    NORMAL = 0
    FIXED_RIFT = 1
    RANDOM_RIFT = 2
    PREY_RIFT = 3


class BattleDialogType(IntEnum):
    """enum__Torappu_BattleDialogType"""

    NONE = 0
    BEFORE = 1
    REACT = 2
    AFTER = 3
    ENUM = 4


class SharedConstsDirection(IntEnum):
    """enum__Torappu_SharedConsts_Direction"""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    E_NUM = 4
    INVALID = 4


class SandboxV2QuestLineBadgeType(IntEnum):
    """enum__Torappu_SandboxV2QuestLineBadgeType"""

    NONE = 0
    SIDE = 1
    GUIDE = 2
    MAIN = 3
    RIFT = 4


class SandboxV2QuestLineScopeType(IntEnum):
    """enum__Torappu_SandboxV2QuestLineScopeType"""

    MAIN = 0
    RIFT = 1
    ALL = 2


class SandboxDevelopmentType(IntEnum):
    """enum__Torappu_SandboxDevelopmentType"""

    NONE = 0
    SURVIVE = 1
    COLLECT = 2
    SHOP = 3
    BATTLE = 4
    DUNGEON = 5
    EXPLORE = 6
    RESOURCE = 7
    INITIAL = 8


class SandboxV2EventType(IntEnum):
    """enum__Torappu_SandboxV2EventType"""

    NONE = 0
    EVENT = 1
    MISSION = 2
    QUEST_EVENT = 3
    QUEST_MISSION = 4


class SandboxV2EventChoiceType(IntEnum):
    """enum__Torappu_SandboxV2EventChoiceType"""

    NONE = 0
    NEXT = 1
    LEAVE = 2
    MISSION = 3


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


class SandboxShopCoinType(IntEnum):
    """enum__Torappu_SandboxShopCoinType"""

    DIMENSION_COIN = 0
    GOLD = 1
    BASE_GOLD = 2
    BASE_GOLDEX = 3


class SandboxV2RiftMainTargetType(IntEnum):
    """enum__Torappu_SandboxV2RiftMainTargetType"""

    NONE = 0
    FIND = 1
    BOSS_HUNT = 2
    WILD_HUNT = 3
    PROTECT = 4
    FIGHT = 5
    CATCH_THIEF = 6
    PREY_HUNT = 7


class SandboxArchiveQuestType(IntEnum):
    """enum__Torappu_SandboxArchiveQuestType"""

    NONE = 0
    MAIN = 1
    SIDE = 2


class SandboxV2BaseUnlockFuncType(IntEnum):
    """enum__Torappu_SandboxV2BaseUnlockFuncType"""

    NONE = 0
    HOME_PUTPOST = 1
    HOME_PORTABLE = 2
    REWARDSHOP = 3
    TECH = 4
    REAR = 5
    BUILD = 6
    SHOP = 7
    RACING = 8


class SandboxV2BaseUnlockFuncDisplayType(IntEnum):
    """enum__Torappu_SandboxV2BaseUnlockFuncDisplayType"""

    NONE = 0
    NEW = 1
    UPDATE = 2
    NUMBER = 3


class SandboxDevelopmentLineStyle(IntEnum):
    """enum__Torappu_SandboxDevelopmentLineStyle"""

    EMPTY = 0
    LEVEL_PASS = 1
    LEVEL_BLOCK = 2


class SandboxV2ConfirmIconType(IntEnum):
    """enum__Torappu_SandboxV2ConfirmIconType"""

    COMMON = 0
    EMERGENCY = 1
    QUIT = 2
    EVACUATE = 3
    EVACUATELOSS = 4
    NORMAL = 5
    COMBAT = 6
    CONSTRUCT = 7
    NEXTDAY = 8
    RIFT_EXIT = 9
    LOAD_ARCHIVE = 10


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


class SandboxV2RacerTalentType(IntEnum):
    """enum__Torappu_SandboxV2RacerTalentType"""

    BORN = 0
    LEARNED = 1


class SandboxV2RacerNameType(IntEnum):
    """enum__Torappu_SandboxV2RacerNameType"""

    PREFIX = 0
    SUFFIX = 1


class SandboxV3MapTileType(IntEnum):
    """enum__Torappu_SandboxV3MapTileType"""

    NONE = 0
    TEXTURE = 1
    BUILDING = 2


class SandboxV3NodeType(IntEnum):
    """enum__Torappu_SandboxV3NodeType"""

    NONE = 0
    HOME = 1
    STORY = 2
    EXPLORE = 3


class SandboxV3MilestoneStage(IntEnum):
    """enum__Torappu_SandboxV3MilestoneStage"""

    EARLY = 0
    MIDDLE = 1
    LATE = 2


class SandboxV3BagItemType(IntEnum):
    """enum__Torappu_SandboxV3BagItemType"""

    NONE = 0
    MATERIALBAG = 1
    RELICBAG = 2


class SandboxV3BasementUnlockFuncType(IntEnum):
    """enum__Torappu_SandboxV3BasementUnlockFuncType"""

    NONE = 0
    HOME_PUTPOST = 1
    TECH = 2
    MAP = 3


class SandboxV3BasementUnlockFuncDisplayType(IntEnum):
    """enum__Torappu_SandboxV3BasementUnlockFuncDisplayType"""

    NONE = 0
    NEW = 1
    UPDATE = 2
    NUMBER = 3


class ScoreGroupType(IntEnum):
    """enum__Torappu_ScoreGroupType"""

    WONDER = 0
    DEBRIS_CLEAN = 1
    NPC_RECRUIT = 2
    TRAP_BUILD = 3
    TRAP_RULE = 4


class SandboxV3NpcType(IntEnum):
    """enum__Torappu_SandboxV3NpcType"""

    NORMAL = 0
    BASE = 1


class SandboxV3QuestLineBadgeType(IntEnum):
    """enum__Torappu_SandboxV3QuestLineBadgeType"""

    NONE = 0
    MAIN = 1
    SIDE = 2
    GUIDE = 3


class SandboxV3ShopType(IntEnum):
    """enum__Torappu_SandboxV3ShopType"""

    NONE = 0
    REST = 1
    BATTLE = 2


class SandboxV3TrapType(IntEnum):
    """enum__Torappu_SandboxV3TrapType"""

    PRODUCER = 0
    INFRASTRUCTURE = 1
    PROCESSOR = 2
    SERVICE = 3
    AESTHETICS = 4
    TACTICAL = 5


class SandboxV3BaseTrapType(IntEnum):
    """enum__Torappu_SandboxV3BaseTrapType"""

    NONE = 0
    PATH = 1
    AGRICULTURE = 2
    SETTLEMENT = 3
    PDLINE = 4
    DECORATION = 5
    OTHER = 6


class SandboxV3BaseBuildType(IntEnum):
    """enum__Torappu_SandboxV3BaseBuildType"""

    NONE = 0
    ROAD = 1
    CANAL = 2
    RAILWAY = 3
    PRODUCTION = 4
    HOUSE = 5
    POWER = 6
    BEAUTY = 7


class SandboxV3ElectricTransferType(IntEnum):
    """enum__Torappu_SandboxV3ElectricTransferType"""

    NONE = 0
    FUNCTION = 1
    SUPPLY = 2
    ADDITION = 3
    AMPLIFY = 4


class SandboxV3BuildScoreType(IntEnum):
    """enum__Torappu_SandboxV3BuildScoreType"""

    NONE = 0
    NPC = 1
    TRAP = 2
    LEVEL = 3
    ENPC = 4


class SandboxV3EnemyRewardType(IntEnum):
    """enum__Torappu_SandboxV3EnemyRewardType"""

    NONE = 0
    ITEM = 1
    POWER = 2
    LUCKYDROP = 3


class SandboxV3TaskDifficultyType(IntEnum):
    """enum__Torappu_SandboxV3TaskDifficultyType"""

    NONE = 0
    EASY = 1
    NORMAL = 2
    HARD = 3


class SandboxV3TaskType(IntEnum):
    """enum__Torappu_SandboxV3TaskType"""

    DEPLOY_TRAP_BY_GROUP = 0
    CONSTRUCT_TRAP_BY_GROUP = 1
    OWN_TRAP_BY_GROUP = 2
    OWN_TRAP_AND_DELIVER = 3
    OWN_TRAP_BY_TYPE = 4
    ITEM_DELIVERY = 5
    GATHER = 6
    KILL_ENEMY = 7
    KILL_ENEMY_FILTER_BY_TAG = 8
    KILL_ENEMY_FILTER_BY_LEVELTYPE = 9
    UNLOCK_ROOM_BY_MASK = 10
    UNLOCK_ROOM_CULMULATIVE = 11
    CATCH_ANIMAL = 12
    PROSPERITY_KEEP = 13
    AESTHETICS_REACH = 14
    PROSPERITY_REACH = 15
    AESTHETICS_INCREASE = 16
    PROSPERITY_INCREASE = 17
    TRADE_IN_SALE = 18
    CHARACTER_CHECK = 19
    RAILWAY_CHECK = 20


class SandboxPermBasicDataHomeEntryDisplayData(GameDataModel):
    """clz_Torappu_SandboxPermBasicData_HomeEntryDisplayData"""

    display_id: str | None = None
    topic_id: str | None = None
    start_ts: int = 0
    end_ts: int = 0


class SandboxPermEnrollPointData(GameDataModel):
    """clz_Torappu_SandboxPermEnrollPointData"""

    enroll_point_id: str | None = None
    enroll_time: int = 0


class SandboxPermBasicData(GameDataModel):
    """clz_Torappu_SandboxPermBasicData"""

    topic_id: str | None = None
    topic_template: str = "NONE"
    topic_name: str | None = None
    topic_start_time: int = 0
    full_stored_time: int = 0
    sort_id: int = 0
    price_item_id: str | None = None
    template_shop_id: str | None = None
    home_entry_display_data: list[SandboxPermBasicDataHomeEntryDisplayData] | None = None
    web_bus_type: str | None = None
    medal_group_id: str | None = None
    show_medal_id: str | None = None
    description: str | None = None
    enroll_points: dict[str, SandboxPermEnrollPointData] | None = None


class SandboxV2NodeData(GameDataModel):
    """clz_Torappu_SandboxV2NodeData"""

    min_distance: float = 0.0


class UnityEngineVector2(GameDataModel):
    """clz_UnityEngine_Vector2"""

    x: float = 0.0
    y: float = 0.0


class SandboxV2MapZoneData(GameDataModel):
    """clz_Torappu_SandboxV2MapZoneData"""

    zone_id: str | None = None
    center: UnityEngineVector2 | None = None
    vertices: list[UnityEngineVector2] | None = None
    triangles: list[list[int]] | None = None
    has_border: bool = False


class SandboxV2MapConfig(GameDataModel):
    """clz_Torappu_SandboxV2MapConfig"""

    is_rift: bool = False
    is_guide: bool = False
    camera_bound_min: UnityEngineVector2 | None = None
    camera_bound_max: UnityEngineVector2 | None = None
    camera_max_normalized_zoom: float = 0.0
    background_id: str | None = None


class SandboxV2MapData(GameDataModel):
    """clz_Torappu_SandboxV2MapData"""

    nodes: dict[str, SandboxV2NodeData] | None = None
    zones: dict[str, SandboxV2MapZoneData] | None = None
    map_config: SandboxV2MapConfig | None = None
    center_node_id: str | None = None
    month_mode_node_id: str | None = None


class SandboxV2ItemTrapData(GameDataModel):
    """clz_Torappu_SandboxV2ItemTrapData"""

    item_id: str | None = None
    trap_id: str | None = None
    trap_phase: int = 0
    trap_level: int = 0
    skill_index: int = 0
    skill_level: int = 0
    building_level: int = 0
    updated_item_id: str | None = None
    min_level_item_id: str | None = None
    base_item_name: str | None = None
    item_type: str = "NONE"
    item_tag: str = "OUTPUT"
    buff_id: str | None = None


class SandboxV2ItemTrapTagData(GameDataModel):
    """clz_Torappu_SandboxV2ItemTrapTagData"""

    tag: str = "OUTPUT"
    tag_name: str | None = None
    tag_pic: str | None = None
    sort_id: int = 0


class SandboxBuildingItemData(GameDataModel):
    """clz_Torappu_SandboxBuildingItemData"""

    item_id: str | None = None
    item_rarity: int = 0


class SandboxV2CraftItemData(GameDataModel):
    """clz_Torappu_SandboxV2CraftItemData"""

    item_id: str | None = None
    type: str = "BASE_BUILDING"
    building_unlock_desc: str | None = None
    material_items: dict[str, int] | None = None
    upgrade_items: dict[str, int] | None = None
    output_ratio: int = 0
    withdraw_ratio: int = 0
    repair_cost: int = 0
    is_hidden: bool = False
    craft_group_id: str | None = None
    recipe_level: int = 0


class SandboxV2LivestockData(GameDataModel):
    """clz_Torappu_SandboxV2LivestockData"""

    livestock_item_id: str | None = None
    shiny_livestock_item_id: str | None = None
    livestock_enemy_id: str | None = None
    target_fence_id: str | None = None


class SandboxV2CraftGroupData(GameDataModel):
    """clz_Torappu_SandboxV2CraftGroupData"""

    items: list[str] | None = None


class SandboxV2AlchemyMaterialData(GameDataModel):
    """clz_Torappu_SandboxV2AlchemyMaterialData"""

    item_id: str | None = None
    count: int = 0


class SandboxV2AlchemyRecipeData(GameDataModel):
    """clz_Torappu_SandboxV2AlchemyRecipeData"""

    recipe_id: str | None = None
    materials: list[SandboxV2AlchemyMaterialData] | None = None
    item_id: str | None = None
    once_alchemy_ratio: int = 0
    recipe_level: int = 0
    unlock_desc: str | None = None


class SandboxV2DrinkMatData(GameDataModel):
    """clz_Torappu_SandboxV2DrinkMatData"""

    id: str | None = None
    type: str = "NONE"
    count: int = 0


class SandboxFoodMatData(GameDataModel):
    """clz_Torappu_SandboxFoodMatData"""

    id: str | None = None
    type: str = "MAIN"
    attribute: str = "NONE"
    variant_type: str = "NONE"
    bonus_duration: int = 0
    buff_desc: str | None = None
    sort_id: int = 0


class SandboxFoodRecipeData(GameDataModel):
    """clz_Torappu_SandboxFoodRecipeData"""

    food_id: str | None = None
    mats: list[str] | None = None


class SandboxFoodVariantData(GameDataModel):
    """clz_Torappu_SandboxFoodVariantData"""

    type: str = "NONE"
    name: str | None = None
    usage: str | None = None


class SandboxFoodData(GameDataModel):
    """clz_Torappu_SandboxFoodData"""

    id: str | None = None
    attributes: list[str] | None = None
    recipes: list[SandboxFoodRecipeData] | None = None
    variants: list[SandboxFoodVariantData] | None = None
    duration: int = 0
    sort_id: int = 0


class SandboxV2NodeTypeData(GameDataModel):
    """clz_Torappu_SandboxV2NodeTypeData"""

    node_type: str = "NONE"
    name: str | None = None
    icon_id: str | None = None


class SandboxV2NodeUpgradeData(GameDataModel):
    """clz_Torappu_SandboxV2NodeUpgradeData"""

    node_upgrade_id: str | None = None
    name: str | None = None
    description: str | None = None
    upgrade_desc: str | None = None
    upgrade_tips: str | None = None
    item_type: str = "NONE"
    item_tag: str = "OUTPUT"
    item_cnt: int = 0
    item_rarity: int = 0


class SandboxV2WeatherData(GameDataModel):
    """clz_Torappu_SandboxV2WeatherData"""

    weather_id: str | None = None
    name: str | None = None
    weather_level: int = 0
    weather_type: str = "NORMAL"
    weather_type_name: str | None = None
    weather_icon_id: str | None = None
    function_desc: str | None = None
    description: str | None = None
    buff_id: str | None = None


class SandboxV2StageData(GameDataModel):
    """clz_Torappu_SandboxV2StageData"""

    stage_id: str | None = None
    level_id: str | None = None
    code: str | None = None
    name: str | None = None
    description: str | None = None
    action_cost: int = 0
    action_cost_enemy_rush: int = 0


class SandboxV2ZoneData(GameDataModel):
    """clz_Torappu_SandboxV2ZoneData"""

    zone_id: str | None = None
    zone_name: str | None = None
    display_name: bool = False
    appellation: str | None = None


class SandboxV2NodeBuffData(GameDataModel):
    """clz_Torappu_SandboxV2NodeBuffData"""

    rune_id: str | None = None
    name: str | None = None
    description: str | None = None
    extra: str | None = None
    icon_id: str | None = None


class SandboxV2RewardItemConfigData(GameDataModel):
    """clz_Torappu_SandboxV2RewardItemConfigData"""

    reward_item: str | None = None
    reward_type: str = "NONE"


class SandboxV2RewardData(GameDataModel):
    """clz_Torappu_SandboxV2RewardData"""

    reward_list: list[SandboxV2RewardItemConfigData] | None = None


class SandboxV2RewardCommonConfig(GameDataModel):
    """clz_Torappu_SandboxV2RewardCommonConfig"""

    reward_item_id: str | None = None
    reward_item_type: str = "NONE"
    count: int = 0


class SandboxV2RewardConfigGroupData(GameDataModel):
    """clz_Torappu_SandboxV2RewardConfigGroupData"""

    stage_map_preview_reward_dict: dict[str, SandboxV2RewardData] | None = None
    stage_detail_preview_reward_dict: dict[str, SandboxV2RewardData] | None = None
    trap_reward_dict: dict[str, SandboxV2RewardCommonConfig] | None = None
    enemy_reward_dict: dict[str, SandboxV2RewardCommonConfig] | None = None
    unit_preview_reward_dict: dict[str, SandboxV2RewardData] | None = None
    stage_reward_dict: dict[str, SandboxV2RewardData] | None = None
    rush_preview_reward_dict: dict[str, SandboxV2RewardData] | None = None


class SandboxV2FloatIconData(GameDataModel):
    """clz_Torappu_SandboxV2FloatIconData"""

    pic_id: str | None = None
    pic_name: str | None = None


class SandboxV2EnemyRushTypeData(GameDataModel):
    """clz_Torappu_SandboxV2EnemyRushTypeData"""

    type: str = "NORMAL"
    description: str | None = None
    sort_id: int = 0


class SandboxV2BattleRushEnemyConfig(GameDataModel):
    """clz_Torappu_SandboxV2BattleRushEnemyConfig"""

    enemy_key: str | None = None
    branch_id: str | None = None
    count: int = 0
    interval: float = 0.0
    pre_delay: float = 0.0


class SandboxV2BattleRushEnemyGroupConfig(GameDataModel):
    """clz_Torappu_SandboxV2BattleRushEnemyGroupConfig"""

    enemy_group_key: str | None = None
    enemy: list[SandboxV2BattleRushEnemyConfig] | None = None
    dynamic_enemy: list[str] | None = None


class SandboxV2BattleRushEnemyDataRushEnemyDBRef(GameDataModel):
    """clz_Torappu_SandboxV2BattleRushEnemyData_RushEnemyDBRef"""

    id: str | None = None
    level: int = 0


class SandboxV2BattleRushEnemyData(GameDataModel):
    """clz_Torappu_SandboxV2BattleRushEnemyData"""

    rush_enemy_group_configs: dict[str, list[SandboxV2BattleRushEnemyGroupConfig]] | None = None
    rush_enemy_db_ref: list[SandboxV2BattleRushEnemyDataRushEnemyDBRef] | None = None


class SandboxV2GameConst(GameDataModel):
    """clz_Torappu_SandboxV2GameConst"""

    main_map_id: str | None = None
    base_trap_id: str | None = None
    portable_trap_id: str | None = None
    door_trap_id: str | None = None
    mine_trap_id: str | None = None
    neutral_boss_enemy_id: list[str] | None = None
    nest_trap_id: str | None = None
    shop_npc_name: str | None = None
    days_between_assessment: int = 0
    portable_construct_unlock_level: int = 0
    outpost_construct_unlock_level: int = 0
    max_enemy_count_same_time_in_rush: int = 0
    max_pre_delay_time_in_rush: float = 0.0
    max_save_cnt: int = 0
    first_season_duration: int = 0
    season_transition_loop: list[str] | None = None
    season_duration_loop: list[int] | None = None
    first_season_start_angle: float = 0.0
    season_transition_angle_loop: list[float] | None = None
    season_angle: float = 0.0
    battle_item_desc: str | None = None
    food_desc: str | None = None
    multiple_survival_day_desc: str | None = None
    multiple_tips: str | None = None
    tech_progress_score: int = 0
    other_enemy_rush_name: str | None = None
    survive_day_text: str | None = None
    survive_period_text: str | None = None
    survive_score_text: str | None = None
    action_point_score_text: str | None = None
    node_explore_desc: str | None = None
    dungeon_explore_desc: str | None = None
    node_complete_desc: str | None = None
    no_rift_dungeon_desc: str | None = None
    base_rushed_desc: str | None = None
    rift_base_desc: str | None = None
    rift_base_rushed_desc: str | None = None
    dungeon_triggered_guide_quest_list: list[str] | None = None
    no_log_in_enemy_stats_enemy_id: list[str] | None = None


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class SandboxV2DiffModeData(GameDataModel):
    """clz_Torappu_SandboxV2DiffModeData"""

    title: str | None = None
    desc: str | None = None
    buff_list: list[str] | None = None
    detail_list: str | None = None
    sort_id: int = 0


class SandboxV2BasicConst(GameDataModel):
    """clz_Torappu_SandboxV2BasicConst"""

    stamina_item_id: str | None = None
    gold_item_id: str | None = None
    dimensioncoin_item_id: str | None = None
    always_show_item_ids_construct: list[str] | None = None
    always_show_item_ids: list[str] | None = None
    bag_bottom_bar_res_type: list[str] | None = None
    failed_cook_food: str | None = None
    max_food_duration: int = 0
    drink_cost_once: int = 0
    drink_make_limit: int = 0
    special_mat_water: str | None = None
    workbench_make_limit: int = 0
    logistics_pos_limit: int = 0
    logistics_unlock_level: int = 0
    logistics_drink_cost: int = 0
    logistics_evacuate_tips: str | None = None
    logistics_evacuate_warning: str | None = None
    base_repair_cost: int = 0
    port_repair_cost: int = 0
    unit_fence_limit: int = 0
    unit_rare_fence_limit: int = 0
    cage_id: str | None = None
    fence_id: str | None = None
    rare_fence_id: str | None = None
    monthly_rush_entry_text_1: str | None = None
    monthly_entry_unlock_text: str | None = None
    monthly_entry_rift_text: str | None = None
    monthly_rush_intro: str | None = None
    monthly_coin: ItemBundle | None = None
    char_rarity_color_list: list[str] | None = None
    squad_char_capacity: int = 0
    total_squad_cnt: int = 0
    toolbox_capacity: int = 0
    tool_cnt_limit_in_squad: int = 0
    mini_squad_char_capacity: int = 0
    mini_squad_drink_cost: int = 0
    normal_squad_drink_cost: int = 0
    empty_squad_drink_cost: int = 0
    achieve_type_all: str | None = None
    construct_mode_bgm_home: str | None = None
    battle_bgm_collect: str | None = None
    battle_bgm_hunt: str | None = None
    battle_bgm_enemy_rush: str | None = None
    battle_bgm_boss_rush: str | None = None
    img_loading_normal_name: str | None = None
    img_loading_base_name: str | None = None
    img_unloading_base_name: str | None = None
    is_challenge_open: bool = False
    is_racing_open: bool = False
    has_explore_mode: bool = False
    explore_mode_buff_descs: list[str] | None = None
    mode_select_tips: str | None = None
    string_res: dict[str, str] | None = None
    diff_list: list[SandboxV2DiffModeData] | None = None
    battle_preload_enemies: list[str] | None = None
    battle_excluded_traps_in_rush: list[str] | None = None


class SandboxV2RiftConst(GameDataModel):
    """clz_Torappu_SandboxV2RiftConst"""

    refresh_rate: int = 0
    random_dungeon_id: str | None = None
    hunt_dungeon_id: str | None = None
    sub_target_reward_id: str | None = None
    prey_quest_reward_id: str | None = None
    dungeon_season_id: str = "NONE"
    fixed_dungeon_type_name: str | None = None
    random_dungeon_type_name: str | None = None
    prey_dungeon_type_name: str | None = None
    no_team_description: str | None = None
    no_team_name: str | None = None
    no_team_background_id: str | None = None
    no_team_small_icon_id: str | None = None
    no_team_big_icon_id: str | None = None
    messenger_enemy_id: str | None = None
    rift_rush_enemy_group_limit: int = 0
    rift_rush_spawn_cd: int = 0


class SandboxV2DevelopmentConst(GameDataModel):
    """clz_Torappu_SandboxV2DevelopmentConst"""

    tech_points_total: int = 0


class TipData(GameDataModel):
    """clz_Torappu_TipData"""

    tip: str | None = None
    weight: float = 0.0
    category: str = "NONE"


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


class LegacyInLevelRuneData(GameDataModel):
    """clz_Torappu_LegacyInLevelRuneData"""

    difficulty_mask: str = "NONE"
    key: str | None = None
    profession_mask: str = "NONE"
    buildable_mask: str = "NONE"
    blackboard: list[BlackboardDataPair] | None = None


class SandboxV2QuestData(GameDataModel):
    """clz_Torappu_SandboxV2QuestData"""

    quest_id: str | None = None
    quest_line: str | None = None
    quest_title: str | None = None
    quest_desc: str | None = None
    quest_target_desc: str | None = None
    is_display: bool = False
    quest_route_type: str = "NONE"
    quest_line_type: str = "NONE"
    quest_route_param: str | None = None
    show_progress_index: int = 0


class SandboxV2NpcData(GameDataModel):
    """clz_Torappu_SandboxV2NpcData"""

    npc_id: str | None = None
    trap_id: str | None = None
    npc_type: str = "NORMAL"
    dialog_ids: dict[str, str] | None = None
    npc_location: list[int] | None = None
    npc_orientation: str = "UP"
    pic_id: str | None = None
    pic_name: str | None = None
    show_pic: bool = False
    react_skill_index: int = 0


class SandboxV2DialogData(GameDataModel):
    """clz_Torappu_SandboxV2DialogData"""

    dialog_id: str | None = None
    avg_id: str | None = None


class SandboxV2QuestLineData(GameDataModel):
    """clz_Torappu_SandboxV2QuestLineData"""

    quest_line_id: str | None = None
    quest_line_title: str | None = None
    quest_line_type: str = "NONE"
    quest_line_badge_type: str = "NONE"
    quest_line_scope_type: str = "MAIN"
    quest_line_desc: str | None = None
    sort_id: int = 0


class SandboxV2GuideQuestData(GameDataModel):
    """clz_Torappu_SandboxV2GuideQuestData"""

    quest_id: str | None = None
    story_id: str | None = None
    trigger_key: str | None = None


class SandboxDevelopmentData(GameDataModel):
    """clz_Torappu_SandboxDevelopmentData"""

    tech_id: str | None = None
    tech_type: str = "NONE"
    position_x: int = 0
    position_y: int = 0
    front_node_id: str | None = None
    next_node_ids: list[str] | None = None
    limit_base_level: int = 0
    token_cost: int = 0
    tech_name: str | None = None
    tech_icon_id: str | None = None
    node_title: str | None = None
    raw_desc: str | None = None
    can_buff_reserch: bool = False


class SandboxV2EventData(GameDataModel):
    """clz_Torappu_SandboxV2EventData"""

    event_id: str | None = None
    type: str = "NONE"
    icon_id: str | None = None
    icon_name: str | None = None
    enter_scene_id: str | None = None


class SandboxV2EventSceneData(GameDataModel):
    """clz_Torappu_SandboxV2EventSceneData"""

    event_scene_id: str | None = None
    title: str | None = None
    desc: str | None = None
    choice_ids: list[str] | None = None


class SandboxV2EventChoiceData(GameDataModel):
    """clz_Torappu_SandboxV2EventChoiceData"""

    choice_id: str | None = None
    type: str = "NONE"
    cost_action: int = 0
    title: str | None = None
    desc: str | None = None
    expedition_id: str | None = None


class SandboxV2ExpeditionData(GameDataModel):
    """clz_Torappu_SandboxV2ExpeditionData"""

    expedition_id: str | None = None
    desc: str | None = None
    effect_desc: str | None = None
    cost_action: int = 0
    cost_drink: int = 0
    char_cnt: int = 0
    profession: str = "NONE"
    professions: list[str] | None = None
    min_elite_rank: int = 0
    duration: int = 0


class SandboxV2EventEffectData(GameDataModel):
    """clz_Torappu_SandboxV2EventEffectData"""

    event_effect_id: str | None = None
    buff_id: str | None = None
    duration: int = 0
    desc: str | None = None


class SandboxShopGoodData(GameDataModel):
    """clz_Torappu_SandboxShopGoodData"""

    good_id: str | None = None
    item_id: str | None = None
    count: int = 0
    coin_type: str = "DIMENSION_COIN"
    value: int = 0
    item_pool_id: str | None = None
    stock: int = 0
    weight: int = 0


class SandboxV2ShopDialogData(GameDataModel):
    """clz_Torappu_SandboxV2ShopDialogData"""

    season_dialogs: dict[str, list[str]] | None = None
    after_buy_dialogs: list[str] | None = None
    shop_empty_dialogs: list[str] | None = None


class SandboxV2LogisticsData(GameDataModel):
    """clz_Torappu_SandboxV2LogisticsData"""

    id: str | None = None
    desc: str | None = None
    no_buff_desc: str | None = None
    icon_id: str | None = None
    profession: str = "NONE"
    sort_id: int = 0
    level_params: list[str] | None = None


class SandboxV2LogisticsCharData(GameDataModel):
    """clz_Torappu_SandboxV2LogisticsCharData"""

    level_upper_limit: int = 0
    char_upper_limit: int = 0


class SandboxV2MonthRushData(GameDataModel):
    """clz_Torappu_SandboxV2MonthRushData"""

    monthly_rush_id: str | None = None
    start_time: int = 0
    end_time: int = 0
    is_last: bool = False
    sort_id: int = 0
    rush_group_key: str | None = None
    monthly_rush_name: str | None = None
    monthly_rush_des: str | None = None
    weather_id: str | None = None
    node_id: str | None = None
    condition_group: str | None = None
    condition_desc: str | None = None
    reward_item_list: list[ItemBundle] | None = None


class SandboxV2RiftParamData(GameDataModel):
    """clz_Torappu_SandboxV2RiftParamData"""

    id: str | None = None
    desc: str | None = None
    icon_id: str | None = None
    bk_color: str | None = None


class SandboxV2RiftSubTargetData(GameDataModel):
    """clz_Torappu_SandboxV2RiftSubTargetData"""

    id: str | None = None
    name: str | None = None
    desc: str | None = None


class SandboxV2RiftMainTargetData(GameDataModel):
    """clz_Torappu_SandboxV2RiftMainTargetData"""

    id: str | None = None
    title: str | None = None
    desc: str | None = None
    story_desc: str | None = None
    target_day_count: int = 0
    target_type: str = "NONE"
    quest_icon_id: str | None = None
    quest_icon_name: str | None = None


class SandboxV2RiftGlobalEffectData(GameDataModel):
    """clz_Torappu_SandboxV2RiftGlobalEffectData"""

    id: str | None = None
    desc: str | None = None


class SandboxV2FixedRiftData(GameDataModel):
    """clz_Torappu_SandboxV2FixedRiftData"""

    rift_id: str | None = None
    rift_name: str | None = None
    reward_group_id: str | None = None


class SandboxV2RiftTeamBuffData(GameDataModel):
    """clz_Torappu_SandboxV2RiftTeamBuffData"""

    team_id: str | None = None
    team_name: str | None = None
    buff_level: int = 0
    buff_desc: str | None = None
    team_small_icon_id: str | None = None
    team_big_icon_id: str | None = None
    team_desc: str | None = None
    team_bg_id: str | None = None


class SandboxV2RiftDifficultyData(GameDataModel):
    """clz_Torappu_SandboxV2RiftDifficultyData"""

    id: str | None = None
    rift_id: str | None = None
    desc: str | None = None
    difficulty_level: int = 0
    reward_group_id: str | None = None


class SandboxArchiveQuestAvgData(GameDataModel):
    """clz_Torappu_SandboxArchiveQuestAvgData"""

    avg_id: str | None = None
    avg_name: str | None = None


class SandboxArchiveQuestCgData(GameDataModel):
    """clz_Torappu_SandboxArchiveQuestCgData"""

    cg_id: str | None = None
    cg_title: str | None = None
    cg_desc: str | None = None
    cg_path: str | None = None


class SandboxArchiveQuestZoneData(GameDataModel):
    """clz_Torappu_SandboxArchiveQuestZoneData"""

    zone_id: str | None = None
    zone_name: str | None = None
    zone_bg_pic_id: str | None = None
    zone_name_id_en: str | None = None


class SandboxArchiveQuestData(GameDataModel):
    """clz_Torappu_SandboxArchiveQuestData"""

    id: str | None = None
    sort_id: int = 0
    quest_type: str = "NONE"
    name: str | None = None
    desc: str | None = None
    avg_data_list: list[SandboxArchiveQuestAvgData] | None = None
    cg_data_list: list[SandboxArchiveQuestCgData] | None = None
    npc_pic_id_list: list[str] | None = None
    zone_data: SandboxArchiveQuestZoneData | None = None


class SandboxArchiveAchievementData(GameDataModel):
    """clz_Torappu_SandboxArchiveAchievementData"""

    id: str | None = None
    achievement_type: list[str] | None = None
    rarity_sort_id: int = 0
    sort_id: int = 0
    name: str | None = None
    desc: str | None = None


class SandboxArchiveAchievementTypeData(GameDataModel):
    """clz_Torappu_SandboxArchiveAchievementTypeData"""

    achievement_type: str | None = None
    name: str | None = None
    sort_id: int = 0


class SandboxArchiveQuestTypeData(GameDataModel):
    """clz_Torappu_SandboxArchiveQuestTypeData"""

    type: str = "NONE"
    name: str | None = None
    icon_id: str | None = None


class SandboxArchiveMusicUnlockData(GameDataModel):
    """clz_Torappu_SandboxArchiveMusicUnlockData"""

    music_id: str | None = None
    unlock_cond_desc: str | None = None


class SandboxV2BaseUpdateCondition(GameDataModel):
    """clz_Torappu_SandboxV2BaseUpdateCondition"""

    desc: str | None = None
    limit_cond: str | None = None
    param: list[str] | None = None


class SandboxV2BaseUpdateFunctionPreviewDetailData(GameDataModel):
    """clz_Torappu_SandboxV2BaseUpdateFunctionPreviewDetailData"""

    func_id: str | None = None
    unlock_type: str = "NONE"
    type_title: str | None = None
    desc: str | None = None
    icon: str | None = None
    dark_mode: bool = False
    sort_id: int = 0
    display_type: str = "NONE"


class SandboxV2BaseFunctionPreviewData(GameDataModel):
    """clz_Torappu_SandboxV2BaseFunctionPreviewData"""

    preview_id: str | None = None
    preview_value: int = 0
    detail_data: SandboxV2BaseUpdateFunctionPreviewDetailData | None = None


class SandboxV2BaseUpdateData(GameDataModel):
    """clz_Torappu_SandboxV2BaseUpdateData"""

    base_level_id: str | None = None
    base_level: int = 0
    conditions: list[SandboxV2BaseUpdateCondition] | None = None
    items: dict[str, int] | None = None
    preview_datas: list[SandboxV2BaseFunctionPreviewData] | None = None
    score_factor: str | None = None
    portable_repair_cost: int = 0
    entry_count: int = 0
    repair_cost: int = 0


class SandboxDevelopmentLineSegmentData(GameDataModel):
    """clz_Torappu_SandboxDevelopmentLineSegmentData"""

    from_node_id: str | None = None
    passing_node_ids: list[str] | None = None
    from_axis_pos_x: int = 0
    from_axis_pos_y: int = 0
    to_axis_pos_x: int = 0
    to_axis_pos_y: int = 0
    line_style: str = "EMPTY"
    unlock_basement_level: int = 0


class SandboxV2BuildingNodeScoreData(GameDataModel):
    """clz_Torappu_SandboxV2BuildingNodeScoreData"""

    node_id: str | None = None
    sort_id: int = 0
    limit_score: int = 0


class SandboxV2SeasonData(GameDataModel):
    """clz_Torappu_SandboxV2SeasonData"""

    season_type: str = "NONE"
    name: str | None = None
    function_desc: str | None = None
    description: str | None = None
    color: str | None = None


class SandboxV2ConfirmIconData(GameDataModel):
    """clz_Torappu_SandboxV2ConfirmIconData"""

    icon_type: str = "COMMON"
    icon_pic_id: str | None = None


class SandboxV2TutorialRepoCharData(GameDataModel):
    """clz_Torappu_SandboxV2TutorialRepoCharData"""

    inst_id: int = 0
    char_id: str | None = None
    evolve_phase: str = "PHASE_0"
    level: int = 0
    favor_point: int = 0
    potential_rank: int = 0
    main_skill_lv: int = 0
    spec_skill_list: list[int] | None = None


class SandboxV2TutorialBasicConst(GameDataModel):
    """clz_Torappu_SandboxV2TutorialBasicConst"""

    training_quest_list: list[str] | None = None


class SandboxV2TutorialData(GameDataModel):
    """clz_Torappu_SandboxV2TutorialData"""

    char_repo_data: dict[int, SandboxV2TutorialRepoCharData] | None = None
    quest_data: dict[str, SandboxV2QuestData] | None = None
    guide_quest_data: dict[str, SandboxV2GuideQuestData] | None = None
    quest_line_data: dict[str, SandboxV2QuestLineData] | None = None
    basic_const: SandboxV2TutorialBasicConst | None = None


class SandboxV2RacerBasicInfo(GameDataModel):
    """clz_Torappu_SandboxV2RacerBasicInfo"""

    racer_id: str | None = None
    sort_id: int = 0
    racer_name: str | None = None
    item_id: str | None = None
    attribute_max_value: list[int] | None = None


class SandboxV2RacerTalentInfo(GameDataModel):
    """clz_Torappu_SandboxV2RacerTalentInfo"""

    talent_id: str | None = None
    talent_type: str = "BORN"
    talent_icon_id: str | None = None
    desc: str | None = None


class SandboxV2RacerNameInfo(GameDataModel):
    """clz_Torappu_SandboxV2RacerNameInfo"""

    name_id: str | None = None
    name_type: str = "PREFIX"
    name_desc: str | None = None


class SandboxV2RacerMedalInfo(GameDataModel):
    """clz_Torappu_SandboxV2RacerMedalInfo"""

    medal_id: str | None = None
    sort_id: int = 0
    name: str | None = None
    desc: str | None = None
    icon_id: str | None = None
    small_icon_id: str | None = None


class SandboxV2RacingItemInfo(GameDataModel):
    """clz_Torappu_SandboxV2RacingItemInfo"""

    racer_item_id: str | None = None
    name: str | None = None
    icon_id: str | None = None
    blackboard: list[BlackboardDataPair] | None = None


class SandboxV2RacingConstData(GameDataModel):
    """clz_Torappu_SandboxV2RacingConstData"""

    attribute_name_list: list[str] | None = None
    racer_max_value: list[int] | None = None
    bag_full_hint_percent: float = 0.0
    temp_bag_full_hint_percent: float = 0.0
    bag_name: str | None = None
    temp_bag_name: str | None = None
    bag_empty_left_desc: str | None = None
    bag_empty_right_desc: str | None = None
    temp_bag_empty_left_desc: str | None = None
    temp_bag_empty_right_desc: str | None = None
    born_talent_icon_id: str | None = None
    born_talent_title: str | None = None
    learned_talent_icon_id: str | None = None
    learned_talent_title: str | None = None
    talent_empty_desc: str | None = None
    slug_item_id: str | None = None
    racing_hp_factor: float = 0.0
    racing_speed_factor: float = 0.0
    racing_acceleration_factor: float = 0.0
    recover_move_speed: float = 0.0
    recover_hp_factor: float = 0.0
    bleeding_factor: float = 0.0
    max_steering_factor: float = 0.0
    steering_mass_level_factor: float = 0.0
    steering_move_speed_factor: float = 0.0
    safe_angle_cos: float = 0.0
    safe_collision_force_level: float = 0.0
    tile_collision_factor: float = 0.0
    collision_force_sector: list[float] | None = None
    collision_force_level: list[float] | None = None
    collision_speed_loss: list[float] | None = None
    collision_hp_loss: list[float] | None = None
    tile_collision_speed_loss: list[float] | None = None
    tile_collision_hp_loss: list[float] | None = None
    auto_use_item_time_range: list[float] | None = None
    recover_acceleration: float = 0.0


class SandboxV2RacingData(GameDataModel):
    """clz_Torappu_SandboxV2RacingData"""

    racer_basic_info: dict[str, SandboxV2RacerBasicInfo] | None = None
    racer_talent_info: dict[str, SandboxV2RacerTalentInfo] | None = None
    racer_name_info: dict[str, SandboxV2RacerNameInfo] | None = None
    racer_medal_info: dict[str, SandboxV2RacerMedalInfo] | None = None
    enemy_item_map: dict[str, str] | None = None
    racing_item_info: dict[str, SandboxV2RacingItemInfo] | None = None
    const_data: SandboxV2RacingConstData | None = None


class SandboxV2ChallengeConst(GameDataModel):
    """clz_Torappu_SandboxV2ChallengeConst"""

    challenge_mode_desc: str | None = None
    daily_title_desc: str | None = None
    debuff_countdown_desc: str | None = None
    gain_all_debuff_desc: str | None = None
    daily_up_attribute_desc: str | None = None


class SandboxV2ChallengeModeUnlockData(GameDataModel):
    """clz_Torappu_SandboxV2ChallengeModeUnlockData"""

    unlock_id: str | None = None
    sort_id: int = 0
    condition_desc: str | None = None


class SandboxV2ChallengeModeRewardData(GameDataModel):
    """clz_Torappu_SandboxV2ChallengeModeRewardData"""

    reward_id: str | None = None
    sort_id: int = 0
    reward_day: int = 0
    reward_item_list: list[ItemBundle] | None = None


class SandboxV2ChallengeModeDifficultyData(GameDataModel):
    """clz_Torappu_SandboxV2ChallengeModeDifficultyData"""

    challenge_day: int = 0
    diff_desc: str | None = None


class SandboxV2ChallengeModeData(GameDataModel):
    """clz_Torappu_SandboxV2ChallengeModeData"""

    challenge_const: SandboxV2ChallengeConst | None = None
    challenge_mode_unlock_data: dict[str, SandboxV2ChallengeModeUnlockData] | None = None
    challenge_mode_reward_data: dict[str, SandboxV2ChallengeModeRewardData] | None = None
    challenge_mode_difficulty_data: list[SandboxV2ChallengeModeDifficultyData] | None = None


class SandboxV2Data(GameDataModel):
    """clz_Torappu_SandboxV2Data"""

    map_data: dict[str, SandboxV2MapData] | None = None
    item_trap_data: dict[str, SandboxV2ItemTrapData] | None = None
    item_trap_tag_data: dict[str, SandboxV2ItemTrapTagData] | None = None
    building_item_data: dict[str, SandboxBuildingItemData] | None = None
    craft_item_data: dict[str, SandboxV2CraftItemData] | None = None
    livestock_produce_data: dict[str, SandboxV2LivestockData] | None = None
    craft_group_data: dict[str, SandboxV2CraftGroupData] | None = None
    alchemy_recipe_data: dict[str, SandboxV2AlchemyRecipeData] | None = None
    drink_mat_data: dict[str, SandboxV2DrinkMatData] | None = None
    food_mat_data: dict[str, SandboxFoodMatData] | None = None
    food_data: dict[str, SandboxFoodData] | None = None
    node_type_data: dict[str, SandboxV2NodeTypeData] | None = None
    node_upgrade_data: dict[str, SandboxV2NodeUpgradeData] | None = None
    weather_data: dict[str, SandboxV2WeatherData] | None = None
    stage_data: dict[str, SandboxV2StageData] | None = None
    zone_data: dict[str, SandboxV2ZoneData] | None = None
    node_buff_data: dict[str, SandboxV2NodeBuffData] | None = None
    reward_config_data: SandboxV2RewardConfigGroupData | None = None
    float_icon_data: dict[str, SandboxV2FloatIconData] | None = None
    enemy_rush_type_data: dict[str, SandboxV2EnemyRushTypeData] | None = None
    rush_enemy_data: SandboxV2BattleRushEnemyData | None = None
    game_const: SandboxV2GameConst | None = None
    basic_const: SandboxV2BasicConst | None = None
    rift_const: SandboxV2RiftConst | None = None
    development_const: SandboxV2DevelopmentConst | None = None
    battle_loading_tips: list[TipData] | None = None
    rune_datas: dict[str, RuneTablePackedRuneData] | None = None
    item_rune_list: dict[str, list[LegacyInLevelRuneData]] | None = None
    quest_data: dict[str, SandboxV2QuestData] | None = None
    npc_data: dict[str, SandboxV2NpcData] | None = None
    dialog_data: dict[str, SandboxV2DialogData] | None = None
    quest_line_data: dict[str, SandboxV2QuestLineData] | None = None
    quest_line_story_data: dict[str, str] | None = None
    guide_quest_data: dict[str, SandboxV2GuideQuestData] | None = None
    development_data: dict[str, SandboxDevelopmentData] | None = None
    event_data: dict[str, SandboxV2EventData] | None = None
    event_scene_data: dict[str, SandboxV2EventSceneData] | None = None
    event_choice_data: dict[str, SandboxV2EventChoiceData] | None = None
    expedition_data: dict[str, SandboxV2ExpeditionData] | None = None
    event_effect_data: dict[str, SandboxV2EventEffectData] | None = None
    shop_good_data: dict[str, SandboxShopGoodData] | None = None
    shop_dialog_data: SandboxV2ShopDialogData | None = None
    logistics_data: list[SandboxV2LogisticsData] | None = None
    logistics_char_mapping: dict[int, dict[int, list[SandboxV2LogisticsCharData]]] | None = None
    material_keyword_data: dict[str, str] | None = None
    month_rush_data: list[SandboxV2MonthRushData] | None = None
    rift_terrain_param_data: dict[str, SandboxV2RiftParamData] | None = None
    rift_climate_param_data: dict[str, SandboxV2RiftParamData] | None = None
    rift_enemy_param_data: dict[str, SandboxV2RiftParamData] | None = None
    rift_sub_target_data: dict[str, SandboxV2RiftSubTargetData] | None = None
    rift_main_target_data: dict[str, SandboxV2RiftMainTargetData] | None = None
    rift_global_effect_data: dict[str, SandboxV2RiftGlobalEffectData] | None = None
    fixed_rift_data: dict[str, SandboxV2FixedRiftData] | None = None
    rift_team_buff_data: dict[str, list[SandboxV2RiftTeamBuffData]] | None = None
    rift_difficulty_data: dict[str, SandboxV2RiftDifficultyData] | None = None
    rift_reward_display_data: dict[str, list[str]] | None = None
    enemy_replace_data: dict[str, dict[str, str]] | None = None
    archive_quest_data: dict[str, SandboxArchiveQuestData] | None = None
    achievement_data: dict[str, SandboxArchiveAchievementData] | None = None
    achievement_type_data: dict[str, SandboxArchiveAchievementTypeData] | None = None
    archive_quest_type_data: dict[str, SandboxArchiveQuestTypeData] | None = None
    archive_music_unlock_data: dict[str, SandboxArchiveMusicUnlockData] | None = None
    base_update: list[SandboxV2BaseUpdateData] | None = None
    development_line_segment_datas: list[SandboxDevelopmentLineSegmentData] | None = None
    building_node_score_data: dict[str, SandboxV2BuildingNodeScoreData] | None = None
    season_data: dict[str, SandboxV2SeasonData] | None = None
    confirm_icon_data: list[SandboxV2ConfirmIconData] | None = None
    shop_update_time_data: list[int] | None = None
    tutorial_data: SandboxV2TutorialData | None = None
    racing_data: SandboxV2RacingData | None = None
    challenge_mode_data: SandboxV2ChallengeModeData | None = None


class SandboxV3ModeData(GameDataModel):
    """clz_Torappu_SandboxV3ModeData"""

    mode_id: str | None = None
    mode_name: str | None = None
    sort_id: int = 0
    mode_description: str | None = None
    mode_description_detail: str | None = None
    difficulty_factor: float = 0.0
    rune_id_list: list[str] | None = None


class SandboxV3MapGridPos(GameDataModel):
    """clz_Torappu_SandboxV3MapGridPos"""

    x: int = 0
    y: int = 0


class SandboxV3MapTileData(GameDataModel):
    """clz_Torappu_SandboxV3MapTileData"""

    tile_id: str | None = None
    tile_type: str = "NONE"
    grid_pos: SandboxV3MapGridPos | None = None
    tile_res_id: str | None = None
    tile_res_rotate_z: int = 0
    tile_deco_id: str | None = None
    tile_deco_rotate_z: int = 0
    height: int = 0
    node_id: str | None = None


class SandboxV3MapNodeData(GameDataModel):
    """clz_Torappu_SandboxV3MapNodeData"""

    node_id: str | None = None
    node_type: str = "NONE"
    stage_id: str | None = None
    zone_id: str | None = None
    front_node_id: str | None = None
    unlock_tile_id_list: list[str] | None = None
    grid_pos: SandboxV3MapGridPos | None = None
    on_tile_id: str | None = None
    height: int = 0


class SandboxV3ZoneData(GameDataModel):
    """clz_Torappu_SandboxV3ZoneData"""

    zone_id: str | None = None
    name: str | None = None
    sort_id: int = 0
    display_name: bool = False
    appellation: str | None = None
    grid_pos: SandboxV3MapGridPos | None = None


class SandboxV3MapConfig(GameDataModel):
    """clz_Torappu_SandboxV3MapConfig"""

    max_spring_back_radius: float = 0.0
    min_spring_back_radius: float = 0.0


class SandboxV3MapData(GameDataModel):
    """clz_Torappu_SandboxV3MapData"""

    tiles: dict[str, SandboxV3MapTileData] | None = None
    nodes: dict[str, SandboxV3MapNodeData] | None = None
    zones: dict[str, SandboxV3ZoneData] | None = None
    map_config: SandboxV3MapConfig | None = None


class SandboxV3NodeTypeData(GameDataModel):
    """clz_Torappu_SandboxV3NodeTypeData"""

    node_type: str = "NONE"
    name: str | None = None


class SandboxV3PowerMilestoneData(GameDataModel):
    """clz_Torappu_SandboxV3PowerMilestoneData"""

    milestone_id: str | None = None
    stage: str = "EARLY"
    target_power_value: int = 0
    choice_slot_cnt: int = 0
    allow_refresh: bool = False
    allow_give_up_choice: bool = False
    default_pool: str | None = None
    refresh_pool: str | None = None


class SandboxV3StageInitialItemData(GameDataModel):
    """clz_Torappu_SandboxV3StageInitialItemData"""

    item_id: str | None = None
    count: int = 0


class SandboxV3StageData(GameDataModel):
    """clz_Torappu_SandboxV3StageData"""

    stage_id: str | None = None
    code: str | None = None
    name: str | None = None
    description: str | None = None
    max_day: int = 0
    max_play_time: float = 0.0
    jump_time: float = 0.0
    target_power_value: int = 0
    day_target_values: list[int] | None = None
    task_pool: list[str] | None = None
    quest_pool_by_difficulty: int = 0
    stat_params: str | None = None
    milestones: dict[str, SandboxV3PowerMilestoneData] | None = None
    task_slots: list[str] | None = None
    initial_item_data: list[SandboxV3StageInitialItemData] | None = None
    squad_max: int = 0
    initial_recruit_num: int = 0
    day_pass_recruit_num: int = 0
    level_rune: str | None = None
    first_day_description: str | None = None
    level_bgm: str | None = None
    is_formation_saved: bool = False


class SandboxV3StoryStageData(GameDataModel):
    """clz_Torappu_SandboxV3StoryStageData"""

    stage_id: str | None = None
    sub_stage_id_list: list[str] | None = None
    initial_sub_stage_index_list: list[int] | None = None


class SandboxV3ExploreStageData(GameDataModel):
    """clz_Torappu_SandboxV3ExploreStageData"""

    stage_id: str | None = None
    sub_stage_pool_id: str | None = None
    stage_difficulty_max: int = 0
    display_enemy_id_list: list[str] | None = None


class SandboxV3ExploreStageDifficultyData(GameDataModel):
    """clz_Torappu_SandboxV3ExploreStageDifficultyData"""

    difficulty_id: str | None = None
    difficulty_level: int = 0
    unlock_cond_desc_list: list[str] | None = None
    difficulty_desc: str | None = None
    difficulty_factor: float = 0.0
    rune_id_list: list[str] | None = None


class SandboxV3SubStageData(GameDataModel):
    """clz_Torappu_SandboxV3SubStageData"""

    sub_stage_id: str | None = None
    level_id: str | None = None
    type_mask: int = 0
    map_preview_id: str | None = None


class SandboxV3StageDropData(GameDataModel):
    """clz_Torappu_SandboxV3StageDropData"""

    stage_id: str | None = None
    reward_first_items: dict[str, int] | None = None
    reward_normal_items: dict[str, float] | None = None
    reward_hard_items: dict[str, float] | None = None


class SandboxV3ItemTypeData(GameDataModel):
    """clz_Torappu_SandboxV3ItemTypeData"""

    item_type: str = "NONE"
    item_type_name: str | None = None
    is_shop_sell: bool = False
    is_bag_show: bool = False
    bag_item_type: str = "NONE"


class SandboxV3BagItemTypeData(GameDataModel):
    """clz_Torappu_SandboxV3BagItemTypeData"""

    bag_item_type: str = "NONE"
    bag_item_type_name: str | None = None
    sort_id: int = 0
    bag_item_type_pic: str | None = None


class SandboxV3ToolkitContentData(GameDataModel):
    """clz_Torappu_SandboxV3ToolkitContentData"""

    content_item_id: str | None = None
    content_cnt_min: int = 0
    content_cnt_max: int = 0


class SandboxV3ItemRandomPoolDataItem(GameDataModel):
    """clz_Torappu_SandboxV3ItemRandomPoolData_Item"""

    item_id: str | None = None
    count: int = 0
    weight: int = 0


class SandboxV3ItemRandomPoolData(GameDataModel):
    """clz_Torappu_SandboxV3ItemRandomPoolData"""

    normal_item_list: list[SandboxV3ItemRandomPoolDataItem] | None = None
    guarantee_item_list: list[SandboxV3ItemRandomPoolDataItem] | None = None


class SandboxV3RandomItemData(GameDataModel):
    """clz_Torappu_SandboxV3RandomItemData"""

    pool_id: str | None = None


class SandboxV3ItemExtraData(GameDataModel):
    """clz_Torappu_SandboxV3ItemExtraData"""

    item_id: str | None = None
    item_type: str = "NONE"
    trap_cfg_id: str | None = None
    recipe_cfg_id: str | None = None
    relic_cfg_id: str | None = None
    item_rarity: int = 0
    item_sort_id_1: int = 0
    item_sort_id_2: int = 0
    is_bag_preview: bool = False


class SandboxV3DefendScoreData(GameDataModel):
    """clz_Torappu_SandboxV3DefendScoreData"""

    rarity: int = 0
    evolve_phase: int = 0
    level: int = 0
    grade: int = 0


class SandboxV3ZoneDefendRewardData(GameDataModel):
    """clz_Torappu_SandboxV3ZoneDefendRewardData"""

    grade: int = 0
    rewards: dict[str, int] | None = None


class SandboxV3ZoneDefendData(GameDataModel):
    """clz_Torappu_SandboxV3ZoneDefendData"""

    zone_id: str | None = None
    icon_id: str | None = None
    title_icon_id: str | None = None
    reward_data_list: list[SandboxV3ZoneDefendRewardData] | None = None


class SandboxV3BasementUpdateCondition(GameDataModel):
    """clz_Torappu_SandboxV3BasementUpdateCondition"""

    desc: str | None = None
    limit_cond: str | None = None
    param: list[str] | None = None


class SandboxV3BasementFunctionPreviewData(GameDataModel):
    """clz_Torappu_SandboxV3BasementFunctionPreviewData"""

    preview_id: str | None = None
    preview_value: int = 0


class SandboxV3BasementUpdateData(GameDataModel):
    """clz_Torappu_SandboxV3BasementUpdateData"""

    base_level_id: str | None = None
    base_level: int = 0
    base_desc: str | None = None
    level_id: str | None = None
    wonder_id: str | None = None
    conditions: list[SandboxV3BasementUpdateCondition] | None = None
    items: dict[str, int] | None = None
    preview_datas: list[SandboxV3BasementFunctionPreviewData] | None = None
    rewards: list[ItemBundle] | None = None


class SandboxV3BasementUpdateFunctionPreviewDetailData(GameDataModel):
    """clz_Torappu_SandboxV3BasementUpdateFunctionPreviewDetailData"""

    func_id: str | None = None
    unlock_type: str = "NONE"
    type_title: str | None = None
    desc: str | None = None
    icon: str | None = None
    dark_mode: bool = False
    sort_id: int = 0
    display_type: str = "NONE"


class SandboxV3WonderData(GameDataModel):
    """clz_Torappu_SandboxV3WonderData"""

    wonder_id: str | None = None
    wonder_name: str | None = None
    sort_id: int = 0


class SandboxV3BuildScoreGroupData(GameDataModel):
    """clz_Torappu_SandboxV3BuildScoreGroupData"""

    sort_id: int = 0
    score_group_type: str = "WONDER"


class SandboxV3QuestData(GameDataModel):
    """clz_Torappu_SandboxV3QuestData"""

    quest_id: str | None = None
    quest_line: str | None = None
    sort_id: int = 0
    quest_title: str | None = None
    quest_desc: str | None = None
    quest_target_desc: str | None = None
    is_display: bool = False
    quest_route_param: str | None = None
    show_progress_index: int = 0


class SandboxV3NpcData(GameDataModel):
    """clz_Torappu_SandboxV3NpcData"""

    npc_id: str | None = None
    trap_id: str | None = None
    sort_id: int = 0
    npc_type: str = "NORMAL"
    dialog_ids: dict[str, str] | None = None
    npc_location: list[int] | None = None
    npc_orientation: str = "UP"
    pic_id: str | None = None
    pic_name: str | None = None
    show_pic: bool = False
    react_skill_index: int = 0


class SandboxV3EnemyNpcData(GameDataModel):
    """clz_Torappu_SandboxV3EnemyNpcData"""

    npc_id: str | None = None
    battle_rune_id: str | None = None


class SandboxV3DialogData(GameDataModel):
    """clz_Torappu_SandboxV3DialogData"""

    dialog_id: str | None = None
    avg_id: str | None = None


class SandboxV3QuestLineData(GameDataModel):
    """clz_Torappu_SandboxV3QuestLineData"""

    quest_line_id: str | None = None
    quest_line_title: str | None = None
    quest_line_badge_type: str = "NONE"
    quest_line_desc: str | None = None
    sort_id: int = 0


class SandboxV3GuideQuestData(GameDataModel):
    """clz_Torappu_SandboxV3GuideQuestData"""

    quest_id: str | None = None
    story_id: str | None = None
    trigger_key: str | None = None


class SandboxV3CookbookData(GameDataModel):
    """clz_Torappu_SandboxV3CookbookData"""

    item_id: str | None = None
    attr_list: list[str] | None = None
    main_mat_list: list[str] | None = None
    item_usage: str | None = None
    item_name: str | None = None
    rune_data: RuneTablePackedRuneData | None = None


class SandboxV3CookSpiceData(GameDataModel):
    """clz_Torappu_SandboxV3CookSpiceData"""

    item_id: str | None = None
    buff_desc: str | None = None
    attr_type: str = "NONE"
    rune_data: RuneTablePackedRuneData | None = None


class SandboxV3BaseShopGoodExtraData(GameDataModel):
    """clz_Torappu_SandboxV3BaseShopGoodExtraData"""

    unlock_desc: str | None = None


class SandboxPermShopGoodData(GameDataModel):
    """clz_Torappu_SandboxPermShopGoodData"""

    good_id: str | None = None
    item_id: str | None = None
    count: int = 0
    coin_type: str = "DIMENSION_COIN"
    value: int = 0
    stock: int = 0


class SandboxPermShopSellData(GameDataModel):
    """clz_Torappu_SandboxPermShopSellData"""

    item_id: str | None = None
    count_in_unit: int = 0
    sell_coin_type: str = "DIMENSION_COIN"
    sell_val: int = 0


class SandboxV3StageShopData(GameDataModel):
    """clz_Torappu_SandboxV3StageShopData"""

    shop_id: str | None = None
    stage_id: str | None = None
    shop_type: str = "NONE"
    priority: int = 0
    can_refresh: bool = False
    display_slot: int = 0


class SandboxShopSlotData(GameDataModel):
    """clz_Torappu_SandboxShopSlotData"""

    slot_id: int = 0
    sort_id: int = 0
    item_pool_id: str | None = None
    price_modifier: float = 0.0


class SandboxV3ShopDetailData(GameDataModel):
    """clz_Torappu_SandboxV3ShopDetailData"""

    slot_data_list: list[SandboxShopSlotData] | None = None


class SandboxV3ShopGoodPoolItemData(GameDataModel):
    """clz_Torappu_SandboxV3ShopGoodPoolItemData"""

    good_id: str | None = None
    weight: int = 0


class SandboxV3ShopGoodPoolData(GameDataModel):
    """clz_Torappu_SandboxV3ShopGoodPoolData"""

    item_pool_id: str | None = None
    normal_item_list: list[SandboxV3ShopGoodPoolItemData] | None = None
    guarantee_item_list: list[SandboxV3ShopGoodPoolItemData] | None = None


class SandboxShopCoinTypeData(GameDataModel):
    """clz_Torappu_SandboxShopCoinTypeData"""

    coin_tye: str = "DIMENSION_COIN"
    item_id: str | None = None
    coin_icon: str | None = None
    coin_color_str: str | None = None


class SandboxV3EventSceneData(GameDataModel):
    """clz_Torappu_SandboxV3EventSceneData"""

    scene_id: str | None = None
    title: str | None = None
    desc: str | None = None
    choice_id_list: list[str] | None = None


class SandboxV3EventChoiceData(GameDataModel):
    """clz_Torappu_SandboxV3EventChoiceData"""

    choice_id: str | None = None
    title: str | None = None
    desc: str | None = None
    expedition_id: str | None = None


class SandboxV3EventExpeditionData(GameDataModel):
    """clz_Torappu_SandboxV3EventExpeditionData"""

    expedition_id: str | None = None
    char_count: int = 0
    required_profession: str = "NONE"
    min_elite_rank: int = 0


class SandboxV3TrapData(GameDataModel):
    """clz_Torappu_SandboxV3TrapData"""

    trap_cfg_id: str | None = None
    trap_id: str | None = None
    trap_phase: int = 0
    trap_level: int = 0
    skill_index: int = 0
    skill_level: int = 0
    item_id: str | None = None
    trap_type: str = "PRODUCER"
    trap_icon: str | None = None
    prosperity: int = 0
    aesthetics: int = 0
    trap_group: str | None = None
    override_max_deploy_cnt: int = 0
    hand_cover_item_id: str | None = None


class SandboxV3TrapTypeData(GameDataModel):
    """clz_Torappu_SandboxV3TrapTypeData"""

    trap_type: str = "PRODUCER"
    type_name: str | None = None
    type_img: str | None = None
    sort_id: int = 0
    tag_color: str | None = None


class SandboxV3BaseTrapData(GameDataModel):
    """clz_Torappu_SandboxV3BaseTrapData"""

    trap_cfg_id: str | None = None
    trap_id: str | None = None
    trap_phase: int = 0
    trap_level: int = 0
    skill_index: int = 0
    skill_level: int = 0
    item_id: str | None = None
    upgrade_item_id: str | None = None
    trap_type: str = "NONE"
    build_type: str = "NONE"
    build_score: int = 0
    derived_build_type: list[str] | None = None
    derived_item_n_max_cnt: dict[str, int] | None = None


class GridPosition(GameDataModel):
    """clz_Torappu_GridPosition"""

    row: int = 0
    col: int = 0


class RangeData(GameDataModel):
    """clz_Torappu_RangeData"""

    id: str | None = None
    direction: str = "UP"
    grids: list[GridPosition] | None = None


class SandboxV3ElectricTransferData(GameDataModel):
    """clz_Torappu_SandboxV3ElectricTransferData"""

    item_id: str | None = None
    cal_type: str = "NONE"
    attack_range: str | None = None
    attack_range_data: RangeData | None = None
    skill_param: str | None = None
    supply_type: list[str] | None = None
    power_output: dict[str, float] | None = None


class SandboxV3BaseTrapTypeData(GameDataModel):
    """clz_Torappu_SandboxV3BaseTrapTypeData"""

    trap_type: str = "NONE"
    type_name: str | None = None
    icon_id: str | None = None
    sort_id: int = 0


class SandboxV3BuildRuleData(GameDataModel):
    """clz_Torappu_SandboxV3BuildRuleData"""

    build_type_1: str = "NONE"
    build_type_2: list[str] | None = None
    extra_build_score: int = 0
    extra_score_desc: str | None = None
    sort_id: int = 0


class SandboxV3BuildScoreData(GameDataModel):
    """clz_Torappu_SandboxV3BuildScoreData"""

    item_id: str | None = None
    param_type: str = "NONE"
    build_score: int = 0
    sort_id: int = 0


class SandboxV3CoinCostData(GameDataModel):
    """clz_Torappu_SandboxV3CoinCostData"""

    coin_type: str = "DIMENSION_COIN"
    coin_count: int = 0


class SandboxV3BaseTrapUpgradeData(GameDataModel):
    """clz_Torappu_SandboxV3BaseTrapUpgradeData"""

    item_id: str | None = None
    upgrade_item_id: str | None = None
    cost_coin_list: list[SandboxV3CoinCostData] | None = None
    upgrade_desc: str | None = None
    upgrade_condition: str | None = None
    upgrade_param_list: list[str] | None = None


class SandboxV3BuildAnimalData(GameDataModel):
    """clz_Torappu_SandboxV3BuildAnimalData"""

    item_id: str | None = None
    enemy_id: str | None = None
    is_legend: bool = False
    is_shiny: bool = False


class SandboxV3BaseTrapDeployData(GameDataModel):
    """clz_Torappu_SandboxV3BaseTrapDeployData"""

    base_level: int = 0
    max_deploy_cnt: int = 0


class SandboxV3ProcessRecipeData(GameDataModel):
    """clz_Torappu_SandboxV3ProcessRecipeData"""

    recipe_cfg_id: str | None = None
    recipe_level: int = 0
    recipe_item_id: str | None = None
    materials: dict[str, int] | None = None
    output_item_id: str | None = None
    output_cnt: int = 0
    output_prosperity: int = 0
    recipe_name: str | None = None
    output_skill_icon: str | None = None


class SandboxV3BuildRecipeData(GameDataModel):
    """clz_Torappu_SandboxV3BuildRecipeData"""

    recipe_cfg_id: str | None = None
    recipe_item_id: str | None = None
    materials: dict[str, int] | None = None
    output_item_id: str | None = None
    output_trap_type: str = "PRODUCER"
    withdraw_ratio: int = 0
    output_cnt: int = 0


class SandboxV3EnemyRewardItem(GameDataModel):
    """clz_Torappu_SandboxV3EnemyRewardItem"""

    item_id: str | None = None
    count: int = 0
    reward_type: str = "NONE"
    weight: int = 0


class SandboxV3EnemyRewardData(GameDataModel):
    """clz_Torappu_SandboxV3EnemyRewardData"""

    source_id: str | None = None
    slot_dict: dict[int, list[SandboxV3EnemyRewardItem]] | None = None


class SandboxV3EnemyLevelRewardData(GameDataModel):
    """clz_Torappu_SandboxV3EnemyLevelRewardData"""

    enemy_level_type: str | None = None
    slot_dict: dict[int, list[SandboxV3EnemyRewardItem]] | None = None


class SandboxV3ProsParam(GameDataModel):
    """clz_Torappu_SandboxV3ProsParam"""

    threshold: int = 0
    plus_value: float = 0.0
    level: int = 0


class SandboxV3StatParamData(GameDataModel):
    """clz_Torappu_SandboxV3StatParamData"""

    stat_id: str | None = None
    pros_params: list[SandboxV3ProsParam] | None = None
    aesth_params: dict[int, float] | None = None


class SandboxV3WeatherData(GameDataModel):
    """clz_Torappu_SandboxV3WeatherData"""

    weather_id: str | None = None
    name: str | None = None
    rune_id: str | None = None
    ex_rune_id: str | None = None
    func_desc: str | None = None
    desc: str | None = None
    enable_fog: bool = False
    screen_effect_id: str | None = None


class SandboxV3RelicPart(GameDataModel):
    """clz_Torappu_SandboxV3RelicPart"""

    key: str | None = None
    selector: str | None = None
    allow_multiple: bool = False
    blackboard: list[BlackboardDataPair] | None = None


class SandboxV3RelicData(GameDataModel):
    """clz_Torappu_SandboxV3RelicData"""

    relic_id: str | None = None
    parts: list[SandboxV3RelicPart] | None = None


class SandboxV3BandLevelData(GameDataModel):
    """clz_Torappu_SandboxV3BandLevelData"""

    level: int = 0
    effect_desc: str | None = None
    unlock_cond_desc: str | None = None


class SandboxV3BandData(GameDataModel):
    """clz_Torappu_SandboxV3BandData"""

    band_id: str | None = None
    name: str | None = None
    sort_id: int = 0
    band_icon: str | None = None
    level_list: list[SandboxV3BandLevelData] | None = None


class SandboxV3TaskSlotData(GameDataModel):
    """clz_Torappu_SandboxV3TaskSlotData"""

    slot_id: str | None = None
    stage_id: str | None = None
    unlock_day: int = 0
    is_fixed: bool = False
    fixed_tasks: list[str] | None = None
    task_level: int = 0


class SandboxV3TaskPoolWeightItem(GameDataModel):
    """clz_Torappu_SandboxV3TaskPoolWeightItem"""

    task_id: str | None = None
    weight: int = 0


class SandboxV3TaskPoolData(GameDataModel):
    """clz_Torappu_SandboxV3TaskPoolData"""

    pool_id: str | None = None
    task_weights: list[SandboxV3TaskPoolWeightItem] | None = None


class SandboxV3TaskData(GameDataModel):
    """clz_Torappu_SandboxV3TaskData"""

    task_id: str | None = None
    task_base_desc: str | None = None
    task_desc: str | None = None
    task_level: int = 0
    difficulty: str = "NONE"
    task_type: str = "DEPLOY_TRAP_BY_GROUP"
    task_type_desc: str | None = None
    str_params: list[str] | None = None
    int_params: list[int] | None = None
    power_value: int = 0
    rewards: list[str] | None = None
    type_mask: int = 0
    check_recipes: list[list[str]] | None = None
    task_group: str | None = None
    pre_task_group_chain: list[str] | None = None


class SandboxV3AvgPostTaskData(GameDataModel):
    """clz_Torappu_SandboxV3AvgPostTaskData"""

    task_id: str | None = None
    avg_id: str | None = None
    quest_id: str | None = None


class SandboxV3LivestockData(GameDataModel):
    """clz_Torappu_SandboxV3LivestockData"""

    enemy_id: str | None = None
    livestock_item_id: str | None = None
    livestock_enemy_id: str | None = None
    shiny_livestock_item_id: str | None = None
    shiny_livestock_enemy_id: str | None = None
    shiny_rate: float = 0.0
    is_legend: bool = False


class SandboxV3GameConst(GameDataModel):
    """clz_Torappu_SandboxV3GameConst"""

    basement_gold_item_id: str | None = None
    basement_gold_ex_item_id: str | None = None
    max_defend_count: int = 0
    defend_progress_volume: int = 0
    default_mode_id: str | None = None
    default_difficulty_id: str | None = None
    hard_difficulty_level: int = 0
    basement_map_unlock_level: int = 0
    defend_unlock_level: int = 0
    high_bgm_base_level: int = 0
    build_mode_bgm_home: str | None = None
    collection_base_gold_id: str | None = None
    collection_base_gold_count: int = 0
    collection_min_time: int = 0
    collection_max_time: int = 0
    base_coin_max: int = 0
    development_points_total: int = 0
    recruit_buy_time: int = 0
    recruit_start_price: int = 0
    recruit_price_multiply: float = 0.0
    recruit_name: str | None = None
    recruit_usage: str | None = None
    shop_discount_rate: float = 0.0
    shop_discount_num_min: int = 0
    shop_discount_num_max: int = 0
    shop_discount_value_min: float = 0.0
    shop_discount_value_max: float = 0.0
    refresh_price: int = 0
    multiply_factor: float = 0.0
    max_refresh_price: int = 0
    refresh_coin_type: str = "DIMENSION_COIN"
    recruit_coin_type: str = "DIMENSION_COIN"
    character_limit: int = 0
    max_life_point: int = 0
    initial_cost: int = 0
    max_cost: int = 0
    give_up_reward_item_id: str | None = None
    give_up_reward_item_cnt: int = 0
    recipe_origin_refresh_times: int = 0
    recipe_repeat_damp: float = 0.0
    task_option_cnt: int = 0
    task_repeat_damp: float = 0.0
    task_origin_refresh_times: int = 0
    task_not_allow_refresh_stage: list[str] | None = None
    task_time_stamp_type: str = "DEPLOY_TRAP_BY_GROUP"
    aesthetics_reward_item: str | None = None
    repeat_relic_convert_id: str | None = None
    repeat_recipe_convert_id: str | None = None
    repeat_recipe_convert_count: int = 0
    bag_preview_cnt: int = 0
    bag_preview_fixed_items: list[str] | None = None
    bag_preview_fixed_cnt: int = 0
    char_rarity_color_list: list[str] | None = None
    spiced_food_name_fmt: str | None = None
    essential_food_mat_item_id: str | None = None
    base_cleaner_item_id: str | None = None
    base_start_point_location: str | None = None
    electric_power_max: int = 0
    basement_node_id: str | None = None
    recipe_refresh_price_init: int = 0
    recipe_refresh_price_add: int = 0
    recipe_refresh_price_max: int = 0
    recipe_refresh_item_id: str | None = None
    day_pass_recruit_refresh_item_id: str | None = None
    day_pass_recruit_refresh_count: list[int] | None = None
    day_pass_recruit_sub_profession_count: int = 0
    day_pass_recruit_profession_count: int = 0
    temp_recruit_percentage: float = 0.0
    shop_npc_refresh_status: str | None = None
    img_loading_normal_name: str | None = None
    tech_token_ratio: float = 0.0
    lucky_reward_max: int = 0
    band_achievement_score: int = 0
    general_trademan_skill_index: int = 0
    general_trademan_avg_path: str | None = Field(default=None, alias="generalTrademanAVGPath")
    hide_cook_entry_node_ids: list[str] | None = None
    hide_shop_entry_node_ids: list[str] | None = None
    show_processor_not_working_interval: int = 0
    neutral_boss_enemy_id: list[str] | None = None
    special_boss_enemy_id: list[str] | None = None
    task_predecessor_ramp_up: float = 0.0
    rainbow_shiny_animal_rate_mul: float = 0.0
    enemy_kill_blacklist: list[str] | None = None


class SandboxV3SubStageRoomConstraint(GameDataModel):
    """clz_Torappu_SandboxV3SubStageRoomConstraint"""

    top: dict[str, int] | None = None
    bottom: dict[str, int] | None = None
    left: dict[str, int] | None = None
    right: dict[str, int] | None = None


class SandboxV3RandomMapPool(GameDataModel):
    """clz_Torappu_SandboxV3RandomMapPool"""

    elements: dict[str, SandboxV3SubStageRoomConstraint] | None = None


class SandboxV3Data(GameDataModel):
    """clz_Torappu_SandboxV3Data"""

    mode_datas: dict[str, SandboxV3ModeData] | None = None
    main_map_data: SandboxV3MapData | None = None
    node_type_data: dict[str, SandboxV3NodeTypeData] | None = None
    stage_data: dict[str, SandboxV3StageData] | None = None
    story_stage_data: dict[str, SandboxV3StoryStageData] | None = None
    explore_stage_data: dict[str, SandboxV3ExploreStageData] | None = None
    explore_stage_difficulty_data: dict[str, SandboxV3ExploreStageDifficultyData] | None = None
    sub_stage_data: dict[str, SandboxV3SubStageData] | None = None
    stage_drop_data: dict[str, SandboxV3StageDropData] | None = None
    navigation_node_ids: list[str] | None = None
    item_type_data: dict[str, SandboxV3ItemTypeData] | None = None
    bag_item_type_data: dict[str, SandboxV3BagItemTypeData] | None = None
    toolkit_content_data: dict[str, SandboxV3ToolkitContentData] | None = None
    item_random_pool_data: dict[str, SandboxV3ItemRandomPoolData] | None = None
    random_item_data: dict[str, SandboxV3RandomItemData] | None = None
    item_extra_data: dict[str, SandboxV3ItemExtraData] | None = None
    development_data: dict[str, SandboxDevelopmentData] | None = None
    development_line_segment_datas: list[SandboxDevelopmentLineSegmentData] | None = None
    defend_score_data: list[SandboxV3DefendScoreData] | None = None
    zone_defend_datas: dict[str, SandboxV3ZoneDefendData] | None = None
    basement_update_datas: list[SandboxV3BasementUpdateData] | None = None
    basement_preview_datas: dict[str, SandboxV3BasementUpdateFunctionPreviewDetailData] | None = None
    wonder_datas: dict[str, SandboxV3WonderData] | None = None
    build_score_group_datas: dict[str, SandboxV3BuildScoreGroupData] | None = None
    basement_weather_weights: dict[str, int] | None = None
    quest_data: dict[str, SandboxV3QuestData] | None = None
    npc_data: dict[str, SandboxV3NpcData] | None = None
    enemy_npc_data: dict[str, SandboxV3EnemyNpcData] | None = None
    dialog_data: dict[str, SandboxV3DialogData] | None = None
    quest_line_data: dict[str, SandboxV3QuestLineData] | None = None
    quest_line_story_data: dict[str, str] | None = None
    guide_quest_data: dict[str, SandboxV3GuideQuestData] | None = None
    cookbook_data: dict[str, SandboxV3CookbookData] | None = None
    cook_spice_data: dict[str, SandboxV3CookSpiceData] | None = None
    base_shop_good_extra_data: dict[str, SandboxV3BaseShopGoodExtraData] | None = None
    base_shop_good_data: dict[str, SandboxPermShopGoodData] | None = None
    base_shop_sell_data: dict[str, SandboxPermShopSellData] | None = None
    base_shop_coin_list: list[str] | None = None
    base_trap_item_list_map: dict[str, list[str]] | None = None
    stage_shop_list_data: dict[str, list[SandboxV3StageShopData]] | None = None
    shop_detail_data: dict[str, SandboxV3ShopDetailData] | None = None
    shop_type_coin_map: dict[str, list[str]] | None = None
    shop_good_pool_data: dict[str, SandboxV3ShopGoodPoolData] | None = None
    shop_good_data: dict[str, SandboxPermShopGoodData] | None = None
    shop_sell_data: dict[str, SandboxPermShopSellData] | None = None
    shop_coin_type_data: dict[str, SandboxShopCoinTypeData] | None = None
    event_scene_data: dict[str, SandboxV3EventSceneData] | None = None
    event_choice_data: dict[str, SandboxV3EventChoiceData] | None = None
    event_expedition_data: dict[str, SandboxV3EventExpeditionData] | None = None
    trap_data: dict[str, SandboxV3TrapData] | None = None
    trap_type_data: dict[str, SandboxV3TrapTypeData] | None = None
    base_trap_data: dict[str, SandboxV3BaseTrapData] | None = None
    electric_transfer_data: dict[str, SandboxV3ElectricTransferData] | None = None
    electric_building_list: list[str] | None = None
    base_trap_type_data: dict[str, SandboxV3BaseTrapTypeData] | None = None
    build_rule_data: list[SandboxV3BuildRuleData] | None = None
    build_score_data: dict[str, SandboxV3BuildScoreData] | None = None
    base_trap_upgrade_data: dict[str, SandboxV3BaseTrapUpgradeData] | None = None
    build_animal_data: dict[str, SandboxV3BuildAnimalData] | None = None
    base_trap_deploy_map: dict[str, list[SandboxV3BaseTrapDeployData]] | None = None
    process_recipe_data: dict[str, SandboxV3ProcessRecipeData] | None = None
    build_recipe_data: dict[str, SandboxV3BuildRecipeData] | None = None
    build_tip_data: list[TipData] | None = None
    enemy_reward_data: dict[str, SandboxV3EnemyRewardData] | None = None
    enemy_level_reward_data: dict[str, SandboxV3EnemyLevelRewardData] | None = None
    milestone_reward_pools: dict[str, list[str]] | None = None
    recipe_weight: dict[str, dict[str, int]] | None = None
    param_data: dict[str, SandboxV3StatParamData] | None = None
    weather_data: dict[str, SandboxV3WeatherData] | None = None
    rune_datas: dict[str, RuneTablePackedRuneData] | None = None
    relic_data: dict[str, SandboxV3RelicData] | None = None
    band_data_map: dict[str, SandboxV3BandData] | None = None
    mode_type_2_band_id_list_map: dict[str, list[str]] | None = None
    task_slot_data: dict[str, SandboxV3TaskSlotData] | None = None
    task_pool_data: dict[str, SandboxV3TaskPoolData] | None = None
    task_data: dict[str, SandboxV3TaskData] | None = None
    avg_post_task_data: dict[str, SandboxV3AvgPostTaskData] | None = None
    livestock_data: dict[str, SandboxV3LivestockData] | None = None
    achievement_data: dict[str, SandboxArchiveAchievementData] | None = None
    achievement_type_data: dict[str, SandboxArchiveAchievementTypeData] | None = None
    archive_quest_data: dict[str, SandboxArchiveQuestData] | None = None
    archive_quest_type_data: dict[str, SandboxArchiveQuestTypeData] | None = None
    archive_music_unlock_data: dict[str, SandboxArchiveMusicUnlockData] | None = None
    game_const: SandboxV3GameConst | None = None
    shop_update_time_data: list[int] | None = None
    extra_load_enemies: list[str] | None = None
    random_map_pool: dict[str, SandboxV3RandomMapPool] | None = None


class SandboxPermDetailData(GameDataModel):
    """clz_Torappu_SandboxPermDetailData"""

    sandbox_v2: dict[str, SandboxV2Data] | None = Field(default=None, alias="SANDBOX_V2")
    sandbox_v3: dict[str, SandboxV3Data] | None = Field(default=None, alias="SANDBOX_V3")


class SandboxPermItemData(GameDataModel):
    """clz_Torappu_SandboxPermItemData"""

    item_id: str | None = None
    item_type: str = "NONE"
    item_name: str | None = None
    item_usage: str | None = None
    item_desc: str | None = None
    item_rarity: int = 0
    sort_id: int = 0
    obtain_approach: str | None = None


class SandboxPermTable(GameDataModel):
    """clz_Torappu_SandboxPermTable"""

    basic_info: dict[str, SandboxPermBasicData] | None = None
    detail: SandboxPermDetailData | None = None
    item_data: dict[str, SandboxPermItemData] | None = None


# root_type clz_Torappu_SandboxPermTable


SandboxPermBasicDataHomeEntryDisplayData.model_rebuild()
SandboxPermEnrollPointData.model_rebuild()
SandboxPermBasicData.model_rebuild()
SandboxV2NodeData.model_rebuild()
UnityEngineVector2.model_rebuild()
SandboxV2MapZoneData.model_rebuild()
SandboxV2MapConfig.model_rebuild()
SandboxV2MapData.model_rebuild()
SandboxV2ItemTrapData.model_rebuild()
SandboxV2ItemTrapTagData.model_rebuild()
SandboxBuildingItemData.model_rebuild()
SandboxV2CraftItemData.model_rebuild()
SandboxV2LivestockData.model_rebuild()
SandboxV2CraftGroupData.model_rebuild()
SandboxV2AlchemyMaterialData.model_rebuild()
SandboxV2AlchemyRecipeData.model_rebuild()
SandboxV2DrinkMatData.model_rebuild()
SandboxFoodMatData.model_rebuild()
SandboxFoodRecipeData.model_rebuild()
SandboxFoodVariantData.model_rebuild()
SandboxFoodData.model_rebuild()
SandboxV2NodeTypeData.model_rebuild()
SandboxV2NodeUpgradeData.model_rebuild()
SandboxV2WeatherData.model_rebuild()
SandboxV2StageData.model_rebuild()
SandboxV2ZoneData.model_rebuild()
SandboxV2NodeBuffData.model_rebuild()
SandboxV2RewardItemConfigData.model_rebuild()
SandboxV2RewardData.model_rebuild()
SandboxV2RewardCommonConfig.model_rebuild()
SandboxV2RewardConfigGroupData.model_rebuild()
SandboxV2FloatIconData.model_rebuild()
SandboxV2EnemyRushTypeData.model_rebuild()
SandboxV2BattleRushEnemyConfig.model_rebuild()
SandboxV2BattleRushEnemyGroupConfig.model_rebuild()
SandboxV2BattleRushEnemyDataRushEnemyDBRef.model_rebuild()
SandboxV2BattleRushEnemyData.model_rebuild()
SandboxV2GameConst.model_rebuild()
ItemBundle.model_rebuild()
SandboxV2DiffModeData.model_rebuild()
SandboxV2BasicConst.model_rebuild()
SandboxV2RiftConst.model_rebuild()
SandboxV2DevelopmentConst.model_rebuild()
TipData.model_rebuild()
RuneDataSelector.model_rebuild()
BlackboardDataPair.model_rebuild()
RuneData.model_rebuild()
RuneTablePackedRuneData.model_rebuild()
LegacyInLevelRuneData.model_rebuild()
SandboxV2QuestData.model_rebuild()
SandboxV2NpcData.model_rebuild()
SandboxV2DialogData.model_rebuild()
SandboxV2QuestLineData.model_rebuild()
SandboxV2GuideQuestData.model_rebuild()
SandboxDevelopmentData.model_rebuild()
SandboxV2EventData.model_rebuild()
SandboxV2EventSceneData.model_rebuild()
SandboxV2EventChoiceData.model_rebuild()
SandboxV2ExpeditionData.model_rebuild()
SandboxV2EventEffectData.model_rebuild()
SandboxShopGoodData.model_rebuild()
SandboxV2ShopDialogData.model_rebuild()
SandboxV2LogisticsData.model_rebuild()
SandboxV2LogisticsCharData.model_rebuild()
SandboxV2MonthRushData.model_rebuild()
SandboxV2RiftParamData.model_rebuild()
SandboxV2RiftSubTargetData.model_rebuild()
SandboxV2RiftMainTargetData.model_rebuild()
SandboxV2RiftGlobalEffectData.model_rebuild()
SandboxV2FixedRiftData.model_rebuild()
SandboxV2RiftTeamBuffData.model_rebuild()
SandboxV2RiftDifficultyData.model_rebuild()
SandboxArchiveQuestAvgData.model_rebuild()
SandboxArchiveQuestCgData.model_rebuild()
SandboxArchiveQuestZoneData.model_rebuild()
SandboxArchiveQuestData.model_rebuild()
SandboxArchiveAchievementData.model_rebuild()
SandboxArchiveAchievementTypeData.model_rebuild()
SandboxArchiveQuestTypeData.model_rebuild()
SandboxArchiveMusicUnlockData.model_rebuild()
SandboxV2BaseUpdateCondition.model_rebuild()
SandboxV2BaseUpdateFunctionPreviewDetailData.model_rebuild()
SandboxV2BaseFunctionPreviewData.model_rebuild()
SandboxV2BaseUpdateData.model_rebuild()
SandboxDevelopmentLineSegmentData.model_rebuild()
SandboxV2BuildingNodeScoreData.model_rebuild()
SandboxV2SeasonData.model_rebuild()
SandboxV2ConfirmIconData.model_rebuild()
SandboxV2TutorialRepoCharData.model_rebuild()
SandboxV2TutorialBasicConst.model_rebuild()
SandboxV2TutorialData.model_rebuild()
SandboxV2RacerBasicInfo.model_rebuild()
SandboxV2RacerTalentInfo.model_rebuild()
SandboxV2RacerNameInfo.model_rebuild()
SandboxV2RacerMedalInfo.model_rebuild()
SandboxV2RacingItemInfo.model_rebuild()
SandboxV2RacingConstData.model_rebuild()
SandboxV2RacingData.model_rebuild()
SandboxV2ChallengeConst.model_rebuild()
SandboxV2ChallengeModeUnlockData.model_rebuild()
SandboxV2ChallengeModeRewardData.model_rebuild()
SandboxV2ChallengeModeDifficultyData.model_rebuild()
SandboxV2ChallengeModeData.model_rebuild()
SandboxV2Data.model_rebuild()
SandboxV3ModeData.model_rebuild()
SandboxV3MapGridPos.model_rebuild()
SandboxV3MapTileData.model_rebuild()
SandboxV3MapNodeData.model_rebuild()
SandboxV3ZoneData.model_rebuild()
SandboxV3MapConfig.model_rebuild()
SandboxV3MapData.model_rebuild()
SandboxV3NodeTypeData.model_rebuild()
SandboxV3PowerMilestoneData.model_rebuild()
SandboxV3StageInitialItemData.model_rebuild()
SandboxV3StageData.model_rebuild()
SandboxV3StoryStageData.model_rebuild()
SandboxV3ExploreStageData.model_rebuild()
SandboxV3ExploreStageDifficultyData.model_rebuild()
SandboxV3SubStageData.model_rebuild()
SandboxV3StageDropData.model_rebuild()
SandboxV3ItemTypeData.model_rebuild()
SandboxV3BagItemTypeData.model_rebuild()
SandboxV3ToolkitContentData.model_rebuild()
SandboxV3ItemRandomPoolDataItem.model_rebuild()
SandboxV3ItemRandomPoolData.model_rebuild()
SandboxV3RandomItemData.model_rebuild()
SandboxV3ItemExtraData.model_rebuild()
SandboxV3DefendScoreData.model_rebuild()
SandboxV3ZoneDefendRewardData.model_rebuild()
SandboxV3ZoneDefendData.model_rebuild()
SandboxV3BasementUpdateCondition.model_rebuild()
SandboxV3BasementFunctionPreviewData.model_rebuild()
SandboxV3BasementUpdateData.model_rebuild()
SandboxV3BasementUpdateFunctionPreviewDetailData.model_rebuild()
SandboxV3WonderData.model_rebuild()
SandboxV3BuildScoreGroupData.model_rebuild()
SandboxV3QuestData.model_rebuild()
SandboxV3NpcData.model_rebuild()
SandboxV3EnemyNpcData.model_rebuild()
SandboxV3DialogData.model_rebuild()
SandboxV3QuestLineData.model_rebuild()
SandboxV3GuideQuestData.model_rebuild()
SandboxV3CookbookData.model_rebuild()
SandboxV3CookSpiceData.model_rebuild()
SandboxV3BaseShopGoodExtraData.model_rebuild()
SandboxPermShopGoodData.model_rebuild()
SandboxPermShopSellData.model_rebuild()
SandboxV3StageShopData.model_rebuild()
SandboxShopSlotData.model_rebuild()
SandboxV3ShopDetailData.model_rebuild()
SandboxV3ShopGoodPoolItemData.model_rebuild()
SandboxV3ShopGoodPoolData.model_rebuild()
SandboxShopCoinTypeData.model_rebuild()
SandboxV3EventSceneData.model_rebuild()
SandboxV3EventChoiceData.model_rebuild()
SandboxV3EventExpeditionData.model_rebuild()
SandboxV3TrapData.model_rebuild()
SandboxV3TrapTypeData.model_rebuild()
SandboxV3BaseTrapData.model_rebuild()
GridPosition.model_rebuild()
RangeData.model_rebuild()
SandboxV3ElectricTransferData.model_rebuild()
SandboxV3BaseTrapTypeData.model_rebuild()
SandboxV3BuildRuleData.model_rebuild()
SandboxV3BuildScoreData.model_rebuild()
SandboxV3CoinCostData.model_rebuild()
SandboxV3BaseTrapUpgradeData.model_rebuild()
SandboxV3BuildAnimalData.model_rebuild()
SandboxV3BaseTrapDeployData.model_rebuild()
SandboxV3ProcessRecipeData.model_rebuild()
SandboxV3BuildRecipeData.model_rebuild()
SandboxV3EnemyRewardItem.model_rebuild()
SandboxV3EnemyRewardData.model_rebuild()
SandboxV3EnemyLevelRewardData.model_rebuild()
SandboxV3ProsParam.model_rebuild()
SandboxV3StatParamData.model_rebuild()
SandboxV3WeatherData.model_rebuild()
SandboxV3RelicPart.model_rebuild()
SandboxV3RelicData.model_rebuild()
SandboxV3BandLevelData.model_rebuild()
SandboxV3BandData.model_rebuild()
SandboxV3TaskSlotData.model_rebuild()
SandboxV3TaskPoolWeightItem.model_rebuild()
SandboxV3TaskPoolData.model_rebuild()
SandboxV3TaskData.model_rebuild()
SandboxV3AvgPostTaskData.model_rebuild()
SandboxV3LivestockData.model_rebuild()
SandboxV3GameConst.model_rebuild()
SandboxV3SubStageRoomConstraint.model_rebuild()
SandboxV3RandomMapPool.model_rebuild()
SandboxV3Data.model_rebuild()
SandboxPermDetailData.model_rebuild()
SandboxPermItemData.model_rebuild()
SandboxPermTable.model_rebuild()

"""building_data.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/building_data.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class BuildingDataRoomType(IntEnum):
    """enum__Torappu_BuildingData_RoomType"""

    NONE = 0
    CONTROL = 1
    POWER = 2
    MANUFACTURE = 4
    SHOP = 8
    DORMITORY = 16
    MEETING = 32
    HIRE = 64
    ELEVATOR = 128
    CORRIDOR = 256
    TRADING = 512
    WORKSHOP = 1024
    TRAINING = 2048
    PRIVATE = 4096
    RECYCLE = 8192
    FUNCTIONAL = 11902
    ALL = 16383


class BuildingDataRoomCategory(IntEnum):
    """enum__Torappu_BuildingData_RoomCategory"""

    NONE = 0
    FUNCTION = 1
    OUTPUT = 2
    CUSTOM = 4
    ELEVATOR = 8
    CORRIDOR = 16
    SPECIAL = 32
    CUSTOM_P = 64
    ELEVATOR_P = 128
    CORRIDOR_P = 256
    ALL = 511


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


class BuildingDataLayoutDataStoreyDataType(IntEnum):
    """enum__Torappu_BuildingData_LayoutData_StoreyData_Type"""

    UPGROUND = 0
    DOWNGROUND = 1


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


class BuildingDataBuffCategory(IntEnum):
    """enum__Torappu_BuildingData_BuffCategory"""

    NONE = 0
    FUNCTION = 1
    OUTPUT = 2
    RECOVERY = 3


class BuildingDataFurnitureInteract(IntEnum):
    """enum__Torappu_BuildingData_FurnitureInteract"""

    NONE = 0
    ANIMATOR = 1
    MUSIC = 2
    FUNCTION = 3


class BuildingDataFurnitureType(IntEnum):
    """enum__Torappu_BuildingData_FurnitureType"""

    FLOOR = 0
    CARPET = 1
    SEATING = 2
    BEDDING = 3
    TABLE = 4
    CABINET = 5
    DECORATION = 6
    WALLPAPER = 7
    WALLDECO = 8
    WALLLAMP = 9
    CEILING = 10
    CEILINGLAMP = 11
    FUNCTION = 12
    INTERACT = 13


class BuildingDataFurnitureSubType(IntEnum):
    """enum__Torappu_BuildingData_FurnitureSubType"""

    NONE = 0
    CHAIR = 1
    SOFA = 2
    BARSTOOL = 3
    STOOL = 4
    BENCH = 5
    ORTHER_S = 6
    POSTER = 7
    CURTAIN = 8
    BOARD_WD = 9
    SHELF = 10
    INSTRUMENT_WD = 11
    ART_WD = 12
    PLAQUE = 13
    CONTRACT = 14
    ANNIHILATION = 15
    ORTHER_WD = 16
    FLOORLAMP = 17
    PLANT = 18
    PARTITION = 19
    COOKING = 20
    CATERING = 21
    DEVICE = 22
    INSTRUMENT_D = 23
    ART_D = 24
    BOARD_D = 25
    ENTERTAINMENT = 26
    STORAGE = 27
    DRESSING = 28
    WARM = 29
    WASH = 30
    ORTHER_D = 31
    COLUMN = 32
    DECORATION_C = 33
    CURTAIN_C = 34
    DEVICE_C = 35
    CONTRACT_2 = 36
    LIGHT = 37
    ORTHER_C = 38
    VISITOR = 39
    MUSIC = 40


class BuildingDataFurnitureLocation(IntEnum):
    """enum__Torappu_BuildingData_FurnitureLocation"""

    NONE = 0
    WALL = 1
    FLOOR = 2
    CARPET = 3
    CEILING = 4
    POSTER = 5
    CEILINGDECAL = 6


class BuildingDataFurnitureCategory(IntEnum):
    """enum__Torappu_BuildingData_FurnitureCategory"""

    FURNITURE = 0
    WALL = 1
    FLOOR = 2


class BuildingDataDiySortType(IntEnum):
    """enum__Torappu_BuildingData_DiySortType"""

    NONE = 0
    THEME = 1
    FURNITURE = 2
    FURNITURE_IN_THEME = 3
    RECENT_THEME = 4
    RECENT_FURNITURE = 5
    MEETING_THEME = 6
    MEETING_FURNITURE = 7
    MEETING_FURNITURE_IN_THEME = 8
    MEETING_RECENT_THEME = 9
    MEETING_RECENT_FURNITURE = 10


class BuildingDataDiyUISortOrder(IntEnum):
    """enum__Torappu_BuildingData_DiyUISortOrder"""

    DESC = 0
    ASC = 1


class BuildingDataFormulaItemType(IntEnum):
    """enum__Torappu_BuildingData_FormulaItemType"""

    NONE = 0
    F_EVOLVE = 1
    F_BUILDING = 2
    F_GOLD = 3
    F_DIAMOND = 4
    F_FURNITURE = 5
    F_EXP = 6
    F_ASC = 7
    F_SKILL = 8


class ItemRarity(IntEnum):
    """enum__Torappu_ItemRarity"""

    TIER_1 = 0
    TIER_2 = 1
    TIER_3 = 2
    TIER_4 = 3
    TIER_5 = 4
    TIER_6 = 5
    E_NUM = 6


class BuildingDataCharStationFilterType(IntEnum):
    """enum__Torappu_BuildingData_CharStationFilterType"""

    All = 0
    DormLock = 1
    NotStationed = 2


class BuildingDataRoomUnlockCondCondItem(GameDataModel):
    """clz_Torappu_BuildingData_RoomUnlockCond_CondItem"""

    type: str = "NONE"
    level: int = 0
    count: int = 0


class BuildingDataRoomUnlockCond(GameDataModel):
    """clz_Torappu_BuildingData_RoomUnlockCond"""

    id: str | None = None
    number: dict[int, BuildingDataRoomUnlockCondCondItem] | None = None


class GridPosition(GameDataModel):
    """clz_Torappu_GridPosition"""

    row: int = 0
    col: int = 0


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class BuildingDataRoomDataBuildCost(GameDataModel):
    """clz_Torappu_BuildingData_RoomData_BuildCost"""

    items: list[ItemBundle] | None = None
    time: int = 0
    labor: int = 0


class BuildingDataRoomDataPhaseData(GameDataModel):
    """clz_Torappu_BuildingData_RoomData_PhaseData"""

    override_name: str | None = None
    override_prefab_id: str | None = None
    unlock_cond_id: str | None = None
    build_cost: BuildingDataRoomDataBuildCost | None = None
    electricity: int = 0
    max_stationed_num: int = 0
    manpower_cost: int = 0


class BuildingDataRoomData(GameDataModel):
    """clz_Torappu_BuildingData_RoomData"""

    id: str = "NONE"
    name: str | None = None
    description: str | None = None
    default_prefab_id: str | None = None
    can_level_down: bool = False
    max_count: int = 0
    category: str = "NONE"
    size: GridPosition | None = None
    phases: list[BuildingDataRoomDataPhaseData] | None = None


class BuildingDataLayoutDataRoomSlot(GameDataModel):
    """clz_Torappu_BuildingData_LayoutData_RoomSlot"""

    id: str | None = None
    clean_cost_id: str | None = None
    cost_labor: int = 0
    provide_labor: int = 0
    size: GridPosition | None = None
    offset: GridPosition | None = None
    category: str = "NONE"
    storey_id: str | None = None


class BuildingDataLayoutDataSlotCleanCostCountCost(GameDataModel):
    """clz_Torappu_BuildingData_LayoutData_SlotCleanCost_CountCost"""

    items: list[ItemBundle] | None = None


class BuildingDataLayoutDataSlotCleanCost(GameDataModel):
    """clz_Torappu_BuildingData_LayoutData_SlotCleanCost"""

    id: str | None = None
    number: dict[int, BuildingDataLayoutDataSlotCleanCostCountCost] | None = None


class BuildingDataLayoutDataStoreyData(GameDataModel):
    """clz_Torappu_BuildingData_LayoutData_StoreyData"""

    id: str | None = None
    y_offset: int = 0
    unlock_control_level: int = 0
    type: str = "UPGROUND"


class BuildingDataLayoutData(GameDataModel):
    """clz_Torappu_BuildingData_LayoutData"""

    id: str | None = None
    slots: dict[str, BuildingDataLayoutDataRoomSlot] | None = None
    clean_costs: dict[str, BuildingDataLayoutDataSlotCleanCost] | None = None
    storeys: dict[str, BuildingDataLayoutDataStoreyData] | None = None


class BuildingDataPrefabInfo(GameDataModel):
    """clz_Torappu_BuildingData_PrefabInfo"""

    id: str | None = None
    blueprint_room_override_id: str | None = None
    size: GridPosition | None = None
    floor_grid_size: GridPosition | None = None
    back_wall_grid_size: GridPosition | None = None
    obstacle_id: str | None = None


class BuildingDataControlRoomPhase(GameDataModel):
    """clz_Torappu_BuildingData_ControlRoomPhase"""

    pass


class BuildingDataControlRoomBean(GameDataModel):
    """clz_Torappu_BuildingData_ControlRoomBean"""

    basic_cost_buff: int = 0
    phases: list[BuildingDataControlRoomPhase] | None = None


class BuildingDataManufactPhase(GameDataModel):
    """clz_Torappu_BuildingData_ManufactPhase"""

    speed: float = 0.0
    output_capacity: int = 0


class BuildingDataManufactRoomBean(GameDataModel):
    """clz_Torappu_BuildingData_ManufactRoomBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataManufactPhase] | None = None


class BuildingDataShopPhase(GameDataModel):
    """clz_Torappu_BuildingData_ShopPhase"""

    counter_num: int = 0
    speed: float = 0.0
    money_capacity: int = 0


class BuildingDataRoomBean1BuildingDataShopPhase(GameDataModel):
    """clz_Torappu_BuildingData_RoomBean_1_Torappu_BuildingData_ShopPhase_"""

    phases: list[BuildingDataShopPhase] | None = None


class BuildingDataHirePhase(GameDataModel):
    """clz_Torappu_BuildingData_HirePhase"""

    economize_rate: float = 0.0
    res_speed: int = 0
    refresh_times: int = 0


class BuildingDataHireRoomBean(GameDataModel):
    """clz_Torappu_BuildingData_HireRoomBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataHirePhase] | None = None


class BuildingDataDormPhase(GameDataModel):
    """clz_Torappu_BuildingData_DormPhase"""

    manpower_recover: int = 0
    decoration_limit: int = 0


class BuildingDataRoomBean1BuildingDataDormPhase(GameDataModel):
    """clz_Torappu_BuildingData_RoomBean_1_Torappu_BuildingData_DormPhase_"""

    phases: list[BuildingDataDormPhase] | None = None


class BuildingDataPrivatePhase(GameDataModel):
    """clz_Torappu_BuildingData_PrivatePhase"""

    decoration_limit: int = 0


class BuildingDataRoomBean1BuildingDataPrivatePhase(GameDataModel):
    """clz_Torappu_BuildingData_RoomBean_1_Torappu_BuildingData_PrivatePhase_"""

    phases: list[BuildingDataPrivatePhase] | None = None


class BuildingDataMeetingPhase(GameDataModel):
    """clz_Torappu_BuildingData_MeetingPhase"""

    friend_slot_inc: int = 0
    max_visitor_num: int = 0
    gathering_speed: int = 0


class BuildingDataMeetingRoomBean(GameDataModel):
    """clz_Torappu_BuildingData_MeetingRoomBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataMeetingPhase] | None = None


class BuildingDataTradingPhase(GameDataModel):
    """clz_Torappu_BuildingData_TradingPhase"""

    order_speed: float = 0.0
    order_limit: int = 0
    order_rarity: int = 0


class BuildingDataTradingRoomBean(GameDataModel):
    """clz_Torappu_BuildingData_TradingRoomBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataTradingPhase] | None = None


class BuildingDataWorkshopPhase(GameDataModel):
    """clz_Torappu_BuildingData_WorkshopPhase"""

    manpower_factor: float = 0.0


class BuildingDataRoomBean1BuildingDataWorkshopPhase(GameDataModel):
    """clz_Torappu_BuildingData_RoomBean_1_Torappu_BuildingData_WorkshopPhase_"""

    phases: list[BuildingDataWorkshopPhase] | None = None


class BuildingDataTrainingPhase(GameDataModel):
    """clz_Torappu_BuildingData_TrainingPhase"""

    spec_skill_lvl_limit: int = 0


class BuildingDataTrainingBean(GameDataModel):
    """clz_Torappu_BuildingData_TrainingBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataTrainingPhase] | None = None


class BuildingDataPowerPhase(GameDataModel):
    """clz_Torappu_BuildingData_PowerPhase"""

    pass


class BuildingDataPowerRoomBean(GameDataModel):
    """clz_Torappu_BuildingData_PowerRoomBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataPowerPhase] | None = None


class BuildingDataRecyclePhase(GameDataModel):
    """clz_Torappu_BuildingData_RecyclePhase"""

    recycle_capacity: int = 0
    recycle_speed: float = 0.0


class BuildingDataRecycleBean(GameDataModel):
    """clz_Torappu_BuildingData_RecycleBean"""

    basic_speed_buff: float = 0.0
    phases: list[BuildingDataRecyclePhase] | None = None


class CharacterDataUnlockCondition(GameDataModel):
    """clz_Torappu_CharacterData_UnlockCondition"""

    phase: str = "PHASE_0"
    level: int = 0


class BuildingDataBuildingBuffCharSlotSlotItem(GameDataModel):
    """clz_Torappu_BuildingData_BuildingBuffCharSlot_SlotItem"""

    buff_id: str | None = None
    cond: CharacterDataUnlockCondition | None = None


class BuildingDataBuildingBuffCharSlot(GameDataModel):
    """clz_Torappu_BuildingData_BuildingBuffCharSlot"""

    buff_data: list[BuildingDataBuildingBuffCharSlotSlotItem] | None = None


class BuildingDataBuildingCharacter(GameDataModel):
    """clz_Torappu_BuildingData_BuildingCharacter"""

    char_id: str | None = None
    max_manpower: int = 0
    buff_char: list[BuildingDataBuildingBuffCharSlot] | None = None


class BuildingDataBuildingBuff(GameDataModel):
    """clz_Torappu_BuildingData_BuildingBuff"""

    buff_id: str | None = None
    buff_name: str | None = None
    buff_icon: str | None = None
    skill_icon: str | None = None
    sort_id: int = 0
    buff_color: str | None = None
    text_color: str | None = None
    buff_category: str = "NONE"
    room_type: str = "NONE"
    description: str | None = None
    efficiency: int = 0
    target_group_sort_id: int = 0
    targets: list[str] | None = None


class BuildingDataWorkshopExtraWeightItem(GameDataModel):
    """clz_Torappu_BuildingData_WorkshopExtraWeightItem"""

    weight: int = 0
    item_id: str | None = None
    item_count: int = 0


class BuildingDataCustomDataFurnitureData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_FurnitureData"""

    id: str | None = None
    sort_id: int = 0
    name: str | None = None
    icon_id: str | None = None
    interact_type: str = "NONE"
    music_id: str | None = None
    type: str = "FLOOR"
    sub_type: str = "NONE"
    location: str = "NONE"
    category: str = "FURNITURE"
    valid_on_rotate: bool = False
    enable_rotate: bool = False
    rarity: int = 0
    theme_id: str | None = None
    group_id: str | None = None
    width: int = 0
    depth: int = 0
    height: int = 0
    comfort: int = 0
    usage: str | None = None
    description: str | None = None
    obtain_approach: str | None = None
    processed_product_id: str | None = None
    processed_product_count: int = 0
    processed_by_product_percentage: int = 0
    processed_by_product_group: list[BuildingDataWorkshopExtraWeightItem] | None = None
    can_be_destroy: bool = False
    is_only: int = 0
    enable_room_type: int = 0
    quantity: int = 0


class BuildingDataCustomDataThemeQuickSetupItem(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_ThemeQuickSetupItem"""

    furniture_id: str | None = None
    pos_0: int = 0
    pos_1: int = 0
    dir: int = 0


class BuildingDataCustomDataThemeData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_ThemeData"""

    id: str | None = None
    enable_room_type: int = 0
    sort_id: int = 0
    name: str | None = None
    theme_type: str | None = None
    desc: str | None = None
    quick_setup: list[BuildingDataCustomDataThemeQuickSetupItem] | None = None
    groups: list[str] | None = None
    furnitures: list[str] | None = None


class BuildingDataCustomDataGroupData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_GroupData"""

    id: str | None = None
    sort_id: int = 0
    name: str | None = None
    theme_id: str | None = None
    comfort: int = 0
    count: int = 0
    furniture: list[str] | None = None


class BuildingDataCustomDataFurnitureTypeData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_FurnitureTypeData"""

    type: str = "FLOOR"
    name: str | None = None
    enable_room_type: int = 0


class BuildingDataCustomDataFurnitureSubTypeData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_FurnitureSubTypeData"""

    sub_type: str = "NONE"
    name: str | None = None
    type: str = "FLOOR"
    sort_id: int = 0
    count_limit: int = 0
    enable_room_type: int = 0


class BuildingDataCustomDataDormitoryDefaultFurnitureItem(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_DormitoryDefaultFurnitureItem"""

    furniture_id: str | None = None
    x_offset: int = 0
    y_offset: int = 0
    default_prefab_id: str | None = None


class BuildingDataCustomDataInteractItem(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_InteractItem"""

    skin_id: str | None = None


class BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_DiyUISortTemplateListData_DiyUISortTemplateData"""

    name: str | None = None
    sequences: list[str] | None = None
    stable_sequence: str | None = None
    stable_sequence_order: str = "DESC"


class BuildingDataCustomDataDiyUISortTemplateListData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData_DiyUISortTemplateListData"""

    diy_sort_type: str = "NONE"
    expand_state: str | None = None
    default_template_index: int = 0
    default_template_order: str = "DESC"
    templates: list[BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData] | None = None


class BuildingDataCustomData(GameDataModel):
    """clz_Torappu_BuildingData_CustomData"""

    furnitures: dict[str, BuildingDataCustomDataFurnitureData] | None = None
    themes: dict[str, BuildingDataCustomDataThemeData] | None = None
    groups: dict[str, BuildingDataCustomDataGroupData] | None = None
    types: dict[str, BuildingDataCustomDataFurnitureTypeData] | None = None
    sub_types: dict[str, BuildingDataCustomDataFurnitureSubTypeData] | None = None
    default_furnitures: dict[str, list[BuildingDataCustomDataDormitoryDefaultFurnitureItem]] | None = None
    interact_groups: dict[str, list[BuildingDataCustomDataInteractItem]] | None = None
    diy_ui_sort_templates: dict[str, dict[str, BuildingDataCustomDataDiyUISortTemplateListData]] | None = Field(default=None, alias="diyUISortTemplates")


class BuildingDataManufactFormulaUnlockRoom(GameDataModel):
    """clz_Torappu_BuildingData_ManufactFormula_UnlockRoom"""

    room_id: str = "NONE"
    room_level: int = 0
    room_count: int = 0


class BuildingDataManufactFormulaUnlockStage(GameDataModel):
    """clz_Torappu_BuildingData_ManufactFormula_UnlockStage"""

    stage_id: str | None = None
    rank: int = 0


class BuildingDataManufactFormula(GameDataModel):
    """clz_Torappu_BuildingData_ManufactFormula"""

    formula_id: str | None = None
    item_id: str | None = None
    count: int = 0
    weight: int = 0
    cost_point: int = 0
    formula_type: str = "NONE"
    buff_type: str | None = None
    costs: list[ItemBundle] | None = None
    require_rooms: list[BuildingDataManufactFormulaUnlockRoom] | None = None
    require_stages: list[BuildingDataManufactFormulaUnlockStage] | None = None


class BuildingDataShopFormulaUnlockRoom(GameDataModel):
    """clz_Torappu_BuildingData_ShopFormula_UnlockRoom"""

    room_id: str = "NONE"
    room_level: int = 0


class BuildingDataShopFormula(GameDataModel):
    """clz_Torappu_BuildingData_ShopFormula"""

    formula_id: str | None = None
    item_id: str | None = None
    formula_type: str = "NONE"
    cost_point: int = 0
    gain_item: ItemBundle | None = None
    require_rooms: list[BuildingDataShopFormulaUnlockRoom] | None = None


class BuildingDataWorkshopFormulaUnlockRoom(GameDataModel):
    """clz_Torappu_BuildingData_WorkshopFormula_UnlockRoom"""

    room_id: str = "NONE"
    room_level: int = 0
    room_count: int = 0


class BuildingDataWorkshopFormulaUnlockStage(GameDataModel):
    """clz_Torappu_BuildingData_WorkshopFormula_UnlockStage"""

    stage_id: str | None = None
    rank: int = 0


class BuildingDataWorkshopFormula(GameDataModel):
    """clz_Torappu_BuildingData_WorkshopFormula"""

    sort_id: int = 0
    formula_id: str | None = None
    rarity: int = 0
    item_id: str | None = None
    count: int = 0
    gold_cost: int = 0
    ap_cost: int = 0
    formula_type: str = "NONE"
    buff_type: str | None = None
    extra_outcome_rate: float = 0.0
    extra_outcome_group: list[BuildingDataWorkshopExtraWeightItem] | None = None
    costs: list[ItemBundle] | None = None
    require_rooms: list[BuildingDataWorkshopFormulaUnlockRoom] | None = None
    require_stages: list[BuildingDataWorkshopFormulaUnlockStage] | None = None


class BuildingDataCreditFormulaValueModel(GameDataModel):
    """clz_Torappu_BuildingData_CreditFormula_ValueModel"""

    basic: int = 0
    addition: int = 0


class BuildingDataCreditFormula(GameDataModel):
    """clz_Torappu_BuildingData_CreditFormula"""

    initiative: dict[int, BuildingDataCreditFormulaValueModel] | None = None
    passive: dict[int, BuildingDataCreditFormulaValueModel] | None = None


class BuildingDataWorkshopRarityInfo(GameDataModel):
    """clz_Torappu_BuildingData_WorkshopRarityInfo"""

    name: str | None = None
    order: int = 0
    rarity_list: list[str] | None = None
    color: str | None = None


class BuildingDataSlotPrequeData(GameDataModel):
    """clz_Torappu_BuildingData_SlotPrequeData"""

    room_type: str = "NONE"
    name: str | None = None
    type_sort_id: int = 0
    is_preque: bool = False
    preque_num: int = 0


class BuildingDataDormitoryPrequeData(GameDataModel):
    """clz_Torappu_BuildingData_DormitoryPrequeData"""

    room_type: str = "NONE"
    name: str | None = None


class BuildingDataStationManageConstData(GameDataModel):
    """clz_Torappu_BuildingData_StationManageConstData"""

    cant_work_toast_no_tired_char: str | None = None
    cant_work_toast_no_avail_queue: str | None = None
    cant_work_toast_no_need: str | None = None
    cant_rest_toast_no_tired_char: str | None = None
    cant_rest_toast_no_avail_dorm: str | None = None
    work_batch_toast: str | None = None
    rest_batch_toast: str | None = None
    room_no_avail_queue_toast: str | None = None
    cant_use_no_person: str | None = None
    cant_use_working: str | None = None
    queue_cleared: str | None = None
    update_time: int = 0
    dorm_lock_update_time: int = 0


class BuildingDataStationManageFilterInfo(GameDataModel):
    """clz_Torappu_BuildingData_StationManageFilterInfo"""

    char_station_filter_type: str = "All"
    name: str | None = None


class BuildingDataMusicSingleData(GameDataModel):
    """clz_Torappu_BuildingData_MusicSingleData"""

    bgm_id: str | None = None
    bgm_sort_id: int = 0
    bgm_start_time: int = 0
    bgm_name: str | None = None
    game_music_id: str | None = None
    obtain_approach: str | None = None
    bgm_desc_unlocked: str | None = None
    unlock_type: str | None = None
    unlock_params: list[str] | None = None


class BuildingDataMusicData(GameDataModel):
    """clz_Torappu_BuildingData_MusicData"""

    default_music: str | None = None
    music_datas: dict[str, BuildingDataMusicSingleData] | None = None


class BuildingDataBuildingRoomTypeBuffSortDataBuffGroupInfo(GameDataModel):
    """clz_Torappu_BuildingData_BuildingRoomTypeBuffSortData_buffGroupInfo"""

    targets: list[str] | None = None
    sort_id: int = 0


class BuildingDataBuildingRoomTypeBuffSortData(GameDataModel):
    """clz_Torappu_BuildingData_BuildingRoomTypeBuffSortData"""

    has_efficiency_sort: bool = False
    default_group_sort_id: int = 0
    efficiency_target_dict: dict[str, BuildingDataBuildingRoomTypeBuffSortDataBuffGroupInfo] | None = None


class BuildingDataTradingRoomSpecialOrderInfo(GameDataModel):
    """clz_Torappu_BuildingData_TradingRoomSpecialOrderInfo"""

    char_id: str | None = None
    icon_id: str | None = None
    title: str | None = None


class BuildingDataTradingRoomInfoData(GameDataModel):
    """clz_Torappu_BuildingData_TradingRoomInfoData"""

    trading_room_special_order_data: dict[str, BuildingDataTradingRoomSpecialOrderInfo] | None = None


class BuildingDataRecycleRoomOutputPoolData(GameDataModel):
    """clz_Torappu_BuildingData_RecycleRoomOutputPoolData"""

    item_pool_id: str | None = None
    item_pool_start_time: int = 0
    item_pool_end_time: int = 0
    extra_pool_id: str | None = None
    extra_pool_requirement: int = 0


class BuildingDataRecycleRoomOutputPoolItemData(GameDataModel):
    """clz_Torappu_BuildingData_RecycleRoomOutputPoolItemData"""

    item_id: str | None = None
    target_tags: list[str] | None = None
    weight: int = 0
    count: int = 0
    extra_pool_value_change: int = 0
    is_new: bool = False


class BuildingDataRecycleRoomOutputPoolContentData(GameDataModel):
    """clz_Torappu_BuildingData_RecycleRoomOutputPoolContentData"""

    items: list[BuildingDataRecycleRoomOutputPoolItemData] | None = None


class BuildingDataRecycleRoomInputItemData(GameDataModel):
    """clz_Torappu_BuildingData_RecycleRoomInputItemData"""

    item_id: str | None = None
    added_time: int = 0


class BuildingDataRecycleRoomConsts(GameDataModel):
    """clz_Torappu_BuildingData_RecycleRoomConsts"""

    recycle_time_requirement: int = 0
    recycle_base_capacity: int = 0
    recycle_boost_speed: float = 0.0
    recycle_boost_limit: int = 0
    recycle_boost_limit_protect: int = 0
    recycle_speed_up_unlock_level: int = 0
    recycle_two_person_unlock_level: int = 0


class BuildingData(GameDataModel):
    """clz_Torappu_BuildingData"""

    control_slot_id: str | None = None
    meeting_slot_id: str | None = None
    init_max_labor: int = 0
    labor_recover_time: int = 0
    manufact_input_capacity: int = 0
    shop_counter_capacity: int = 0
    comfort_limit: int = 0
    credit_initiative_limit: int = 0
    credit_passive_limit: int = 0
    credit_comfort_factor: int = 0
    credit_guaranteed: int = 0
    credit_ceiling: int = 0
    manufact_unlock_tips: str | None = None
    shop_unlock_tips: str | None = None
    manufact_station_buff: float = 0.0
    comfort_manpower_recover_factor: int = 0
    manpower_display_factor: int = 0
    shop_output_ratio: dict[str, int] | None = None
    shop_stack_ratio: dict[str, int] | None = None
    basic_favor_per_day: int = 0
    human_resource_limit: int = 0
    tired_ap_threshold: int = 0
    processed_count_ratio: int = 0
    trading_strategy_unlock_level: int = 0
    trading_reduce_time_unit: int = 0
    trading_labor_cost_unit: int = 0
    manufact_reduce_time_unit: int = 0
    manufact_labor_cost_unit: int = 0
    labor_assist_unlock_level: int = 0
    ap_to_labor_unlock_level: int = 0
    ap_to_labor_ratio: int = 0
    social_resource_limit: int = 0
    social_slot_num: int = 0
    furni_duplication_limit: int = 0
    assist_favor_report: int = 0
    manufact_manpower_cost_by_num: list[int] | None = None
    trading_manpower_cost_by_num: list[int] | None = None
    training_bonus_max: int = 0
    beta_remove_time: int = 0
    furni_highlight_time: float = 0.0
    can_not_visit_toast: str | None = None
    meeting_message_board_emote_time: int = 0
    music_player_open_time: int = 0
    rooms_without_remove_staff: list[str] | None = None
    private_favor_level_thresholds: list[int] | None = None
    room_unlock_conds: dict[str, BuildingDataRoomUnlockCond] | None = None
    rooms: dict[str, BuildingDataRoomData] | None = None
    layouts: dict[str, BuildingDataLayoutData] | None = None
    prefabs: dict[str, BuildingDataPrefabInfo] | None = None
    control_data: BuildingDataControlRoomBean | None = None
    manufact_data: BuildingDataManufactRoomBean | None = None
    shop_data: BuildingDataRoomBean1BuildingDataShopPhase | None = None
    hire_data: BuildingDataHireRoomBean | None = None
    dorm_data: BuildingDataRoomBean1BuildingDataDormPhase | None = None
    private_room_data: BuildingDataRoomBean1BuildingDataPrivatePhase | None = None
    meeting_data: BuildingDataMeetingRoomBean | None = None
    trading_data: BuildingDataTradingRoomBean | None = None
    workshop_data: BuildingDataRoomBean1BuildingDataWorkshopPhase | None = None
    training_data: BuildingDataTrainingBean | None = None
    power_data: BuildingDataPowerRoomBean | None = None
    recycle_data: BuildingDataRecycleBean | None = None
    chars: dict[str, BuildingDataBuildingCharacter] | None = None
    buffs: dict[str, BuildingDataBuildingBuff] | None = None
    workshop_bonus: dict[str, list[str]] | None = None
    custom_data: BuildingDataCustomData | None = None
    manufact_formulas: dict[str, BuildingDataManufactFormula] | None = None
    shop_formulas: dict[str, BuildingDataShopFormula] | None = None
    workshop_formulas: dict[str, BuildingDataWorkshopFormula] | None = None
    credit_formula: BuildingDataCreditFormula | None = None
    gold_items: dict[str, int] | None = None
    assistant_unlock: list[int] | None = None
    workshop_rarities: list[BuildingDataWorkshopRarityInfo] | None = None
    todo_item_sort_priority_dict: dict[str, int] | None = None
    slot_preque_datas: dict[str, BuildingDataSlotPrequeData] | None = None
    dormitory_preque_datas: dict[str, BuildingDataDormitoryPrequeData] | None = None
    workshop_target_des_dict: dict[str, str] | None = None
    trading_order_des_dict: dict[str, str] | None = None
    station_manage_const_data: BuildingDataStationManageConstData | None = None
    station_manage_filter_infos: dict[int, BuildingDataStationManageFilterInfo] | None = None
    music_data: BuildingDataMusicData | None = None
    emojis: list[str] | None = None
    category_names: dict[str, str] | None = None
    buff_sort_data: dict[str, BuildingDataBuildingRoomTypeBuffSortData] | None = None
    trading_room_info_data: BuildingDataTradingRoomInfoData | None = None
    recycle_room_output_pool_datas: dict[str, BuildingDataRecycleRoomOutputPoolData] | None = None
    recycle_room_output_pool_content_datas: dict[str, BuildingDataRecycleRoomOutputPoolContentData] | None = None
    recycle_room_input_item_datas: dict[str, BuildingDataRecycleRoomInputItemData] | None = None
    recycle_room_consts: BuildingDataRecycleRoomConsts | None = None


# root_type clz_Torappu_BuildingData


BuildingDataRoomUnlockCondCondItem.model_rebuild()
BuildingDataRoomUnlockCond.model_rebuild()
GridPosition.model_rebuild()
ItemBundle.model_rebuild()
BuildingDataRoomDataBuildCost.model_rebuild()
BuildingDataRoomDataPhaseData.model_rebuild()
BuildingDataRoomData.model_rebuild()
BuildingDataLayoutDataRoomSlot.model_rebuild()
BuildingDataLayoutDataSlotCleanCostCountCost.model_rebuild()
BuildingDataLayoutDataSlotCleanCost.model_rebuild()
BuildingDataLayoutDataStoreyData.model_rebuild()
BuildingDataLayoutData.model_rebuild()
BuildingDataPrefabInfo.model_rebuild()
BuildingDataControlRoomPhase.model_rebuild()
BuildingDataControlRoomBean.model_rebuild()
BuildingDataManufactPhase.model_rebuild()
BuildingDataManufactRoomBean.model_rebuild()
BuildingDataShopPhase.model_rebuild()
BuildingDataRoomBean1BuildingDataShopPhase.model_rebuild()
BuildingDataHirePhase.model_rebuild()
BuildingDataHireRoomBean.model_rebuild()
BuildingDataDormPhase.model_rebuild()
BuildingDataRoomBean1BuildingDataDormPhase.model_rebuild()
BuildingDataPrivatePhase.model_rebuild()
BuildingDataRoomBean1BuildingDataPrivatePhase.model_rebuild()
BuildingDataMeetingPhase.model_rebuild()
BuildingDataMeetingRoomBean.model_rebuild()
BuildingDataTradingPhase.model_rebuild()
BuildingDataTradingRoomBean.model_rebuild()
BuildingDataWorkshopPhase.model_rebuild()
BuildingDataRoomBean1BuildingDataWorkshopPhase.model_rebuild()
BuildingDataTrainingPhase.model_rebuild()
BuildingDataTrainingBean.model_rebuild()
BuildingDataPowerPhase.model_rebuild()
BuildingDataPowerRoomBean.model_rebuild()
BuildingDataRecyclePhase.model_rebuild()
BuildingDataRecycleBean.model_rebuild()
CharacterDataUnlockCondition.model_rebuild()
BuildingDataBuildingBuffCharSlotSlotItem.model_rebuild()
BuildingDataBuildingBuffCharSlot.model_rebuild()
BuildingDataBuildingCharacter.model_rebuild()
BuildingDataBuildingBuff.model_rebuild()
BuildingDataWorkshopExtraWeightItem.model_rebuild()
BuildingDataCustomDataFurnitureData.model_rebuild()
BuildingDataCustomDataThemeQuickSetupItem.model_rebuild()
BuildingDataCustomDataThemeData.model_rebuild()
BuildingDataCustomDataGroupData.model_rebuild()
BuildingDataCustomDataFurnitureTypeData.model_rebuild()
BuildingDataCustomDataFurnitureSubTypeData.model_rebuild()
BuildingDataCustomDataDormitoryDefaultFurnitureItem.model_rebuild()
BuildingDataCustomDataInteractItem.model_rebuild()
BuildingDataCustomDataDiyUISortTemplateListDataDiyUISortTemplateData.model_rebuild()
BuildingDataCustomDataDiyUISortTemplateListData.model_rebuild()
BuildingDataCustomData.model_rebuild()
BuildingDataManufactFormulaUnlockRoom.model_rebuild()
BuildingDataManufactFormulaUnlockStage.model_rebuild()
BuildingDataManufactFormula.model_rebuild()
BuildingDataShopFormulaUnlockRoom.model_rebuild()
BuildingDataShopFormula.model_rebuild()
BuildingDataWorkshopFormulaUnlockRoom.model_rebuild()
BuildingDataWorkshopFormulaUnlockStage.model_rebuild()
BuildingDataWorkshopFormula.model_rebuild()
BuildingDataCreditFormulaValueModel.model_rebuild()
BuildingDataCreditFormula.model_rebuild()
BuildingDataWorkshopRarityInfo.model_rebuild()
BuildingDataSlotPrequeData.model_rebuild()
BuildingDataDormitoryPrequeData.model_rebuild()
BuildingDataStationManageConstData.model_rebuild()
BuildingDataStationManageFilterInfo.model_rebuild()
BuildingDataMusicSingleData.model_rebuild()
BuildingDataMusicData.model_rebuild()
BuildingDataBuildingRoomTypeBuffSortDataBuffGroupInfo.model_rebuild()
BuildingDataBuildingRoomTypeBuffSortData.model_rebuild()
BuildingDataTradingRoomSpecialOrderInfo.model_rebuild()
BuildingDataTradingRoomInfoData.model_rebuild()
BuildingDataRecycleRoomOutputPoolData.model_rebuild()
BuildingDataRecycleRoomOutputPoolItemData.model_rebuild()
BuildingDataRecycleRoomOutputPoolContentData.model_rebuild()
BuildingDataRecycleRoomInputItemData.model_rebuild()
BuildingDataRecycleRoomConsts.model_rebuild()
BuildingData.model_rebuild()

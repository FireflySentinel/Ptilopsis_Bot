"""item_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/item_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class ItemRarity(IntEnum):
    """enum__Torappu_ItemRarity"""

    TIER_1 = 0
    TIER_2 = 1
    TIER_3 = 2
    TIER_4 = 3
    TIER_5 = 4
    TIER_6 = 5
    E_NUM = 6


class ItemReslockStatus(IntEnum):
    """enum__Torappu_ItemReslockStatus"""

    NOT_SUPPORT_RESLOCK = 0
    MAT_GACHA_RESLOCK_BLACKLIST = 1
    CHAR_POTENTIAL_BLACKLIST = 2
    COMMON_BLACKLIST = 999
    CAN_RESLOCK = 1000


class ItemClassifyType(IntEnum):
    """enum__Torappu_ItemClassifyType"""

    NONE = 0
    CONSUME = 1
    NORMAL = 2
    MATERIAL = 3
    MEMENTO = 4


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


class OccPer(IntEnum):
    """enum__Torappu_OccPer"""

    ALWAYS = 0
    ALMOST = 1
    USUAL = 2
    OFTEN = 3
    SOMETIMES = 4
    NEVER = 5
    DEFINITELY_BUFF = 6


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


class ItemDropShopType(IntEnum):
    """enum__Torappu_ItemDropShopType"""

    HGGSHD_SHOP = 0
    LGGSHD_SHOP = 1
    XSHD_SHOP = 2
    EPGS_SHOP = 3
    REP_SHOP = 4
    CLASSIC_SHOP = 5


class VoucherDisplayType(IntEnum):
    """enum__Torappu_VoucherDisplayType"""

    NONE = 0
    DIVIDE = 1


class ItemDataStageDropInfo(GameDataModel):
    """clz_Torappu_ItemData_StageDropInfo"""

    stage_id: str | None = None
    occ_per: str = "ALWAYS"
    sort_id: int = 0


class ItemDataBuildingProductInfo(GameDataModel):
    """clz_Torappu_ItemData_BuildingProductInfo"""

    room_type: str = "NONE"
    formula_id: str | None = None


class ItemDataVoucherRelateInfo(GameDataModel):
    """clz_Torappu_ItemData_VoucherRelateInfo"""

    voucher_id: str | None = None
    voucher_item_type: str = "NONE"


class ItemDataShopRelateInfo(GameDataModel):
    """clz_Torappu_ItemData_ShopRelateInfo"""

    shop_type: str = "HGGSHD_SHOP"
    shop_group: int = 0
    start_ts: int = 0


class ItemData(GameDataModel):
    """clz_Torappu_ItemData"""

    item_id: str | None = None
    name: str | None = None
    description: str | None = None
    rarity: str = "TIER_1"
    icon_id: str | None = None
    override_bkg: str | None = None
    stack_icon_id: str | None = None
    sort_id: int = 0
    usage: str | None = None
    obtain_approach: str | None = None
    hide_in_item_get: bool = False
    reslock_status: str = "NOT_SUPPORT_RESLOCK"
    can_reslock: bool = False
    classify_type: str = "NONE"
    item_type: str = "NONE"
    stage_drop_list: list[ItemDataStageDropInfo] | None = None
    building_product_list: list[ItemDataBuildingProductInfo] | None = None
    voucher_relate_list: list[ItemDataVoucherRelateInfo] | None = None
    shop_relate_info_list: list[ItemDataShopRelateInfo] | None = None


class ExpItemFeature(GameDataModel):
    """clz_Torappu_ExpItemFeature"""

    id: str | None = None
    gain_exp: int = 0


class ApSupplyFeature(GameDataModel):
    """clz_Torappu_ApSupplyFeature"""

    id: str | None = None
    ap: int = 0
    has_ts: bool = False


class CharVoucherItemFeature(GameDataModel):
    """clz_Torappu_CharVoucherItemFeature"""

    id: str | None = None
    display_type: str = "NONE"


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class UniCollectionInfo(GameDataModel):
    """clz_Torappu_UniCollectionInfo"""

    uni_collection_item_id: str | None = None
    unique_item: list[ItemBundle] | None = None


class ItemPackInfo(GameDataModel):
    """clz_Torappu_ItemPackInfo"""

    pack_id: str | None = None
    content: list[ItemBundle] | None = None


class FullPotentialCharacterInfo(GameDataModel):
    """clz_Torappu_FullPotentialCharacterInfo"""

    item_id: str | None = None
    ts: int = 0


class ActivityPotentialCharacterInfo(GameDataModel):
    """clz_Torappu_ActivityPotentialCharacterInfo"""

    char_id: str | None = None


class FavorCharacterInfo(GameDataModel):
    """clz_Torappu_FavorCharacterInfo"""

    item_id: str | None = None
    char_id: str | None = None
    favor_add_amt: int = 0


class InventoryData(GameDataModel):
    """clz_Torappu_InventoryData"""

    items: dict[str, ItemData] | None = None
    exp_items: dict[str, ExpItemFeature] | None = None
    potential_items: dict[int, dict[str, str]] | None = None
    ap_supplies: dict[str, ApSupplyFeature] | None = None
    char_voucher_items: dict[str, CharVoucherItemFeature] | None = None
    unique_info: dict[str, int] | None = None
    item_time_limit: dict[str, int] | None = None
    uni_collection_info: dict[str, UniCollectionInfo] | None = None
    item_pack_infos: dict[str, ItemPackInfo] | None = None
    full_potential_characters: dict[str, FullPotentialCharacterInfo] | None = None
    activity_potential_characters: dict[str, ActivityPotentialCharacterInfo] | None = None
    favor_characters: dict[str, FavorCharacterInfo] | None = None
    item_shop_name_dict: dict[str, str] | None = None


# root_type clz_Torappu_InventoryData
ItemTable = InventoryData


ItemDataStageDropInfo.model_rebuild()
ItemDataBuildingProductInfo.model_rebuild()
ItemDataVoucherRelateInfo.model_rebuild()
ItemDataShopRelateInfo.model_rebuild()
ItemData.model_rebuild()
ExpItemFeature.model_rebuild()
ApSupplyFeature.model_rebuild()
CharVoucherItemFeature.model_rebuild()
ItemBundle.model_rebuild()
UniCollectionInfo.model_rebuild()
ItemPackInfo.model_rebuild()
FullPotentialCharacterInfo.model_rebuild()
ActivityPotentialCharacterInfo.model_rebuild()
FavorCharacterInfo.model_rebuild()
InventoryData.model_rebuild()

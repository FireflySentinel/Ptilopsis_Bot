"""medal_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/medal_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class MedalRarity(IntEnum):
    """enum__Torappu_MedalRarity"""

    T1 = 0
    T1D5 = 1
    T2 = 2
    T2D5 = 3
    T3 = 4
    T3D5 = 5


class MedalExpireType(IntEnum):
    """enum__Torappu_MedalExpireType"""

    NONE = 0
    INIT = 1
    TEMP = 2
    PERM = 3


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


class MedalExpireTime(GameDataModel):
    """clz_Torappu_MedalExpireTime"""

    start: int = 0
    end: int = 0
    type: str = "NONE"


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class MedalRewardGroupData(GameDataModel):
    """clz_Torappu_MedalRewardGroupData"""

    group_id: str | None = None
    slot_id: int = 0
    item_list: list[ItemBundle] | None = None


class MedalPerData(GameDataModel):
    """clz_Torappu_MedalPerData"""

    medal_id: str | None = None
    medal_name: str | None = None
    medal_type: str | None = None
    slot_id: int = 0
    pre_medal_id_list: list[str] | None = None
    rarity: str = "T1"
    template: str | None = None
    unlock_param: list[str] | None = None
    get_method: str | None = None
    description: str | None = None
    advanced_medal: str | None = None
    origin_medal: str | None = None
    display_time: int = 0
    expire_times: list[MedalExpireTime] | None = None
    medal_reward_group: list[MedalRewardGroupData] | None = None
    is_hidden: bool = False


class MedalGroupData(GameDataModel):
    """clz_Torappu_MedalGroupData"""

    group_id: str | None = None
    group_name: str | None = None
    group_desc: str | None = None
    medal_id: list[str] | None = None
    sort_id: int = 0
    group_back_color: str | None = None
    group_get_time: int = 0
    shared_expire_times: list[MedalExpireTime] | None = None


class MedalTypeData(GameDataModel):
    """clz_Torappu_MedalTypeData"""

    medal_group_id: str | None = None
    sort_id: int = 0
    medal_name: str | None = None
    group_data: list[MedalGroupData] | None = None


class MedalData(GameDataModel):
    """clz_Torappu_MedalData"""

    medal_list: list[MedalPerData] | None = None
    medal_type_data: dict[str, MedalTypeData] | None = None


# root_type clz_Torappu_MedalData
MedalTable = MedalData


MedalExpireTime.model_rebuild()
ItemBundle.model_rebuild()
MedalRewardGroupData.model_rebuild()
MedalPerData.model_rebuild()
MedalGroupData.model_rebuild()
MedalTypeData.model_rebuild()
MedalData.model_rebuild()

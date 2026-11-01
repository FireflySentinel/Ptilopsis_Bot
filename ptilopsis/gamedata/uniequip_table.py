"""uniequip_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/uniequip_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from ptilopsis.gamedata._base import GameDataModel


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


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


class UniEquipType(IntEnum):
    """enum__Torappu_UniEquipType"""

    INITIAL = 0
    ADVANCED = 1


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class UniEquipData(GameDataModel):
    """clz_Torappu_UniEquipData"""

    uni_equip_id: str | None = None
    uni_equip_name: str | None = None
    uni_equip_icon: str | None = None
    uni_equip_desc: str | None = None
    type_icon: str | None = None
    type_name_1: str | None = None
    type_name_2: str | None = None
    equip_shining_color: str | None = None
    show_evolve_phase: str = "PHASE_0"
    unlock_evolve_phase: str = "PHASE_0"
    char_id: str | None = None
    tmpl_id: str | None = None
    show_level: int = 0
    unlock_level: int = 0
    mission_list: list[str] | None = None
    unlock_favors: dict[str, int] | None = None
    item_cost: dict[int, list[ItemBundle]] | None = None
    type: str = "INITIAL"
    uni_equip_get_time: int = 0
    uni_equip_show_end: int = 0
    char_equip_order: int = 0
    has_unlock_mission: bool = False
    is_special_equip: bool = False
    special_equip_desc: str | None = None
    special_equip_color: str | None = None
    char_color: str | None = None


class UniEquipMissionData(GameDataModel):
    """clz_Torappu_UniEquipMissionData"""

    template: str | None = None
    desc: str | None = None
    param_list: list[str] | None = None
    uni_equip_mission_id: str | None = None
    uni_equip_mission_sort: int = 0
    uni_equip_id: str | None = None
    jump_stage_id: str | None = None


class SubProfessionData(GameDataModel):
    """clz_Torappu_SubProfessionData"""

    sub_profession_id: str | None = None
    sub_profession_name: str | None = None
    sub_profession_catagory: int = 0


class UniEquipTypeInfo(GameDataModel):
    """clz_Torappu_UniEquipTypeInfo"""

    uni_equip_type_name: str | None = None
    sort_id: int = 0
    is_special: bool = False
    is_initial: bool = False


class UniEquipTrack(GameDataModel):
    """clz_Torappu_UniEquipTrack"""

    char_id: str | None = None
    equip_id: str | None = None
    type: str = "INITIAL"
    archive_show_time_end: int = 0


class UniEquipTimeInfo(GameDataModel):
    """clz_Torappu_UniEquipTimeInfo"""

    time_stamp: int = 0
    track_list: list[UniEquipTrack] | None = None


class UniEquipTable(GameDataModel):
    """clz_Torappu_UniEquipTable"""

    equip_dict: dict[str, UniEquipData] | None = None
    mission_list: dict[str, UniEquipMissionData] | None = None
    sub_prof_dict: dict[str, SubProfessionData] | None = None
    sub_prof_to_prof_dict: dict[str, int] | None = None
    char_equip: dict[str, list[str]] | None = None
    equip_type_infos: list[UniEquipTypeInfo] | None = None
    equip_track_dict: list[UniEquipTimeInfo] | None = None


# root_type clz_Torappu_UniEquipTable
UniequipTable = UniEquipTable


ItemBundle.model_rebuild()
UniEquipData.model_rebuild()
UniEquipMissionData.model_rebuild()
SubProfessionData.model_rebuild()
UniEquipTypeInfo.model_rebuild()
UniEquipTrack.model_rebuild()
UniEquipTimeInfo.model_rebuild()
UniEquipTable.model_rebuild()

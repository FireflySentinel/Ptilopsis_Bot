"""char_patch_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/char_patch_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class SpecialOperatorTargetType(IntEnum):
    """enum__Torappu_SpecialOperatorTargetType"""

    NONE = 0
    ROGUE = 1


class BuildableType(IntEnum):
    """enum__Torappu_BuildableType"""

    NONE = 0
    MELEE = 1
    RANGED = 2
    ALL = 3


class RarityRank(IntEnum):
    """enum__Torappu_RarityRank"""

    TIER_1 = 0
    TIER_2 = 1
    TIER_3 = 2
    TIER_4 = 3
    TIER_5 = 4
    TIER_6 = 5
    E_NUM = 6


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


class CharacterDataPotentialRankTypeEnum(IntEnum):
    """enum__Torappu_CharacterData_PotentialRank_TypeEnum"""

    BUFF = 0
    CUSTOM = 1


class AbnormalFlag(IntEnum):
    """enum__Torappu_AbnormalFlag"""

    STUNNED = 0
    SP_RECOVER_STOPPED = 1
    TARGET_FREE = 2
    BLOCK_FREE = 3
    HIDDEN = 4
    INVINCIBLE = 5
    UNDEADABLE = 6
    HEAL_FREE = 7
    UNBALANCE_IMMUNE = 8
    INVISIBLE = 9
    UNUSED_PLACEHOLDER_2 = 14
    ALLY_TARGET_FREE = 15
    UNUSED_PLACEHOLDER_1 = 10
    DISARMED = 11
    SILENCED = 12
    UNMOVABLE = 13
    FROZEN = 16
    CAMOUFLAGE = 17
    FORCE_DISARMED = 18
    STUNNED_NO_AMPLIFY_DAMAGE = 19
    DISABLE_COMBAT = 20
    ELEMENT_FREE_ALL = 21
    UNMOVABLE_PRIVATE = 22
    COLD = 23
    SKILL_NOT_ACTIVATABLE = 24
    LEVITATE = 25
    DURANCE = 26
    NOT_WITHDRAWABLE = 27
    OUT_OF_GROUND = 28
    SP_MODIFY_STOPPED = 29
    ANTI_STATUS_RESISTABLE = 30
    DISARMED_COMBAT = 31
    TOWER_TARGET_FREE = 32
    FEARED = 33
    SKILL_ACTIVABLE_IN_ABNORMAL = 34
    MOTION_TARGET_FREE = 35
    FORCE_LEVITATE = 36
    BUFF_ADD_CAN_BE_CANCELED_IF_DEFENSE = 37
    DEFENSE_BUFF_ADD_IF_CANCELABLE_BUFF = 38
    PALSY = 39
    PALSYING = 40
    ATTRACTED = 41
    FEARED_PRIVATE = 42
    DOZE = 43
    TELEPORTED = 44
    GROUND_BOUND = 45
    E_NUM = 46


class AbnormalCombo(IntEnum):
    """enum__Torappu_AbnormalCombo"""

    SLEEPING = 0
    SHELTERING = 1
    ISOLATE = 2
    E_NUM = 3


class AttributeType(IntEnum):
    """enum__Torappu_AttributeType"""

    MAX_HP = 0
    ATK = 1
    DEF = 2
    MAGIC_RESISTANCE = 3
    COST = 4
    BLOCK_CNT = 5
    MOVE_SPEED = 6
    ATTACK_SPEED = 7
    BASE_ATTACK_TIME = 8
    RESERVED_0 = 9
    RESERVED_1 = 10
    RESERVED_2 = 11
    RESERVED_3 = 12
    HP_RECOVERY_PER_SEC = 13
    SP_RECOVERY_PER_SEC = 14
    ABILITY_RANGE_FORWARD_EXTEND = 15
    MAX_DEPLOY_COUNT = 16
    DEF_PENETRATE = 17
    MAGIC_RESIST_PENETRATE = 18
    HP_RECOVERY_PER_SEC_BY_MAX_HP_RATIO = 19
    TAUNT_LEVEL = 20
    RESPAWN_TIME = 21
    MAX_DECK_STACK_CNT = 22
    MASS_LEVEL = 23
    BASE_FORCE_LEVEL = 24
    DEF_PENETRATE_FIXED = 25
    ONE_MINUS_STATUS_RESISTANCE = 26
    MAGIC_RESIST_PENETRATE_FIXED = 27
    MAX_EP = 28
    EP_RECOVERY_PER_SEC = 29
    SP_RECOVER_RATIO = 30
    EP_DAMAGE_RESISTANCE = 31
    EP_RESISTANCE = 32
    DAMAGE_HITRATE_PHYSICAL = 33
    DAMAGE_HITRATE_MAGICAL = 34
    EP_BREAK_RECOVER_SPEED = 35
    SLOW_DOWN = 36
    BLOCK_RADIUS_SCALE = 37
    E_NUM = 38


class AttributeModifierDataAttributeModifierFormulaItemType(IntEnum):
    """enum__Torappu_AttributeModifierData_AttributeModifier_FormulaItemType"""

    ADDITION = 0
    MULTIPLIER = 1
    FINAL_ADDITION = 2
    FINAL_SCALER = 3


class PlayerBattleRank(IntEnum):
    """enum__Torappu_PlayerBattleRank"""

    FAIL = 1
    PASS = 2
    COMPLETE = 3
    ERR_ZERO = 0


class CharPatchDataPatchInfo(GameDataModel):
    """clz_Torappu_CharPatchData_PatchInfo"""

    tmpl_ids: list[str] | None = None
    default: str | None = None


class CharacterDataPowerData(GameDataModel):
    """clz_Torappu_CharacterData_PowerData"""

    nation_id: str | None = None
    group_id: str | None = None
    team_id: str | None = None


class CharacterDataUnlockCondition(GameDataModel):
    """clz_Torappu_CharacterData_UnlockCondition"""

    phase: str = "PHASE_0"
    level: int = 0


class BlackboardDataPair(GameDataModel):
    """clz_Torappu_Blackboard_DataPair"""

    key: str | None = None
    value: float = 0.0
    value_str: str | None = None


class CharacterDataTraitData(GameDataModel):
    """clz_Torappu_CharacterData_TraitData"""

    unlock_condition: CharacterDataUnlockCondition | None = None
    required_potential_rank: int = 0
    blackboard: list[BlackboardDataPair] | None = None
    override_descripton: str | None = None
    prefab_key: str | None = None
    range_id: str | None = None


class CharacterDataTraitDataBundle(GameDataModel):
    """clz_Torappu_CharacterData_TraitDataBundle"""

    candidates: list[CharacterDataTraitData] | None = None


class AttributesData(GameDataModel):
    """clz_Torappu_AttributesData"""

    max_hp: int = 0
    atk: int = 0
    def_: int = Field(default=0, alias="def")
    magic_resistance: float = 0.0
    cost: int = 0
    block_cnt: int = 0
    move_speed: float = 0.0
    attack_speed: float = 0.0
    base_attack_time: float = 0.0
    respawn_time: int = 0
    hp_recovery_per_sec: float = 0.0
    sp_recovery_per_sec: float = 0.0
    max_deploy_count: int = 0
    max_deck_stack_cnt: int = 0
    taunt_level: int = 0
    mass_level: int = 0
    base_force_level: int = 0
    block_volume: int = 0
    stun_immune: bool = False
    silence_immune: bool = False
    sleep_immune: bool = False
    frozen_immune: bool = False
    levitate_immune: bool = False
    disarmed_combat_immune: bool = False
    feared_immune: bool = False
    palsy_immune: bool = False
    attract_immune: bool = False
    teleport_immune: bool = False
    ground_bound_immune: bool = False


class AttributesKeyFrame(GameDataModel):
    """clz_Torappu_KeyFrames_2_KeyFrame_Torappu_AttributesData_Torappu_AttributesData_"""

    level: int = 0
    data: AttributesData | None = None


class ItemBundle(GameDataModel):
    """clz_Torappu_ItemBundle"""

    id: str | None = None
    count: int = 0
    type: str = "NONE"


class CharacterDataPhaseData(GameDataModel):
    """clz_Torappu_CharacterData_PhaseData"""

    character_prefab_key: str | None = None
    range_id: str | None = None
    max_level: int = 0
    attributes_key_frames: list[AttributesKeyFrame] | None = None
    evolve_cost: list[ItemBundle] | None = None


class CharacterDataMainSkillSpecializeLevelData(GameDataModel):
    """clz_Torappu_CharacterData_MainSkill_SpecializeLevelData"""

    unlock_cond: CharacterDataUnlockCondition | None = None
    lvl_up_time: int = 0
    level_up_cost: list[ItemBundle] | None = None


class CharacterDataMainSkill(GameDataModel):
    """clz_Torappu_CharacterData_MainSkill"""

    skill_id: str | None = None
    override_prefab_key: str | None = None
    override_token_key: str | None = None
    level_up_cost_cond: list[CharacterDataMainSkillSpecializeLevelData] | None = None
    unlock_cond: CharacterDataUnlockCondition | None = None


class TalentData(GameDataModel):
    """clz_Torappu_TalentData"""

    unlock_condition: CharacterDataUnlockCondition | None = None
    required_potential_rank: int = 0
    prefab_key: str | None = None
    name: str | None = None
    description: str | None = None
    range_id: str | None = None
    blackboard: list[BlackboardDataPair] | None = None
    token_key: str | None = None
    is_hide_talent: bool = False


class CharacterDataTalentDataBundle(GameDataModel):
    """clz_Torappu_CharacterData_TalentDataBundle"""

    candidates: list[TalentData] | None = None


class AttributeModifierDataAttributeModifier(GameDataModel):
    """clz_Torappu_AttributeModifierData_AttributeModifier"""

    attribute_type: str = "MAX_HP"
    formula_item: str = "ADDITION"
    value: float = 0.0
    load_from_blackboard: bool = False
    fetch_base_value_from_source_entity: bool = False


class AttributeModifierData(GameDataModel):
    """clz_Torappu_AttributeModifierData"""

    abnormal_flags: list[str] | None = None
    abnormal_immunes: list[str] | None = None
    abnormal_antis: list[str] | None = None
    abnormal_combos: list[str] | None = None
    abnormal_combo_immunes: list[str] | None = None
    attribute_modifiers: list[AttributeModifierDataAttributeModifier] | None = None


class ExternalBuff(GameDataModel):
    """clz_Torappu_ExternalBuff"""

    attributes: AttributeModifierData | None = None


class CharacterDataPotentialRank(GameDataModel):
    """clz_Torappu_CharacterData_PotentialRank"""

    type: str = "BUFF"
    description: str | None = None
    buff: ExternalBuff | None = None
    equivalent_cost: list[ItemBundle] | None = None


class AttributesDeltaData(GameDataModel):
    """clz_Torappu_AttributesDeltaData"""

    max_hp: int = 0
    atk: int = 0
    def_: int = Field(default=0, alias="def")
    magic_resistance: float = 0.0
    cost: int = 0
    block_cnt: int = 0
    move_speed: float = 0.0
    attack_speed: float = 0.0
    base_attack_time: float = 0.0
    respawn_time: int = 0
    hp_recovery_per_sec: float = 0.0
    sp_recovery_per_sec: float = 0.0
    max_deploy_count: int = 0
    max_deck_stack_cnt: int = 0
    taunt_level: int = 0
    mass_level: int = 0
    base_force_level: int = 0
    block_volume: int = 0
    stun_immune: bool = False
    silence_immune: bool = False
    sleep_immune: bool = False
    frozen_immune: bool = False
    levitate_immune: bool = False
    disarmed_combat_immune: bool = False
    feared_immune: bool = False
    palsy_immune: bool = False
    attract_immune: bool = False
    teleport_immune: bool = False
    ground_bound_immune: bool = False


class AttributesDeltaKeyFrame(GameDataModel):
    """clz_Torappu_KeyFrames_2_KeyFrame_Torappu_AttributesDeltaData_Torappu_AttributesData_"""

    level: int = 0
    data: AttributesDeltaData | None = None


class CharacterDataSkillLevelCost(GameDataModel):
    """clz_Torappu_CharacterData_SkillLevelCost"""

    unlock_cond: CharacterDataUnlockCondition | None = None
    lvl_up_cost: list[ItemBundle] | None = None


class CharacterData(GameDataModel):
    """clz_Torappu_CharacterData"""

    name: str | None = None
    description: str | None = None
    sort_index: int = 0
    sp_target_type: str = "NONE"
    sp_target_id: str | None = None
    can_use_general_potential_item: bool = False
    can_use_activity_potential_item: bool = False
    potential_item_id: str | None = None
    activity_potential_item_id: str | None = None
    classic_potential_item_id: str | None = None
    nation_id: str | None = None
    group_id: str | None = None
    team_id: str | None = None
    main_power: CharacterDataPowerData | None = None
    sub_power: list[CharacterDataPowerData] | None = None
    display_number: str | None = None
    appellation: str | None = None
    position: str = "NONE"
    tag_list: list[str] | None = None
    item_usage: str | None = None
    item_desc: str | None = None
    item_obtain_approach: str | None = None
    is_not_obtainable: bool = False
    is_sp_char: bool = False
    max_potential_level: int = 0
    rarity: str = "TIER_1"
    profession: str = "NONE"
    sub_profession_id: str | None = None
    trait: CharacterDataTraitDataBundle | None = None
    phases: list[CharacterDataPhaseData] | None = None
    skills: list[CharacterDataMainSkill] | None = None
    display_token_dict: dict[str, bool] | None = None
    talents: list[CharacterDataTalentDataBundle] | None = None
    potential_ranks: list[CharacterDataPotentialRank] | None = None
    favor_key_frames: list[AttributesDeltaKeyFrame] | None = None
    all_skill_lvlup: list[CharacterDataSkillLevelCost] | None = None


class CharPatchDataUnlockCondItem(GameDataModel):
    """clz_Torappu_CharPatchData_UnlockCond_Item"""

    stage_id: str | None = None
    complete_state: str = "ERR_ZERO"
    unlock_ts: int = 0


class CharPatchDataUnlockCond(GameDataModel):
    """clz_Torappu_CharPatchData_UnlockCond"""

    conds: list[CharPatchDataUnlockCondItem] | None = None


class CharPatchDataPatchDetailInfo(GameDataModel):
    """clz_Torappu_CharPatchData_PatchDetailInfo"""

    patch_id: str | None = None
    sort_id: int = 0
    info_param: str | None = None
    trans_sort_id: int = 0


class CharPatchData(GameDataModel):
    """clz_Torappu_CharPatchData"""

    infos: dict[str, CharPatchDataPatchInfo] | None = None
    patch_chars: dict[str, CharacterData] | None = None
    unlock_conds: dict[str, CharPatchDataUnlockCond] | None = None
    patch_detail_info_list: dict[str, CharPatchDataPatchDetailInfo] | None = None


# root_type clz_Torappu_CharPatchData
CharPatchTable = CharPatchData


CharPatchDataPatchInfo.model_rebuild()
CharacterDataPowerData.model_rebuild()
CharacterDataUnlockCondition.model_rebuild()
BlackboardDataPair.model_rebuild()
CharacterDataTraitData.model_rebuild()
CharacterDataTraitDataBundle.model_rebuild()
AttributesData.model_rebuild()
AttributesKeyFrame.model_rebuild()
ItemBundle.model_rebuild()
CharacterDataPhaseData.model_rebuild()
CharacterDataMainSkillSpecializeLevelData.model_rebuild()
CharacterDataMainSkill.model_rebuild()
TalentData.model_rebuild()
CharacterDataTalentDataBundle.model_rebuild()
AttributeModifierDataAttributeModifier.model_rebuild()
AttributeModifierData.model_rebuild()
ExternalBuff.model_rebuild()
CharacterDataPotentialRank.model_rebuild()
AttributesDeltaData.model_rebuild()
AttributesDeltaKeyFrame.model_rebuild()
CharacterDataSkillLevelCost.model_rebuild()
CharacterData.model_rebuild()
CharPatchDataUnlockCondItem.model_rebuild()
CharPatchDataUnlockCond.model_rebuild()
CharPatchDataPatchDetailInfo.model_rebuild()
CharPatchData.model_rebuild()

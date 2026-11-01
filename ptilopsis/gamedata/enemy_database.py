"""enemy_database.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/enemy_database.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class SourceApplyWay(IntEnum):
    """enum__Torappu_SourceApplyWay"""

    NONE = 0
    MELEE = 1
    RANGED = 2
    ALL = 3


class MotionMode(IntEnum):
    """enum__Torappu_MotionMode"""

    WALK = 0
    FLY = 1
    E_NUM = 2


class EnemyLevelType(IntEnum):
    """enum__Torappu_EnemyLevelType"""

    NORMAL = 0
    ELITE = 1
    BOSS = 2
    E_NUM = 3


class SpType(IntEnum):
    """enum__Torappu_SpType"""

    NONE = 0
    INCREASE_WITH_TIME = 1
    INCREASE_WHEN_ATTACK = 2
    INCREASE_WHEN_TAKEN_DAMAGE = 4
    ATTACK_OR_DAMAGE = 6
    ALL = 7


class UndefinableStr(GameDataModel):
    """clz_Torappu_Undefinable_1_System_String_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: str | None = Field(default=None, alias="m_value")


class UndefinableInt(GameDataModel):
    """clz_Torappu_Undefinable_1_System_Int32_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: int = Field(default=0, alias="m_value")


class UndefinableFloat(GameDataModel):
    """clz_Torappu_Undefinable_1_System_Single_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: float = Field(default=0.0, alias="m_value")


class UndefinableBool(GameDataModel):
    """clz_Torappu_Undefinable_1_System_Boolean_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: bool = Field(default=False, alias="m_value")


class EnemyDatabaseAttributesData(GameDataModel):
    """clz_Torappu_EnemyDatabase_AttributesData"""

    max_hp: UndefinableInt | None = None
    atk: UndefinableInt | None = None
    def_: UndefinableInt | None = Field(default=None, alias="def")
    magic_resistance: UndefinableFloat | None = None
    cost: UndefinableInt | None = None
    block_cnt: UndefinableInt | None = None
    move_speed: UndefinableFloat | None = None
    attack_speed: UndefinableFloat | None = None
    base_attack_time: UndefinableFloat | None = None
    respawn_time: UndefinableInt | None = None
    hp_recovery_per_sec: UndefinableFloat | None = None
    sp_recovery_per_sec: UndefinableFloat | None = None
    max_deploy_count: UndefinableInt | None = None
    mass_level: UndefinableInt | None = None
    base_force_level: UndefinableInt | None = None
    taunt_level: UndefinableInt | None = None
    ep_damage_resistance: UndefinableFloat | None = None
    ep_resistance: UndefinableFloat | None = None
    damage_hitrate_physical: UndefinableFloat | None = None
    damage_hitrate_magical: UndefinableFloat | None = None
    ep_break_recover_speed: UndefinableFloat | None = None
    block_volume: UndefinableInt | None = None
    stun_immune: UndefinableBool | None = None
    silence_immune: UndefinableBool | None = None
    sleep_immune: UndefinableBool | None = None
    frozen_immune: UndefinableBool | None = None
    levitate_immune: UndefinableBool | None = None
    disarmed_combat_immune: UndefinableBool | None = None
    feared_immune: UndefinableBool | None = None
    palsy_immune: UndefinableBool | None = None
    attract_immune: UndefinableBool | None = None
    teleport_immune: UndefinableBool | None = None
    ground_bound_immune: UndefinableBool | None = None


class UndefinableSourceApplyWay(GameDataModel):
    """clz_Torappu_Undefinable_1_Torappu_SourceApplyWay_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: str = Field(default="NONE", alias="m_value")


class UndefinableMotionMode(GameDataModel):
    """clz_Torappu_Undefinable_1_Torappu_MotionMode_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: str = Field(default="WALK", alias="m_value")


class UndefinableStrList(GameDataModel):
    """clz_Torappu_Undefinable_1_System_String___"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: list[str] | None = Field(default=None, alias="m_value")


class UndefinableEnemyLevelType(GameDataModel):
    """clz_Torappu_Undefinable_1_Torappu_EnemyLevelType_"""

    m_defined: bool = Field(default=False, alias="m_defined")
    m_value: str = Field(default="NORMAL", alias="m_value")


class BlackboardDataPair(GameDataModel):
    """clz_Torappu_Blackboard_DataPair"""

    key: str | None = None
    value: float = 0.0
    value_str: str | None = None


class LevelDataEnemyDataESkillData(GameDataModel):
    """clz_Torappu_LevelData_EnemyData_ESkillData"""

    prefab_key: str | None = None
    priority: int = 0
    cooldown: float = 0.0
    init_cooldown: float = 0.0
    sp_cost: int = 0
    blackboard: list[BlackboardDataPair] | None = None


class LevelDataEnemyDataESpData(GameDataModel):
    """clz_Torappu_LevelData_EnemyData_ESpData"""

    sp_type: str = "NONE"
    max_sp: int = 0
    init_sp: int = 0
    increment: float = 0.0


class EnemyDatabaseEnemyData(GameDataModel):
    """clz_Torappu_EnemyDatabase_EnemyData"""

    name: UndefinableStr | None = None
    description: UndefinableStr | None = None
    prefab_key: UndefinableStr | None = None
    attributes: EnemyDatabaseAttributesData | None = None
    apply_way: UndefinableSourceApplyWay | None = None
    motion: UndefinableMotionMode | None = None
    enemy_tags: UndefinableStrList | None = None
    life_point_reduce: UndefinableInt | None = None
    level_type: UndefinableEnemyLevelType | None = None
    range_radius: UndefinableFloat | None = None
    num_of_extra_drops: UndefinableInt | None = None
    view_radius: UndefinableFloat | None = None
    not_count_in_total: UndefinableBool | None = None
    talent_blackboard: list[BlackboardDataPair] | None = None
    skills: list[LevelDataEnemyDataESkillData] | None = None
    sp_data: LevelDataEnemyDataESpData | None = None


class EnemyDatabaseEnemyLevel(GameDataModel):
    """clz_Torappu_EnemyDatabase_EnemyLevel"""

    level: int = 0
    enemy_data: EnemyDatabaseEnemyData | None = None


class KvpStringListEnemyDatabaseEnemyLevel(GameDataModel):
    """kvp__string__list_clz_Torappu_EnemyDatabase_EnemyLevel"""

    key: str | None = Field(default=None, alias="Key")
    value: list[EnemyDatabaseEnemyLevel] | None = Field(default=None, alias="Value")


class EnemyDatabase(GameDataModel):
    """clz_Torappu_EnemyDatabase"""

    enemies: list[KvpStringListEnemyDatabaseEnemyLevel] | None = None


# root_type clz_Torappu_EnemyDatabase


UndefinableStr.model_rebuild()
UndefinableInt.model_rebuild()
UndefinableFloat.model_rebuild()
UndefinableBool.model_rebuild()
EnemyDatabaseAttributesData.model_rebuild()
UndefinableSourceApplyWay.model_rebuild()
UndefinableMotionMode.model_rebuild()
UndefinableStrList.model_rebuild()
UndefinableEnemyLevelType.model_rebuild()
BlackboardDataPair.model_rebuild()
LevelDataEnemyDataESkillData.model_rebuild()
LevelDataEnemyDataESpData.model_rebuild()
EnemyDatabaseEnemyData.model_rebuild()
EnemyDatabaseEnemyLevel.model_rebuild()
KvpStringListEnemyDatabaseEnemyLevel.model_rebuild()
EnemyDatabase.model_rebuild()

"""levels/<levelId>.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/prts___levels.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum
from typing import Any

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class BattleFunctionDisableMask(IntEnum):
    """enum__Torappu_BattleFunctionDisableMask"""

    NONE = 0
    CARD_LIST = 1
    CHARACTER_MENU = 2
    CHARACTER_INFO = 4
    SYSTEM_MENU = 8
    PAUSE_BUTTON = 16
    SPEED_SWITCHER_BUTTON = 32
    BATTLE_STATUS = 64
    COST_PANEL = 128
    SLOW_MOTION = 256
    PAUSE_BUTTON_INTERACT = 512
    SYSTEM_MENU_INTERACT = 1024
    SPEED_SWITCHER_BUTTON_INTERACT = 2048
    UNIT_HUD_SKILL_CAST_MASK = 4096
    WITHDRAWABLE_PANEL = 8192
    COST_PANEL_KEEP_CHARACTERLIMIT = 16384
    CHARACTER_LIMIT = 32768
    AUTOCHESS_SELL_OR_DESTORY = 65536
    CHARACTER_MENU_PANEL = 131072
    DRAG_UI_CARD = 262144
    ALL = 524287


class TileDataHeightType(IntEnum):
    """enum__Torappu_TileData_HeightType"""

    LOWLAND = 0
    HIGHLAND = 1
    E_NUM = 2


class BuildableType(IntEnum):
    """enum__Torappu_BuildableType"""

    NONE = 0
    MELEE = 1
    RANGED = 2
    ALL = 3


class MotionMask(IntEnum):
    """enum__Torappu_MotionMask"""

    NONE = 0
    WALK_ONLY = 1
    FLY_ONLY = 2
    ALL = 3


class PlayerSideMask(IntEnum):
    """enum__Torappu_PlayerSideMask"""

    ALL = 0
    SIDE_A = 2
    SIDE_B = 4
    SIDE_C = 8
    SIDE_D = 16
    NONE = 255


class SharedConstsDirection(IntEnum):
    """enum__Torappu_SharedConsts_Direction"""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    E_NUM = 4
    INVALID = 4


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


class MotionMode(IntEnum):
    """enum__Torappu_MotionMode"""

    WALK = 0
    FLY = 1
    E_NUM = 2


class CheckpointType(IntEnum):
    """enum__Torappu_CheckpointType"""

    MOVE = 0
    WAIT_FOR_SECONDS = 1
    WAIT_FOR_PLAY_TIME = 2
    WAIT_CURRENT_FRAGMENT_TIME = 3
    WAIT_CURRENT_WAVE_TIME = 4
    DISAPPEAR = 5
    APPEAR_AT_POS = 6
    ALERT = 7
    PATROL_MOVE = 8
    WAIT_BOSSRUSH_WAVE = 9
    MAP_OFFSET_MOVE = 10
    INVALID = 11


class SourceApplyWay(IntEnum):
    """enum__Torappu_SourceApplyWay"""

    NONE = 0
    MELEE = 1
    RANGED = 2
    ALL = 3


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


class LevelDataWaveDataFragmentDataActionDataActionType(IntEnum):
    """enum__Torappu_LevelData_WaveData_FragmentData_ActionData_ActionType"""

    SPAWN = 0
    PREVIEW_CURSOR = 1
    STORY = 2
    TUTORIAL = 3
    PLAY_BGM = 4
    DISPLAY_ENEMY_INFO = 5
    ACTIVATE_PREDEFINED = 6
    PLAY_OPERA = 7
    TRIGGER_PREDEFINED = 8
    BATTLE_EVENTS = 9
    WITHDRAW_PREDEFINED = 10
    DIALOG = 11
    SHOW_ALL_HIDDEN_CARDS = 12
    EMPTY = 13
    E_NUM = 14


class LevelDataWaveDataFragmentDataActionDataRandomType(IntEnum):
    """enum__Torappu_LevelData_WaveData_FragmentData_ActionData_RandomType"""

    ALWAYS = 0
    PER_DAY = 1
    NEVER = 2
    PER_SETTLE_DAY = 3
    PER_SEASON = 4


class LevelDataWaveDataFragmentDataActionDataRefreshType(IntEnum):
    """enum__Torappu_LevelData_WaveData_FragmentData_ActionData_RefreshType"""

    ALWAYS = 0
    PER_DAY = 1
    NEVER = 2
    PER_SETTLE_DAY = 3
    PER_SEASON = 4


class EvolvePhase(IntEnum):
    """enum__Torappu_EvolvePhase"""

    PHASE_0 = 0
    PHASE_1 = 1
    PHASE_2 = 2
    PHASE_3 = 3
    E_NUM = 4


class BlackboardDataPair(GameDataModel):
    """clz_Torappu_Blackboard_DataPair"""

    key: str | None = None
    value: float = 0.0
    value_str: str | None = None


class LevelDataOptions(GameDataModel):
    """clz_Torappu_LevelData_Options"""

    character_limit: int = 0
    max_life_point: int = 0
    initial_cost: int = 0
    max_cost: int = 0
    cost_increase_time: float = 0.0
    move_multiplier: float = 0.0
    steering_enabled: bool = False
    reachable_check_ignore_start_tile: bool = False
    is_training_level: bool = False
    is_hard_training_level: bool = False
    is_predefined_cards_selectable: bool = False
    display_rest_time: bool = False
    max_play_time: float = 0.0
    function_disable_mask: str = "NONE"
    config_black_board: list[BlackboardDataPair] | None = None


class HgInternalMapData(GameDataModel):
    """hg__internal__MapData"""

    row_size: int = Field(default=0, alias="row_size")
    column_size: int = Field(default=0, alias="column_size")
    matrix_data: list[int] | None = Field(default=None, alias="matrix_data")


class UnityEngineVector3(GameDataModel):
    """clz_UnityEngine_Vector3"""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


class MapEffectData(GameDataModel):
    """clz_Torappu_MapEffectData"""

    key: str | None = None
    offset: UnityEngineVector3 | None = None
    direction: str = "UP"


class TileData(GameDataModel):
    """clz_Torappu_TileData"""

    tile_key: str | None = None
    height_type: str = "LOWLAND"
    buildable_type: str = "NONE"
    passable_mask: str = "NONE"
    player_side_mask: str = "ALL"
    blackboard: list[BlackboardDataPair] | None = None
    effects: list[MapEffectData] | None = None


class GridPosition(GameDataModel):
    """clz_Torappu_GridPosition"""

    row: int = 0
    col: int = 0


class MapDataEdge(GameDataModel):
    """clz_Torappu_MapData_Edge"""

    pos: GridPosition | None = None
    direction: str = "UP"
    block_mask: str = "NONE"


class MapData(GameDataModel):
    """clz_Torappu_MapData"""

    map: Any | None = None
    tiles: list[TileData] | None = None
    block_edges: list[MapDataEdge] | None = None
    tags: list[str] | None = None
    effects: list[MapEffectData] | None = None
    layer_rects: list[str] | None = None


class LegacyInLevelRuneData(GameDataModel):
    """clz_Torappu_LegacyInLevelRuneData"""

    difficulty_mask: str = "NONE"
    key: str | None = None
    profession_mask: str = "NONE"
    buildable_mask: str = "NONE"
    blackboard: list[BlackboardDataPair] | None = None


class LevelDataGlobalBuffData(GameDataModel):
    """clz_Torappu_LevelData_GlobalBuffData"""

    prefab_key: str | None = None
    blackboard: list[BlackboardDataPair] | None = None
    override_camera_effect: str | None = None
    pass_profession_mask_flag: bool = False
    profession_mask: str = "NONE"
    player_side_mask: str = "ALL"


class UnityEngineVector2(GameDataModel):
    """clz_UnityEngine_Vector2"""

    x: float = 0.0
    y: float = 0.0


class RouteDataCheckpointData(GameDataModel):
    """clz_Torappu_RouteData_CheckpointData"""

    type: str = "MOVE"
    time: float = 0.0
    position: GridPosition | None = None
    reach_offset: UnityEngineVector2 | None = None
    randomize_reach_offset: bool = False
    reach_distance: float = 0.0


class RouteData(GameDataModel):
    """clz_Torappu_RouteData"""

    motion_mode: str = "WALK"
    start_position: GridPosition | None = None
    end_position: GridPosition | None = None
    spawn_random_range: UnityEngineVector2 | None = None
    spawn_offset: UnityEngineVector2 | None = None
    checkpoints: list[RouteDataCheckpointData] | None = None
    allow_diagonal_move: bool = False
    visit_every_tile_center: bool = False
    visit_every_node_center: bool = False
    visit_every_check_point: bool = False


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


class LevelDataEnemyData(GameDataModel):
    """clz_Torappu_LevelData_EnemyData"""

    name: str | None = None
    description: str | None = None
    key: str | None = None
    attributes: AttributesData | None = None
    apply_way: str = "NONE"
    motion: str = "WALK"
    enemy_tags: list[str] | None = None
    not_count_in_total: bool = False
    alias: str | None = None
    life_point_reduce: int = 0
    range_radius: float = 0.0
    num_of_extra_drops: int = 0
    view_radius: float = 0.0
    level_type: str = "NORMAL"
    talent_blackboard: list[BlackboardDataPair] | None = None
    skills: list[LevelDataEnemyDataESkillData] | None = None
    sp_data: LevelDataEnemyDataESpData | None = None


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


class LevelDataEnemyDataDbReference(GameDataModel):
    """clz_Torappu_LevelData_EnemyDataDbReference"""

    use_db: bool = False
    id: str | None = None
    level: int = 0
    overwritten_data: EnemyDatabaseEnemyData | None = None


class LevelDataWaveDataFragmentDataActionData(GameDataModel):
    """clz_Torappu_LevelData_WaveData_FragmentData_ActionData"""

    action_type: str = "SPAWN"
    managed_by_scheduler: bool = False
    key: str | None = None
    count: int = 0
    pre_delay: float = 0.0
    interval: float = 0.0
    route_index: int = 0
    block_fragment: bool = False
    auto_preview_route: bool = False
    auto_display_enemy_info: bool = False
    is_unharmful_and_always_count_as_killed: bool = False
    hidden_group: str | None = None
    random_spawn_group_key: str | None = None
    random_spawn_group_pack_key: str | None = None
    random_type: str = "ALWAYS"
    refresh_type: str = "ALWAYS"
    weight: int = 0
    dont_block_wave: bool = False
    force_block_wave_in_branch: bool = False


class LevelDataWaveDataFragmentData(GameDataModel):
    """clz_Torappu_LevelData_WaveData_FragmentData"""

    pre_delay: float = 0.0
    actions: list[LevelDataWaveDataFragmentDataActionData] | None = None


class LevelDataWaveData(GameDataModel):
    """clz_Torappu_LevelData_WaveData"""

    pre_delay: float = 0.0
    post_delay: float = 0.0
    max_time_waiting_for_next_wave: float = 0.0
    fragments: list[LevelDataWaveDataFragmentData] | None = None
    advanced_wave_tag: str | None = None


class LevelDataBranchDataPhaseData(GameDataModel):
    """clz_Torappu_LevelData_BranchData_PhaseData"""

    pre_delay: float = 0.0
    actions: list[LevelDataWaveDataFragmentDataActionData] | None = None


class LevelDataBranchData(GameDataModel):
    """clz_Torappu_LevelData_BranchData"""

    phases: list[LevelDataBranchDataPhaseData] | None = None


class CharacterDataUniqueEquipPair(GameDataModel):
    """clz_Torappu_CharacterData_UniqueEquipPair"""

    key: str | None = None
    level: int = 0


class CharacterDataMasterInfo(GameDataModel):
    """clz_Torappu_CharacterData_MasterInfo"""

    master_id: str | None = None
    level: int = 0


class CharacterInstMetadata(GameDataModel):
    """clz_Torappu_CharacterInst_Metadata"""

    character_key: str | None = None
    level: int = 0
    phase: str = "PHASE_0"
    favor_point: int = 0
    potential_rank: int = 0


class CharacterInstTalentInst(GameDataModel):
    """clz_Torappu_CharacterInst_TalentInst"""

    prefab_key: str | None = None
    blackboard: list[BlackboardDataPair] | None = None


class LevelDataPredefinedDataPredefinedCharacter(GameDataModel):
    """clz_Torappu_LevelData_PredefinedData_PredefinedCharacter"""

    position: GridPosition | None = None
    direction: str = "UP"
    hidden: bool = False
    alias: str | None = None
    uni_equip_ids: list[CharacterDataUniqueEquipPair] | None = None
    show_sp_illust: bool = False
    master_infos: list[CharacterDataMasterInfo] | None = None
    inst: CharacterInstMetadata | None = None
    skill_index: int = 0
    main_skill_lvl: int = 0
    skin_id: str | None = None
    tmpl_id: str | None = None
    override_skill_blackboard: list[BlackboardDataPair] | None = None
    override_talents: list[CharacterInstTalentInst] | None = None


class LevelDataPredefinedDataPredefinedCard(GameDataModel):
    """clz_Torappu_LevelData_PredefinedData_PredefinedCard"""

    hidden: bool = False
    alias: str | None = None
    uni_equip_ids: list[CharacterDataUniqueEquipPair] | None = None
    show_sp_illust: bool = False
    master_infos: list[CharacterDataMasterInfo] | None = None
    inst: CharacterInstMetadata | None = None
    skill_index: int = 0
    main_skill_lvl: int = 0
    skin_id: str | None = None
    tmpl_id: str | None = None
    override_skill_blackboard: list[BlackboardDataPair] | None = None
    override_talents: list[CharacterInstTalentInst] | None = None


class LevelDataPredefinedDataPredefinedTokenCard(GameDataModel):
    """clz_Torappu_LevelData_PredefinedData_PredefinedTokenCard"""

    initial_cnt: int = 0
    hidden: bool = False
    alias: str | None = None
    uni_equip_ids: list[CharacterDataUniqueEquipPair] | None = None
    show_sp_illust: bool = False
    master_infos: list[CharacterDataMasterInfo] | None = None
    inst: CharacterInstMetadata | None = None
    skill_index: int = 0
    main_skill_lvl: int = 0
    skin_id: str | None = None
    tmpl_id: str | None = None
    override_skill_blackboard: list[BlackboardDataPair] | None = None
    override_talents: list[CharacterInstTalentInst] | None = None


class LevelDataPredefinedData(GameDataModel):
    """clz_Torappu_LevelData_PredefinedData"""

    character_insts: list[LevelDataPredefinedDataPredefinedCharacter] | None = None
    token_insts: list[LevelDataPredefinedDataPredefinedCharacter] | None = None
    character_cards: list[LevelDataPredefinedDataPredefinedCard] | None = None
    token_cards: list[LevelDataPredefinedDataPredefinedTokenCard] | None = None


class LevelData(GameDataModel):
    """clz_Torappu_LevelData"""

    options: LevelDataOptions | None = None
    level_id: str | None = None
    map_id: str | None = None
    bgm_event: str | None = None
    environment_se: str | None = None
    map_data: MapData | None = None
    tiles_disallow_to_locate: list[GridPosition] | None = None
    runes: list[LegacyInLevelRuneData] | None = None
    optional_runes: dict[str, list[LegacyInLevelRuneData]] | None = None
    global_buffs: list[LevelDataGlobalBuffData] | None = None
    routes: list[RouteData] | None = None
    extra_routes: list[RouteData] | None = None
    enemies: list[LevelDataEnemyData] | None = None
    enemy_db_refs: list[LevelDataEnemyDataDbReference] | None = None
    waves: list[LevelDataWaveData] | None = None
    branches: dict[str, LevelDataBranchData] | None = None
    predefines: LevelDataPredefinedData | None = None
    hard_predefines: LevelDataPredefinedData | None = None
    exclude_char_id_list: list[str] | None = None
    random_seed: int = 0
    opera_config: str | None = None
    camera_plugin: str | None = None


# root_type clz_Torappu_LevelData


BlackboardDataPair.model_rebuild()
LevelDataOptions.model_rebuild()
HgInternalMapData.model_rebuild()
UnityEngineVector3.model_rebuild()
MapEffectData.model_rebuild()
TileData.model_rebuild()
GridPosition.model_rebuild()
MapDataEdge.model_rebuild()
MapData.model_rebuild()
LegacyInLevelRuneData.model_rebuild()
LevelDataGlobalBuffData.model_rebuild()
UnityEngineVector2.model_rebuild()
RouteDataCheckpointData.model_rebuild()
RouteData.model_rebuild()
AttributesData.model_rebuild()
LevelDataEnemyDataESkillData.model_rebuild()
LevelDataEnemyDataESpData.model_rebuild()
LevelDataEnemyData.model_rebuild()
UndefinableStr.model_rebuild()
UndefinableInt.model_rebuild()
UndefinableFloat.model_rebuild()
UndefinableBool.model_rebuild()
EnemyDatabaseAttributesData.model_rebuild()
UndefinableSourceApplyWay.model_rebuild()
UndefinableMotionMode.model_rebuild()
UndefinableStrList.model_rebuild()
UndefinableEnemyLevelType.model_rebuild()
EnemyDatabaseEnemyData.model_rebuild()
LevelDataEnemyDataDbReference.model_rebuild()
LevelDataWaveDataFragmentDataActionData.model_rebuild()
LevelDataWaveDataFragmentData.model_rebuild()
LevelDataWaveData.model_rebuild()
LevelDataBranchDataPhaseData.model_rebuild()
LevelDataBranchData.model_rebuild()
CharacterDataUniqueEquipPair.model_rebuild()
CharacterDataMasterInfo.model_rebuild()
CharacterInstMetadata.model_rebuild()
CharacterInstTalentInst.model_rebuild()
LevelDataPredefinedDataPredefinedCharacter.model_rebuild()
LevelDataPredefinedDataPredefinedCard.model_rebuild()
LevelDataPredefinedDataPredefinedTokenCard.model_rebuild()
LevelDataPredefinedData.model_rebuild()
LevelData.model_rebuild()

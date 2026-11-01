"""enemy_handbook_table.json 的数据模型。

由 scripts/gen_gamedata_models.py 从 FBS/enemy_handbook_table.fbs 生成,请勿手改;
字段语义见 dump.cs 里的同名类。
"""

from __future__ import annotations

from enum import IntEnum

from pydantic import Field

from ptilopsis.gamedata._base import GameDataModel


class EnemyLevelType(IntEnum):
    """enum__Torappu_EnemyLevelType"""

    NORMAL = 0
    ELITE = 1
    BOSS = 2
    E_NUM = 3


class EnemyHandBookDataTextFormat(IntEnum):
    """enum__Torappu_EnemyHandBookData_TextFormat"""

    NORMAL = 0
    TITLE = 1
    SILENCE = 2


class EnemyHandBookDamageType(IntEnum):
    """enum__Torappu_EnemyHandBookDamageType"""

    PHYSIC = 0
    MAGIC = 1
    HEAL = 2
    NO_DAMAGE = 3


class EnemyHandbookLevelInfoDataRangePair(GameDataModel):
    """clz_Torappu_EnemyHandbookLevelInfoData_RangePair"""

    min: float = 0.0
    max: float = 0.0


class EnemyHandbookLevelInfoData(GameDataModel):
    """clz_Torappu_EnemyHandbookLevelInfoData"""

    class_level: str | None = None
    attack: EnemyHandbookLevelInfoDataRangePair | None = None
    def_: EnemyHandbookLevelInfoDataRangePair | None = Field(default=None, alias="def")
    magic_res: EnemyHandbookLevelInfoDataRangePair | None = None
    max_hp: EnemyHandbookLevelInfoDataRangePair | None = Field(
        default=None, alias="maxHP"
    )
    move_speed: EnemyHandbookLevelInfoDataRangePair | None = None
    attack_speed: EnemyHandbookLevelInfoDataRangePair | None = None
    enemy_damage_res: EnemyHandbookLevelInfoDataRangePair | None = None
    enemy_res: EnemyHandbookLevelInfoDataRangePair | None = None


class EnemyHandBookDataAbilty(GameDataModel):
    """clz_Torappu_EnemyHandBookData_Abilty"""

    text: str | None = None
    text_format: str = "NORMAL"


class EnemyHandBookData(GameDataModel):
    """clz_Torappu_EnemyHandBookData"""

    enemy_id: str | None = None
    enemy_index: str | None = None
    enemy_tags: list[str] | None = None
    sort_id: int = 0
    name: str | None = None
    enemy_level: str = "NORMAL"
    description: str | None = None
    attack_type: str | None = None
    ability: str | None = None
    is_invalid_killed: bool = False
    override_kill_cnt_infos: dict[str, int] | None = None
    hide_in_handbook: bool = False
    hide_in_stage: bool = False
    ability_list: list[EnemyHandBookDataAbilty] | None = None
    link_enemies: list[str] | None = None
    damage_type: list[str] | None = None
    invisible_detail: bool = False


class EnemyHandbookRaceData(GameDataModel):
    """clz_Torappu_EnemyHandbookRaceData"""

    id: str | None = None
    race_name: str | None = None
    sort_id: int = 0


class EnemyHandBookDataGroup(GameDataModel):
    """clz_Torappu_EnemyHandBookDataGroup"""

    level_info_list: list[EnemyHandbookLevelInfoData] | None = None
    enemy_data: dict[str, EnemyHandBookData] | None = None
    race_data: dict[str, EnemyHandbookRaceData] | None = None


# root_type clz_Torappu_EnemyHandBookDataGroup
EnemyHandbookTable = EnemyHandBookDataGroup


EnemyHandbookLevelInfoDataRangePair.model_rebuild()
EnemyHandbookLevelInfoData.model_rebuild()
EnemyHandBookDataAbilty.model_rebuild()
EnemyHandBookData.model_rebuild()
EnemyHandbookRaceData.model_rebuild()
EnemyHandBookDataGroup.model_rebuild()

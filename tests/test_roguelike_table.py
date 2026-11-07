"""初代集成战略旧表的真实物品记录与关卡读取兼容性。"""

import json
from pathlib import Path
from typing import Any

import pytest

from ptilopsis.gamedata.roguelike_table import RoguelikeTable
from ptilopsis.jobs.params import TABLES

FIXTURE = Path(__file__).parent / "fixtures" / "roguelike_table.json"


def legacy_table() -> dict[str, Any]:
    """游戏原表中的物品与关卡摘录,来源见 fixture 的 _source 字段。"""
    return json.loads(FIXTURE.read_text())


def test_registered_model_preserves_legacy_item_records() -> None:
    raw = legacy_table()
    assert TABLES["roguelike_table"].model is RoguelikeTable
    table = RoguelikeTable.model_validate(raw)
    assert table.item_table is not None
    assert table.item_table.items is not None
    # 完整回读原记录,防止字段因未建模、别名错误或过滤而静默丢失。
    assert {
        item_id: item.model_dump(by_alias=True)
        for item_id, item in table.item_table.items.items()
    } == raw["itemTable"]["items"]

    cactus = table.item_table.items["relic_2"]
    assert (cactus.name, cactus.usage, cactus.value, cactus.sort_id) == (
        "脱水仙人掌干",
        "可携带干员+1",
        8,
        2,
    )
    unlock = table.item_table.items["relic_4"].stable_unlock_cond
    assert unlock is not None
    assert (unlock.unlock_cond_detail, unlock.unlock_cnt) == ("", 50)
    squad = table.item_table.items["relic_b3"]
    assert (squad.type, squad.rarity, squad.value) == ("RELIC", "BORN", 0)
    assert table.item_table.items["hp"].type == "HP"


@pytest.mark.parametrize(
    "item_table",
    [None, {}, {"items": None}, {"items": {}}],
)
def test_empty_item_table_preserves_existing_stage_data(
    item_table: dict[str, Any] | None,
) -> None:
    raw = legacy_table()
    raw["itemTable"] = item_table
    table = RoguelikeTable.model_validate(raw)
    assert table.stages is not None
    assert {
        stage_id: stage.model_dump(by_alias=True)
        for stage_id, stage in table.stages.items()
    } == raw["stages"]


def test_stage_only_input_remains_supported() -> None:
    raw = legacy_table()
    del raw["itemTable"]
    table = RoguelikeTable.model_validate(raw)
    assert table.item_table is None
    assert table.stages is not None
    assert table.stages["ro_n_1_1"].code == "ISW-NO"
    assert table.stages["ro_n_1_1"].name == "路边劫匪"


def test_optional_item_fields_may_be_absent() -> None:
    raw = legacy_table()
    item = raw["itemTable"]["items"]["relic_2"]
    for field in ("description", "unlockCondParams", "stableUnlockCond"):
        del item[field]
    table = RoguelikeTable.model_validate(raw)
    assert table.item_table is not None
    assert table.item_table.items is not None
    cactus = table.item_table.items["relic_2"]
    assert cactus.description is None
    assert cactus.unlock_cond_params is None
    assert cactus.stable_unlock_cond is None
    assert cactus.name == "脱水仙人掌干"

"""初代集成战略旧表模型能按原字段完整回读真实记录。"""

import json
from pathlib import Path

from ptilopsis.gamedata.roguelike_table import RoguelikeTable

FIXTURE = Path(__file__).parent / "fixtures" / "roguelike_table.json"


def test_legacy_records_round_trip() -> None:
    raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
    del raw["_source"]
    table = RoguelikeTable.model_validate(raw)
    # 字段没建模或 alias 写错会在回读时丢失;blackboard 每项只带 value / valueStr
    # 之一,所以只比较 JSON 里出现过的字段
    assert table.model_dump(by_alias=True, exclude_unset=True) == raw

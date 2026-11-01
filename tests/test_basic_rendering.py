"""basic job 建页输出的 golden 测试。

夹具是从国服数据里截出的三名干员及其引用到的条目(道具只留名称、描述、
用途),覆盖召唤物(displayTokenDict / overrideTokenKey 两种来源)、势力、
模组、干员密录、悖论模拟、后勤技能显示名、无技能 / 无法精英化等分支。
"""

import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import pytest

from ptilopsis.jobs import basic
from ptilopsis.jobs.params import TABLES
from ptilopsis.utils import richtext

pytestmark = pytest.mark.anyio

FIXTURE_DIR = Path(__file__).parent / "fixtures" / "basic"
GOLDEN_DIR = Path(__file__).parent / "golden" / "basic"

# 干员一览/干员id 的节选:黑角不在表里,风丸按限定干员处理
ID_TABLE = {
    "凯尔希": {"id": 3, "approach": "", "date": "2019-04-30"},
    "风丸": {"id": 316, "approach": "活动获得", "date": "2023-10-12"},
}


class StubRichText(richtext.RichText):
    """把原文包一层标记,golden 不依赖富文本的具体规则。"""

    def __init__(self) -> None:
        pass  # 用不到样式表与术语表

    def compile(self, text: str | None, *, convert_newline: bool = True) -> str:
        return f"[RTS]{text or ''}"


class RecordingWiki:
    """把写入的页面记下来;读取时返回事先给定的页面。"""

    def __init__(
        self, pages: dict[str, str] | None = None, occupied: Iterable[str] = ()
    ) -> None:
        self.stored = pages or {}
        self.edited: dict[str, str] = {}
        self.protected: list[str] = []
        self.occupied = set(occupied)
        """已存在(如被重定向占用)的页面名,create 时不建也不保护。"""

    async def read_many(self, titles: Any) -> dict[str, str]:
        return {title: self.stored[title] for title in titles if title in self.stored}

    async def edit(self, title: str, text: str, **_: Any) -> None:
        self.edited[title] = text

    async def protect(self, **_: Any) -> None:
        return None

    async def create(
        self, title: str, text: str, protections: str | None = None, **_: Any
    ) -> bool:
        if title in self.occupied:
            return False
        self.edited[title] = text
        if protections is not None:
            self.protected.append(title)
        return True


def load_tables() -> dict[str, Any]:
    raw = json.loads((FIXTURE_DIR / "operators.json").read_text(encoding="utf-8"))
    tables = {}
    for name, data in raw.items():
        model = TABLES[name].model
        validate = getattr(model, "validate_python", None) or model.model_validate
        tables[name] = validate(data)
    return tables


def load_golden() -> dict[str, str]:
    return {
        path.stem: path.read_text(encoding="utf-8")
        for path in sorted(GOLDEN_DIR.glob("*.wiki"))
    }


async def run_basic(wiki: RecordingWiki, tables: dict[str, Any]) -> None:
    await basic.run.func(
        wiki=wiki,
        character_table=tables["character_table"],
        uniequip_table=tables["uniequip_table"],
        battle_equip_table=tables["battle_equip_table"],
        skill_table=tables["skill_table"],
        building_data=tables["building_data"],
        item_table=tables["item_table"],
        team_table=tables["handbook_team_table"],
        stories_table=tables["handbook_info_table"],
        skin_table=tables["skin_table"],
        gamedata_const=tables["gamedata_const"],
        charword_table=tables["charword_table"],
        medal_table=tables["medal_table"],
        id_table=ID_TABLE,
        rts=StubRichText(),
        char_list=[],
    )


async def test_created_pages_match_golden() -> None:
    tables = load_tables()
    wiki = RecordingWiki()

    await run_basic(wiki, tables)

    # 外文名重定向页不经过模板渲染,不做 golden
    pages = {
        title: text
        for title, text in wiki.edited.items()
        if not text.startswith("#redirect")
    }
    golden = load_golden()
    assert sorted(pages) == sorted(golden)
    for title, text in pages.items():
        assert text == golden[title], title


async def test_occupied_page_is_skipped_and_left_unprotected() -> None:
    """页面名被重定向等占用时不建页、不保护,也不建指向它的外文名重定向。"""

    tables = load_tables()
    wiki = RecordingWiki(occupied={"凯尔希"})

    await run_basic(wiki, tables)

    appellation = tables["character_table"]["char_003_kalts"].appellation
    assert "凯尔希" not in wiki.edited and "凯尔希" not in wiki.protected
    assert appellation not in wiki.edited
    # 其它干员照常建页并保护
    assert {"黑角", "风丸"} <= set(wiki.protected)


def test_equip_unlock_favor_without_trust_requirement() -> None:
    """电弧、机械师的模组各阶段都不要求信赖(unlockFavors 全为 0)。"""

    tables = load_tables()
    uniequip_table = tables["uniequip_table"]
    equip = uniequip_table.equip_dict["uniequip_002_kalts"]
    equip.unlock_favors = {"1": 0, "2": 0, "3": 0}

    content = "".join(
        basic.get_battle_equip(
            tables["character_table"]["char_003_kalts"],
            "char_003_kalts",
            tables["battle_equip_table"],
            uniequip_table,
            tables["item_table"],
            StubRichText(),
        )
    )

    assert "\n|解锁信赖=0\n|解锁信赖2=0\n|解锁信赖3=0\n" in content


async def test_update_jobs_keep_created_pages() -> None:
    """数据不变时,update / update_handbook 替换回去的片段应与建页输出一致。"""

    tables = load_tables()
    wiki = RecordingWiki(load_golden())

    await basic.update.func(
        wiki=wiki,
        character_table=tables["character_table"],
        uniequip_table=tables["uniequip_table"],
        battle_equip_table=tables["battle_equip_table"],
        building_data=tables["building_data"],
        item_table=tables["item_table"],
        team_table=tables["handbook_team_table"],
        skin_table=tables["skin_table"],
        charword_table=tables["charword_table"],
        rts=StubRichText(),
    )
    await basic.update_handbook.func(
        wiki=wiki,
        character_table=tables["character_table"],
        item_table=tables["item_table"],
        stories_table=tables["handbook_info_table"],
        medal_table=tables["medal_table"],
        rts=StubRichText(),
    )

    assert wiki.edited == {}

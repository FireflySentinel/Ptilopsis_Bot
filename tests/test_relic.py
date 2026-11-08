"""收藏品页面:按主题汇总、渲染、合并到已有页面,以及 job 的读写流程,全部离线。"""

from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, Any, cast

import pytest

from ptilopsis.__main__ import jobs_for
from ptilopsis.gamedata.roguelike_topic_table import RoguelikeTopicTable
from ptilopsis.jobs import discover_jobs
from ptilopsis.jobs.relic import (
    GENERIC_OBTAIN,
    PREAMBLE,
    MergeError,
    Relic,
    collect_relics,
    find_common,
    merge_page,
    render_page,
    run,
)
from ptilopsis.log import logger
from ptilopsis.utils.job import JobContext
from ptilopsis.utils.wiki import PageRevision, Wiki, WikiError

if TYPE_CHECKING:
    from ptilopsis.utils.data import GameData

THEMES = {1: "傀影与猩红孤钻", 2: "水月与深蓝之树", 3: "探索者的银凇止境"}


def item(topic: int, key: str, name: str, **fields: Any) -> dict[str, Any]:
    """原始 JSON 里的一件收藏品。"""
    item_id = f"rogue_{topic}_relic_{key}"
    return {
        "id": item_id,
        "name": name,
        "type": "RELIC",
        "rarity": "NORMAL",
        "description": f"{name}的描述",
        "usage": f"{name}的效果",
        "obtainApproach": GENERIC_OBTAIN,
        "iconId": item_id,
        **fields,
    }


def tables(
    items: list[dict[str, Any]],
    groups: dict[int, list[dict[str, int]]] | None = None,
) -> RoguelikeTopicTable:
    """拼出只含收藏品的 roguelike_topic_table。

    ``groups`` 为 {主题: [{收藏品 id: 生效难度, ...}, ...]},一个字典是一组难度变体。
    """
    details = {}
    for number in THEMES:
        own = {i["id"]: i for i in items if i["id"].startswith(f"rogue_{number}_")}
        upgrade_groups = {
            f"group_{index}": {
                "relicData": [
                    {"relicId": relic_id, "equivalentGrade": grade}
                    for relic_id, grade in members.items()
                ]
            }
            for index, members in enumerate((groups or {}).get(number, []))
        }
        details[f"rogue_{number}"] = {
            "items": own,
            "difficultyUpgradeRelicGroups": upgrade_groups,
        }
    return RoguelikeTopicTable.model_validate(
        {
            "topics": {
                f"rogue_{n}": {"id": f"rogue_{n}", "name": name, "sort": n}
                for n, name in THEMES.items()
            },
            "details": details,
        }
    )


def relics_of(*args: Any, **kwargs: Any) -> dict[str, Relic]:
    return {relic.name: relic for relic in collect_relics(tables(*args, **kwargs))}


def body(page: str) -> str:
    assert page.startswith(PREAMBLE + "\n\n")
    return page.removeprefix(PREAMBLE + "\n\n")


# ----- 汇总与渲染 -----


def test_collect_groups_same_name_across_themes_and_difficulty_variants() -> None:
    relics = relics_of(
        [
            item(3, "map", "地形图"),
            item(3, "map_a", "地形图-α"),
            item(3, "map_b", "地形图-β"),
            item(1, "map", "地形图"),
            item(2, "other", "别的收藏品"),
        ],
        groups={
            3: [
                {
                    "rogue_3_relic_map_b": 6,
                    "rogue_3_relic_map": 0,
                    "rogue_3_relic_map_a": 3,
                }
            ]
        },
    )
    assert set(relics) == {"地形图", "别的收藏品"}
    themes = relics["地形图"].themes
    assert [theme.number for theme in themes] == [1, 3]
    # 难度变体按生效难度排序,-α / -β 归到基础版本名下
    variants = themes[1].variants
    assert [(v.difficulty, v.item.id) for v in variants] == [
        (0, "rogue_3_relic_map"),
        (3, "rogue_3_relic_map_a"),
        (6, "rogue_3_relic_map_b"),
    ]


def test_render_page() -> None:
    relics = relics_of(
        [
            item(1, "a", "藏品", usage="攻击力+10%", description="旧描述"),
            item(
                2,
                "a",
                "藏品",
                rarity="RARE",
                usage="部署【迷彩】干员时<敌人>攻击力|+1",
                description="新描述",
                unlockCondDesc="通关一次",
                obtainApproach="商店购买",
            ),
            item(2, "a_a", "藏品-α", rarity="RARE", usage="部署时攻击力+2"),
        ],
        groups={2: [{"rogue_2_relic_a": 0, "rogue_2_relic_a_a": 3}]},
    )
    color = "{{color|#d800db|难度%d及以上生效：}}"
    assert body(render_page(relics["藏品"])) == "\n".join(
        [
            "{{收藏品/common",
            "|名称=藏品",
            "|iconId=rogue_2_relic_a",
            "|稀有度=1",
            # 描述取最新主题原文;变体描述不同时都保留
            "|描述=新描述<br/><br/>藏品-α的描述",
            "|主题1=傀影与猩红孤钻",
            "|角标1=",
            "|售价1=8",
            "|效果1=攻击力+10%",
            "|获取条件1=",
            "|解锁条件1=",
            "|主题2=水月与深蓝之树",
            "|角标2=",
            "|售价2=12",
            "|效果2="
            + color % 0
            + "部署【迷彩】干员时&lt;敌人&gt;攻击力&#124;+1<br/>"
            + color % 3
            + "部署时攻击力+2",
            "|获取条件2=" + color % 0 + "商店购买<br/>" + color % 3 + "－",
            "|解锁条件2=" + color % 0 + "通关一次<br/>" + color % 3 + "－",
            "}}",
            "",
        ]
    )


# ----- 合并到已有页面 -----


@pytest.fixture
def relic() -> Relic:
    return relics_of(
        [item(1, "a", "藏品"), item(2, "a", "藏品"), item(3, "a", "藏品")]
    )["藏品"]


def human_page(themes: Iterable[tuple[int, str]], extra: str = "") -> str:
    """人工写的页面:主题编号与名称自定,效果与角标都改过。"""
    lines = ["人工正文", "{{收藏品/common", "|名称=藏品", "|iconId=rogue_2_relic_a"]
    lines += ["|稀有度=0", "|描述=\n藏品的描述"]
    for number, name in themes:
        lines += [
            f"|主题{number}={name}",
            f"|角标{number}={{{{收藏品/角标|stack}}}}",
            f"|售价{number}=8",
            f"|效果{number}=攻击力{{{{+|10|+10}}}}<!-- | -->[[攻击力|ATK]]",
            f"|获取条件{number}=",
            f"|解锁条件{number}=",
        ]
    return "\n".join(lines) + extra + "\n}}\n[[分类:收藏品]]\n"


def test_rendered_page_is_a_fixed_point(relic: Relic) -> None:
    page = render_page(relic)
    assert merge_page(page, relic) == page


def test_appends_missing_theme_and_refreshes_headers_only(relic: Relic) -> None:
    before = human_page([(1, THEMES[1]), (2, THEMES[2])], extra="\n|备注=人工备注")
    after = merge_page(before, relic)

    # 新主题接在最后一个主题之后、人工参数之前;已有主题与正文原样保留
    assert after == before.replace(
        "|解锁条件2=\n",
        "|解锁条件2=\n"
        "|主题3=探索者的银凇止境\n|角标3=\n|售价3=8\n"
        "|效果3=藏品的效果\n|获取条件3=\n|解锁条件3=\n",
    ).replace("|iconId=rogue_2_relic_a", "|iconId=rogue_3_relic_a")
    assert merge_page(after, relic) == after


def test_refresh_keeps_whitespace_and_adds_missing_header(relic: Relic) -> None:
    before = human_page(THEMES.items())
    before = before.replace("|描述=\n藏品的描述", "|描述=\n人工描述\n")
    before = before.replace("|稀有度=0\n", "")
    after = merge_page(before, relic)
    assert "|描述=\n藏品的描述\n\n" in after
    assert "{{收藏品/common\n|稀有度=0\n|名称=藏品" in after
    assert merge_page(after, relic) == after


def test_refresh_removes_appended_glossary_and_preserves_theme_fields(
    relic: Relic,
) -> None:
    before = human_page(THEMES.items()).replace("rogue_2_relic_a", "rogue_3_relic_a")
    before = before.replace("藏品的描述", "藏品的描述<br/>【迷彩】额外术语解释")
    after = merge_page(before, relic)
    assert after == before.replace("<br/>【迷彩】额外术语解释", "")
    assert merge_page(after, relic) == after


def test_theme_names_may_be_bold_or_linked(relic: Relic) -> None:
    page = human_page(
        [(1, f"'''{THEMES[1]}'''"), (2, f"[[{THEMES[2]}|水月]]"), (3, THEMES[3])]
    ).replace("rogue_2_relic_a", "rogue_3_relic_a")
    assert merge_page(page, relic) == page


@pytest.mark.parametrize(
    ("page", "reason"),
    [
        ("{{干员信息|名称=藏品}}", "不是收藏品页面"),
        ("{{收藏品/common|主题1=a}}{{收藏品/common|主题1=a}}", "2 个"),
        (human_page([(1, THEMES[1]), (2, THEMES[3])]), "插在已有主题之间"),
        (human_page([(1, "别的主题")]), "对不上"),
        (human_page([(1, THEMES[1]), (3, THEMES[2])]), "连续"),
        (human_page([(1, THEMES[1])], extra="\n|效果2=x"), "效果2"),
        (human_page([]).replace("rogue_2_relic_a", "rogue_9_relic_a"), "数据源"),
        ("{{收藏品/common|主题1=[[a}}", "未闭合"),
        ("{{收藏品/common|无名参数}}", "未命名"),
    ],
)
def test_ambiguous_pages_are_rejected(relic: Relic, page: str, reason: str) -> None:
    with pytest.raises(MergeError, match=reason):
        merge_page(page, relic)


# ----- job -----


class FakeWiki:
    """只实现 job 用到的 read_revisions / edit。"""

    def __init__(self, pages: dict[str, str], redirects: Iterable[str] = ()) -> None:
        self.pages = pages
        self.redirects = set(redirects)
        self.edits: list[dict[str, Any]] = []
        self.errors: dict[str, WikiError] = {}

    async def read_revisions(self, titles: Iterable[str]) -> dict[str, PageRevision]:
        return {
            title: PageRevision(
                title=title,
                text=self.pages[title],
                revid=7,
                timestamp="2026-01-01T00:00:00Z",
                starttimestamp="2026-01-02T00:00:00Z",
                redirect=title in self.redirects,
                contentmodel="wikitext",
            )
            for title in titles
            if title in self.pages
        }

    async def edit(self, **kwargs: Any) -> dict[str, Any]:
        if error := self.errors.get(kwargs["title"]):
            raise error
        self.edits.append(kwargs)
        return {"edit": {"result": "Success"}}


@pytest.fixture
def logged_warnings() -> Iterator[list[str]]:
    captured: list[str] = []
    sink = logger.add(
        lambda message: captured.append(str(message).strip()),
        level="WARNING",
        format="{message}",
    )
    yield captured
    logger.remove(sink)


def relic_tables() -> RoguelikeTopicTable:
    names = ["新藏品", "旧藏品", "无变化", "重定向", "同名干员", "冲突"]
    return tables(
        [item(n, str(i), name) for i, name in enumerate(names) for n in (1, 2)]
    )


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("description", "usage", "expected_description", "expected_usage"),
    [
        (
            "伊比利亚海民在浅滩捕杀巨鳞时常穿的外衣，独特的造型与颜色让他们看起来"
            "像是普通的礁石。罗德岛工程部以此为原型设计了具有视觉隐匿效果的作战服，"
            "目前尚在测试阶段。",
            "远程干员获得【迷彩】",
            "伊比利亚海民在浅滩捕杀巨鳞时常穿的外衣，独特的造型与颜色让他们看起来"
            "像是普通的礁石。罗德岛工程部以此为原型设计了具有视觉隐匿效果的作战服，"
            "目前尚在测试阶段。",
            "远程干员获得【迷彩】",
        ),
        (
            "原表描述\r\n【迷彩】原表中的说明",
            "远程干员获得【迷彩】\n攻击力|+1<测试>",
            "原表描述<br/>【迷彩】原表中的说明",
            "远程干员获得【迷彩】<br/>攻击力&#124;+1&lt;测试&gt;",
        ),
        (None, "远程干员获得【迷彩】", "", "远程干员获得【迷彩】"),
        ("", "远程干员获得【迷彩】", "", "远程干员获得【迷彩】"),
    ],
)
async def test_job_uses_only_cn_topic_table_text(
    description: str | None,
    usage: str,
    expected_description: str,
    expected_usage: str,
) -> None:
    topic_table = tables(
        [item(2, "fight_132", "捕鳞蓑", description=description, usage=usage)]
    )

    class FakeGameData:
        config = None

        def __init__(self) -> None:
            self.reads: list[tuple[str, str]] = []

        async def get(self, path: str, region: str = "CN") -> dict[str, Any]:
            self.reads.append((path, region))
            if path == "excel/roguelike_topic_table.json":
                return topic_table.model_dump(by_alias=True)
            raise AssertionError(path)

    fake, data = FakeWiki({}), FakeGameData()
    await run.run(JobContext(cast("Wiki", fake), cast("GameData", data)))
    assert data.reads == [("excel/roguelike_topic_table.json", "CN")]
    assert len(fake.edits) == 1 and fake.edits[0]["title"] == "捕鳞蓑"
    params = find_common(fake.edits[0]["text"]).params
    assert params["描述"].value == expected_description
    assert params["效果1"].value == expected_usage


@pytest.mark.anyio
async def test_job_creates_updates_and_skips(logged_warnings: list[str]) -> None:
    topic_table = relic_tables()
    relics = {relic.name: relic for relic in collect_relics(topic_table)}
    old = render_page(relics["旧藏品"]).replace(f"|主题2={THEMES[2]}", "|主题2=")
    old = old[: old.index("|主题2=")] + "}}\n"
    fake = FakeWiki(
        {
            "旧藏品": old,
            "无变化": render_page(relics["无变化"]),
            "重定向": "#重定向 [[别处]]",
            "同名干员": "{{干员信息}}",
            "冲突": old.replace("旧藏品", "冲突"),
        },
        redirects=["重定向"],
    )
    fake.errors["冲突"] = WikiError("editconflict", "Edit conflict.")

    await run.func(cast("Wiki", fake), topic_table)

    create, update = fake.edits
    assert create["title"] == "新藏品"
    assert create["createonly"] is True and create["summary"] == "init"
    assert create["text"] == render_page(relics["新藏品"])
    assert update["title"] == "旧藏品" and update["summary"] == "update"
    assert update["nocreate"] is True
    assert update["basetimestamp"] == "2026-01-01T00:00:00Z"
    assert update["starttimestamp"] == "2026-01-02T00:00:00Z"
    assert update["text"] == merge_page(old, relics["旧藏品"])
    assert f"|主题2={THEMES[2]}" in update["text"]
    assert [w.split(" ")[1] for w in logged_warnings] == ["重定向", "同名干员", "冲突"]


@pytest.mark.anyio
async def test_job_propagates_unexpected_api_errors() -> None:
    topic_table = relic_tables()
    fake = FakeWiki({})
    fake.errors["新藏品"] = WikiError("permissiondenied", "no")
    with pytest.raises(WikiError, match="permissiondenied"):
        await run.func(cast("Wiki", fake), topic_table)


def test_relic_mode_is_also_in_regular() -> None:
    discover_jobs()
    assert jobs_for(("relic",)) == ["relic.run"]
    assert jobs_for(("regular",)).count("relic.run") == 1


def test_overlapping_modes_run_each_job_once() -> None:
    assert jobs_for(("regular", "relic")) == jobs_for(("regular",))
    jobs = jobs_for(("special", "jp"))
    assert jobs.count("charword.update") == 1
    assert jobs.index("charword.update") < jobs.index("update_jp.run")

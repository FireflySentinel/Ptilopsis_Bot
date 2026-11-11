# Ptilopsis Bot

用于自动更新 [PRTS Wiki](https://prts.wiki) 明日方舟相关页面的机器人。

机器人会定期或手动触发，从游戏官方资源中拉取最新游戏数据，解析后通过 MediaWiki API 写入 Wiki 对应页面（干员、敌人、关卡、家具、剧情、皮肤、模组、活动等）。

## 功能概览

- **多服支持**：CN（官服）、JP / US / KR（YoStar 海外服）、TW。
- **国服数据来源**：直接从 Mooncell 自建的资源仓库 [torappu](https://torappu.prts.wiki)（[API 文档](https://torappu.prts.wiki/api/v1/scalar)）按 `resVersion` 在线读取解包好的 gamedata，不再依赖 GitHub 上的 `ArknightsGameData` 仓库；下载过的文件缓存在 `.cache/torappu/<resVersion>/`。
- **海外服数据来源**：开源仓库 [`ArknightsGameData_YoStar`](https://github.com/Kengxxiao/ArknightsGameData_YoStar)（子模块）。
- **版本对比**：国服以 torappu 上 gamedata 已解包完成的最新版本为准，海外服查官方 CDN；仅在检测到 `resVersion` 变化时执行更新。
- **Wiki 写入**：封装 MediaWiki API 提供 `edit` / `read` / `category` / `protect` / `upload` 等操作，自动登录并带重试。
- **错误追踪**：通过 Sentry 上报运行异常。

## 项目结构

```text
ptilopsis/
├── __main__.py        # 入口，按命令行参数分派任务
├── config.py          # config.json 的 pydantic 模型 + 环境变量读取
├── gamedata/          # 各表的 pydantic 模型（由 FBS 生成，见下文「数据模型」）+ 客户端展示规则
├── jobs/              # 各类 Wiki 更新任务
│   ├── basic.py           # 干员基础信息（含后勤技能详情）
│   ├── sidebar.py         # 侧边栏干员一览
│   ├── charword.py        # 干员语音 / 档案
│   ├── skin.py            # 皮肤 / 立绘
│   ├── stage.py           # 关卡（含悖论模拟、剿灭等）
│   ├── enemy.py           # 敌人图鉴 / 数据
│   ├── furni.py           # 家具
│   ├── item.py            # 道具
│   ├── relic.py           # 集成战略收藏品
│   ├── medal.py           # 勋章
│   ├── mission.py         # 任务
│   ├── new_module.py      # 新模组
│   ├── activity.py        # 活动
│   ├── char_attr.py       # 干员属性
│   ├── story_review.py    # 剧情回顾
│   ├── term.py            # 术语
│   ├── update_jp.py       # JP 服增量更新
│   ├── weedy.py           # 高规格自动任务
│   ├── params.py          # job 可注入的现成依赖：各表的类型化模型、关卡加载器、RichText、CharIdTable …
│   └── ...
└── utils/
    ├── data.py            # GameData，统一访问 torappu（国服）/ 子模块（海外服）数据
    ├── torappu.py         # torappu HTTP 客户端：版本列表、文件下载、目录列举
    ├── unpacker.py        # 各服版本号检查与记录
    ├── wiki.py            # MediaWiki API 客户端（带 retry）
    ├── di.py              # 依赖注入：Depends / analyze / Resolver
    ├── job.py             # @job 注册表、JobContext、按名字调度
    └── richTextStyles.py  # 游戏富文本 → Wiki 模板转换
thirdparty/
├── OpenArknightsFBS/         # FlatBuffers schema (submodule，仅生成模型时用)
└── ArknightsGameData_YoStar/ # 海外服游戏数据 (submodule)
scripts/
├── gen_gamedata_models.py     # 从 FBS 生成 ptilopsis/gamedata 下的模型
├── parity_jobs.py             # 把各 job 生成的页面落盘，供重构前后 diff
└── parity_basic.py            # 同上，只针对 basic / char_attr 的渲染函数
.github/workflows/         # GitHub Actions 定时 / 手动触发
config.json                # 非敏感配置：各服 CDN 地址、FlatBuffers 表名等
.env.example               # 敏感配置的环境变量样例
version_local.json         # 本地已更新到的资源版本
version_remote.json        # 通过 --remote 拉取时使用的版本记录
```

## 配置

配置分为两部分，**敏感信息一律不入库**：

| 内容 | 位置 | 说明 |
| --- | --- | --- |
| torappu 地址、各服 CDN 地址、FlatBuffers 表名、chatMask 等 | `config.json` | 随仓库提交，由 `ptilopsis/config.py` 中的 pydantic 模型校验；字段名以 camelCase 书写，多余或缺失字段会直接报错 |
| Wiki 登录凭据、Sentry DSN | 环境变量 | 本地开发用 `.env`（已被 `.gitignore` 忽略），CI 用 GitHub Actions Secrets |

需要的环境变量：

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `PTILOPSIS_USERNAME` | 是 | Wiki 用户名，不带 `@BotName` 后缀 |
| `PTILOPSIS_PASSWORD` | 是 | 请使用 [Special:BotPasswords](https://prts.wiki/w/Special:BotPasswords) 生成的机器人密码，格式为 `<BotName>@<32位随机串>`，**不要使用主账号密码** |
| `PTILOPSIS_SENTRY_DSN` | 否 | 留空则不启用错误上报 |
| `PTILOPSIS_CONFIG_PATH` | 否 | 指定 `config.json` 路径，默认取工作目录 / 仓库根目录 |

本地开发：

```bash
cp .env.example .env   # 然后填入真实值
```

CI：在仓库 Settings → Secrets and variables → Actions 中添加同名 Secret，
`main1` ~ `main4` 四个 workflow 会自动注入。

> 注意：改动主账号密码会使该账号下**所有** BotPassword 失效，需要重新生成并更新 Secret。

## 环境准备

- Python ≥ 3.13
- [uv](https://docs.astral.sh/uv/)
- `flatc`（FlatBuffers 编译器，运行时位于仓库根目录调用）

```bash
git clone --recurse-submodules https://github.com/MooncellWiki/Ptilopsis_Bot.git
cd Ptilopsis_Bot
uv sync --locked
```

如果忘记 `--recurse-submodules`，可以补一句：

```bash
git submodule update --init --recursive
```

## 运行

`uv sync` 后会注册 `ptil` 命令

```bash
ptil [flags] [modes ...]
```

### 标志位（flags）

| 参数 | 作用 |
| --- | --- |
| `--check` | 检查 torappu 上是否有 gamedata 已就绪的新 CN 版本，无更新则退出 |
| `--check-jp` | 检查 JP / US / KR 服是否有新版本 |
| `--check-global` | 检查所有海外服版本后退出 |
| `--remote` | CI 模式：版本记录改用 `version_remote.json`，自动更新海外服数据子模块，并在结束后提交推送 |
| `--force` | 即便没有新版本也强制运行 |
| `--dev` | Wiki 客户端进入预览模式，仅打印将要提交的内容，不实际写入 |
| `-h`, `--help` | 显示完整帮助 |

### 任务模式（modes，可组合）

| 模式 | 包含任务 |
| --- | --- |
| `new` | 新干员相关：`sidebar.update` → `basic.run` → `charword.run` |
| `regular` | 常规更新：基建、关卡、敌人、皮肤、家具、道具、新模组、收藏品、活动、任务、属性、勋章、剧情、术语 |
| `special` | 干员详情 / 密录、悖论模拟、剿灭、语音补全等 |
| `jp` | JP 服增量更新 |
| `weedy` | 高规格自动任务 |
| `relic` | 单独维护集成战略收藏品页面（`regular` 已包含）：新建缺失的页面，给已有页面补上新主题（见下文） |
| `demand` | 占位 / 调试入口 |

### 常用调用示例

```bash
# 仅检查 CN 服并执行常规更新
ptil --check regular

# CI 模式：跑完 new + regular + special 并提交版本记录
ptil --check --remote new regular special

# 检查并更新 JP 服
ptil --check-jp --remote jp

# 预览模式：不真正提交到 Wiki
ptil --dev regular

# 单独维护收藏品页面（regular 已包含）：可先预览，确认后再正式写入
ptil --dev relic
ptil relic
```

### 收藏品页面（`relic`）

`relic.run` 读取国服 `roguelike_topic_table` 和灰蕈迷境的旧表 `roguelike_table`，每个收藏品一个页面，正文是
`{{收藏品/common}}`。不同主题里的同名收藏品合成一个页面，难度变体（`xx-α` 等）按生效难度写进同一主题。
同时收录 `ACTIVE_TOOL` 支援装备，使用同一个模板并标记 `类型=支援装备`，归入既有的 `分类:集成战略`。
支援装备页先显示黄色装备说明框，再显示与收藏品页面一致的售价、角标两个蓝色说明框。
支援装备不使用普通收藏品的售价公式；新主题的售价留空，已有的人工售价、角标与装置链接保留。
描述仅采用数据源的 `description` 字段，保留 wikitext 转义与换行处理，不解析或追加效果中的术语说明。
页面上的主题按发布时间从 1 连续编号，灰蕈排在最前，与 `rogue_N` 的 N 本身无关。
灰蕈只取 `RELIC` 且稀有度不为 `BORN` 的物品，不包含分队效果；售价直接使用旧表的 `value`。
仅出现在灰蕈的收藏品保留 `relic_N` 图标编号，由模板使用本站已有的 `收藏品 N.png`；
跨主题收藏品仍用最新主题的图标。与敌人重名的收藏品使用 `酸液源石虫(收藏品)`、`“复仇者”(收藏品)` 作为页面名，
保留原有敌人页。

维护规则是幂等的，重复运行不会产生新的编辑，因此不需要保存任何状态：

- 页面不存在：按全部主题新建，编辑摘要为 `init`。
- 页面已存在：刷新 `iconId` / `稀有度` / `描述`，按顺序插入页面上缺少的主题，编辑摘要为 `update`；
  已有主题参数只调整编号，字段值（角标、售价、效果等）、人工添加的参数和模板以外的正文都不动。
- 以下情况跳过并打 warning，需要人工处理：页面是重定向；页面已存在但不是收藏品页面（同名干员 / 道具等，
  需要建立消歧义页）；页面上的主题名或顺序与游戏数据对不上；页面 `iconId`
  所在的主题比游戏数据还新。
- 读取后页面被他人改动或删除时放弃这次编辑，下次运行重新合并。

`模板:收藏品/common` 支持 7 个主题，有收藏品超过时会打 warning 提醒先扩展模板。
收藏品维护已包含在 `regular` 中，国服更新 workflow 会自动执行，不经过预览；也可用 `relic` 模式单独运行。
首次运行可能批量新建或改写几百个页面，想先确认内容的话，要在下一次国服更新 workflow 之前手动跑
`ptil --dev relic` 预览，再用 `ptil relic` 正式写入。

## GitHub Actions

| Workflow | 触发 | 命令 |
| --- | --- | --- |
| `main-cn` | `workflow_dispatch` | `ptil --check --remote new regular special` |
| `main-cn-force` | `workflow_dispatch` | 同上，附 `--force` |
| `main-jp` | `workflow_dispatch` | `ptil --check-jp --remote jp` |
| `weedy` | `workflow_dispatch` | `ptil weedy` |
| `ruff` | `push: master` / PR | Ruff lint |

## 开发

使用 [Ruff](https://github.com/astral-sh/ruff)

```bash
uv run ruff check .
uv run ruff format .
```

### 数据模型

job 读到的 gamedata 全部是 pydantic 模型，不再直接操作 dict。`ptilopsis/gamedata/` 下的整表模型由
`thirdparty/OpenArknightsFBS/FBS/*.fbs` 生成，FBS 更新后重新生成即可：

```bash
uv run python scripts/gen_gamedata_models.py --all              # 项目用到的全部表
uv run python scripts/gen_gamedata_models.py character_table    # 只生成指定表
```

- 生成规则：`table clz_Torappu_X` → `class X(GameDataModel)`，字段名转 snake_case
  （`def` → `def_`、`dict` → `dict_` 这类与关键字 / 类型名撞车的加下划线并给 alias）；
  `[dict__K__V]` → `dict[K, V]`；`kvp__K__V` → 带 `key` / `value` 的类；
  `enum__X` 字段保留成员名字符串，同时生成 `IntEnum` 供比较顺序；
  `SimpleKVTable` 根表 → `TypeAdapter(dict[str, X])`。
- FlatBuffers 里 string / table / vector 字段都可能缺失，生成的模型把它们一律声明成
  `T | None`，未判空的访问会被 pyright 指出；标量按 FBS 默认值填充。
- `levels/*.json`（关卡地图、波次、预设编队）的模型在 `level_data.py`，来自 `prts___levels.fbs`。
- `range_table` / `battle_misc_table` / `roguelike_table` 没有 FBS schema，是按同样约定手写的。
- 新表生成好模型后，在 `ptilopsis/jobs/params.py` 的 `TABLES` 里登记路径与模型，
  再加一个 `XxxTable` 别名即可注入。

### 页面比对

改动 job 的渲染逻辑后，用 `scripts/parity_jobs.py` 把各 job 生成的页面落盘做 diff。它不登录 wiki：
`edit` 只记录不提交，`read` 匿名读取真实页面并缓存到 `.cache/wiki/`，`category` 返回空列表以便把
"只处理未建页条目"的 job 全量跑一遍（数据按 `version_local.json` 里的国服版本从 torappu 读取）：

```bash
PYTHONHASHSEED=0 uv run python scripts/parity_jobs.py out/before            # 全部 job
PYTHONHASHSEED=0 uv run python scripts/parity_jobs.py out/before --jobs stage.run item.run
# 切换分支后
PYTHONHASHSEED=0 uv run python scripts/parity_jobs.py out/after
diff -r out/before out/after
```

脚本默认使用自身所在仓库的 `.cache/` 和 `thirdparty/ArknightsGameData_YoStar/`。
跨 worktree 共用数据时，由调用方通过 `--data-root` 指定这两个目录所在的根目录。
例如，主工作区使用常规 `.git/` 目录的仓库，可以在 worktree 中这样调用：

```bash
PYTHONHASHSEED=0 uv run python scripts/parity_jobs.py out/after \
  --data-root "$(git rev-parse --path-format=absolute --git-common-dir)/.."
```

脚本本身不调用 Git；也可以直接传入 `--data-root /path/to/shared-data`。
国服版本仍由当前运行目录的 `version_local.json` 决定。

`scripts/parity_basic.py` 是只针对 `basic` / `char_attr` 渲染函数的旧版本，用法相同。

仓库已配置 `pre-commit`，建议本地启用：

```bash
uv run pre-commit install
```

### 编写 job

job 是用 `@job` 注册的普通函数，参数按注解注入（实现见 `ptilopsis/utils/di.py`，
借鉴 torappu 的 task 写法）；gamedata 一律以 `ptilopsis/gamedata/` 里的模型注入：

```python
from typing import Annotated

from ptilopsis.gamedata.character_table import CharacterData
from ptilopsis.jobs.params import (
    CharacterTable, CharIdTable, ItemTable, Levels, RichText, StageTable, category, table,
)
from ptilopsis.utils.job import SkipJob, job
from ptilopsis.utils.wiki import Wiki


@job
def run(
    wiki: Wiki,
    item_table: ItemTable,                      # InventoryData
    stage_table: StageTable,                    # StageTable
    character_table_jp: Annotated[
        dict[str, CharacterData], table("character_table", "JP")
    ],                                          # 海外服数据指定 region
    levels: Levels,                             # levels(level_id) -> LevelData
    id_table: CharIdTable,
    rts: RichText,
    pages: Annotated[list[str], category("分类:道具")],
) -> None:
    for stage in stage_table.stages.values():
        if stage.level_id:
            level = levels(stage.level_id)
    ...
```

- `Wiki` / `GameData` / `Config` / `JobContext` 直接按类型注入，其余依赖用 `Depends`
  标记；`params.py` 里放着各表的类型化别名（`CharacterTable`、`ItemTable` …）、
  关卡加载器 `Levels`、敌人数据库索引 `EnemyLevels`、富文本转换器 `RichText` /
  `RichTextHtml`、干员序号表 `CharIdTable` 等。
- 同一次运行里相同的依赖只解析一次；依赖或 job 抛 `SkipJob` 表示这次没事可做。
- job 名默认是 `<模块>.<函数>`，`__main__.py` 的 `MODE_JOBS` 用它编排各模式的执行顺序。
  签名有问题（参数注不进去）会在导入时就报错。
- 模型字段都可能为 `None`（见「数据模型」），改渲染逻辑后用 `scripts/parity_jobs.py` 比对页面。

## 致谢

- [torappu](https://torappu.prts.wiki) — Mooncell 自建的明日方舟资源仓库，国服游戏数据来源
- [MooncellWiki/OpenArknightsFBS](https://github.com/MooncellWiki/OpenArknightsFBS) — FlatBuffers schema
- [Kengxxiao/ArknightsGameData_YoStar](https://github.com/Kengxxiao/ArknightsGameData_YoStar) — 海外服游戏数据

import subprocess

import anyio
import click
import sentry_sdk

from ptilopsis.config import Config, Settings, config, get_settings
from ptilopsis.jobs import discover_jobs
from ptilopsis.log import logger
from ptilopsis.utils.data import YOSTAR_DIR, GameData
from ptilopsis.utils.job import JobContext, registered_jobs, run_jobs
from ptilopsis.utils.wiki import Wiki

MODE_JOBS: dict[str, list[str]] = {
    # 先 sidebar，避免影响 old_num
    "new": ["sidebar.update", "basic.run", "charword.run"],
    "regular": [
        "stage.run",
        "enemy.run",
        "enemy.update_data",
        "skin.run",
        "furni.run",
        "item.run",
        "new_module.run",
        "relic.run",
        "activity.run",
        "mission.run",
        "char_attr.run",
        "medal.run",
        "story_review.run",
        "term.run",
    ],
    "special": [
        # "furni.update",
        "basic.update",  # 干员详情
        "basic.update_handbook",  # 干员密录
        "stage.run_memory",  # 悖论模拟
        "stage.run_campaign",  # 剿灭
        # "stage.run_crisis",  # 需 crisis_info
        # "stage.run_rogue_like",
        # "stage.run_recalrune",
        "charword.update",
        # "route.run", "formula.run", "range.run",
    ],
    # "demand.run" 尚未启用
    "demand": [],
    "jp": ["charword.update", "update_jp.run"],
    "weedy": ["weedy.run"],
    # 收藏品也在 regular 中;此模式可单独维护收藏品页面
    "relic": ["relic.run"],
    "medal": ["medal.run"],
    # 集成战略关卡,出新主题 / DLC 时手动跑;主题见 stage.ROGUE_TOPIC
    "rogue": ["stage.run_rogue_like"],
}
"""各模式按顺序执行的 job 名(``<模块>.<函数>``),多个模式按这里的键顺序合并,
同一个 job 出现在多个模式里时只在第一次出现的位置执行一次。"""

MODES = list(MODE_JOBS)


def jobs_for(args: tuple[str, ...]) -> list[str]:
    """把 mode 名与 job 名(``<模块>.<函数>``)混合的参数解析成 job 名列表。

    需要先 :func:`~ptilopsis.jobs.discover_jobs`。mode 名仍按
    :data:`MODE_JOBS` 的键顺序展开;显式 job 名追加在所有 mode 展开之后,
    整体保序去重。名字不属于任何 mode 或已注册 job 时抛
    :class:`click.UsageError`;显式 job 的先后依赖(sidebar 先于 basic)由
    调用者自己保证。
    """
    if not args:
        return []
    known = {job.name for job in registered_jobs()}
    unknown = [arg for arg in args if arg not in MODE_JOBS and arg not in known]
    if unknown:
        raise click.UsageError(
            f"unknown mode/job: {', '.join(unknown)}.\n"
            f"modes: {', '.join(MODES)}\n"
            f"jobs: {', '.join(sorted(known))}"
        )
    names = list(
        dict.fromkeys(
            name for mode, jobs in MODE_JOBS.items() if mode in args for name in jobs
        )
    )
    missing = [name for name in names if name not in known]
    if missing:
        # MODE_JOBS 里的笔误属于配置错误,同样在一切网络操作之前失败
        raise click.UsageError(
            f"MODE_JOBS references unregistered jobs: {', '.join(missing)}.\n"
            f"registered: {', '.join(sorted(known))}"
        )
    seen = set(names)
    for arg in args:
        if arg not in MODE_JOBS and arg not in seen:
            seen.add(arg)
            names.append(arg)
    return names


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--check",
    "check_mode",
    flag_value="cn",
    default=None,
    help="检查 CN 服是否有新版本，无更新则退出",
)
@click.option(
    "--check-jp",
    "check_mode",
    flag_value="jp",
    help="检查 JP / US / KR 服是否有新版本",
)
@click.option(
    "--check-global",
    "check_mode",
    flag_value="global",
    help="检查所有海外服后退出",
)
@click.option(
    "--remote",
    is_flag=True,
    help="CI 模式：版本记录用 version_remote.json，拉取海外服数据子模块，"
    "结束后自动提交推送",
)
@click.option(
    "--force",
    is_flag=True,
    help="即便没有新版本也强制运行（仅对 --check 生效）",
)
@click.option(
    "--dev",
    "dev",
    is_flag=True,
    help="Wiki 客户端预览模式，仅打印将要提交的内容，不实际写入",
)
@click.argument(
    "modes",
    nargs=-1,
    help="要运行的 mode 名或 job 名(module.function),如 "
    '"new regular special" 或 "stage.run"',
)
def main(
    check_mode: str | None,
    remote: bool,
    force: bool,
    dev: bool,
    modes: tuple[str, ...],
) -> None:
    settings = get_settings()
    if settings.sentry_dsn:
        sentry_sdk.init(dsn=settings.sentry_dsn, traces_sample_rate=1.0)

    # 有 Wiki 任务时先校验凭据再跑检查，缺失时不做任何网络请求就退出
    if modes:
        settings.require_wiki_credentials()

    # 名字先全部解析一遍，写错任何一个都不做任何网络/git 操作就退出
    if modes:
        discover_jobs()
    jobs = jobs_for(modes)

    if remote:
        # 国服数据在线读 torappu，只有海外服还依赖子模块
        _git("submodule", "update", "--init", "--remote", "--", YOSTAR_DIR)
        game_config = config.model_copy(update={"version": "version_remote.json"})
    else:
        game_config = config

    # 网络 I/O 全部在 anyio 事件循环里跑（与 torappu 一致）；git 操作留在外面
    should_push = anyio.run(_amain, game_config, settings, check_mode, force, dev, jobs)
    if should_push:
        _push_remote(remote)


async def _amain(
    game_config: Config,
    settings: Settings,
    check_mode: str | None,
    force: bool,
    dev: bool,
    jobs: list[str],
) -> bool:
    """检查版本、跑 job；返回是否需要提交推送。"""
    gamedata = GameData(config=game_config)
    try:
        if check_mode == "cn":
            if not await gamedata.unpacker.check_update() and not force:
                gamedata.unpacker.commit_version()
                logger.info("No version update. Program exit.")
                return False
        elif check_mode == "jp":
            sign1 = await gamedata.unpacker.check_update("JP")
            sign2 = await gamedata.unpacker.check_update("US")
            await gamedata.unpacker.check_update("KR")
            if not sign1 and not sign2:
                gamedata.unpacker.commit_version()
                logger.info("No version update. Program exit.")
                return False
        elif check_mode == "global":
            await gamedata.unpacker.check_all_update()
            gamedata.unpacker.commit_version()
            # 只记录版本号不跑任务；--remote 下要推送，否则记录只留在 CI 的工作区里
            return True

        if not jobs:
            gamedata.unpacker.commit_version()
            return True

        username, password = settings.require_wiki_credentials()
        wiki = await Wiki.login(
            config.api_url,
            username,
            password,
            "dev" if dev else "product",
            rate_safety=settings.rate_safety,
            write_min_interval=settings.write_min_interval,
        )
        try:
            # 登录成功后才推进版本号：登录失败（凭据缺失/过期/被吊销）时保持旧版本，
            # 下一次运行仍能检测到更新并重跑，而不是被误判为「无更新」而跳过
            gamedata.unpacker.commit_version()

            failed = await run_jobs(jobs, JobContext(wiki, gamedata))
            if failed:
                logger.error(f"{len(failed)} job(s) failed: {', '.join(failed)}")
        finally:
            await wiki.aclose()
    finally:
        await gamedata.aclose()
    return True


def _push_remote(remote: bool) -> None:
    """--remote 模式下把更新后的数据与版本号提交推送。"""
    if not remote:
        return
    _git("add", ".")
    _git("commit", "-m", "remote update")
    _git("push")


def _git(*args: str) -> None:
    # 与之前的 os.system 一样不检查返回码：没有改动时 commit 失败也照常往下走
    subprocess.run(["git", *args], check=False)


if __name__ == "__main__":
    main()

"""``ptil`` 命令行参数解析:modes 既接受 mode 名也接受 job 名。"""

import pytest
from click.exceptions import UsageError

from ptilopsis.__main__ import MODE_JOBS, jobs_for
from ptilopsis.jobs import discover_jobs


def test_expands_modes_in_declared_order() -> None:
    # 参数顺序不影响展开顺序,仍按 MODE_JOBS 的键顺序
    discover_jobs()
    assert jobs_for(("special", "new")) == [
        *MODE_JOBS["new"],
        *MODE_JOBS["special"],
    ]


def test_appends_job_names_after_modes() -> None:
    discover_jobs()
    assert jobs_for(("new", "relic.run")) == [*MODE_JOBS["new"], "relic.run"]


def test_dedupes_job_already_covered_by_mode() -> None:
    discover_jobs()
    assert jobs_for(("regular", "furni.run")) == MODE_JOBS["regular"]


def test_dedupes_repeated_job_names() -> None:
    discover_jobs()
    assert jobs_for(("relic.run", "relic.run")) == ["relic.run"]


def test_mode_jobs_only_references_registered_jobs() -> None:
    # MODE_JOBS 里的笔误同样在启动时就失败,而不是登录 Wiki 之后
    discover_jobs()
    for mode in MODE_JOBS:
        jobs_for((mode,))


def test_rejects_unknown_name() -> None:
    with pytest.raises(UsageError, match=r"unknown mode/job: nope\.run"):
        jobs_for(("regular", "nope.run"))


def test_empty_args() -> None:
    assert jobs_for(()) == []

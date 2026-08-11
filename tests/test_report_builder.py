from datetime import datetime, timedelta, timezone

import pytest

from jason.execution_result import ExecutionResult
from jason.report_builder import ReportBuilder
from jason.sprint import Sprint, SprintResult
from jason.task import Task


def make_sprint(*task_ids: str) -> Sprint:
    return Sprint(
        id="sprint-1",
        title="Sprint de relatórios",
        tasks=tuple(Task(task_id, f"Tarefa {task_id}", "Executar") for task_id in task_ids),
    )


def test_builds_report_for_a_fully_successful_sprint():
    sprint = make_sprint("task-1", "task-2")
    sprint_result = SprintResult(
        sprint_id=sprint.id,
        task_results=(
            ExecutionResult("ok", "", 0),
            ExecutionResult("ok", "", 0),
        ),
    )
    started_at = datetime(2026, 7, 29, 10, tzinfo=timezone.utc)
    finished_at = started_at + timedelta(seconds=45)

    report = ReportBuilder().build(
        sprint, sprint_result, started_at=started_at, finished_at=finished_at
    )

    assert report.sprint_id == sprint.id
    assert report.total_tasks == 2
    assert report.successful_tasks == 2
    assert report.failed_tasks == 0
    assert report.duration == timedelta(seconds=45)
    assert report.task_results == sprint_result.task_results


def test_counts_failed_tasks_from_non_zero_returncodes():
    sprint = make_sprint("task-1", "task-2", "task-3")
    sprint_result = SprintResult(
        sprint_id=sprint.id,
        task_results=(
            ExecutionResult("ok", "", 0),
            ExecutionResult("", "erro", 1),
            ExecutionResult("", "erro", 2),
        ),
    )

    report = ReportBuilder().build(
        sprint,
        sprint_result,
        started_at=datetime(2026, 7, 29, 10, tzinfo=timezone.utc),
        finished_at=datetime(2026, 7, 29, 10, 2, tzinfo=timezone.utc),
    )

    assert report.total_tasks == 3
    assert report.successful_tasks == 1
    assert report.failed_tasks == 2
    assert report.duration == timedelta(minutes=2)


def test_rejects_incompatible_sprint_and_result_instead_of_masking_them():
    sprint = make_sprint("task-1", "task-2")
    incomplete_result = SprintResult(
        sprint_id=sprint.id,
        task_results=(ExecutionResult("ok", "", 0),),
    )

    with pytest.raises(ValueError, match="mesma quantidade de tarefas"):
        ReportBuilder().build(
            sprint,
            incomplete_result,
            started_at=datetime(2026, 7, 29, 10, tzinfo=timezone.utc),
            finished_at=datetime(2026, 7, 29, 10, 1, tzinfo=timezone.utc),
        )

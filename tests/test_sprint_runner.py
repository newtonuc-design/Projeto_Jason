from jason.execution_result import ExecutionResult
from jason.sprint import Sprint, SprintResult
from jason.sprint_runner import SprintRunner
from jason.task import Task


class FakeTaskRunner:
    def __init__(self) -> None:
        self.tasks = []

    def run(self, task):
        self.tasks.append(task)
        return ExecutionResult(stdout=task.id, stderr="", returncode=0)


def test_sprint_contains_only_its_planned_work():
    sprint = Sprint(
        id="sprint-1",
        title="Sprint inicial",
        tasks=(Task("task-1", "Planejar", "Planeje a entrega."),),
    )

    assert sprint.id == "sprint-1"
    assert sprint.tasks[0].id == "task-1"
    assert not hasattr(sprint, "task_results")


def test_sprint_runner_returns_result_without_mutating_sprint_definition():
    task = Task("task-1", "Planejar", "Planeje a entrega.")
    sprint = Sprint(id="sprint-1", title="Sprint inicial", tasks=(task,))
    task_runner = FakeTaskRunner()

    result = SprintRunner(task_runner).run(sprint)

    assert isinstance(result, SprintResult)
    assert result.sprint_id == sprint.id
    assert result.task_results == (ExecutionResult("task-1", "", 0),)
    assert task_runner.tasks == [task]
    assert sprint.tasks == (task,)
    assert not hasattr(result, "tasks")

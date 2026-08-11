from jason.execution_plan import ExecutionPlan, PlanResult
from jason.execution_result import ExecutionResult
from jason.plan_runner import PlanRunner
from jason.sprint import Sprint, SprintResult
from jason.task import Task


class FakeSprintRunner:
    def __init__(self) -> None:
        self.executed_sprint_ids = []

    def run(self, sprint: Sprint) -> SprintResult:
        self.executed_sprint_ids.append(sprint.id)
        return SprintResult(
            sprint_id=sprint.id,
            task_results=(ExecutionResult(sprint.id, "", 0),),
        )


def make_sprint(sprint_id: str) -> Sprint:
    return Sprint(
        id=sprint_id,
        title=f"Sprint {sprint_id}",
        tasks=(Task(f"{sprint_id}-task", "Executar", "Execute a tarefa."),),
    )


def test_plan_runner_executes_sprints_in_the_plan_order():
    first_sprint = make_sprint("sprint-1")
    second_sprint = make_sprint("sprint-2")
    plan = ExecutionPlan(
        id="plan-1",
        title="Plano inicial",
        objective="Entregar as duas sprints.",
        sprints=(first_sprint, second_sprint),
    )
    sprint_runner = FakeSprintRunner()

    result = PlanRunner(sprint_runner).run(plan)

    assert isinstance(result, PlanResult)
    assert sprint_runner.executed_sprint_ids == ["sprint-1", "sprint-2"]
    assert [item.sprint_id for item in result.sprint_results] == ["sprint-1", "sprint-2"]
    assert result.plan_id == plan.id
    assert result.total_sprints == 2
    assert result.executed_sprints == 2
    assert plan.sprints == (first_sprint, second_sprint)


def test_plan_runner_returns_empty_result_for_a_plan_without_sprints():
    plan = ExecutionPlan(
        id="plan-empty",
        title="Plano vazio",
        objective="Não há trabalho planejado.",
        sprints=(),
    )
    sprint_runner = FakeSprintRunner()

    result = PlanRunner(sprint_runner).run(plan)

    assert sprint_runner.executed_sprint_ids == []
    assert result.sprint_results == ()
    assert result.total_sprints == 0
    assert result.executed_sprints == 0

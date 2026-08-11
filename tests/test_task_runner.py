from jason.execution_result import ExecutionResult
from jason.task import Task
from jason.task_runner import TaskRunner


class FakeExecutor:
    def __init__(self, result):
        self.result = result
        self.instructions = []

    def execute(self, instruction):
        self.instructions.append(instruction)
        return self.result


def test_task_runner_delegates_task_instruction_to_executor_and_returns_its_result():
    execution_result = ExecutionResult("saida", "", 0)
    executor = FakeExecutor(execution_result)
    task = Task(
        id="task-123",
        title="Revisar módulo",
        instruction="Revise o módulo de autenticação.",
    )

    result = TaskRunner(executor).run(task)

    assert executor.instructions == ["Revise o módulo de autenticação."]
    assert result is execution_result

"""Execução sequencial das tarefas definidas em uma sprint."""

from __future__ import annotations

from .sprint import Sprint, SprintResult
from .task_runner import TaskRunner


class SprintRunner:
    """Executa as tarefas planejadas sem alterar a definição da sprint."""

    def __init__(self, task_runner: TaskRunner) -> None:
        self._task_runner = task_runner

    def run(self, sprint: Sprint) -> SprintResult:
        """Executa cada tarefa e devolve um resultado independente."""
        task_results = tuple(self._task_runner.run(task) for task in sprint.tasks)
        return SprintResult(sprint_id=sprint.id, task_results=task_results)

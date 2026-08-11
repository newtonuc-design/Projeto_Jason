"""Camada mínima que delega tarefas a um executor."""

from __future__ import annotations

from .executor import Executor
from .execution_result import ExecutionResult
from .task import Task


class TaskRunner:
    """Obtém a instrução da tarefa e delega sua execução a um Executor."""

    def __init__(self, executor: Executor) -> None:
        self._executor = executor

    def run(self, task: Task) -> ExecutionResult:
        """Executa a instrução da tarefa sem compor ou alterar prompts."""
        return self._executor.execute(task.instruction)

"""Modelos independentes para planejamento e execução de sprints."""

from __future__ import annotations

from dataclasses import dataclass

from .execution_result import ExecutionResult
from .task import Task


@dataclass(frozen=True)
class Sprint:
    """Definição imutável de uma sprint e das tarefas que a compõem.

    Este modelo descreve o trabalho planejado. Ele não contém estado nem
    evidências da execução.
    """

    id: str
    title: str
    tasks: tuple[Task, ...]


@dataclass(frozen=True)
class SprintResult:
    """Resultado exclusivo da execução de uma sprint.

    A definição da sprint permanece em :class:`Sprint`; este modelo registra
    somente as saídas devolvidas para as tarefas executadas.
    """

    sprint_id: str
    task_results: tuple[ExecutionResult, ...]

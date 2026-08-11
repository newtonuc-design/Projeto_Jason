"""Modelos de planejamento e resultado da execução de múltiplas sprints."""

from __future__ import annotations

from dataclasses import dataclass

from .sprint import Sprint, SprintResult


@dataclass(frozen=True)
class ExecutionPlan:
    """Definição ordenada das sprints necessárias para atingir um objetivo."""

    id: str
    title: str
    objective: str
    sprints: tuple[Sprint, ...]


@dataclass(frozen=True)
class PlanResult:
    """Resultados produzidos ao executar as sprints de um plano."""

    plan_id: str
    sprint_results: tuple[SprintResult, ...]
    total_sprints: int
    executed_sprints: int

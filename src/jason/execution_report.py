"""Modelo de relatório para uma execução de sprint."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

from .execution_result import ExecutionResult


@dataclass(frozen=True)
class ExecutionReport:
    """Métricas e resultados produzidos por uma execução de sprint."""

    sprint_id: str
    started_at: datetime
    finished_at: datetime
    duration: timedelta
    total_tasks: int
    successful_tasks: int
    failed_tasks: int
    task_results: tuple[ExecutionResult, ...]

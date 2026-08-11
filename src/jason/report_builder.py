"""Transformação determinística de resultados de sprint em relatórios."""

from __future__ import annotations

from datetime import datetime

from .execution_report import ExecutionReport
from .sprint import Sprint, SprintResult


class ReportBuilder:
    """Produz relatórios sem executar, persistir ou corrigir dados de origem."""

    def build(
        self,
        sprint: Sprint,
        sprint_result: SprintResult,
        *,
        started_at: datetime,
        finished_at: datetime,
    ) -> ExecutionReport:
        """Transforma dados compatíveis de uma sprint em um relatório.

        A incompatibilidade entre planejamento e execução é um erro de entrada:
        ela não é completada nem inferida por este componente.
        """
        if sprint.id != sprint_result.sprint_id:
            raise ValueError("Sprint e SprintResult devem possuir o mesmo sprint_id.")
        if len(sprint.tasks) != len(sprint_result.task_results):
            raise ValueError("Sprint e SprintResult devem possuir a mesma quantidade de tarefas.")

        successful_tasks = sum(
            result.returncode == 0 for result in sprint_result.task_results
        )
        total_tasks = len(sprint.tasks)

        return ExecutionReport(
            sprint_id=sprint.id,
            started_at=started_at,
            finished_at=finished_at,
            duration=finished_at - started_at,
            total_tasks=total_tasks,
            successful_tasks=successful_tasks,
            failed_tasks=total_tasks - successful_tasks,
            task_results=sprint_result.task_results,
        )

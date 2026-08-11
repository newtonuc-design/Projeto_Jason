"""Orquestração sequencial de sprints pertencentes a um plano."""

from __future__ import annotations

from .execution_plan import ExecutionPlan, PlanResult
from .sprint_runner import SprintRunner


class PlanRunner:
    """Delega cada sprint na ordem definida pelo plano."""

    def __init__(self, sprint_runner: SprintRunner) -> None:
        self._sprint_runner = sprint_runner

    def run(self, plan: ExecutionPlan) -> PlanResult:
        """Executa cada sprint uma única vez, na ordem recebida."""
        sprint_results = tuple(self._sprint_runner.run(sprint) for sprint in plan.sprints)
        return PlanResult(
            plan_id=plan.id,
            sprint_results=sprint_results,
            total_sprints=len(plan.sprints),
            executed_sprints=len(sprint_results),
        )

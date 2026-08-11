"""
Reasoner

Converte um ExecutionPlan em uma Decision.
"""

from __future__ import annotations

from .decision import Decision
from .execution_plan import ExecutionPlan


class Reasoner:

    def decide(self, plan: ExecutionPlan) -> Decision:

        return Decision(
            action=f"Executar plano: {plan.objective}",
            confidence=1.0,
            rationale=f"{plan.total_steps} etapas planejadas."
        )


"""
Planner

Transforma uma WorkRequest em um ExecutionPlan.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .execution_plan import ExecutionPlan
from .models import WorkRequest


class Planner(ABC):

    @abstractmethod
    def create_plan(self, request: WorkRequest) -> ExecutionPlan:
        """
        Produz um plano de execução.
        """
        raise NotImplementedError


class DefaultPlanner(Planner):

    def create_plan(self, request: WorkRequest) -> ExecutionPlan:

        plan = ExecutionPlan(
            objective=request.intent
        )

        plan.add_step("Receber solicitação")

        plan.add_step("Analisar contexto")

        plan.add_step("Executar tarefa")

        return plan


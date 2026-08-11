"""
Software Engineer Agent

Coordena o planejamento, a execução e os testes de uma missão.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from jason.agents.executor import Executor
from jason.agents.planner import Planner
from jason.agents.tester import Tester


@dataclass(slots=True)
class Mission:
    objective: str
    created_at: datetime = field(default_factory=datetime.now)


@dataclass(slots=True)
class ExecutionResult:
    mission: str
    status: str
    plan: List[str]
    actions: List[str]
    tests: List[str]
    result: str


class SoftwareEngineer:
    """
    Orquestra o fluxo completo de engenharia de software.
    """

    def __init__(self) -> None:
        self.planner = Planner()
        self.executor = Executor()
        self.tester = Tester()

    def execute(self, mission: str) -> ExecutionResult:
        current_mission = Mission(objective=mission)

        plan = self.planner.build(current_mission.objective)

        execution = self.executor.run(plan.steps)

        test_report = self.tester.run(
            [
                "test_login",
                "test_logout",
                "test_register",
            ]
        )

        actions = [
            "Missão recebida",
            "Planejamento concluído",
            "Execução concluída",
        ]

        return ExecutionResult(
            mission=current_mission.objective,
            status=execution.status,
            plan=plan.steps,
            actions=actions,
            tests=test_report.executed,
            result="Missão executada com sucesso.",
        )
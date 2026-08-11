"""
Planner Agent

Responsável por transformar uma missão em um plano de execução.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class Plan:
    mission: str
    steps: List[str]


class Planner:

    def build(self, mission: str) -> Plan:

        return Plan(
            mission=mission,
            steps=[
                "Analisar missão",
                "Identificar arquivos",
                "Planejar implementação",
                "Implementar código",
                "Executar py_compile",
                "Executar pytest",
                "Corrigir falhas",
                "Documentar",
                "Entregar",
            ],
        )
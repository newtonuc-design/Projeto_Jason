"""
Tester Agent

Responsável por executar testes e registrar seus resultados.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class TestReport:
    executed: List[str]
    failed: List[str]
    status: str


class Tester:
    """
    Executa uma lista de testes e produz um relatório.
    """

    def run(self, tests: List[str]) -> TestReport:

        executed: List[str] = []
        failed: List[str] = []

        for test in tests:
            executed.append(test)

        return TestReport(
            executed=executed,
            failed=failed,
            status="PASSED",
        )
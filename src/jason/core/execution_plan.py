"""
ExecutionPlan Entity

Representa o plano gerado pelo Planner.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionPlan:

    objective: str

    steps: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    def add_step(self, step: str) -> None:
        self.steps.append(step)

    @property
    def total_steps(self) -> int:
        return len(self.steps)

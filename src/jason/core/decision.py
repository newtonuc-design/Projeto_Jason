"""
Decision Entity

Representa a decisão tomada pelo Reasoner.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Decision:

    action: str

    confidence: float = 1.0

    rationale: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    def approved(self) -> bool:
        return self.confidence >= 0.80


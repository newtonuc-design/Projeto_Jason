"""
Agent Entity

Representa um trabalhador digital do ecossistema Jason.
"""

from dataclasses import dataclass, field
from typing import Any

from .models import AgentProfile


@dataclass
class Agent:
    profile: AgentProfile

    memory: Any | None = None
    knowledge: Any | None = None
    planner: Any | None = None
    reasoning: Any | None = None
    toolbox: Any | None = None
    runtime: Any | None = None

    state: dict = field(default_factory=dict)
    metrics: dict = field(default_factory=dict)

    def is_enabled(self) -> bool:
        return self.profile.enabled

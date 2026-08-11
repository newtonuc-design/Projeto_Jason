from __future__ import annotations

from jason.core.models import (
    AgentProfile,
    AgentResult,
    Handoff,
    RiskLevel,
)


class PythonAgent:
    """Primeiro agente especializado do Jason."""

    @property
    def profile(self) -> AgentProfile:
        return AgentProfile(
            agent_id="python-agent",
            capabilities=frozenset({"python"}),
            permitted_risk=RiskLevel.MEDIUM,
        )

    def execute(self, handoff: Handoff) -> AgentResult:
        return AgentResult(
            success=True,
            summary=f"PythonAgent executou '{handoff.intent}'.",
        )
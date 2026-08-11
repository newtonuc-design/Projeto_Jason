"""Adaptadores em memória para desenvolvimento local e testes."""

from __future__ import annotations

from collections import defaultdict

from .core.models import AgentProfile, AuditEvent, RiskLevel
from .core.ports import SpecializedAgent


class InMemoryMemory:
    def __init__(self) -> None:
        self.records: dict[str, list[dict]] = defaultdict(list)

    def recall(self, query: str, *, correlation_id: str, limit: int = 5) -> list[dict]:
        query_terms = set(query.lower().split())
        matches = [
            item for item in self.records[correlation_id]
            if query_terms.intersection(str(item).lower().split())
        ]
        return matches[-limit:]

    def remember(self, record: dict, *, correlation_id: str) -> None:
        self.records[correlation_id].append(record)


class InMemoryAudit:
    def __init__(self) -> None:
        self.events: list[AuditEvent] = []

    def record(self, event: AuditEvent) -> None:
        self.events.append(event)


class InMemoryAgentRegistry:
    def __init__(self, agents: list[SpecializedAgent] | None = None) -> None:
        self._agents = list(agents or [])

    def register(self, agent: SpecializedAgent) -> None:
        self._agents.append(agent)

    def find(self, capabilities: frozenset[str], risk: RiskLevel) -> SpecializedAgent | None:
        candidates = [
            agent for agent in self._agents
            if agent.profile.enabled
            and capabilities.issubset(agent.profile.capabilities)
            and risk <= agent.profile.permitted_risk
        ]
        return sorted(candidates, key=lambda agent: agent.profile.agent_id)[0] if candidates else None


class DefaultApprovalPolicy:
    """Ações de risco alto/crítico nunca são liberadas automaticamente."""

    def requires_approval(self, *, risk: RiskLevel, explicitly_required: bool) -> bool:
        return explicitly_required or risk >= RiskLevel.HIGH

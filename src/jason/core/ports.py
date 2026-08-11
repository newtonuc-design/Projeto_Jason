"""Portas para integrações; adaptadores concretos ficam fora do núcleo."""

from __future__ import annotations

from typing import Protocol

from .models import AgentProfile, AgentResult, AuditEvent, Handoff, RiskLevel


class MemoryPort(Protocol):
    def recall(self, query: str, *, correlation_id: str, limit: int = 5) -> list[dict]: ...

    def remember(self, record: dict, *, correlation_id: str) -> None: ...


class AuditPort(Protocol):
    def record(self, event: AuditEvent) -> None: ...


class SpecializedAgent(Protocol):
    @property
    def profile(self) -> AgentProfile: ...

    def execute(self, handoff: Handoff) -> AgentResult: ...


class AgentRegistryPort(Protocol):
    def find(self, capabilities: frozenset[str], risk: RiskLevel) -> SpecializedAgent | None: ...


class ApprovalPolicy(Protocol):
    def requires_approval(self, *, risk: RiskLevel, explicitly_required: bool) -> bool: ...

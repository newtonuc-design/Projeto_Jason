"""Modelos do domínio de orquestração definidos pelo ADR-0004."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, IntEnum
from typing import Any
from uuid import uuid4


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Priority(IntEnum):
    LOW = 10
    NORMAL = 50
    HIGH = 80
    CRITICAL = 100


class RiskLevel(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class TaskStatus(str, Enum):
    RECEIVED = "received"
    PENDING_APPROVAL = "pending_approval"
    DISPATCHED = "dispatched"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class AgentProfile:
    """Identidade, capacidades e limites de um agente especializado."""

    agent_id: str
    capabilities: frozenset[str]
    permitted_risk: RiskLevel = RiskLevel.MEDIUM
    enabled: bool = True


@dataclass(frozen=True)
class WorkRequest:
    """Entrada canônica para demandas de usuários, agentes ou eventos."""

    intent: str
    required_capabilities: frozenset[str]
    payload: dict[str, Any] = field(default_factory=dict)
    priority: Priority = Priority.NORMAL
    risk: RiskLevel = RiskLevel.LOW
    requester_id: str = "user"
    correlation_id: str = field(default_factory=lambda: str(uuid4()))
    requires_approval: bool = False
    max_attempts: int = 1


@dataclass(frozen=True)
class Handoff:
    """Transferência de contexto e responsabilidade entre Jason e um agente."""

    task_id: str
    correlation_id: str
    intent: str
    payload: dict[str, Any]
    context: tuple[dict[str, Any], ...]
    priority: Priority
    risk: RiskLevel
    autonomy_limits: tuple[str, ...]
    return_criteria: str


@dataclass(frozen=True)
class AgentResult:
    success: bool
    summary: str
    data: dict[str, Any] = field(default_factory=dict)
    evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class AuditEvent:
    event_type: str
    correlation_id: str
    actor_id: str
    details: dict[str, Any]
    timestamp: datetime = field(default_factory=utcnow)


@dataclass(frozen=True)
class OrchestrationResult:
    task_id: str
    correlation_id: str
    status: TaskStatus
    assigned_agent_id: str | None
    summary: str
    result: AgentResult | None = None

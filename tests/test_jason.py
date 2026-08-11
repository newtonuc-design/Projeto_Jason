from jason.core.models import AgentProfile, AgentResult, RiskLevel, TaskStatus, WorkRequest
from jason.in_memory import (
    DefaultApprovalPolicy,
    InMemoryAgentRegistry,
    InMemoryAudit,
    InMemoryMemory,
)
from jason.orchestrator import Jason


class OperationsAgent:
    profile = AgentProfile(
        agent_id="operations-agent",
        capabilities=frozenset({"operate"}),
        permitted_risk=RiskLevel.MEDIUM,
    )

    def execute(self, handoff):
        return AgentResult(True, f"Executado: {handoff.intent}", evidence=("runbook-42",))


def build_jason():
    audit = InMemoryAudit()
    return Jason(
        memory=InMemoryMemory(),
        audit=audit,
        agents=InMemoryAgentRegistry([OperationsAgent()]),
        approval_policy=DefaultApprovalPolicy(),
    ), audit


def test_jason_routes_and_audits_a_request():
    jason, audit = build_jason()
    result = jason.orchestrate(WorkRequest("reiniciar serviço", frozenset({"operate"})))

    assert result.status is TaskStatus.COMPLETED
    assert result.assigned_agent_id == "operations-agent"
    assert [event.event_type for event in audit.events] == [
        "task.received", "task.dispatched", "task.completed"
    ]


def test_high_risk_request_waits_for_governance_approval():
    jason, audit = build_jason()
    result = jason.orchestrate(
        WorkRequest("alterar produção", frozenset({"operate"}), risk=RiskLevel.HIGH)
    )

    assert result.status is TaskStatus.PENDING_APPROVAL
    assert result.assigned_agent_id is None
    assert audit.events[-1].event_type == "task.pending_approval"

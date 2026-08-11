"""Agente Jason: orquestrador central previsto no ADR-0004."""

from __future__ import annotations

from uuid import uuid4

from .core.models import (
    AgentResult,
    AuditEvent,
    Handoff,
    OrchestrationResult,
    TaskStatus,
    WorkRequest,
)
from .core.ports import AgentRegistryPort, ApprovalPolicy, AuditPort, MemoryPort


class Jason:
    """Coordena agentes sem executar tarefas especializadas de domínio."""

    agent_id = "jason"

    def __init__(
        self,
        *,
        memory: MemoryPort,
        audit: AuditPort,
        agents: AgentRegistryPort,
        approval_policy: ApprovalPolicy,
    ) -> None:
        self._memory = memory
        self._audit = audit
        self._agents = agents
        self._approval_policy = approval_policy

    def orchestrate(self, request: WorkRequest, *, approved: bool = False) -> OrchestrationResult:
        """Recebe, contextualiza, governa, delega e registra uma demanda."""
        task_id = str(uuid4())
        correlation_id = request.correlation_id
        self._record("task.received", correlation_id, task_id=task_id, intent=request.intent)
        context = tuple(self._memory.recall(request.intent, correlation_id=correlation_id))

        if self._approval_policy.requires_approval(
            risk=request.risk, explicitly_required=request.requires_approval
        ) and not approved:
            result = OrchestrationResult(
                task_id, correlation_id, TaskStatus.PENDING_APPROVAL, None,
                "A tarefa exige aprovação de governança antes do handoff.",
            )
            self._persist(result, request)
            self._record("task.pending_approval", correlation_id, task_id=task_id)
            return result

        agent = self._agents.find(request.required_capabilities, request.risk)
        if agent is None:
            result = OrchestrationResult(
                task_id, correlation_id, TaskStatus.FAILED, None,
                "Nenhum agente autorizado possui as capacidades solicitadas.",
            )
            self._persist(result, request)
            self._record("task.routing_failed", correlation_id, task_id=task_id)
            return result

        handoff = Handoff(
            task_id=task_id,
            correlation_id=correlation_id,
            intent=request.intent,
            payload=request.payload,
            context=context,
            priority=request.priority,
            risk=request.risk,
            autonomy_limits=("executar somente o escopo delegado", "registrar evidências"),
            return_criteria="Retornar resultado, evidências e status final ao Jason.",
        )
        self._record("task.dispatched", correlation_id, task_id=task_id, agent_id=agent.profile.agent_id)
        agent_result = self._execute_with_retry(agent, handoff, request.max_attempts)
        status = TaskStatus.COMPLETED if agent_result.success else TaskStatus.FAILED
        result = OrchestrationResult(
            task_id, correlation_id, status, agent.profile.agent_id, agent_result.summary, agent_result
        )
        self._persist(result, request)
        self._record(f"task.{status.value}", correlation_id, task_id=task_id, agent_id=agent.profile.agent_id)
        return result

    def _execute_with_retry(self, agent, handoff: Handoff, max_attempts: int) -> AgentResult:
        attempts = max(1, max_attempts)
        last_result: AgentResult | None = None
        for attempt in range(1, attempts + 1):
            try:
                last_result = agent.execute(handoff)
            except Exception as error:  # boundary: falha de agente não derruba o orquestrador
                last_result = AgentResult(False, f"Falha do agente: {error}")
            if last_result.success:
                return last_result
            self._record("task.retry", handoff.correlation_id, task_id=handoff.task_id, attempt=attempt)
        return last_result or AgentResult(False, "Execução não produziu resultado.")

    def _persist(self, result: OrchestrationResult, request: WorkRequest) -> None:
        self._memory.remember(
            {
                "task_id": result.task_id,
                "intent": request.intent,
                "status": result.status.value,
                "assigned_agent_id": result.assigned_agent_id,
                "summary": result.summary,
            },
            correlation_id=result.correlation_id,
        )

    def _record(self, event_type: str, correlation_id: str, **details: object) -> None:
        self._audit.record(AuditEvent(event_type, correlation_id, self.agent_id, dict(details)))

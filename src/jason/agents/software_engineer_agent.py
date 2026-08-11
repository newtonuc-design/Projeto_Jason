from jason.core.models import AgentProfile, AgentResult, Handoff, RiskLevel
from jason.agents.software_engineer import SoftwareEngineer


class SoftwareEngineerAgent:
    @property
    def profile(self) -> AgentProfile:
        return AgentProfile(
            agent_id="software-engineer-agent",
            capabilities=frozenset({"software-engineering"}),
            permitted_risk=RiskLevel.MEDIUM,
        )

    def execute(self, handoff: Handoff) -> AgentResult:
        result = SoftwareEngineer().execute(handoff.intent)

        return AgentResult(
            success=result.status == "COMPLETED",
            summary=result.result,
            data={
                "mission": result.mission,
                "status": result.status,
                "plan": result.plan,
                "actions": result.actions,
                "tests": result.tests,
            },
        )

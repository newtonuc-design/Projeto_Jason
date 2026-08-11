from jason.agents.python_agent import PythonAgent
from jason.agents.software_engineer_agent import SoftwareEngineerAgent
from jason.core.models import WorkRequest
from jason.in_memory import (
    DefaultApprovalPolicy,
    InMemoryAgentRegistry,
    InMemoryAudit,
    InMemoryMemory,
)
from jason.orchestrator import Jason


memory = InMemoryMemory()
audit = InMemoryAudit()

registry = InMemoryAgentRegistry()
registry.register(PythonAgent())
registry.register(SoftwareEngineerAgent())

jason = Jason(
    memory=memory,
    audit=audit,
    agents=registry,
    approval_policy=DefaultApprovalPolicy(),
)

request = WorkRequest(
    intent="Criar endpoint FastAPI",
    required_capabilities=frozenset({"python"}),
)

result = jason.orchestrate(request)

print(result)

from pathlib import Path
import tempfile

from src.memory_agent import MemoryAgent


def test_memory_agent_run_commands():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "memory.json"
        agent = MemoryAgent()

        remembered = agent.run("remember", {"key": "chave", "value": "valor", "tags": ["teste"]})
        assert remembered.key == "chave"
        assert remembered.value == "valor"

        recalled = agent.run("recall", {"key": "chave"})
        assert recalled is not None
        assert recalled.value == "valor"

        results = agent.run("search", {"query": "val"})
        assert len(results) == 1
        assert results[0].key == "chave"

        assert agent.run("list") == ["chave"]
        assert agent.run("forget", {"key": "chave"}) is True
        assert agent.run("recall", {"key": "chave"}) is None


def test_memory_agent_run_unknown_command_raises():
    agent = MemoryAgent()
    try:
        agent.run("invalid", {})
        assert False, "Expected ValueError for unknown command"
    except ValueError as exc:
        assert "Comando desconhecido" in str(exc)

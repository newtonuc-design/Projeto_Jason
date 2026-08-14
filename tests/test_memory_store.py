from pathlib import Path
import tempfile

from src.memory_store import MemoryStore


def test_memory_store_remember_and_recall():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "memory.json"
        store = MemoryStore(storage_path=file_path)

        entry = store.remember("teste", "valor de teste", tags=["importante", "agenda"])
        assert entry.key == "teste"
        assert entry.value == "valor de teste"
        assert "importante" in entry.tags

        recalled = store.recall("teste")
        assert recalled is not None
        assert recalled.value == "valor de teste"

        assert store.search("teste")
        assert store.search("valor")
        assert store.search("agenda")

        assert store.list_keys() == ["teste"]
        assert store.forget("teste") is True
        assert store.recall("teste") is None
        assert store.forget("teste") is False


def test_memory_store_persistence():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "memory.json"
        store = MemoryStore(storage_path=file_path)
        store.remember("persistencia", "dados importantes", tags=["persistente"])

        second_store = MemoryStore(storage_path=file_path)
        entry = second_store.recall("persistencia")
        assert entry is not None
        assert entry.value == "dados importantes"
        assert entry.tags == ["persistente"]

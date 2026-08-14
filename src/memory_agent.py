from __future__ import annotations
from typing import Any, Dict, Iterable, List, Optional

from .agent import Agent
from .memory_store import MemoryEntry, MemoryStore


class MemoryAgent(Agent):
    """Agent specialized in persistent memory management."""

    def __init__(self, store: Optional[MemoryStore] = None) -> None:
        self._store = store if store is not None else MemoryStore()

    @property
    def name(self) -> str:
        return "Agente de Memória"

    @property
    def description(self) -> str:
        return "Gerencia memória institucional, permitindo lembrar, consultar, buscar e esquecer registros."

    def run(self, command: str, payload: Optional[Dict[str, Any]] = None) -> Any:
        if payload is None:
            payload = {}

        command = command.strip().lower()
        if command == "remember":
            key = payload.get("key")
            value = payload.get("value")
            if not key or value is None:
                raise ValueError("remember requires non-empty 'key' and 'value'")
            return self.remember(
                key=str(key),
                value=str(value),
                tags=payload.get("tags"),
            )
        if command == "recall":
            key = payload.get("key")
            if not key:
                raise ValueError("recall requires a non-empty 'key'")
            return self.recall(key=str(key))
        if command == "search":
            query = payload.get("query")
            if query is None:
                raise ValueError("search requires a non-empty 'query'")
            return self.search(query=str(query), limit=int(payload.get("limit", 10)))
        if command == "forget":
            key = payload.get("key")
            if not key:
                raise ValueError("forget requires a non-empty 'key'")
            return self.forget(key=str(key))
        if command == "list":
            return self.list_keys()
        raise ValueError(f"Comando desconhecido: {command}")

    def remember(self, key: str, value: str, tags: Optional[Iterable[str]] = None) -> MemoryEntry:
        return self._store.remember(key=key, value=value, tags=tags)

    def recall(self, key: str) -> Optional[MemoryEntry]:
        return self._store.recall(key=key)

    def search(self, query: str, limit: int = 10) -> List[MemoryEntry]:
        return self._store.search(query=query, limit=limit)

    def forget(self, key: str) -> bool:
        return self._store.forget(key=key)

    def list_keys(self) -> List[str]:
        return self._store.list_keys()

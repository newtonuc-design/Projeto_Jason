from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from threading import RLock
from typing import Dict, Iterable, List, Optional
import json


@dataclass
class MemoryEntry:
    key: str
    value: str
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict[str, object]:
        return {
            "key": self.key,
            "value": self.value,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def from_dict(data: Dict[str, object]) -> "MemoryEntry":
        return MemoryEntry(
            key=str(data["key"]),
            value=str(data["value"]),
            tags=list(data.get("tags", [])),
            created_at=datetime.fromisoformat(str(data["created_at"])),
            updated_at=datetime.fromisoformat(str(data["updated_at"])),
        )


class MemoryStore:
    """A thread-safe store for memory entries with optional persistence."""

    def __init__(self, storage_path: Optional[Path] = None) -> None:
        self._storage_path = Path(storage_path) if storage_path is not None else None
        self._entries: Dict[str, MemoryEntry] = {}
        self._lock = RLock()

        if self._storage_path is not None:
            self._storage_path.parent.mkdir(parents=True, exist_ok=True)
            if self._storage_path.exists():
                self._load()

    def _load(self) -> None:
        with self._lock:
            try:
                with self._storage_path.open("r", encoding="utf-8") as handle:
                    data = json.load(handle)
                self._entries = {
                    item["key"]: MemoryEntry.from_dict(item)
                    for item in data
                }
            except (json.JSONDecodeError, FileNotFoundError):
                self._entries = {}

    def _save(self) -> None:
        if self._storage_path is None:
            return
        with self._lock:
            with self._storage_path.open("w", encoding="utf-8") as handle:
                json.dump([entry.to_dict() for entry in self._entries.values()], handle, ensure_ascii=False, indent=2)

    def remember(self, key: str, value: str, tags: Optional[Iterable[str]] = None) -> MemoryEntry:
        if not key:
            raise ValueError("Memory key must not be empty")
        if value is None:
            raise ValueError("Memory value must not be None")
        tags_list = list(tags) if tags is not None else []
        with self._lock:
            entry = self._entries.get(key)
            now = datetime.utcnow()
            if entry is None:
                entry = MemoryEntry(key=key, value=value, tags=tags_list, created_at=now, updated_at=now)
            else:
                entry.value = value
                entry.tags = tags_list
                entry.updated_at = now
            self._entries[key] = entry
            self._save()
            return entry

    def recall(self, key: str) -> Optional[MemoryEntry]:
        with self._lock:
            return self._entries.get(key)

    def search(self, query: str, limit: int = 10) -> List[MemoryEntry]:
        if query is None:
            raise ValueError("Query must not be None")
        with self._lock:
            lower_query = query.lower()
            results = [entry for entry in self._entries.values()
                       if lower_query in entry.key.lower() or lower_query in entry.value.lower() or any(lower_query in tag.lower() for tag in entry.tags)]
            return results[:limit]

    def forget(self, key: str) -> bool:
        with self._lock:
            if key in self._entries:
                del self._entries[key]
                self._save()
                return True
            return False

    def list_keys(self) -> List[str]:
        with self._lock:
            return list(self._entries.keys())

    def all_entries(self) -> List[MemoryEntry]:
        with self._lock:
            return list(self._entries.values())

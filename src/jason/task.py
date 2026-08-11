"""Modelo de tarefa para a camada mínima de execução."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """Tarefa pronta para ser delegada a um executor."""

    id: str
    title: str
    instruction: str

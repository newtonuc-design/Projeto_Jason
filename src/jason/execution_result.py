"""Modelo neutro para o resultado lógico de uma execução."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionResult:
    """Saídas e código final produzidos por uma instrução executada."""

    stdout: str
    stderr: str
    returncode: int

"""Contrato para componentes que executam instruções."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from .execution_result import ExecutionResult


@runtime_checkable
class Executor(Protocol):
    """Define a operação de execução sem conhecer a infraestrutura."""

    def execute(self, instruction: str) -> ExecutionResult:
        """Executa uma instrução e devolve o resultado da execução."""
        ...

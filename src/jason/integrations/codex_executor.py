"""Infraestrutura mínima para executar instruções pelo Codex CLI."""

from __future__ import annotations

import subprocess
from typing import Callable, Sequence

from ..executor import Executor
from ..execution_result import ExecutionResult

CommandBuilder = Callable[[str], Sequence[str]]


def build_codex_command(instruction: str) -> list[str]:
    """Monta o comando padrão do Codex CLI para uma instrução."""
    return ["codex", "exec", instruction]


class CodexExecutor(Executor):
    """Executa comandos construídos para o Codex CLI, sem política de negócio."""

    def __init__(
        self,
        command_builder: CommandBuilder = build_codex_command,
        *,
        runner: Callable[..., subprocess.CompletedProcess[str]] | None = None,
    ) -> None:
        self._command_builder = command_builder
        self._runner = runner or subprocess.run

    def execute(self, instruction: str) -> ExecutionResult:
        """Executa a instrução e devolve as saídas e o código do processo."""
        completed = self._runner(
            list(self._command_builder(instruction)),
            capture_output=True,
            text=True,
            check=False,
        )
        return ExecutionResult(
            stdout=completed.stdout,
            stderr=completed.stderr,
            returncode=completed.returncode,
        )

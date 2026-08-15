"""Infraestrutura mínima para executar instruções pelo Codex CLI."""

from __future__ import annotations

import os
import shutil
import subprocess
from typing import Callable, Sequence

from ..executor import Executor
from ..execution_result import ExecutionResult

CommandBuilder = Callable[[str], Sequence[str]]


def build_codex_command(instruction: str) -> list[str]:
    """Monta o comando padrão do Codex CLI para uma instrução."""
    return ["codex", "exec", instruction]


def resolve_codex_command(
    command: Sequence[str],
    *,
    os_name: str | None = None,
    which: Callable[[str], str | None] = shutil.which,
) -> list[str]:
    """Resolve o launcher ``codex.cmd`` usado por instalações npm no Windows."""
    resolved = list(command)
    if resolved and resolved[0] == "codex" and (os_name or os.name) == "nt":
        resolved[0] = which("codex.cmd") or "codex.cmd"
    return resolved


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
            resolve_codex_command(self._command_builder(instruction)),
            capture_output=True,
            text=True,
            check=False,
        )
        return ExecutionResult(
            stdout=completed.stdout,
            stderr=completed.stderr,
            returncode=completed.returncode,
        )

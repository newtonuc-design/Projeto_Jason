"""
CommandRunner

Executa comandos do sistema operacional.
"""

from __future__ import annotations

import subprocess


class CommandRunner:
    def run(self, command: list[str]) -> tuple[int, str, str]:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        return (
            process.returncode,
            process.stdout,
            process.stderr,
        )
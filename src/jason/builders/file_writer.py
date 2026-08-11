"""
FileWriter

Responsável por criar e escrever arquivos.
"""

from __future__ import annotations

from pathlib import Path


class FileWriter:
    def create(self, path: str) -> Path:
        file = Path(path)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=True)
        return file

    def write(self, path: str, content: str) -> Path:
        file = self.create(path)
        file.write_text(content, encoding="utf-8")
        return file
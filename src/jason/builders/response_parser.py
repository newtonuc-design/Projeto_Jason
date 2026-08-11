"""
ResponseParser

Converte respostas em estrutura padronizada.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ParsedResponse:
    success: bool
    content: str


class ResponseParser:
    def parse(self, response: str) -> ParsedResponse:
        return ParsedResponse(
            success=True,
            content=response.strip(),
        )
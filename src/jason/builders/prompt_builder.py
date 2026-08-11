"""
PromptBuilder

Responsável por montar prompts para os agentes.
"""

from __future__ import annotations


class PromptBuilder:
    def build(self, template: str, **kwargs) -> str:
        return template.format(**kwargs)
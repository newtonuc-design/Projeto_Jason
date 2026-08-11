"""
Executor

Executa uma Decision e produz um resultado.
"""

from __future__ import annotations

from .decision import Decision


class Executor:

    def execute(self, decision: Decision):

        return {
            "success": True,
            "action": decision.action,
            "confidence": decision.confidence,
            "message": "Execution finished."
        }

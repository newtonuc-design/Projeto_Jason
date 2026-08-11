"""
Builder Agent

Primeiro agente construtor do Jason.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class BuildRequest:
    module: str
    objective: str


class BuilderAgent:
    def run(self, request: BuildRequest) -> dict:
        return {
            "status": "pending",
            "module": request.module,
            "objective": request.objective,
        }
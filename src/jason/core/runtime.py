"""
Jason Agent Runtime

Orquestra Planner e Reasoner.
"""

from __future__ import annotations

from .agent import Agent
from .planner import DefaultPlanner
from .reasoner import Reasoner


class AgentRuntime:

    def __init__(self, agent: Agent):
        self.agent = agent
        self.planner = DefaultPlanner()
        self.reasoner = Reasoner()

    def run(self, request):

        plan = self.planner.create_plan(request)

        decision = self.reasoner.decide(plan)

        return decision


from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    """Base class for agents in Projeto Jason."""

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

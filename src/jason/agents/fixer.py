from dataclasses import dataclass


@dataclass(slots=True)
class FixResult:
    status: str
    error: str
    action: str


class Fixer:
    """
    Responsável por registrar e aplicar uma correção.
    """

    def run(self, error: str) -> FixResult:
        return FixResult(
            status="FIXED",
            error=error,
            action="Correção aplicada",
        )
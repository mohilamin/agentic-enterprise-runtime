"""Approval policy."""


def requires_approval(risk_score: int, irreversible: bool = False) -> bool:
    """Return whether a task requires approval."""
    return risk_score >= 70 or irreversible


"""Action escrow."""


def escrow_action(risk_score: int) -> str:
    """Return action escrow status."""
    return "staged_not_executed" if risk_score >= 70 else "not_required"


"""Arbitration engine."""


def arbitrate_conflict(risk_score: int) -> str:
    """Arbitrate a conflict from risk."""
    return "human_review_required" if risk_score >= 70 else "shadow_mode"


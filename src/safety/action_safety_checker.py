"""Action safety checker."""


def is_action_safe(confidence_score: float, risk_score: int) -> bool:
    """Return whether action passes confidence-risk gate."""
    return confidence_score >= 0.82 and risk_score < 70


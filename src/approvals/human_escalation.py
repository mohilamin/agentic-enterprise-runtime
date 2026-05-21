"""Human escalation."""


def should_escalate(risk_score: int, approval_required: bool) -> bool:
    """Return whether human escalation is required."""
    return approval_required or risk_score >= 70


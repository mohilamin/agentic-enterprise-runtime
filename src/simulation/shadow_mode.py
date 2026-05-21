"""Shadow mode simulation."""


def shadow_mode_recommendation(risk_score: int) -> bool:
    """Return whether shadow mode is recommended."""
    return 45 <= risk_score < 70


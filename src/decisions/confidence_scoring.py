"""Confidence scoring."""


def score_confidence(routing_score: float, evidence_quality: float = 0.9) -> float:
    """Calculate confidence score."""
    return round(min(1.0, routing_score * evidence_quality), 3)


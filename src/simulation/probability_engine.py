"""Probability engine."""


def expected_loss(cost: float, probability: float) -> float:
    """Calculate expected loss."""
    return round(cost * probability, 2)


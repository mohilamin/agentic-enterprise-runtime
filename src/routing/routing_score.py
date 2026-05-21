"""Routing score helpers."""


def calculate_routing_score(domain_match: bool, risk_high: bool = False) -> float:
    """Calculate a deterministic routing score."""
    return round((0.9 if domain_match else 0.55) - (0.05 if risk_high else 0.0), 3)


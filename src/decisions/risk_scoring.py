"""Risk scoring."""


def score_risk(business_impact: int, blast_radius: int) -> int:
    """Calculate task risk."""
    return max(business_impact, blast_radius)


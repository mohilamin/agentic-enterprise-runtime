"""Contradiction resolver."""


def resolve_contradiction(recommendations: list[str]) -> str:
    """Resolve contradictory recommendations."""
    return "governance_safe_path" if "block" in recommendations else recommendations[0]


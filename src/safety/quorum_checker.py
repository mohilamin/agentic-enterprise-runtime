"""Agent quorum checker."""


def quorum_passed(agreements: int, required: int = 2) -> bool:
    """Return whether quorum passed."""
    return agreements >= required


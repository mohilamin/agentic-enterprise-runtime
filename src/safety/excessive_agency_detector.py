"""Excessive agency detection."""


def detect_excessive_agency(requested_action: str) -> bool:
    """Detect excessive autonomy."""
    return requested_action in {"execute_irreversible_action", "bypass_approval"}


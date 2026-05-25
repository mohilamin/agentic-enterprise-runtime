"""Deterministic fallback helpers for optional live-agent mode."""


def deterministic_fallback(reason: str = "optional live-agent dependency not installed or API key missing") -> dict[str, object]:
    """Return a structured fallback response."""
    return {
        "mode": "deterministic_fallback",
        "available": False,
        "reason": reason,
        "deterministic_policy_enforced": True,
    }


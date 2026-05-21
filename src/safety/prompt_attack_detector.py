"""Prompt attack detection."""

PATTERNS = ["ignore previous instructions", "bypass policy", "reveal hidden data", "exfiltrate"]


def detect_prompt_attack(prompt: str) -> bool:
    """Detect prompt attack patterns."""
    text = prompt.lower()
    return any(pattern in text for pattern in PATTERNS)


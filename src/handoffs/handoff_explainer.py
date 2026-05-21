"""Handoff explanations."""


def explain_handoff(from_agent: str, to_agent: str) -> str:
    """Explain a handoff."""
    return f"{from_agent} handed off to {to_agent} because specialist governance or domain review was required."


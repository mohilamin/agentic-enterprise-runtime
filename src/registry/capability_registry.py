"""Capability registry helpers."""

from src.runtime_core import AGENT_SPECS


def get_capabilities(agent_id: str) -> list[str]:
    """Return capabilities for an agent."""
    return list(AGENT_SPECS[agent_id][1])


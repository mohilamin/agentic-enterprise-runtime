"""Governance agent."""
from src.agents.base_agent import BaseAgent


def GovernanceAgent() -> BaseAgent:
    """Create governance agent."""
    return BaseAgent("governance_agent")

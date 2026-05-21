"""Support agent."""
from src.agents.base_agent import BaseAgent


def SupportAgent() -> BaseAgent:
    """Create support agent."""
    return BaseAgent("support_agent")

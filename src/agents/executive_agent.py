"""Executive agent."""
from src.agents.base_agent import BaseAgent


def ExecutiveAgent() -> BaseAgent:
    """Create executive agent."""
    return BaseAgent("executive_agent")

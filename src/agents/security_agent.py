"""Security agent."""
from src.agents.base_agent import BaseAgent


def SecurityAgent() -> BaseAgent:
    """Create security agent."""
    return BaseAgent("security_agent")

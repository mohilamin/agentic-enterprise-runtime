"""Finance agent."""
from src.agents.base_agent import BaseAgent


def FinanceAgent() -> BaseAgent:
    """Create finance agent."""
    return BaseAgent("finance_agent")

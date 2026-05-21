"""Healthcare ops agent."""
from src.agents.base_agent import BaseAgent


def HealthcareOpsAgent() -> BaseAgent:
    """Create healthcare ops agent."""
    return BaseAgent("healthcare_ops_agent")

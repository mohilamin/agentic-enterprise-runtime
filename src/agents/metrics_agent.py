"""Metrics agent."""
from src.agents.base_agent import BaseAgent


def MetricsAgent() -> BaseAgent:
    """Create metrics agent."""
    return BaseAgent("metrics_agent")

"""Data quality agent."""
from src.agents.base_agent import BaseAgent


def DataQualityAgent() -> BaseAgent:
    """Create data quality agent."""
    return BaseAgent("data_quality_agent")

"""Reliability agent."""
from src.agents.base_agent import BaseAgent


def ReliabilityAgent() -> BaseAgent:
    """Create reliability agent."""
    return BaseAgent("reliability_agent")

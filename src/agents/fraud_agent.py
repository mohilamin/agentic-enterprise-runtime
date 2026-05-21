"""Fraud agent."""
from src.agents.base_agent import BaseAgent


def FraudAgent() -> BaseAgent:
    """Create fraud agent."""
    return BaseAgent("fraud_agent")

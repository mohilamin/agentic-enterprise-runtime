"""Supply chain agent."""
from src.agents.base_agent import BaseAgent


def SupplyChainAgent() -> BaseAgent:
    """Create supply chain agent."""
    return BaseAgent("supply_chain_agent")

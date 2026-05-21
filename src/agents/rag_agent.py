"""RAG agent."""
from src.agents.base_agent import BaseAgent


def RagAgent() -> BaseAgent:
    """Create RAG agent."""
    return BaseAgent("rag_agent")

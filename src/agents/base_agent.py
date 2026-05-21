"""Base deterministic agent."""

from src.runtime_core import evaluate_agent_task


class BaseAgent:
    """Deterministic enterprise agent."""

    def __init__(self, agent_id: str) -> None:
        self.agent_id = agent_id

    def evaluate_task(self, task: dict[str, object]) -> dict[str, object]:
        """Evaluate a task."""
        return evaluate_agent_task(self.agent_id, task)

    def recommend_tools(self) -> list[str]:
        """Return default recommended tools."""
        return []

    def produce_recommendation(self, task: dict[str, object]) -> dict[str, object]:
        """Produce a deterministic recommendation."""
        return self.evaluate_task(task)

    def explain_decision(self) -> str:
        """Explain agent decision logic."""
        return "Deterministic rule-based agent uses domain, policy, confidence, and risk signals."


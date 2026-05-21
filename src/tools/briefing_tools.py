"""Briefing tools."""
from src.tools.tool_executor import run_tool


def generate_executive_briefing(task_id: str) -> dict[str, object]: return run_tool("generate_executive_briefing", task_id)
def summarize_cross_domain_risk(task_id: str) -> dict[str, object]: return run_tool("summarize_cross_domain_risk", task_id)
def rank_decision_options(task_id: str) -> dict[str, object]: return run_tool("rank_decision_options", task_id)


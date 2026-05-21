"""Fraud tools."""
from src.tools.tool_executor import run_tool


def score_transaction_risk(task_id: str) -> dict[str, object]: return run_tool("score_transaction_risk", task_id)
def check_identity_graph(task_id: str) -> dict[str, object]: return run_tool("check_identity_graph", task_id)
def freeze_account_shadow(task_id: str) -> dict[str, object]: return run_tool("freeze_account_shadow", task_id)
def estimate_false_positive_cost(task_id: str) -> dict[str, object]: return run_tool("estimate_false_positive_cost", task_id)


"""Support tools."""
from src.tools.tool_executor import run_tool


def summarize_support_case(task_id: str) -> dict[str, object]: return run_tool("summarize_support_case", task_id)
def recommend_refund(task_id: str) -> dict[str, object]: return run_tool("recommend_refund", task_id)
def mask_customer_pii(task_id: str) -> dict[str, object]: return run_tool("mask_customer_pii", task_id)
def escalate_support_case(task_id: str) -> dict[str, object]: return run_tool("escalate_support_case", task_id)


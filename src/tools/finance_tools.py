"""Finance tools."""
from src.tools.tool_executor import run_tool


def query_revenue_anomalies(task_id: str) -> dict[str, object]: return run_tool("query_revenue_anomalies", task_id)
def calculate_margin_impact(task_id: str) -> dict[str, object]: return run_tool("calculate_margin_impact", task_id)
def check_invoice_status(task_id: str) -> dict[str, object]: return run_tool("check_invoice_status", task_id)
def simulate_finance_approval(task_id: str) -> dict[str, object]: return run_tool("simulate_finance_approval", task_id)


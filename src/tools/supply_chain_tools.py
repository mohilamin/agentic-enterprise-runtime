"""Supply chain tools."""
from src.tools.tool_executor import run_tool


def check_inventory_risk(task_id: str) -> dict[str, object]: return run_tool("check_inventory_risk", task_id)
def simulate_reroute(task_id: str) -> dict[str, object]: return run_tool("simulate_reroute", task_id)
def estimate_stockout_cost(task_id: str) -> dict[str, object]: return run_tool("estimate_stockout_cost", task_id)
def escalate_supplier_delay(task_id: str) -> dict[str, object]: return run_tool("escalate_supplier_delay", task_id)


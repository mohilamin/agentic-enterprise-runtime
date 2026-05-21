"""Data platform tools."""
from src.tools.tool_executor import run_tool


def check_data_quality(task_id: str) -> dict[str, object]: return run_tool("check_data_quality", task_id)
def validate_data_contract(task_id: str) -> dict[str, object]: return run_tool("validate_data_contract", task_id)
def run_root_cause_analysis(task_id: str) -> dict[str, object]: return run_tool("run_root_cause_analysis", task_id)
def estimate_blast_radius(task_id: str) -> dict[str, object]: return run_tool("estimate_blast_radius", task_id)
def simulate_backfill(task_id: str) -> dict[str, object]: return run_tool("simulate_backfill", task_id)


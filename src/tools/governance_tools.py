"""Governance tools."""
from src.tools.tool_executor import run_tool


def check_access_policy(task_id: str) -> dict[str, object]: return run_tool("check_access_policy", task_id)
def detect_prompt_injection(task_id: str) -> dict[str, object]: return run_tool("detect_prompt_injection", task_id)
def detect_tool_misuse(task_id: str) -> dict[str, object]: return run_tool("detect_tool_misuse", task_id)
def create_governance_incident(task_id: str) -> dict[str, object]: return run_tool("create_governance_incident", task_id)
def request_human_approval(task_id: str) -> dict[str, object]: return run_tool("request_human_approval", task_id)


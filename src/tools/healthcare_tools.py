"""Healthcare tools."""
from src.tools.tool_executor import run_tool


def validate_claim_documents(task_id: str) -> dict[str, object]: return run_tool("validate_claim_documents", task_id)
def check_policy_eligibility(task_id: str) -> dict[str, object]: return run_tool("check_policy_eligibility", task_id)
def route_to_medical_review(task_id: str) -> dict[str, object]: return run_tool("route_to_medical_review", task_id)
def summarize_claim_risk(task_id: str) -> dict[str, object]: return run_tool("summarize_claim_risk", task_id)


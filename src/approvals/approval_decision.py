"""Interactive approval decision helpers."""

from src.v02_core import submit_approval_decision


def submit_decision(approval_id: str, status: str, reviewer: str = "demo_reviewer", comment: str = "") -> dict[str, object]:
    """Submit a simulated approval decision."""
    return submit_approval_decision(approval_id, status, reviewer, comment)


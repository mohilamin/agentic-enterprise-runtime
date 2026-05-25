"""Tool policy evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_tool_policy() -> float:
    """Return tool policy precision."""
    return float(run_evaluations()["tool_policy_precision"])


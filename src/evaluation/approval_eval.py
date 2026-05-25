"""Approval evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_approvals() -> float:
    """Return approval decision accuracy."""
    return float(run_evaluations()["approval_decision_accuracy"])


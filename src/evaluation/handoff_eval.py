"""Handoff evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_handoffs() -> float:
    """Return handoff acceptance accuracy."""
    return float(run_evaluations()["handoff_acceptance_accuracy"])


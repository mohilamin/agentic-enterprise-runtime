"""Conflict evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_conflicts() -> float:
    """Return conflict resolution accuracy."""
    return float(run_evaluations()["conflict_resolution_accuracy"])


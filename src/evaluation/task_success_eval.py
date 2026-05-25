"""Task success evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_task_success() -> float:
    """Return task resolution accuracy."""
    return float(run_evaluations()["task_resolution_accuracy"])


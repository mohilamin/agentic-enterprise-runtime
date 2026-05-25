"""Run the V0.2 evaluation suite."""

from src.v02_core import run_evaluations


def run_evaluation_suite() -> dict[str, object]:
    """Run deterministic evaluation reports."""
    return run_evaluations()


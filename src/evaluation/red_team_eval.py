"""Red-team evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_red_team() -> float:
    """Return red-team detection rate."""
    return float(run_evaluations()["red_team_detection_rate"])


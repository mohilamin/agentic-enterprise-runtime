"""Decision lineage evaluation facade."""

from src.v02_core import run_evaluations


def evaluate_lineage() -> float:
    """Return lineage completeness."""
    return float(run_evaluations()["decision_lineage_completeness"])


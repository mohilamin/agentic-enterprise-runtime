"""Run deterministic red-team scenarios."""

from src.v02_core import generate_red_team_outputs


def run_red_team_scenarios() -> dict[str, object]:
    """Run red-team suite."""
    return generate_red_team_outputs()


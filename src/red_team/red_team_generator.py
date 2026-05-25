"""Generate deterministic red-team scenarios."""

from src.v02_core import generate_red_team_outputs


def generate_red_team_scenarios() -> dict[str, object]:
    """Generate scenarios and scorecard."""
    return generate_red_team_outputs()


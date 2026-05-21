"""Runtime scorecard loader."""

import json

from src.common.paths import SCORECARDS


def load_runtime_scorecard() -> dict:
    """Load runtime scorecard."""
    return json.loads((SCORECARDS / "runtime_health_scorecard.json").read_text(encoding="utf-8"))


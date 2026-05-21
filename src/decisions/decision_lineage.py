"""Decision lineage."""

import json

from src.common.paths import DECISIONS


def load_decision_lineage() -> dict:
    """Load decision lineage."""
    return json.loads((DECISIONS / "decision_lineage.json").read_text(encoding="utf-8"))


"""Handoff graph helpers."""

import json

from src.common.paths import HANDOFFS


def load_handoff_graph() -> dict:
    """Load handoff graph JSON."""
    return json.loads((HANDOFFS / "agent_handoff_graph.json").read_text(encoding="utf-8"))


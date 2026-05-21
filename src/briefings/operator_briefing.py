"""Operator briefing."""

from pathlib import Path

from src.common.paths import BRIEFINGS


def load_operator_briefing() -> str:
    """Load operator briefing."""
    return Path(BRIEFINGS / "operator_agent_briefings.md").read_text(encoding="utf-8")


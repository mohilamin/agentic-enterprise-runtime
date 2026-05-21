"""Executive briefing."""

from pathlib import Path

from src.common.paths import BRIEFINGS


def load_executive_briefing() -> str:
    """Load executive briefing."""
    return Path(BRIEFINGS / "executive_agent_briefings.md").read_text(encoding="utf-8")


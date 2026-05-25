"""Red-team report helpers."""

import json

from src.common.paths import RED_TEAM
from src.v02_core import generate_red_team_outputs


def load_red_team_results() -> list[dict[str, object]]:
    """Read red-team results, generating them when missing."""
    path = RED_TEAM / "red_team_results.json"
    if not path.exists():
        generate_red_team_outputs()
    return json.loads(path.read_text(encoding="utf-8"))


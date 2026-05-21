"""Shared memory."""

import json

from src.common.paths import MEMORY


def load_shared_memory() -> dict:
    """Load shared memory."""
    return json.loads((MEMORY / "shared_agent_memory.json").read_text(encoding="utf-8"))


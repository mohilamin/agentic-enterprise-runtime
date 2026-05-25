"""Flagship demo report helpers."""

import json

from src.common.paths import DEMO
from src.v02_core import run_flagship_demo


def load_demo_summary() -> dict[str, object]:
    """Load or generate flagship demo summary."""
    path = DEMO / "flagship_demo_summary.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else run_flagship_demo()

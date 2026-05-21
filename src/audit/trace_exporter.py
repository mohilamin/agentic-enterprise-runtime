"""Trace exporter."""

import json

from src.common.paths import AUDIT


def load_runtime_trace() -> dict:
    """Load runtime trace."""
    return json.loads((AUDIT / "runtime_trace.json").read_text(encoding="utf-8"))


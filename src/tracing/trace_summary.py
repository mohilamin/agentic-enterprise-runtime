"""Runtime trace summary facade."""

import json

from src.common.paths import TRACES
from src.v02_core import generate_trace_outputs


def build_runtime_trace_summary() -> dict[str, object]:
    """Read or generate the runtime trace summary."""
    path = TRACES / "runtime_trace_summary.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else generate_trace_outputs()


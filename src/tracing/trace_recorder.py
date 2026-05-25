"""Trace recorder implementation."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.tracing.trace_event import TraceEvent


class TraceRecorder:
    """Small in-memory trace recorder used by deterministic pipeline tests."""

    def __init__(self) -> None:
        self.events: list[dict[str, object]] = []

    def start_span(self, trace_id: str, span_id: str, task_id: str, span_type: str, parent_span_id: str = "") -> dict[str, object]:
        """Start and store a span event."""
        event = TraceEvent(trace_id, span_id, parent_span_id, task_id, span_type, "started").to_dict()
        self.events.append(event)
        return event

    def end_span(self, span_id: str, status: str = "ok", duration_ms: int = 1) -> dict[str, object]:
        """End a stored span event."""
        event = next((item for item in self.events if item["span_id"] == span_id), None)
        if event is None:
            event = TraceEvent("trace_unknown", span_id, "", "task_unknown", "unknown", status).to_dict()
            self.events.append(event)
        event["status"] = status
        event["duration_ms"] = duration_ms
        return event

    def record_event(self, event: dict[str, object]) -> None:
        """Record a complete trace event."""
        self.events.append(event)

    def write_jsonl(self, path: Path) -> None:
        """Write trace events to JSONL."""
        with path.open("w", encoding="utf-8") as file:
            for event in self.events:
                file.write(json.dumps(event) + "\n")

    def write_span_csvs(self, path: Path) -> None:
        """Write trace events to CSV."""
        pd.DataFrame(self.events).to_csv(path, index=False)


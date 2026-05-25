"""Trace event models."""

from dataclasses import asdict, dataclass


@dataclass
class TraceEvent:
    """Runtime trace event."""

    trace_id: str
    span_id: str
    parent_span_id: str
    task_id: str
    span_type: str
    status: str
    duration_ms: int = 0

    def to_dict(self) -> dict[str, object]:
        """Return a serializable event payload."""
        return asdict(self)


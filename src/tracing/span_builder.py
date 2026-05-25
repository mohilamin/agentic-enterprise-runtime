"""Span builder helpers."""


def build_span(trace_id: str, span_id: str, task_id: str, span_type: str, status: str = "ok") -> dict[str, object]:
    """Build a trace span dictionary."""
    return {
        "trace_id": trace_id,
        "span_id": span_id,
        "parent_span_id": "",
        "task_id": task_id,
        "span_type": span_type,
        "status": status,
    }


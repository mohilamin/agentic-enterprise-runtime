"""Tool executor."""

from src.runtime_core import execute_tool


def run_tool(tool_id: str, task_id: str) -> dict[str, object]:
    """Run a deterministic tool simulation."""
    return execute_tool(tool_id, task_id)


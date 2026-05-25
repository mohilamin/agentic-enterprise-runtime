"""Safe live-tool descriptor adapter."""


def to_live_tool_descriptor(tool: dict[str, object], allow_execution: bool = False) -> dict[str, object]:
    """Convert a deterministic tool into a non-executing live descriptor by default."""
    return {
        "tool_id": tool.get("tool_id", tool.get("tool_name", "tool")),
        "description": tool.get("description", "Simulated tool"),
        "risk_level": tool.get("risk_level", "medium"),
        "real_execution_enabled": bool(allow_execution),
        "simulation_required": not allow_execution,
    }


"""Access evaluator."""


def is_tool_allowed(tool_id: str, allowed_tools: str) -> bool:
    """Return whether a tool is in the allowed tool list."""
    return tool_id in set(str(allowed_tools).split("|"))


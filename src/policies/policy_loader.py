"""Policy loader."""

from src.common.config import load_yaml


def load_tool_policies() -> dict:
    """Load tool policies."""
    return load_yaml("config/tool_policies.yaml")


"""Tool registry access."""

import pandas as pd

from src.common.paths import TOOLS
from src.runtime_core import build_tool_registry


def load_tool_registry() -> pd.DataFrame:
    """Load or build the tool registry."""
    path = TOOLS / "tool_registry.csv"
    return pd.read_csv(path) if path.exists() else build_tool_registry()


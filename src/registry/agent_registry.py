"""Agent registry access."""

import pandas as pd

from src.common.paths import AGENTS
from src.runtime_core import build_agent_registry


def load_agent_registry() -> pd.DataFrame:
    """Load or build the agent registry."""
    path = AGENTS / "agent_registry.csv"
    return pd.read_csv(path) if path.exists() else build_agent_registry()


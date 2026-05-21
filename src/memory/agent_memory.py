"""Agent memory."""

import pandas as pd

from src.common.paths import MEMORY


def load_agent_memory() -> pd.DataFrame:
    """Load agent performance memory."""
    return pd.read_csv(MEMORY / "agent_performance_memory.csv")


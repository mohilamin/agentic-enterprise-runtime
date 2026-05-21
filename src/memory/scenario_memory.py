"""Scenario memory."""

import pandas as pd

from src.common.paths import MEMORY


def load_scenario_memory() -> pd.DataFrame:
    """Load scenario memory."""
    return pd.read_csv(MEMORY / "scenario_memory.csv")


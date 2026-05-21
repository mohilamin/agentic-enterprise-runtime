"""Decision engine."""

import pandas as pd

from src.runtime_core import create_final_decisions


def build_final_decisions(
    tasks: pd.DataFrame, routing: pd.DataFrame, permissions: pd.DataFrame, simulations: pd.DataFrame
) -> pd.DataFrame:
    """Build final decisions."""
    return create_final_decisions(tasks, routing, permissions, simulations)


"""Outcome simulator."""

import pandas as pd

from src.runtime_core import run_probability_simulations


def simulate_outcomes(tasks: pd.DataFrame, scenarios: pd.DataFrame) -> pd.DataFrame:
    """Simulate outcomes."""
    return run_probability_simulations(tasks, scenarios)


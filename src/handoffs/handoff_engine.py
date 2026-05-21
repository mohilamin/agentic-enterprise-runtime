"""Handoff engine."""

import pandas as pd

from src.runtime_core import generate_handoffs


def build_handoffs(tasks: pd.DataFrame) -> pd.DataFrame:
    """Build handoff history."""
    return generate_handoffs(tasks)


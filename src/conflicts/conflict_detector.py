"""Conflict detection."""

import pandas as pd

from src.runtime_core import detect_conflicts


def build_conflicts(tasks: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Detect conflicts."""
    return detect_conflicts(tasks)


"""Incident generator."""

import pandas as pd

from src.runtime_core import detect_safety_incidents


def build_safety_incidents(tasks: pd.DataFrame, permissions: pd.DataFrame) -> pd.DataFrame:
    """Build safety incidents."""
    return detect_safety_incidents(tasks, permissions)


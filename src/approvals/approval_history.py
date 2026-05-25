"""Approval history helpers."""

import pandas as pd

from src.common.paths import APPROVALS


def load_approval_history() -> pd.DataFrame:
    """Load approval decision history."""
    path = APPROVALS / "approval_decision_history.csv"
    return pd.read_csv(path) if path.exists() else pd.DataFrame()


"""Approval queue."""

import pandas as pd

from src.runtime_core import create_approval_outputs


def build_approval_queue(decisions: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build approval queue."""
    return create_approval_outputs(decisions)


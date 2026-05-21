"""Audit logger."""

import pandas as pd

from src.runtime_core import create_audit_outputs


def build_audit_log(tasks: pd.DataFrame, permissions: pd.DataFrame, decisions: pd.DataFrame) -> pd.DataFrame:
    """Build audit log."""
    return create_audit_outputs(tasks, permissions, decisions)


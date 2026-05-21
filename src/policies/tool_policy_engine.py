"""Tool policy engine."""

import pandas as pd

from src.runtime_core import evaluate_tool_permissions


def evaluate_permissions(tasks: pd.DataFrame, agents: pd.DataFrame, tools: pd.DataFrame) -> pd.DataFrame:
    """Evaluate tool permissions."""
    return evaluate_tool_permissions(tasks, agents, tools)


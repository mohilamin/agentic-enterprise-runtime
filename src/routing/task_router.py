"""Task routing engine."""

import pandas as pd

from src.runtime_core import route_tasks


def route_enterprise_tasks(tasks: pd.DataFrame, agents: pd.DataFrame) -> pd.DataFrame:
    """Route enterprise tasks to agents."""
    return route_tasks(tasks, agents)


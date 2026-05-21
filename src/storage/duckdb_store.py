"""DuckDB runtime warehouse."""

import duckdb
import pandas as pd

from src.common.paths import (
    AGENTS,
    APPROVALS,
    AUDIT,
    CONFLICTS,
    DECISIONS,
    HANDOFFS,
    INCIDENTS,
    RUNTIME,
    SCORECARDS,
    SIMULATIONS,
    TASKS,
    TOOLS,
    WAREHOUSE,
)


def load_duckdb_store() -> str:
    """Load runtime outputs into DuckDB."""
    WAREHOUSE.mkdir(parents=True, exist_ok=True)
    db_path = WAREHOUSE / "agentic_enterprise_runtime.duckdb"
    con = duckdb.connect(str(db_path))
    tables = {
        "agents": AGENTS / "agent_registry.csv",
        "tools": TOOLS / "tool_registry.csv",
        "tasks": TASKS / "enterprise_tasks.csv",
        "probability_scenarios": SIMULATIONS / "probability_scenarios.csv",
        "routing_decisions": RUNTIME / "task_routing_decisions.csv",
        "tool_permission_decisions": DECISIONS / "tool_permission_decisions.csv",
        "handoff_history": HANDOFFS / "agent_handoff_history.csv",
        "conflicts": CONFLICTS / "agent_conflicts.csv",
        "final_decisions": DECISIONS / "final_agent_decisions.csv",
        "approval_queue": APPROVALS / "human_approval_queue.csv",
        "audit_log": AUDIT / "agent_action_history.csv",
        "safety_incidents": INCIDENTS / "agent_safety_incidents.csv",
    }
    for table, path in tables.items():
        frame = pd.read_csv(path)
        con.register(f"{table}_df", frame)
        con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM {table}_df")
    scorecards = []
    for path in SCORECARDS.glob("*.csv"):
        frame = pd.read_csv(path)
        frame["scorecard_name"] = path.stem
        scorecards.append(frame.astype(str))
    if scorecards:
        scorecard_frame = pd.concat(scorecards, ignore_index=True, sort=False)
        con.register("scorecards_df", scorecard_frame)
        con.execute("CREATE OR REPLACE TABLE scorecards AS SELECT * FROM scorecards_df")
    con.close()
    return str(db_path)


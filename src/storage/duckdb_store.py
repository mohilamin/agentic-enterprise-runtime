"""DuckDB runtime warehouse."""

import json

import duckdb
import pandas as pd

from src.common.paths import (
    AGENTS,
    APPROVALS,
    AUDIT,
    CONFLICTS,
    DECISIONS,
    DEMO,
    EVALUATIONS,
    HANDOFFS,
    INCIDENTS,
    LIVE_AGENTS,
    RED_TEAM,
    RUNTIME,
    SCORECARDS,
    SIMULATIONS,
    TASKS,
    TOOLS,
    TRACES,
    WAREHOUSE,
)


def _json_to_frame(path) -> pd.DataFrame:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return pd.DataFrame(payload)
    return pd.DataFrame([payload])


def _jsonl_to_frame(path) -> pd.DataFrame:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return pd.DataFrame(rows)


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
        "tool_call_spans": TRACES / "tool_call_spans.csv",
        "handoff_spans": TRACES / "handoff_spans.csv",
        "guardrail_spans": TRACES / "guardrail_spans.csv",
        "red_team_scenarios": RED_TEAM / "red_team_scenarios.csv",
        "red_team_results": RED_TEAM / "red_team_results.csv",
        "approval_decision_history": APPROVALS / "approval_decision_history.csv",
        "v02_runtime_upgrade_summary": SCORECARDS / "v02_runtime_upgrade_summary.csv",
    }
    for table, path in tables.items():
        if path.exists():
            frame = pd.read_csv(path)
            con.register(f"{table}_df", frame)
            con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM {table}_df")
    json_tables = {
        "trace_events": TRACES / "agent_trace_events.jsonl",
        "evaluation_reports": EVALUATIONS / "evaluation_summary.json",
        "flagship_demo_summary": DEMO / "flagship_demo_summary.json",
        "live_agent_adapter_status": LIVE_AGENTS / "live_agent_adapter_status.json",
    }
    for table, path in json_tables.items():
        if path.exists():
            frame = _jsonl_to_frame(path) if path.suffix == ".jsonl" else _json_to_frame(path)
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

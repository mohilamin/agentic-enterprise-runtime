"""Streamlit dashboard."""

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from src.common.paths import (
    AGENTS,
    APPROVALS,
    AUDIT,
    BRIEFINGS,
    CONFLICTS,
    DECISIONS,
    HANDOFFS,
    INCIDENTS,
    RUNTIME,
    SCORECARDS,
    SIMULATIONS,
    TOOLS,
)


def _csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path) if path.exists() else pd.DataFrame()


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def main() -> None:
    """Render dashboard."""
    st.set_page_config(page_title="Agentic Enterprise Runtime", layout="wide")
    st.title("Agentic Enterprise Runtime")
    score = _json(SCORECARDS / "runtime_health_scorecard.json")
    cols = st.columns(4)
    cols[0].metric("Safety Score", score.get("overall_runtime_safety_score", 0))
    cols[1].metric("Human Escalation Rate", score.get("human_escalation_rate", 0))
    cols[2].metric("Blocked Action Rate", score.get("blocked_action_rate", 0))
    cols[3].metric("Approval Queue", score.get("approval_queue_volume", 0))
    tabs = st.tabs([
        "Agent Registry", "Tool Registry", "Task Routing", "Handoffs", "Tool Governance",
        "Probability Scenarios", "Conflicts", "Approval Queue", "Safety Incidents",
        "Decision Lineage", "Audit Trail", "Scorecards", "Briefings",
    ])
    paths = [
        AGENTS / "agent_registry.csv", TOOLS / "tool_registry.csv", RUNTIME / "task_routing_decisions.csv",
        HANDOFFS / "agent_handoff_history.csv", DECISIONS / "tool_permission_decisions.csv",
        SIMULATIONS / "probability_scenarios.csv", CONFLICTS / "conflict_resolution_decisions.csv",
        APPROVALS / "human_approval_queue.csv", INCIDENTS / "agent_safety_incidents.csv",
        DECISIONS / "final_agent_decisions.csv", AUDIT / "agent_action_history.csv",
    ]
    for tab, path in zip(tabs[:11], paths, strict=False):
        with tab:
            st.dataframe(_csv(path).head(200), use_container_width=True)
    with tabs[11]:
        for path in sorted(SCORECARDS.glob("*.json")):
            st.subheader(path.stem)
            st.json(_json(path))
    with tabs[12]:
        for path in [BRIEFINGS / "executive_agent_briefings.md", BRIEFINGS / "operator_agent_briefings.md"]:
            st.subheader(path.stem)
            st.markdown(path.read_text(encoding="utf-8") if path.exists() else "")


if __name__ == "__main__":
    main()


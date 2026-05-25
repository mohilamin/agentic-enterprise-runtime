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
    DEMO,
    EVALUATIONS,
    HANDOFFS,
    INCIDENTS,
    LIVE_AGENTS,
    RED_TEAM,
    RUNTIME,
    SCORECARDS,
    SIMULATIONS,
    TOOLS,
    TRACES,
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
    v02 = _json(SCORECARDS / "v02_runtime_upgrade_summary.json")
    if v02:
        st.subheader("V0.2 Runtime Upgrade Overview")
        v02_cols = st.columns(5)
        v02_cols[0].metric("Evaluation Score", v02.get("evaluation_score", 0))
        v02_cols[1].metric("Red-Team Detection", v02.get("red_team_detection_rate", 0))
        v02_cols[2].metric("Trace Completeness", v02.get("trace_completeness_score", 0))
        v02_cols[3].metric("Approval Health", v02.get("approval_workflow_health_score", 0))
        v02_cols[4].metric("Fallback", v02.get("deterministic_fallback_status", "unknown"))
    tabs = st.tabs([
        "V0.2 Overview", "Trace Explorer", "Evaluation Harness", "Red-Team Results",
        "Live Agent Adapter", "Approval Workflow", "Flagship Demo", "Guardrail Spans",
        "Decision Lineage", "Runtime Regression", "Agent Registry", "Tool Registry",
        "Task Routing", "Handoffs", "Tool Governance", "Probability Scenarios",
        "Conflicts", "Approval Queue", "Safety Incidents", "Audit Trail", "Scorecards",
        "Briefings",
    ])
    with tabs[0]:
        st.json(v02)
    with tabs[1]:
        st.dataframe(_csv(TRACES / "tool_call_spans.csv").head(200), use_container_width=True)
        st.dataframe(_csv(TRACES / "handoff_spans.csv").head(100), use_container_width=True)
    with tabs[2]:
        st.json(_json(EVALUATIONS / "evaluation_summary.json"))
        st.dataframe(_csv(EVALUATIONS / "agent_regression_suite.csv"), use_container_width=True)
    with tabs[3]:
        st.dataframe(_csv(RED_TEAM / "red_team_results.csv"), use_container_width=True)
    with tabs[4]:
        st.json(_json(LIVE_AGENTS / "live_agent_adapter_status.json"))
    with tabs[5]:
        st.dataframe(_csv(APPROVALS / "human_approval_queue.csv").head(100), use_container_width=True)
        st.dataframe(_csv(APPROVALS / "approval_decision_history.csv").head(100), use_container_width=True)
        st.json(_json(APPROVALS / "approval_sla_report.json"))
    with tabs[6]:
        st.json(_json(DEMO / "flagship_demo_summary.json"))
        demo_briefing = DEMO / "flagship_demo_briefing.md"
        st.markdown(demo_briefing.read_text(encoding="utf-8") if demo_briefing.exists() else "")
    with tabs[7]:
        st.dataframe(_csv(TRACES / "guardrail_spans.csv").head(200), use_container_width=True)
    with tabs[8]:
        st.json(_json(DECISIONS / "decision_lineage.json"))
    with tabs[9]:
        st.dataframe(_csv(EVALUATIONS / "agent_regression_suite.csv"), use_container_width=True)
    paths = [
        AGENTS / "agent_registry.csv", TOOLS / "tool_registry.csv", RUNTIME / "task_routing_decisions.csv",
        HANDOFFS / "agent_handoff_history.csv", DECISIONS / "tool_permission_decisions.csv",
        SIMULATIONS / "probability_scenarios.csv", CONFLICTS / "conflict_resolution_decisions.csv",
        APPROVALS / "human_approval_queue.csv", INCIDENTS / "agent_safety_incidents.csv",
        AUDIT / "agent_action_history.csv",
    ]
    for tab, path in zip(tabs[10:20], paths, strict=False):
        with tab:
            st.dataframe(_csv(path).head(200), use_container_width=True)
    with tabs[20]:
        for path in sorted(SCORECARDS.glob("*.json")):
            st.subheader(path.stem)
            st.json(_json(path))
    with tabs[21]:
        for path in [BRIEFINGS / "executive_agent_briefings.md", BRIEFINGS / "operator_agent_briefings.md"]:
            st.subheader(path.stem)
            st.markdown(path.read_text(encoding="utf-8") if path.exists() else "")


if __name__ == "__main__":
    main()

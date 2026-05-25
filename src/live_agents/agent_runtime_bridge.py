"""Bridge deterministic runtime outputs into optional live-agent context."""

from __future__ import annotations

import pandas as pd

from src.common.paths import DECISIONS, TASKS


def prepare_live_context(task_id: str) -> dict[str, object]:
    """Prepare advisory live-agent context for a task."""
    tasks = pd.read_csv(TASKS / "enterprise_tasks.csv") if (TASKS / "enterprise_tasks.csv").exists() else pd.DataFrame()
    decisions = pd.read_csv(DECISIONS / "final_agent_decisions.csv") if (DECISIONS / "final_agent_decisions.csv").exists() else pd.DataFrame()
    task = tasks.loc[tasks["task_id"].eq(task_id)].head(1).to_dict(orient="records")
    decision = decisions.loc[decisions["task_id"].eq(task_id)].head(1).to_dict(orient="records")
    return {
        "task": task[0] if task else {"task_id": task_id},
        "deterministic_decision": decision[0]["final_decision"] if decision else "request_more_evidence",
        "policy_authoritative": True,
    }


def merge_live_recommendation_with_policy_result(live_recommendation: dict[str, object], policy_result: dict[str, object]) -> dict[str, object]:
    """Merge advisory live output with authoritative deterministic policy."""
    return {
        "live_recommendation": live_recommendation,
        "policy_result": policy_result,
        "final_authority": "deterministic_policy_engine",
        "can_bypass_policy": False,
    }


def enforce_deterministic_governance(policy_result: dict[str, object]) -> dict[str, object]:
    """Return the deterministic policy decision as the authoritative outcome."""
    return {
        "governance_status": policy_result.get("governance_status", policy_result.get("decision", "require_human_approval")),
        "authoritative": True,
        "reason": "deterministic runtime policy remains system of record",
    }


def produce_hybrid_decision(task_id: str, live_recommendation: dict[str, object], policy_result: dict[str, object]) -> dict[str, object]:
    """Produce a hybrid-mode decision with deterministic governance authority."""
    governance = enforce_deterministic_governance(policy_result)
    return {
        "task_id": task_id,
        "hybrid_mode": True,
        "live_recommendation": live_recommendation.get("recommendation", "advisory_only"),
        "final_decision": governance["governance_status"],
        "governance_authoritative": governance["authoritative"],
    }


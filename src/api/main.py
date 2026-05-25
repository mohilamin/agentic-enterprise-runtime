"""FastAPI app for the agentic runtime."""

import json
from pathlib import Path
from typing import Any

import pandas as pd
from fastapi import FastAPI

from src.api.schemas import (
    ApprovalDecisionRequest,
    ConflictRequest,
    RouteTaskRequest,
    ScenarioRequest,
    ToolAccessRequest,
)
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
    LIVE_AGENTS,
    RED_TEAM,
    SCORECARDS,
    TASKS,
    TOOLS,
    TRACES,
)
from src.conflicts.arbitration_engine import arbitrate_conflict
from src.pipeline.run_all import run_pipeline
from src.routing.routing_score import calculate_routing_score
from src.safety.prompt_attack_detector import detect_prompt_attack
from src.simulation.probability_engine import expected_loss
from src.v02_core import (
    generate_red_team_outputs,
    run_evaluations,
    run_flagship_demo,
)
from src.v02_core import (
    submit_approval_decision as record_approval_decision,
)

app = FastAPI(title="Agentic Enterprise Runtime")


def _records(path: Path, limit: int = 100) -> list[dict[str, Any]]:
    return pd.read_csv(path).head(limit).fillna("").to_dict(orient="records") if path.exists() else []


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _jsonl(path: Path, limit: int = 100) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines()[:limit]:
        if line.strip():
            rows.append(json.loads(line))
    return rows


@app.get("/health")
def health() -> dict[str, str]:
    """Health endpoint."""
    return {"status": "ok", "service": "agentic-enterprise-runtime"}


@app.get("/runtime-summary")
def runtime_summary() -> dict[str, Any]:
    """Runtime summary."""
    summary = _json(SCORECARDS / "runtime_health_scorecard.json")
    v02 = _json(SCORECARDS / "v02_runtime_upgrade_summary.json")
    if v02:
        summary.update(
            {
                "trace_completeness_score": v02.get("trace_completeness_score"),
                "evaluation_score": v02.get("evaluation_score"),
                "red_team_detection_rate": v02.get("red_team_detection_rate"),
                "approval_queue_volume": summary.get("approval_queue_volume", 0),
                "live_agent_mode_status": v02.get("deterministic_fallback_status"),
                "deterministic_fallback_status": v02.get("deterministic_fallback_status"),
            }
        )
    return summary


@app.get("/agents")
def agents() -> list[dict[str, Any]]:
    """Agents."""
    return _records(AGENTS / "agent_registry.csv", 1000)


@app.get("/tools")
def tools() -> list[dict[str, Any]]:
    """Tools."""
    return _records(TOOLS / "tool_registry.csv", 1000)


@app.get("/tasks")
def tasks() -> list[dict[str, Any]]:
    """Tasks."""
    return _records(TASKS / "enterprise_tasks.csv")


@app.get("/tasks/{task_id}")
def task_detail(task_id: str) -> dict[str, Any]:
    """Task detail."""
    return next((row for row in _records(TASKS / "enterprise_tasks.csv", 10000) if row["task_id"] == task_id), {"found": False})


@app.get("/decisions")
def decisions() -> list[dict[str, Any]]:
    """Decisions."""
    return _records(DECISIONS / "final_agent_decisions.csv")


@app.get("/handoffs")
def handoffs() -> list[dict[str, Any]]:
    """Handoffs."""
    return _records(HANDOFFS / "agent_handoff_history.csv")


@app.get("/conflicts")
def conflicts() -> list[dict[str, Any]]:
    """Conflicts."""
    return _records(CONFLICTS / "conflict_resolution_decisions.csv")


@app.get("/approval-queue")
def approval_queue() -> list[dict[str, Any]]:
    """Approval queue."""
    return _records(APPROVALS / "human_approval_queue.csv")


@app.get("/audit-log")
def audit_log() -> list[dict[str, Any]]:
    """Audit log."""
    return _records(AUDIT / "agent_action_history.csv")


@app.get("/scorecards")
def scorecards() -> dict[str, Any]:
    """Scorecards."""
    return {path.stem: _json(path) for path in SCORECARDS.glob("*.json")}


@app.get("/traces")
def traces() -> list[dict[str, Any]]:
    """Trace event sample."""
    return _jsonl(TRACES / "agent_trace_events.jsonl")


@app.get("/traces/summary")
def traces_summary() -> dict[str, Any]:
    """Trace summary."""
    return _json(TRACES / "runtime_trace_summary.json")


@app.get("/evaluations")
def evaluations() -> dict[str, Any]:
    """Evaluation summary and reports."""
    return {
        "summary": _json(EVALUATIONS / "evaluation_summary.json"),
        "task_success": _json(EVALUATIONS / "task_success_report.json"),
        "tool_policy": _json(EVALUATIONS / "tool_policy_accuracy_report.json"),
        "red_team": _json(EVALUATIONS / "red_team_detection_report.json"),
    }


@app.get("/red-team-scenarios")
def red_team_scenarios() -> list[dict[str, Any]]:
    """Red-team scenarios."""
    return _json(RED_TEAM / "red_team_scenarios.json")


@app.get("/red-team-results")
def red_team_results() -> list[dict[str, Any]]:
    """Red-team results."""
    return _json(RED_TEAM / "red_team_results.json")


@app.get("/live-agent-status")
def live_agent_status() -> dict[str, Any]:
    """Optional live-agent adapter status."""
    return _json(LIVE_AGENTS / "live_agent_adapter_status.json")


@app.get("/approval-history")
def approval_history() -> list[dict[str, Any]]:
    """Approval decision history."""
    return _records(APPROVALS / "approval_decision_history.csv")


@app.get("/flagship-demo-summary")
def flagship_demo_summary() -> dict[str, Any]:
    """Flagship demo summary."""
    return _json(DEMO / "flagship_demo_summary.json")


@app.get("/v02-summary")
def v02_summary() -> dict[str, Any]:
    """V0.2 runtime summary."""
    return _json(SCORECARDS / "v02_runtime_upgrade_summary.json")


@app.get("/briefings")
def briefings() -> dict[str, str]:
    """Briefings."""
    return {
        "executive": (BRIEFINGS / "executive_agent_briefings.md").read_text(encoding="utf-8") if (BRIEFINGS / "executive_agent_briefings.md").exists() else "",
        "operator": (BRIEFINGS / "operator_agent_briefings.md").read_text(encoding="utf-8") if (BRIEFINGS / "operator_agent_briefings.md").exists() else "",
    }


@app.post("/route-task")
def route_task(request: RouteTaskRequest) -> dict[str, Any]:
    """Route task demo."""
    return {
        "selected_agent": f"{request.domain}_agent" if request.domain != "supply_chain" else "supply_chain_agent",
        "routing_score": calculate_routing_score(True, request.risk_score >= 70),
        "escalation_required": request.risk_score >= 70,
    }


@app.post("/evaluate-tool-access")
def evaluate_tool_access(request: ToolAccessRequest) -> dict[str, Any]:
    """Evaluate tool access demo."""
    attack = detect_prompt_attack(request.prompt)
    return {
        "decision": "deny" if attack else "allow_with_policy_check",
        "policy_reason": "prompt_injection_block" if attack else "least_privilege_check_passed",
    }


@app.post("/simulate-scenario")
def simulate_scenario(request: ScenarioRequest) -> dict[str, Any]:
    """Simulate scenario demo."""
    return {
        "scenario_id": request.scenario_id,
        "expected_loss_action": expected_loss(request.cost_of_action, 0.1),
        "expected_loss_inaction": expected_loss(request.cost_of_inaction, 0.08),
    }


@app.post("/resolve-conflict")
def resolve_conflict(request: ConflictRequest) -> dict[str, Any]:
    """Resolve conflict demo."""
    return {"arbitration_result": arbitrate_conflict(request.risk_score), "agents_involved": request.agents_involved}


@app.post("/submit-approval-decision")
def submit_approval_decision(request: ApprovalDecisionRequest) -> dict[str, Any]:
    """Submit approval decision demo."""
    return record_approval_decision(request.approval_id, request.decision)


@app.post("/run-flagship-demo")
def run_flagship_demo_endpoint() -> dict[str, Any]:
    """Run flagship demo."""
    return run_flagship_demo()


@app.post("/run-red-team-scenario")
def run_red_team_scenario_endpoint() -> dict[str, Any]:
    """Run red-team scenarios."""
    return generate_red_team_outputs()


@app.post("/run-evaluation-suite")
def run_evaluation_suite_endpoint() -> dict[str, Any]:
    """Run evaluation suite."""
    return run_evaluations()


@app.post("/run-pipeline")
def run_pipeline_endpoint() -> dict[str, Any]:
    """Run pipeline."""
    return run_pipeline()

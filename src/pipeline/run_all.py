"""Run the full agentic enterprise runtime pipeline."""

from src.common.config import settings
from src.common.logging import get_logger
from src.runtime_core import (
    build_agent_registry,
    build_tool_registry,
    create_approval_outputs,
    create_audit_outputs,
    create_briefings,
    create_final_decisions,
    create_memory_outputs,
    create_scorecards,
    detect_conflicts,
    detect_safety_incidents,
    evaluate_tool_permissions,
    generate_domain_cases,
    generate_handoffs,
    generate_probability_scenarios,
    generate_tasks,
    route_tasks,
    run_probability_simulations,
)
from src.storage.duckdb_store import load_duckdb_store
from src.v02_core import (
    create_v02_scorecards,
    generate_red_team_outputs,
    generate_trace_outputs,
    live_agent_status,
    run_evaluations,
    run_flagship_demo,
    update_approval_workflow,
)

LOGGER = get_logger(__name__)


def run_pipeline() -> dict[str, object]:
    """Run all runtime stages."""
    task_count = int(settings().get("task_count", 600))
    generate_domain_cases()
    scenarios = generate_probability_scenarios()
    tasks = generate_tasks(task_count=task_count)
    agents = build_agent_registry()
    tools = build_tool_registry()
    routing = route_tasks(tasks, agents)
    permissions = evaluate_tool_permissions(tasks, agents, tools)
    handoffs = generate_handoffs(tasks)
    conflicts, conflict_resolutions = detect_conflicts(tasks)
    simulations = run_probability_simulations(tasks, scenarios)
    incidents = detect_safety_incidents(tasks, permissions)
    decisions = create_final_decisions(tasks, routing, permissions, simulations)
    queue, escrow = create_approval_outputs(decisions)
    audit = create_audit_outputs(tasks, permissions, decisions)
    create_memory_outputs(decisions, conflicts)
    create_briefings(decisions, queue, conflicts, incidents)
    create_scorecards(tasks, permissions, decisions, handoffs, conflicts, simulations, incidents, queue)
    live_status = live_agent_status()
    trace_summary = generate_trace_outputs()
    red_team_scorecard = generate_red_team_outputs()
    approval_sla = update_approval_workflow()
    evaluation_summary = run_evaluations()
    demo_summary = run_flagship_demo()
    v02_summary = create_v02_scorecards()
    db_path = load_duckdb_store()
    summary = {
        "tasks": len(tasks),
        "agents": len(agents),
        "tools": len(tools),
        "routing_decisions": len(routing),
        "tool_permission_decisions": len(permissions),
        "handoffs": len(handoffs),
        "conflicts": len(conflicts),
        "conflict_resolutions": len(conflict_resolutions),
        "simulations": len(simulations),
        "safety_incidents": len(incidents),
        "final_decisions": len(decisions),
        "approval_queue": len(queue),
        "action_escrow": len(escrow),
        "audit_events": len(audit),
        "warehouse": db_path,
        "v02_trace_completeness_score": trace_summary["trace_completeness_score"],
        "v02_evaluation_score": evaluation_summary["overall_runtime_evaluation_score"],
        "v02_red_team_detection_rate": red_team_scorecard["red_team_detection_rate"],
        "v02_approval_sla_score": approval_sla["approval_sla_score"],
        "v02_live_agent_mode": live_status["mode"],
        "v02_flagship_demo": demo_summary["scenario_name"],
        "v02_summary_score": v02_summary["overall_v02_runtime_maturity_score"],
    }
    LOGGER.info("Runtime pipeline completed: %s", summary)
    return summary


if __name__ == "__main__":
    run_pipeline()

# Metrics

- `task_resolution_rate`: share of tasks with a decision other than request more evidence.
- `autonomous_execution_rate`: share of tasks executed or shadow-executed.
- `human_escalation_rate`: share of tasks requiring human approval.
- `blocked_action_rate`: share of blocked tasks.
- `policy_violation_rate`: share of denied tool permission decisions.
- `prompt_attack_block_rate`: share of safety incidents classified as prompt attacks.
- `tool_permission_pass_rate`: share of allowed or approval-routed tool decisions.
- `overall_runtime_safety_score`: blended governance score for V0.1 evidence.

## V0.2 Metrics

- `trace_completeness_score`: share of required trace artifacts and core spans present.
- `task_resolution_accuracy`: share of tasks routed to the expected primary agent.
- `tool_policy_precision`: estimated correctness of policy decisions.
- `unsafe_tool_block_rate`: share of unsafe tool requests blocked or escalated.
- `prompt_attack_block_rate`: share of prompt attacks detected and blocked.
- `red_team_detection_rate`: share of adversarial scenarios detected.
- `decision_lineage_completeness`: share of final decisions with lineage evidence.
- `approval_sla_score`: approval workflow health score based on queue volume and SLA.
- `deterministic_fallback_health`: live-agent fallback readiness score.
- `overall_v02_runtime_maturity_score`: blended V0.2 score across tracing, evals, red-team, approvals, fallback, and demo readiness.

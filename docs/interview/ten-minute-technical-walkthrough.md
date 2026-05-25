# Ten-Minute Technical Walkthrough

## 1. Problem Framing

Future enterprise AI systems will coordinate many agents across domains. The runtime must govern tool access, handoffs, conflicts, approvals, and audit evidence.

## 2. Runtime Architecture

Start with `README.md` and `architecture/architecture.md`. Explain that deterministic orchestration is the system of record.

## 3. Agent and Tool Registries

Mention:
- `config/agent_registry.yaml`
- `config/tool_registry.yaml`
- `src/registry/agent_registry.py`
- `src/registry/tool_registry.py`

Registries make agent capabilities and tool permissions explicit.

## 4. Policy Engine

Mention:
- `config/tool_policies.yaml`
- `src/policies/tool_policy_engine.py`

Policy controls include least privilege, approval requirements, prompt injection blocking, sensitive data handling, and irreversible-action checks.

## 5. Task Routing

Mention:
- `src/routing/task_router.py`

Routing considers task type, domain, required capabilities, risk level, and expected primary/secondary agents.

## 6. Handoffs

Mention:
- `src/handoffs/handoff_engine.py`

Handoffs are explicit records with evidence and accepted flags.

## 7. Conflict Arbitration

Mention:
- `src/conflicts/arbitration_engine.py`

Conflicts are resolved using authority, evidence, risk, reversibility, and governance status.

## 8. Probability Simulation

Mention:
- `src/simulation/probability_engine.py`

The runtime compares action cost, inaction cost, false positives, false negatives, reversibility, and blast radius.

## 9. Red-Team Scenarios

Mention:
- `src/red_team/red_team_runner.py`

Scenarios cover prompt injection, approval bypass, cross-domain tool abuse, memory contamination, and unsafe irreversible actions.

## 10. Evaluation Harness

Mention:
- `src/evaluation/evaluation_runner.py`

The harness validates routing, policy, handoffs, conflicts, approvals, lineage, audit completeness, and red-team detection.

## 11. Tracing and Auditability

Mention:
- `src/tracing/trace_recorder.py`

The trace layer writes task, tool, handoff, guardrail, and final decision spans.

## 12. Approval Workflow

Mention:
- `src/approvals/approval_decision.py`

High-risk actions are staged in an approval queue and action escrow.

## 13. FastAPI and Streamlit

Mention:
- `src/api/main.py`
- `src/dashboard/app.py`

The API and dashboard expose runtime evidence for demos and reviews.

## 14. What Would Change in Production

Replace deterministic adapters with real agent framework calls, add identity and RBAC, export traces to OpenTelemetry, use OPA for policies, connect approvals to ServiceNow/Jira, store data in Snowflake/Databricks, and deploy behind authenticated cloud services.


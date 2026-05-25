# Five-Minute Demo Script

## 0:00-0:30 — Business Problem

Enterprise AI will involve many specialized agents, not one chatbot. The hard part is governance: which agent can use which tool, when work should be handed off, how conflicts are resolved, how risk is scored, and how every decision is audited.

Presenter notes:
- Do not oversell this as production software.
- Emphasize deterministic simulation and no external API requirement.
- Frame the project as an AI infrastructure control plane.

## 0:30-1:10 — Architecture

Show the README architecture diagram and dashboard overview.

Point to:
- agent registry
- tool registry
- task router
- policy engine
- handoff engine
- conflict arbitration
- probability simulator
- approval queue
- trace recorder
- evaluation harness

## 1:10-2:10 — Flagship Scenario

Run:

```bash
python -m src.demo.run_flagship_demo
```

Story:
1. A support refund request arrives.
2. The support agent triages the request.
3. Fraud indicators appear.
4. The fraud agent reviews account freeze risk.
5. The security agent detects prompt injection.
6. The governance agent reviews policy.
7. Conflict arbitration runs.
8. Direct account freeze is blocked.
9. A human approval item is created.
10. Executive briefing evidence is generated.

## 2:10-3:00 — Traces and Audit

Show:
- `data/traces/agent_trace_events.jsonl`
- `data/traces/tool_call_spans.csv`
- `data/traces/handoff_spans.csv`
- `data/traces/guardrail_spans.csv`
- `data/decisions/decision_lineage.json`
- `data/audit/agent_action_history.csv`

Explain that the value is not only the final answer; it is reconstructing how the system reached it.

## 3:00-3:50 — Evaluation and Red-Team

Show:
- task success report
- tool policy accuracy report
- unsafe tool block rate
- prompt attack block rate
- red-team results

Explain that governed agents need regression tests and adversarial scenarios, not only happy-path demos.

## 3:50-4:30 — Approval Workflow and Scorecards

Show:
- human approval queue
- approval decision history
- approval SLA report
- `v02_runtime_upgrade_summary`
- `red_team_scorecard`
- `evaluation_scorecard`

## 4:30-5:00 — Production Mapping

Explain how this could map to:
- OpenAI Agents SDK or LangGraph
- OpenPolicyAgent
- OpenTelemetry
- ServiceNow/Jira approvals
- Snowflake/Databricks
- identity provider and RBAC
- cloud deployment

Commands:

```bash
python -m src.pipeline.run_all
python -m src.demo.run_flagship_demo
streamlit run src/dashboard/app.py
uvicorn src.api.main:app --reload
```


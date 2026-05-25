# AI Platform Interview Talking Points

- The optional live-agent adapter models how OpenAI Agents SDK or LangGraph could plug in without replacing governance.
- Tool governance is enforced before execution and real execution is disabled by default.
- Guardrails detect prompt injection, unsafe tools, missing evidence, and approval-required actions.
- The approval workflow stages high-risk actions instead of allowing autonomous execution.
- Agent evaluations cover routing, tool policy, handoff accuracy, conflict resolution, approval decisions, red-team detection, lineage, and audit completeness.
- Trace outputs make agent workflows observable and debuggable.
- Production mapping: real agent SDK, OPA, OpenTelemetry, IAM, ServiceNow/Jira, Snowflake/Databricks, and cloud deployment.


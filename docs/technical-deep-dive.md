# Technical Deep Dive

V0.1 uses deterministic agents instead of LLM calls so reviewers can inspect orchestration logic. The architecture maps naturally to OpenAI Agents SDK, LangGraph, LlamaIndex tools, OpenPolicyAgent, Snowflake/Databricks, Kafka, Slack/Jira approvals, and OpenTelemetry in future versions.

## V0.2 Additions

V0.2 keeps deterministic execution as the system of record and adds production-shaped controls around it:

- optional live-agent adapter with dynamic imports and deterministic fallback
- trace events and span exports for routing, tools, handoffs, guardrails, approvals, and final decisions
- offline evaluation harness comparing runtime outputs to generated task ground truth
- red-team scenario pack for prompt injection, approval bypass, tool abuse, memory contamination, and irreversible action risk
- approval decision history and SLA scorecards
- flagship demo scenario with support, fraud, security, governance, and executive agents

The key architectural choice is that live-agent outputs are advisory. They can enrich a recommendation, but they cannot bypass deterministic policy, safety checks, approval workflow, audit logging, or decision lineage.

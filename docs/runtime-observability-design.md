# Runtime Observability Design

The V0.2 trace layer emits task, tool, handoff, guardrail, approval, and final-decision spans.

Outputs:
- `data/traces/agent_trace_events.jsonl`
- `data/traces/tool_call_spans.csv`
- `data/traces/handoff_spans.csv`
- `data/traces/guardrail_spans.csv`
- `data/traces/runtime_trace_summary.json`

The trace summary tracks trace count, span count, tool calls, handoffs, guardrails, approval requirements, blocked actions, and trace completeness. This approximates production agent observability patterns while staying offline and deterministic.


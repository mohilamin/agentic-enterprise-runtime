# Senior Engineer Talking Points

- Deterministic simulation keeps the system inspectable and testable.
- Agents and tools are registry-driven, not scattered through ad hoc code.
- Policy enforcement is authoritative; live-agent recommendations are advisory.
- Tool requests produce permission decisions and audit evidence.
- Handoffs and conflicts are explicit runtime artifacts.
- Evaluation harnesses compare outputs to expected task behavior.
- Red-team scenarios exercise prompt injection, tool abuse, approval bypass, and unsafe irreversible actions.
- Tracing reconstructs task, tool, handoff, guardrail, and final decision flow.
- In production, I would add real IAM/RBAC, OPA, OpenTelemetry, durable queues, cloud warehouse storage, and service-management approval integration.


# Likely Interview Questions

## Why not use a real LLM?

The goal is to make the governance runtime inspectable and deterministic. Live-agent mode is optional because tests should not depend on paid APIs or nondeterministic responses.

## How would this work with OpenAI Agents SDK?

The adapter would map registry agents to SDK agents, local tools to tool/function specs, and handoff rules to agent handoffs. The deterministic policy engine would remain authoritative.

## How would you prevent prompt injection?

Prompt injection is detected before tool execution. If detected, tool calls are blocked, a safety incident is created, and the decision path is audited.

## How do you evaluate agent decisions?

The evaluation harness compares runtime outputs to generated ground truth and checks routing accuracy, policy precision, unsafe tool blocking, approvals, lineage completeness, and audit completeness.

## What is the difference between confidence and risk?

Confidence measures how strongly the agent supports a recommendation. Risk measures potential harm, governance exposure, reversibility, and blast radius. High confidence does not override high risk.

## Why does deterministic simulation matter?

It makes the system reproducible, testable, and reviewable. It also separates governance architecture from LLM behavior.

## What would need to change for production?

Add real IAM, RBAC, OPA, OpenTelemetry, durable storage, production queues, secrets management, real approval systems, cloud deployment, and live tool adapters.

## How would you integrate identity and access management?

Map requester, agent, and tool permissions to an identity provider. Enforce role, domain, purpose, and approval policies before any tool execution.

## How would you scale this?

Move tasks and spans to event streams, store outputs in a warehouse, run evaluations as CI/regression jobs, and expose operational views through observability tooling.

## How would you monitor it?

Export traces to OpenTelemetry, add metrics for policy violations, approval queue age, red-team regression, tool failures, and action outcomes.

## How would you handle data privacy?

Keep sensitive tool outputs masked, enforce purpose-based access, audit all access, and block or escalate any cross-domain or unapproved sensitive data request.

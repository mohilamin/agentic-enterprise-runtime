# AGENTS.md

You are building a flagship AI Infrastructure + Data Engineering + Multi-Agent Governance project.

Project name:
Agentic Enterprise Runtime

Primary goal:
Build a local governed multi-agent enterprise runtime that simulates how specialized AI agents coordinate tasks, request tools, evaluate permissions, hand off work, resolve conflicts, score risk, simulate outcomes, and generate audit-ready decisions.

## Business Context

Future enterprises will deploy many specialized AI agents. The hard problem is not creating one agent. The hard problem is orchestrating many agents safely.

This project must demonstrate:
- multi-agent task routing
- tool governance
- policy enforcement
- agent handoffs
- conflict resolution
- probability-based scenario simulation
- decision lineage
- human approval workflows
- auditability
- enterprise risk controls

## Core Outcome

The system should answer:

"Can this multi-agent workflow complete the task safely, with the right tools, under the right policies, with auditable reasoning?"

## Build Principles

- Write clean, modular, production-style Python.
- Use Python 3.12.
- Use type hints.
- Use docstrings for public functions.
- Use structured logging.
- Add error handling.
- Use synthetic data only.
- Do not use real sensitive data.
- Do not require external services in V0.1.
- Keep V0.1 deterministic and locally runnable.
- Simulate agents deterministically; do not require paid LLM APIs.
- Every agent action must have a reason.
- Every tool call must have permission evaluation.
- Every handoff must have explanation.
- Every blocked action must include policy reasons.
- Every risky action must include risk score and approval status.
- Every scenario must include probability assumptions.
- Every major runtime stage must have tests.
- README must be public-facing and recruiter-friendly.
- Technical docs must be strong enough for senior AI platform engineers.

## Commit Message Requirements

- Do not use generic AI-like commit messages such as "Build project," "Create files," "Build agents," "Build runtime," or "Build orchestration."
- Use human, professional, scoped commit messages.
- Prefer Conventional Commit style:
  - `feat(runtime): add multi-agent task router`
  - `feat(tools): implement governed tool registry`
  - `feat(policy): enforce agent tool permissions`
  - `feat(simulation): add probabilistic outcome scoring`
  - `feat(memory): add shared agent memory store`
  - `feat(audit): generate agent action audit trail`
  - `feat(api): expose agent runtime endpoints`
  - `test(policy): cover unsafe tool access blocking`
  - `docs(readme): explain multi-agent governance architecture`
  - `fix(routing): correct handoff confidence threshold`

## Definition of Done

A task is complete only when code runs locally, tests pass, ruff passes, README is detailed and diagram-rich, domain and probability scenarios exist, registries exist, runtime decisions exist, handoff graph exists, conflict decisions exist, approval queue exists, audit logs exist, scorecards exist, briefings exist, dashboard and API can launch, GitHub Actions and Docker exist, and no real sensitive data is used.


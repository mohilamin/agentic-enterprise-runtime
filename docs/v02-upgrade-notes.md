# V0.2 Upgrade Notes

V0.2 adds optional live-agent adapters, trace-style observability, evaluation harnesses, red-team scenarios, interactive approvals, a flagship demo, new API endpoints, dashboard sections, DuckDB tables, and scorecards.

Design constraints preserved:
- deterministic mode remains default
- no external API key required
- tests run offline
- live-agent recommendations are advisory
- deterministic policy enforcement remains authoritative
- no secrets are stored in the repo

New scorecards:
- `v02_runtime_upgrade_summary`
- `red_team_scorecard`
- `evaluation_scorecard`
- `trace_observability_scorecard`
- `approval_workflow_scorecard`
- `live_agent_adapter_scorecard`

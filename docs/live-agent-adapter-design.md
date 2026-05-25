# Live Agent Adapter Design

V0.2 adds an optional live-agent adapter without changing the deterministic runtime contract.

Default behavior:
- `live_agent_mode: false`
- `hybrid_mode: false`
- no API key required
- optional SDK imports only
- deterministic fallback when the SDK or credentials are missing

The adapter maps local agent registry rows to framework-style agent specs, local tools to function descriptors, and local handoffs to handoff descriptors. Real tool execution is disabled by default. Live-agent recommendations may propose actions, but deterministic policy remains authoritative.

The bridge writes:
- `data/live_agents/live_agent_adapter_status.json`
- `data/live_agents/live_agent_bridge_report.json`
- `data/live_agents/hybrid_decision_report.csv`


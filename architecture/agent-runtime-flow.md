# Agent Runtime Flow

Task -> intent classification -> task routing -> agent recommendation -> tool policy evaluation -> handoff/conflict checks -> simulation -> safety gates -> final decision -> approval/audit/briefing.

V0.2 wraps the flow in trace spans, evaluation checks, red-team assertions, and approval history updates.

Task intake routes work to a specialist agent, evaluates tool access, simulates outcomes, applies safety gates, and generates a final auditable decision.

"""Flagship scenario metadata."""


def flagship_scenario() -> dict[str, object]:
    """Return the flagship demo scenario contract."""
    return {
        "scenario_name": "support_refund_with_fraud_and_prompt_injection",
        "expected_final_decision": "require_human_approval",
        "expected_agents": ["support_agent", "fraud_agent", "security_agent", "governance_agent", "executive_agent"],
    }


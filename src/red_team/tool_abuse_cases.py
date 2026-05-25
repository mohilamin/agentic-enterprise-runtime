"""Tool abuse red-team cases."""


def cross_domain_tool_abuse_case() -> dict[str, object]:
    """Return a cross-domain tool abuse test case."""
    return {"attack_type": "cross_domain_tool_abuse", "expected_final_decision": "blocked"}


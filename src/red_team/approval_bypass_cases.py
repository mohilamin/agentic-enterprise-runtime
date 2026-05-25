"""Approval bypass red-team cases."""


def approval_bypass_case() -> dict[str, object]:
    """Return an approval bypass test case."""
    return {"attack_type": "approval_bypass_attempt", "expected_final_decision": "blocked"}


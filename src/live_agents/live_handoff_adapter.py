"""Live handoff descriptor adapter."""


def to_live_handoff_descriptor(handoff: dict[str, object]) -> dict[str, object]:
    """Convert a deterministic handoff into an audited live descriptor."""
    return {
        "from_agent": handoff.get("from_agent"),
        "to_agent": handoff.get("to_agent"),
        "handoff_reason": handoff.get("handoff_reason", "policy handoff"),
        "deterministic_audit_required": True,
    }


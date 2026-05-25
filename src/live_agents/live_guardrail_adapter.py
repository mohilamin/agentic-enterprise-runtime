"""Guardrail adapter for live-agent advisory mode."""

from src.safety.prompt_attack_detector import detect_prompt_attack


def evaluate_live_guardrails(prompt: str, tool_allowed: bool, has_evidence: bool, approval_required: bool) -> dict[str, object]:
    """Evaluate prompt, tool, evidence, and approval guardrails."""
    prompt_attack = detect_prompt_attack(prompt)
    triggered = []
    if prompt_attack:
        triggered.append("prompt_injection")
    if not tool_allowed:
        triggered.append("unsafe_tool")
    if not has_evidence:
        triggered.append("missing_evidence")
    if approval_required:
        triggered.append("approval_required")
    return {
        "guardrail_passed": not triggered,
        "triggered_guardrails": triggered,
        "final_policy_result": "deny" if prompt_attack or not tool_allowed else "require_approval" if approval_required else "allow",
    }


"""Optional OpenAI Agents SDK adapter.

The dependency is intentionally optional. Tests and default runtime execution
never require a live SDK or API key.
"""

from __future__ import annotations

import os
from typing import Any

from src.live_agents.fallback import deterministic_fallback


class OpenAIAgentAdapter:
    """Bridge local agent configs to optional live-agent framework specs."""

    def is_available(self) -> bool:
        """Return whether the optional SDK and runtime credentials are available."""
        try:
            __import__("agents")
        except Exception:
            return False
        return bool(os.environ.get("OPENAI_API_KEY"))

    def build_agent_spec(self, agent_config: dict[str, Any]) -> dict[str, Any]:
        """Convert a deterministic agent row into a live-agent-ready spec."""
        return {
            "name": agent_config.get("agent_name", agent_config.get("agent_id", "agent")),
            "instructions": agent_config.get("description", "Follow deterministic runtime governance."),
            "tools": str(agent_config.get("allowed_tools", "")).split("|") if agent_config.get("allowed_tools") else [],
            "governance_authoritative": True,
        }

    def run_agent_task(self, task: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
        """Run a task through optional live mode or return deterministic fallback."""
        if not self.is_available():
            return deterministic_fallback()
        return {
            "mode": "live_agent_advisory",
            "available": True,
            "task_id": task.get("task_id"),
            "recommendation": context.get("deterministic_decision", "request_more_evidence"),
            "policy_authoritative": True,
        }

    def convert_tool_registry_to_function_specs(self, tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Convert deterministic tool records into safe function descriptors."""
        return [
            {
                "name": tool.get("tool_id", tool.get("tool_name", "tool")),
                "description": tool.get("description", "Simulated deterministic tool."),
                "risk_level": tool.get("risk_level", "medium"),
                "execution_enabled": False,
            }
            for tool in tools
        ]

    def convert_handoffs_to_agent_specs(self, handoffs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Convert handoff rows into advisory live handoff descriptors."""
        return [
            {
                "from_agent": handoff.get("from_agent"),
                "to_agent": handoff.get("to_agent"),
                "audit_required": True,
                "reason": handoff.get("handoff_reason", "deterministic handoff rule"),
            }
            for handoff in handoffs
        ]


"""API schemas."""

from pydantic import BaseModel


class RouteTaskRequest(BaseModel):
    """Route task request."""

    task_type: str
    domain: str
    risk_score: int = 50


class ToolAccessRequest(BaseModel):
    """Tool access request."""

    agent_id: str
    tool_id: str
    prompt: str = ""


class ScenarioRequest(BaseModel):
    """Scenario simulation request."""

    scenario_id: str
    cost_of_action: float = 1000
    cost_of_inaction: float = 5000


class ConflictRequest(BaseModel):
    """Conflict resolution request."""

    risk_score: int
    agents_involved: list[str]


class ApprovalDecisionRequest(BaseModel):
    """Approval decision request."""

    approval_id: str
    decision: str


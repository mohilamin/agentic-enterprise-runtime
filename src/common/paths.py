"""Project path helpers."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"
TASKS = DATA / "tasks"
AGENTS = DATA / "agents"
TOOLS = DATA / "tools"
RUNTIME = DATA / "runtime"
DECISIONS = DATA / "decisions"
HANDOFFS = DATA / "handoffs"
CONFLICTS = DATA / "conflicts"
SIMULATIONS = DATA / "simulations"
APPROVALS = DATA / "approvals"
MEMORY = DATA / "memory"
AUDIT = DATA / "audit"
INCIDENTS = DATA / "incidents"
BRIEFINGS = DATA / "briefings"
WAREHOUSE = DATA / "warehouse"
SCORECARDS = DATA / "scorecards"


def ensure_dirs() -> None:
    """Create runtime directories."""
    for path in [
        RAW,
        TASKS,
        AGENTS,
        TOOLS,
        RUNTIME,
        DECISIONS,
        HANDOFFS,
        CONFLICTS,
        SIMULATIONS,
        APPROVALS,
        MEMORY,
        AUDIT,
        INCIDENTS,
        BRIEFINGS,
        WAREHOUSE,
        SCORECARDS,
    ]:
        path.mkdir(parents=True, exist_ok=True)


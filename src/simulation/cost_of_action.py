"""Cost helpers."""


def compare_action_costs(cost_action: float, cost_inaction: float) -> str:
    """Compare action and inaction costs."""
    return "act" if cost_action <= cost_inaction else "wait"


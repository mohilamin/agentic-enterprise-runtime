"""Evaluation dataset helpers."""

import json

from src.common.paths import TASKS


def load_task_ground_truth() -> dict[str, object]:
    """Load task ground truth labels."""
    return json.loads((TASKS / "task_ground_truth.json").read_text(encoding="utf-8"))


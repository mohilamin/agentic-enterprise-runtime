"""Intent classifier."""


def classify_intent(task_type: str) -> str:
    """Classify task intent from task type."""
    return task_type.replace("_", " ")


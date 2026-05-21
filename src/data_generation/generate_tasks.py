"""Generate synthetic enterprise tasks."""

from src.common.config import settings
from src.common.logging import get_logger
from src.runtime_core import generate_tasks

LOGGER = get_logger(__name__)


def main():
    """Generate enterprise tasks."""
    task_count = int(settings().get("task_count", 600))
    frame = generate_tasks(task_count=task_count)
    LOGGER.info("Generated %s tasks", len(frame))
    return frame


if __name__ == "__main__":
    main()


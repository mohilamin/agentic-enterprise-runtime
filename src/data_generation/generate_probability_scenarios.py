"""Generate probability scenarios."""

from src.common.logging import get_logger
from src.runtime_core import generate_probability_scenarios

LOGGER = get_logger(__name__)


def main():
    """Generate probability scenarios."""
    frame = generate_probability_scenarios()
    LOGGER.info("Generated %s probability scenarios", len(frame))
    return frame


if __name__ == "__main__":
    main()


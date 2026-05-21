"""Generate synthetic enterprise domain data."""

from src.common.logging import get_logger
from src.runtime_core import build_agent_registry, build_tool_registry, generate_domain_cases

LOGGER = get_logger(__name__)


def main() -> dict[str, int]:
    """Generate domain data plus registries."""
    build_agent_registry()
    build_tool_registry()
    counts = generate_domain_cases()
    LOGGER.info("Generated domain data: %s", counts)
    return counts


if __name__ == "__main__":
    main()


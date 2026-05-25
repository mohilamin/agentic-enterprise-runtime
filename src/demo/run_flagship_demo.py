"""Run the flagship V0.2 scenario."""

from src.v02_core import run_flagship_demo


def main() -> dict[str, object]:
    """Run flagship demo and print a concise summary."""
    summary = run_flagship_demo()
    print(summary)
    return summary


if __name__ == "__main__":
    main()


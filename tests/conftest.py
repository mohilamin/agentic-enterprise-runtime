"""Shared fixtures."""

import pytest

from src.pipeline.run_all import run_pipeline


@pytest.fixture(scope="session", autouse=True)
def pipeline_outputs() -> dict[str, object]:
    """Run the runtime pipeline once for tests."""
    return run_pipeline()


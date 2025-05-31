import os

import pytest


# Configuration for Playwright tests
def pytest_configure(config):
    # Set up any global configurations here
    os.environ["PLAYWRIGHT_HEADLESS"] = "true"  # Run in headless mode by default


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Fixture to set browser context arguments."""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
        "record_video_dir": "e2e_tests/videos",
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Fixture to set browser launch arguments."""
    return {
        **browser_type_launch_args,
        "headless": os.getenv("PLAYWRIGHT_HEADLESS", "true").lower() == "true",
        "slow_mo": int(os.getenv("PLAYWRIGHT_SLOW_MO", "0")),
    }

import os
import pytest
import subprocess
import time
import signal
from playwright.sync_api import sync_playwright

# Default port for the FastAPI server
SERVER_PORT = 8000

@pytest.fixture(scope="session")
def server_process():
    """Start the FastAPI server as a subprocess for testing."""
    # Start the server
    process = subprocess.Popen(
        ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", str(SERVER_PORT)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid  # Create a new process group
    )
    
    # Give the server time to start
    time.sleep(2)
    
    yield process
    
    # Shutdown the server after tests
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    process.wait()

@pytest.fixture(scope="session")
def playwright_browser(server_process):
    """Create a browser instance for testing."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(playwright_browser):
    """Create a new page for each test."""
    page = playwright_browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def base_url():
    """Return the base URL for the FastAPI server."""
    return f"http://localhost:{SERVER_PORT}"

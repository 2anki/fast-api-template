import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    This fixture uses a context manager to ensure proper cleanup.
    """
    with TestClient(app) as test_client:
        yield test_client

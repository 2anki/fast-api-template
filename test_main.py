import asyncio
import pytest
from fastapi.testclient import TestClient
from main import app

# Use pytest fixture to create a client with proper event loop setup
@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI!"}

def test_read_item(client):
    response = client.get("/items/42?q=test-query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test-query"}

def test_create_item(client):
    payload = {
        "name": "Book",
        "description": "Fiction novel",
        "price": 100.0,
        "tax": 10.0
    }
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Book"
    assert response.json()["total_price"] == 110.0

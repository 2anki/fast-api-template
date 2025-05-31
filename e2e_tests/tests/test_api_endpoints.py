import pytest
from playwright.sync_api import Page, expect
import json

def test_root_endpoint(page: Page, base_url: str):
    """Test that the root endpoint returns the expected response."""
    # Make a request to the root endpoint
    page.goto(f"{base_url}/")
    
    # Get the pre-formatted response (Playwright renders JSON responses in a pre tag)
    response_text = page.locator("pre").inner_text()
    response_json = json.loads(response_text)
    
    # Verify the response
    assert response_json == {"message": "Welcome to FastAPI!"}

def test_read_item_endpoint(page: Page, base_url: str):
    """Test that the read item endpoint returns the expected response."""
    # Make a request to the read item endpoint with query parameters
    page.goto(f"{base_url}/items/42?q=test-query")
    
    # Get the pre-formatted response
    response_text = page.locator("pre").inner_text()
    response_json = json.loads(response_text)
    
    # Verify the response
    assert response_json == {"item_id": 42, "q": "test-query"}

def test_create_item_endpoint(page: Page, base_url: str):
    """Test that the create item endpoint processes the request correctly."""
    # Create the payload
    payload = {
        "name": "Book",
        "description": "Fiction novel",
        "price": 100.0,
        "tax": 10.0
    }
    
    # Navigate to a blank page first
    page.goto(f"{base_url}")
    
    # Use the fetch API to make a POST request
    response_json = page.evaluate("""async (payload) => {
        const response = await fetch('/items/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        return await response.json();
    }""", payload)
    
    # Verify the response
    assert response_json["name"] == "Book"
    assert response_json["total_price"] == 110.0

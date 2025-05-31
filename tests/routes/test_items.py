def test_read_item(client):
    """Test the read_item endpoint returns the expected item data."""
    response = client.get("/items/42?q=test-query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test-query"}


def test_create_item(client):
    """Test the create_item endpoint correctly processes an item and returns the expected result."""
    payload = {
        "name": "Book",
        "description": "Fiction novel",
        "price": 100.0,
        "tax": 10.0,
    }
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Book"
    assert response.json()["total_price"] == 110.0

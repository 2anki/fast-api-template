def test_read_root(client):
    """Test the root endpoint returns the expected welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI!"}

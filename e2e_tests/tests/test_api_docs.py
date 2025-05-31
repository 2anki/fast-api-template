import pytest
from playwright.sync_api import Page, expect
from ..pages.api_docs_page import ApiDocsPage

def test_swagger_ui_loads(page: Page, base_url: str):
    """Test that the Swagger UI documentation loads correctly."""
    # Navigate to the docs page
    api_docs = ApiDocsPage(page)
    api_docs.navigate()
    
    # Verify that the page title contains 'FastAPI'
    title = page.title()
    assert "FastAPI" in title, f"Expected 'FastAPI' in title, got '{title}'"
    
    # Verify that the Swagger UI is loaded
    assert api_docs.is_loaded(), "Swagger UI did not load properly"
    
    # Verify that we have endpoints displayed
    assert api_docs.get_endpoint_count() > 0, "No endpoints were found in the API documentation"

def test_root_endpoint_documentation(page: Page, base_url: str):
    """Test that the root endpoint is documented correctly."""
    api_docs = ApiDocsPage(page)
    api_docs.navigate()
    
    # Find the GET method for root endpoint - using more specific selector
    root_endpoint = page.locator('#operations-root-read_root__get')
    expect(root_endpoint).to_be_visible()
    
    # Check that the page contains the root path
    page_content = page.content()
    assert "/" in page_content, "Root endpoint path '/' not found in page content"

def test_items_endpoint_documentation(page: Page, base_url: str):
    """Test that the items endpoints are documented correctly."""
    api_docs = ApiDocsPage(page)
    api_docs.navigate()
    
    # Check for items endpoint using a more specific selector
    items_endpoint = page.locator('#operations-items-read_item_items__item_id__get')
    expect(items_endpoint).to_be_visible()
    
    # Check for POST method for creating items using a more specific selector
    create_items_endpoint = page.locator('#operations-items-create_item_items__post')
    expect(create_items_endpoint).to_be_visible()

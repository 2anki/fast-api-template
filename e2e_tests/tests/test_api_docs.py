import pytest
from playwright.sync_api import Page, expect
from e2e_tests.pages.api_docs_page import ApiDocsPage

def test_swagger_ui_loads(page: Page, base_url: str):
    """Test that the Swagger UI documentation loads correctly."""
    # Navigate to the docs page
    api_docs = ApiDocsPage(page)
    api_docs.navigate()
    
    # Verify that the page title contains 'FastAPI'
    expect(page).to_have_title(lambda title: "FastAPI" in title)
    
    # Verify that the Swagger UI is loaded
    assert api_docs.is_loaded(), "Swagger UI did not load properly"
    
    # Verify that we have endpoints displayed
    assert api_docs.get_endpoint_count() > 0, "No endpoints were found in the API documentation"

def test_root_endpoint_documentation(page: Page, base_url: str):
    """Test that the root endpoint is documented correctly."""
    api_docs = ApiDocsPage(page)
    api_docs.navigate()
    
    # Expand the root endpoint section
    api_docs.expand_endpoint("root")
    
    # Check for GET method
    get_method = page.locator('.opblock-get')
    expect(get_method).to_be_visible()
    
    # Check that the endpoint path is correct
    endpoint_path = page.locator('.opblock-get .opblock-summary-path')
    expect(endpoint_path).to_have_text('/')

def test_items_endpoint_documentation(page: Page, base_url: str):
    """Test that the items endpoints are documented correctly."""
    api_docs = ApiDocsPage(page)
    api_docs.navigate()
    
    # Expand the items endpoint section
    api_docs.expand_endpoint("items")
    
    # Check for GET and POST methods
    get_method = page.locator('.opblock-get')
    expect(get_method).to_be_visible()
    
    post_method = page.locator('.opblock-post')
    expect(post_method).to_be_visible()

from playwright.sync_api import Page
from .base_page import BasePage

class ApiDocsPage(BasePage):
    """Page object for the Swagger UI API documentation page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.docs_path = "/docs"
        
    def navigate(self):
        """Navigate to the API documentation page."""
        self.navigate_to(self.docs_path)
        
    def is_loaded(self) -> bool:
        """Check if the Swagger UI is loaded."""
        return self.page.locator(".swagger-ui").is_visible()
    
    def expand_endpoint(self, endpoint_name: str):
        """Expand an endpoint section by its name/description."""
        # Find and click on the endpoint tag to expand it
        self.page.locator(f"text={endpoint_name}").first.click()
        
    def get_endpoint_count(self) -> int:
        """Get the number of endpoints displayed."""
        return self.page.locator(".opblock").count()
        
    def execute_request(self, endpoint_index: int = 0):
        """Execute a request for a specific endpoint by index."""
        # Click the "Try it out" button
        self.page.locator(".opblock .try-out__btn").nth(endpoint_index).click()
        # Click the "Execute" button
        self.page.locator(".opblock .execute").nth(endpoint_index).click()
        
    def get_response_code(self, endpoint_index: int = 0) -> str:
        """Get the response code after executing a request."""
        response_element = self.page.locator(".responses-table .response").nth(endpoint_index)
        return response_element.inner_text()

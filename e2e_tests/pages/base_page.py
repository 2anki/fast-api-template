from playwright.sync_api import Page


class BasePage:
    """Base page object that all page objects will inherit from."""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "http://localhost:8000"

    def navigate_to(self, path: str):
        """Navigate to a specific path from the base URL."""
        full_url = f"{self.base_url}{path}"
        self.page.goto(full_url)

    def get_title(self) -> str:
        """Get the title of the current page."""
        return self.page.title()

    def get_url(self) -> str:
        """Get the current URL."""
        return self.page.url

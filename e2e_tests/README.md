# End-to-End Tests with Playwright

This directory contains end-to-end tests for the FastAPI application using Playwright.

## Structure

- `conftest.py` - Contains pytest fixtures for setting up the test environment
- `playwright.config.py` - Playwright configuration
- `pages/` - Page Object Models for different pages in the application
- `tests/` - Test files

## Running the Tests

### Prerequisites

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:
   ```bash
   playwright install
   ```

### Running All Tests

```bash
pytest e2e_tests/tests
```

### Running Specific Test Files

```bash
pytest e2e_tests/tests/test_api_docs.py
```

### Running with UI Mode (non-headless)

```bash
PLAYWRIGHT_HEADLESS=false pytest e2e_tests/tests
```

### Running with Slow Motion (for debugging)

```bash
PLAYWRIGHT_SLOW_MO=100 pytest e2e_tests/tests
```

## Page Object Model

The tests use the Page Object Model pattern to encapsulate page-specific logic. This makes tests more maintainable and readable.

- `BasePage` - Base class for all page objects
- `ApiDocsPage` - Page object for the Swagger UI documentation

## Test Reports

Test videos are recorded in the `e2e_tests/videos` directory when tests are run.

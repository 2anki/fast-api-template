# FastAPI Template

A well-structured FastAPI template project with a modular architecture, designed for scalability and maintainability.

## Project Structure

```
fast-api-template/
├── app/                          # Main application package
│   ├── __init__.py               # Makes app a Python package
│   ├── main.py                   # FastAPI app configuration
│   ├── models/                   # Data models
│   │   ├── __init__.py
│   │   └── items.py              # Item Pydantic model
│   ├── routes/                   # API route handlers
│   │   ├── __init__.py
│   │   ├── items.py              # Item-related endpoints
│   │   └── root.py               # Root endpoint
│   └── services/                 # Business logic
│       ├── __init__.py
│       └── item_service.py       # Item-related business logic
├── e2e_tests/                    # End-to-end tests with Playwright
│   ├── README.md                 # E2E testing documentation
│   ├── conftest.py               # Test fixtures for E2E tests
│   ├── playwright.config.py      # Playwright configuration
│   ├── pages/                    # Page Object Models
│   │   ├── base_page.py          # Base page object
│   │   └── api_docs_page.py      # API docs page object
│   └── tests/                    # E2E test files
│       ├── test_api_docs.py      # Tests for API documentation
│       └── test_api_endpoints.py # Tests for API endpoints
├── main.py                       # Entry point for running the app
├── tests/                        # Unit/Integration test directory
│   ├── __init__.py
│   ├── conftest.py               # Pytest fixtures
│   ├── routes/                   # Route tests
│   │   ├── __init__.py
│   │   ├── test_items.py         # Tests for item routes
│   │   └── test_root.py          # Tests for root route
│   └── services/                 # Service tests
│       ├── __init__.py
│       └── test_item_service.py  # Tests for item service
```

## Features

- Modular architecture with separation of concerns
- Comprehensive test suite with unit, integration, and end-to-end tests
- Clean project structure
- Type hints throughout the codebase
- End-to-end testing with Playwright
- CI/CD with GitHub Actions
- Docker support for containerization
- Ready for production deployment

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fast-api-template.git
cd fast-api-template

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
# Run the application with hot reload
python main.py

# Or use uvicorn directly
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc

## Running Tests

### Unit and Integration Tests

```bash
# Run all unit/integration tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/routes/test_items.py
```

### End-to-End Tests with Playwright

```bash
# Install Playwright browsers
playwright install

# Run all E2E tests
pytest e2e_tests/tests

# Run with UI mode (non-headless)
PLAYWRIGHT_HEADLESS=false pytest e2e_tests/tests

# Run with slow motion for debugging
PLAYWRIGHT_SLOW_MO=100 pytest e2e_tests/tests
```

See [e2e_tests/README.md](e2e_tests/README.md) for more details on the end-to-end tests.

## CI/CD with GitHub Actions

This project includes GitHub Actions workflows for continuous integration and deployment:

### Test Workflow

Runs on push to main and pull requests:
- Executes unit and integration tests on multiple Python versions
- Runs end-to-end tests with Playwright
- Uploads test coverage to Codecov

### Lint Workflow

Runs on push to main and pull requests:
- Checks code with flake8 for errors
- Verifies formatting with black
- Validates import order with isort

### Docker Workflow

Runs on push to main and tags:
- Builds the Docker image
- Tests the image
- Pushes the image to GitHub Container Registry (on main branch or tags)

## Docker

You can build and run the application using Docker:

```bash
# Build the Docker image
docker build -t fast-api-template .

# Run the container
docker run -p 8000:8000 fast-api-template
```

The API will be available at http://localhost:8000

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Lær Smart AS

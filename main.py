import uvicorn
from app.main import app

# This file serves as the entry point for running the application
# It imports the app instance from the app package

if __name__ == "__main__":
    # Run the application with uvicorn when this script is executed directly
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

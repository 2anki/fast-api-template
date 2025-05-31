from fastapi import FastAPI

from app.routes import items, root

app = FastAPI(
    title="FastAPI Template",
    description="A template for FastAPI applications with a clean structure",
    version="0.1.0",
)

# Include routers
app.include_router(root.router)
app.include_router(items.router)

# Add any middleware, event handlers, etc. here

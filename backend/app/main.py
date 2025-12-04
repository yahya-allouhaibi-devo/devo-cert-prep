"""FastAPI application entry point."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup and shutdown events.

    Startup:
        - Create database tables (development only)
        - Initialize any required services

    Shutdown:
        - Clean up resources
    """
    # Startup
    print("🚀 Starting up...")
    try:
        create_db_and_tables()
        print("✅ Database tables created")
    except Exception as e:
        print(f"⚠️  Database connection failed: {e}")
        print("ℹ️  Start PostgreSQL with: docker-compose up db")

    yield

    # Shutdown
    print("🛑 Shutting down...")


# Create FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Cloud Certification Prep Platform - AI-powered practice questions and exam simulations",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint to verify the API is running."""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": "0.1.0",
    }


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Cloud Certification Prep Platform API",
        "docs": "/api/docs",
        "health": "/health",
    }


# TODO: Include API routers here
# Example:
# from app.api import auth, users, certifications
# app.include_router(auth.router, prefix=settings.API_V1_PREFIX, tags=["auth"])
# app.include_router(users.router, prefix=settings.API_V1_PREFIX, tags=["users"])

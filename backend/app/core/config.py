"""Application configuration settings."""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    DATABASE_URL: str = "postgresql://devuser:devpassword@localhost:5432/devo_cert_prep"

    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Cloud Certification Prep Platform"

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    ALLOWED_ORIGINS: Optional[str] = None

    # AWS
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    S3_BUCKET_NAME: Optional[str] = None
    S3_REGION: Optional[str] = None

    # Google OAuth
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_REDIRECT_URI: Optional[str] = None

    # JWT
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    JWT_SECRET_KEY: Optional[str] = None
    ALGORITHM: str = "HS256"
    JWT_ALGORITHM: Optional[str] = None
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = None
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: Optional[int] = None

    # Application
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Admin
    ADMIN_EMAILS: Optional[str] = None

    class Config:
        case_sensitive = True
        env_file = ".env"


# Global settings instance
settings = Settings()

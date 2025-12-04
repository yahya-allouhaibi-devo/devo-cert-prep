"""Database configuration and session management."""

from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
from app.core.config import settings

# Import all models to ensure they are registered with SQLModel
from app.models import (  # noqa: F401
    User,
    Certification,
    Topic,
    Question,
    UserProgress,
    Session as SessionModel,
    Bookmark,
)

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Log SQL queries (disable in production)
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,
    max_overflow=10,
)


def create_db_and_tables() -> None:
    """Create all database tables.

    This should be called on application startup.
    In production, use Alembic migrations instead.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get database session for dependency injection.

    Usage in FastAPI routes:
        @app.get("/items")
        def read_items(session: Session = Depends(get_session)):
            ...

    Yields:
        Session: SQLModel database session
    """
    with Session(engine) as session:
        yield session

"""User model for authentication and profile management."""

from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class UserRole(str, Enum):
    """User role enumeration."""
    USER = "user"
    ADMIN = "admin"


class User(SQLModel, table=True):
    """User model with Google OAuth and role-based access.

    Attributes:
        id: Primary key
        email: User's email (from Google OAuth)
        name: User's full name (from Google)
        picture_url: Profile picture URL (from Google)
        role: User role (user or admin)
        active_certification_id: Currently selected certification for study
        created_at: Account creation timestamp
        updated_at: Last update timestamp
        is_active: Account active status
    """
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True, max_length=255)
    name: str = Field(max_length=255)
    picture_url: Optional[str] = Field(default=None, max_length=500)
    role: UserRole = Field(default=UserRole.USER, index=True)
    active_certification_id: Optional[int] = Field(default=None, foreign_key="certifications.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, index=True)

    # Relationships
    active_certification: Optional["Certification"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[User.active_certification_id]"}
    )

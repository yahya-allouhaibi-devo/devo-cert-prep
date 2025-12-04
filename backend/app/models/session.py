"""Session model for JWT token management."""

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Session(SQLModel, table=True):
    """Session model for managing JWT refresh tokens.

    PostgreSQL-based session management for JWT authentication.
    Access tokens are short-lived and not stored; refresh tokens are stored here.

    Attributes:
        id: Primary key
        user_id: User who owns this session
        refresh_token: JWT refresh token (hashed)
        user_agent: Browser/client user agent
        ip_address: Client IP address
        expires_at: When refresh token expires
        created_at: When session was created
        last_used_at: Last time token was refreshed
        is_active: Whether session is valid
    """
    __tablename__ = "sessions"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    refresh_token: str = Field(max_length=500, unique=True, index=True)
    user_agent: Optional[str] = Field(default=None, max_length=500)
    ip_address: Optional[str] = Field(default=None, max_length=45)
    expires_at: datetime = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_used_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, index=True)

"""Bookmark model for saving and flagging questions."""

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Bookmark(SQLModel, table=True):
    """Bookmark model for user-saved questions.

    Allows users to bookmark questions for later review or flag them as
    problematic/incorrect.

    Attributes:
        id: Primary key
        user_id: User who created the bookmark
        question_id: Bookmarked question
        is_flagged: Whether question is flagged (vs just bookmarked)
        flag_reason: Reason for flagging (if is_flagged=True)
        notes: User's personal notes on this question
        created_at: When bookmark was created
    """
    __tablename__ = "bookmarks"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    question_id: int = Field(foreign_key="questions.id", index=True)
    is_flagged: bool = Field(default=False, index=True)
    flag_reason: Optional[str] = Field(default=None, max_length=500)
    notes: Optional[str] = Field(default=None, max_length=1000)
    created_at: datetime = Field(default_factory=datetime.utcnow)

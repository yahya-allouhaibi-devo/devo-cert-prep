"""Question model for practice questions and exam content."""

from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import JSON


class QuestionDifficulty(str, Enum):
    """Question difficulty levels."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class QuestionSource(str, Enum):
    """Question source types."""
    AI_GENERATED = "ai_generated"
    SCRAPED = "scraped"
    MANUAL = "manual"


class QuestionStatus(str, Enum):
    """Question approval status."""
    DRAFT = "draft"
    PENDING_REVIEW = "pending_review"
    APPROVED = "approved"
    REJECTED = "rejected"


class Question(SQLModel, table=True):
    """Question model for practice and exam questions.

    Attributes:
        id: Primary key
        topic_id: Associated topic/domain
        question_text: The main question text
        explanation: Detailed explanation of correct answer
        options: JSON array of answer options (e.g., ["A. Option 1", "B. Option 2"])
        correct_answer: Correct option key (e.g., "A")
        difficulty: Question difficulty level
        source: How question was created
        source_url: Original URL if scraped
        image_url: S3 URL for question diagram/image
        question_metadata: Additional JSON metadata (AI confidence, etc.)
        status: Approval status
        quality_score: Average user rating (1-5)
        rating_count: Number of user ratings
        flag_count: Number of times flagged as incorrect/poor quality
        created_by: User ID who created (for manual questions)
        created_at: When question was created
        updated_at: Last update timestamp
        is_active: Whether to include in question pool
    """
    __tablename__ = "questions"

    id: Optional[int] = Field(default=None, primary_key=True)
    topic_id: int = Field(foreign_key="topics.id", index=True)
    question_text: str = Field(max_length=2000)
    explanation: Optional[str] = Field(default=None, max_length=2000)
    options: dict = Field(sa_column=Column(JSON), description="JSON array of answer options")
    correct_answer: str = Field(max_length=10)
    difficulty: QuestionDifficulty = Field(default=QuestionDifficulty.MEDIUM, index=True)
    source: QuestionSource = Field(default=QuestionSource.AI_GENERATED, index=True)
    source_url: Optional[str] = Field(default=None, max_length=500)
    image_url: Optional[str] = Field(default=None, max_length=500)
    question_metadata: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    status: QuestionStatus = Field(default=QuestionStatus.DRAFT, index=True)
    quality_score: Optional[float] = Field(default=None, ge=1, le=5)
    rating_count: int = Field(default=0)
    flag_count: int = Field(default=0, index=True)
    created_by: Optional[int] = Field(default=None, foreign_key="users.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, index=True)

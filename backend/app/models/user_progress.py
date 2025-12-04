"""User progress model for tracking question attempts and performance."""

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class UserProgress(SQLModel, table=True):
    """User progress tracking for practice questions.

    Tracks every attempt a user makes on a question to enable:
    - Adaptive question weighting (focus on weak areas)
    - Performance analytics
    - Progress tracking over time

    Attributes:
        id: Primary key
        user_id: User who attempted the question
        question_id: Question that was attempted
        is_correct: Whether answer was correct
        selected_answer: User's selected answer (e.g., "A")
        time_spent_seconds: Time taken to answer
        practice_mode: Type of practice (general, topic-specific, exam)
        attempted_at: When question was answered
    """
    __tablename__ = "user_progress"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    question_id: int = Field(foreign_key="questions.id", index=True)
    is_correct: bool = Field(index=True)
    selected_answer: str = Field(max_length=10)
    time_spent_seconds: Optional[int] = Field(default=None)
    practice_mode: str = Field(max_length=50, index=True)  # "general", "topic", "exam"
    attempted_at: datetime = Field(default_factory=datetime.utcnow, index=True)

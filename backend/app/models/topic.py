"""Topic model for certification exam domains/topics."""

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Topic(SQLModel, table=True):
    """Topic model representing exam domains and subject areas.

    Each certification has multiple topics/domains with different weights.
    For example, AWS SAA has: Design Resilient Architectures (30%), etc.

    Attributes:
        id: Primary key
        certification_id: Parent certification
        name: Topic name (e.g., "Design Resilient Architectures")
        description: Detailed description of topic coverage
        weight_percentage: Weight of this topic in the exam (0-100)
        order: Display order for UI
        is_active: Whether to include in practice/exams
        created_at: When topic was added
        updated_at: Last update timestamp
    """
    __tablename__ = "topics"

    id: Optional[int] = Field(default=None, primary_key=True)
    certification_id: int = Field(foreign_key="certifications.id", index=True)
    name: str = Field(max_length=255)
    description: Optional[str] = Field(default=None)
    weight_percentage: int = Field(ge=0, le=100)
    order: int = Field(default=0)
    is_active: bool = Field(default=True, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

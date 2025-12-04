"""Certification model for cloud certifications."""

from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


class CertificationProvider(str, Enum):
    """Supported certification providers."""
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    SNOWFLAKE = "snowflake"


class Certification(SQLModel, table=True):
    """Certification model representing cloud certifications.

    Attributes:
        id: Primary key
        provider: Cloud provider (AWS, Azure, GCP, Snowflake)
        name: Full certification name (e.g., "AWS Solutions Architect Associate")
        short_name: Abbreviated name (e.g., "SAA-C03")
        description: Detailed description of the certification
        exam_duration_minutes: Time limit for exam simulation
        exam_question_count: Number of questions in real exam
        passing_score_percentage: Minimum score to pass (0-100)
        is_active: Whether users can select this certification
        created_at: When certification was added to platform
        updated_at: Last update timestamp
    """
    __tablename__ = "certifications"

    id: Optional[int] = Field(default=None, primary_key=True)
    provider: CertificationProvider = Field(index=True)
    name: str = Field(max_length=255, index=True)
    short_name: str = Field(max_length=50)
    description: Optional[str] = Field(default=None)
    exam_duration_minutes: int = Field(gt=0)
    exam_question_count: int = Field(gt=0)
    passing_score_percentage: int = Field(ge=0, le=100)
    is_active: bool = Field(default=True, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

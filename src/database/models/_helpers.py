from enum import StrEnum

from sqlmodel import Field, SQLModel


class ProgressLevel(StrEnum):
    """ProgressLevel Enum denoting the status of an entity."""

    NOT_STARTED = "Not-Started"
    IN_PROGRESS = "In-Progress"
    COMPLETED = "Completed"


class UrgencyLevel(StrEnum):
    """UrgencyLevel Enum to indicate the urgency of an entity.

    Inspired by the urgency levels used in an Eisenhower Matrix
    """

    LOWEST = "Lowest"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class BaseSchema(SQLModel):
    """Shared shape of majority of the database entities.

    Reusable shape for common fields
    """

    title: str | None = Field(default="A fun project")
    description: str | None = Field(default="A cool description")
    status: ProgressLevel = Field(default=ProgressLevel.NOT_STARTED)
    urgency: UrgencyLevel = Field(default=UrgencyLevel.LOW)

from sqlmodel import Field

from ._helpers import BaseSchema


class MilestoneCreate(BaseSchema):
    """DTO from TUI to QueryDriver."""

    pass


class MilestoneSelect(BaseSchema):
    """DTO from QueryDriver to TUI.

    All Milestones stored in the database HAVE primary keys
    """

    id: int = Field(primary_key=True)


class Milestone(BaseSchema, table=True):
    """Milestone entity.

    Milestones represent a major progress point of a Project. They
    MUST belong to a project and can optionally have associated tasks
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)

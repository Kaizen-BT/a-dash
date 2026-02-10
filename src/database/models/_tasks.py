from sqlmodel import Field

from ._helpers import BaseSchema


class TaskCreate(BaseSchema):
    """DTO from TUI to QueryDriver."""

    pass


class TaskSelect(BaseSchema):
    """DTO from QueryDriver to TUI.

    All Tasks stored in the database HAVE primary keys
    """

    id: int = Field(primary_key=True)


class Task(BaseSchema, table=True):
    """Task entity.

    All tasks belong to a project and optionally to a milestone of the same
    project
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)

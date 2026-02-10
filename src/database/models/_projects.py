from sqlmodel import Field

from ._helpers import BaseSchema


class ProjectCreate(BaseSchema):
    """DTO from TUI to QueryDriver."""

    pass


class ProjectSelect(BaseSchema):
    """DTO from QueryDriver to TUI.

    All Projects stored in the database HAVE primary keys
    """

    id: int = Field(primary_key=True)


class Project(BaseSchema, table=True):
    """Project entity.

    This is the main entity of interest and HAS tasks and milestones
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)

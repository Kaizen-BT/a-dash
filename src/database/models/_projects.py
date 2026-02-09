from sqlmodel import Field

from ._helpers import BaseSchema


class Project(BaseSchema, table=True):
    """Project entity.

    This is the main entity of interest and OWNS tasks and milestones
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)

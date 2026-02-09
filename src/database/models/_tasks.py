from sqlmodel import Field

from ._helpers import BaseSchema


class Task(BaseSchema, table=True):
    """Task entity.

    All tasks belong to a project and optionally to a milestone of the same
    project
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)

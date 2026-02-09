from sqlmodel import Field

from ._helpers import BaseSchema


class Milestone(BaseSchema, table=True):
    """Milestone entity.

    Milestones represent a major progress point of a Project. They
    MUST belong to a project and can optionally have associated tasks
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)

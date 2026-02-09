from sqlmodel import Field, SQLModel


class Project(SQLModel, table=True):
    """Project entity.

    This is the main entity of interest and OWNS tasks and milestones
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = "A nice project"
    description: str | None = "A cool description"

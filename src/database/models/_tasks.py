from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    """Task entity.

    All tasks belong to a project and optionally to a milestone of the same
    project
    """

    # TODO: Fill in using the apporpriate columns
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = "A nice project"
    description: str | None = "Oh no task due soon"

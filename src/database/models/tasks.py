from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = "A nice project"
    description: str | None = "Oh no task due soon"

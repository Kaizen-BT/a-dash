from sqlmodel import Field, SQLModel


class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = "A nice project"
    description: str | None = "A cool description"

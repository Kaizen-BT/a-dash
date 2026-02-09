from sqlmodel import Field, SQLModel


class Milestone(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = "A project Milestone"
    description: str | None = "Ohhhh milestoneeeeee"

from __future__ import annotations

from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from database.models import Project


def setup_mem_engine() -> Engine:
    """Sets up an in memory engine to play around with SQLModel"""
    return create_engine("sqlite://", echo=True)


def create_db_and_tables(engine: Engine) -> None:
    return SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    engine = setup_mem_engine()
    create_db_and_tables(engine)

    # Create a session and add some entities

    with Session(engine) as session:
        first_project = Project(description="This is a Project")
        print(f"The id should be None: {first_project.id}")
        session.add(first_project)
        session.commit()
        print(f"The id should not be None: {first_project.id}")

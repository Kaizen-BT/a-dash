from __future__ import annotations

from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine

from database.models import Project  # noqa: F401


def setup_mem_engine() -> Engine:
    """Sets up an in memory engine to play around with SQLModel"""
    return create_engine("sqlite://", echo=True)


def create_db_and_tables(engine: Engine) -> None:
    return SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    engine = setup_mem_engine()
    create_db_and_tables(engine)

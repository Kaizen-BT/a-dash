from sqlmodel import Session, SQLModel, create_engine, select

from .models import Project


class QueryDriver:
    """
    Sets up an engine to the database and expose common
    query operations
    """

    # TODO: Improve documentation
    # TODO: Check if SQLModel has an async engine

    def __init__(self, db_path: str) -> None:
        self._engine = create_engine(db_path)
        SQLModel.metadata.create_all(self._engine)

    def get_all_projects(self):
        with Session(self._engine) as session:
            return session.exec(select(Project)).all()

    def _create_test_data(self) -> None:
        with Session(self._engine) as session:
            first_project = Project(description="This is a Project")
            session.add(first_project)
            session.commit()

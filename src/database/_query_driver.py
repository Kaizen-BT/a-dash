from collections.abc import Sequence

from sqlmodel import Session, SQLModel, create_engine, select

from .models import Project


class QueryDriver:
    """QueryDriver to facilitate database connection and query operations"""

    # TODO: Improve documentation
    # TODO: Check if SQLModel has an async engine

    def __init__(self, db_path: str) -> None:
        """
        Connect to database and create tables

        Args:
            db_path (str): path to the database
        """
        self._engine = create_engine(db_path)
        SQLModel.metadata.create_all(self._engine)

    def get_all_projects(self) -> Sequence[Project]:
        """
        Instantiates a session to fetch all projects closed upon function return

        Returns:
            Sequence[Project]: Snapshot of all the projects during function call
        """
        with Session(self._engine) as session:
            return session.exec(select(Project)).all()

    def _create_test_data(self) -> None:
        with Session(self._engine) as session:
            first_project = Project(description="This is a Project")
            session.add(first_project)
            session.commit()

    def add_project(self) -> None:
        pass

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from database import QueryDriver


class Dashboard(App):
    """Main page of the dashboard.

    Attributes:
        TITLE:
        SUB_TITLE:
        query_driver:

    """

    TITLE = "Alens Dashboard"
    SUB_TITLE = "My mini dashboard"

    def __init__(self, query_driver: QueryDriver) -> None:
        super().__init__()
        self.query_driver = query_driver

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

"""Dashboard Page.

This is the page users will see upon launch and is responsible for injecting
the QueryDriver into the Controllers
"""

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

    def __init__(self, query_driver: QueryDriver) -> None:  # noqa: D107
        super().__init__()
        self.query_driver = query_driver

    def compose(self) -> ComposeResult:  # noqa: D102
        yield Header()
        yield Footer()

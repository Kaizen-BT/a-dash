from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class Dashboard(App):
    TITLE = "Alens Dashboard"
    SUB_TITLE = "My mini dashboard"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()
    print("Hello, welcome to the dashboard")

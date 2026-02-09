from __future__ import annotations

from database import QueryDriver
from tui.main import Dashboard

if __name__ == "__main__":
    querydriver = QueryDriver("sqlite://")
    querydriver._create_test_data()
    dashboard = Dashboard(querydriver)
    dashboard.run()

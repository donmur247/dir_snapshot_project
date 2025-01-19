"""User interface module for custom widgets."""

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Placeholder


class DirListWidget(Widget):
    """Directory list widget."""

    DEFAULT_CSS = """
    DirListWidget {
        width: 100%;
        height: 100%;
        layout: grid;
        grid-size: 2 2;
        grid-rows: 10% 90%;
        grid-columns: 2fr 1fr;
    }

    #title {
        column-span: 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Placeholder("List of Directories - TITLE", id="title")
        yield Placeholder("List of Directories - CONTENT")
        yield Placeholder("List of Directories - SIDEBAR")


class SnapshotListWidget(Widget):
    """Snapshot list widget."""

    DEFAULT_CSS = """
    SnapshotListWidget {
        width: 100%;
        height: 100%;
    }

    #title {
        dock: top;
        height: 2;
    }

    #button {
        dock: bottom;
        height: 4;
    }
    """

    def compose(self) -> ComposeResult:
        yield Placeholder("List of Snapshots - TITLE", id="title")
        yield Placeholder("List of Snapshots - CONTENT", id="content")
        yield Placeholder("List of Snapshots - BUTTON", id="button")


class ContentWidget(Widget):
    """Content widget."""

    DEFAULT_CSS = """
    ContentWidget {
        width: 100%;
        height: 100%;
    }

    #title {
        dock: top;
        height: 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Placeholder("Content Widget - TITLE", id="title")
        yield Placeholder("Content Widget - CONTENT")

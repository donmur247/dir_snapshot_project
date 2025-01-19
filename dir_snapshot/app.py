"""Application module for Directory Snapshot App."""

from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Placeholder

from dir_snapshot import APP_TITLE, APP_SUBTITLE


class DirSnapshotApp(App):
    """Main Directory Snapshot App class."""

    CSS_PATH = (Path(__file__).parent / "styles" / "styles.tcss").as_posix()
    TITLE = APP_TITLE
    SUB_TITLE = APP_SUBTITLE
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Placeholder("List of Directories Widget", id="list-of-dirs")
        yield Placeholder("List of Snapshots Widget")
        yield Placeholder("Display Screen Widget")
        yield Footer()

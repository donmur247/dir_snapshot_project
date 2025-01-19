"""Application module for Directory Snapshot App."""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from dir_snapshot import APP_TITLE, APP_SUBTITLE, TCSS_DIR
from dir_snapshot.ui import ContentWidget, DirListWidget, SnapshotListWidget


class DirSnapshotApp(App):
    """Main Directory Snapshot App class."""

    CSS_PATH = (TCSS_DIR / "app_styles.tcss").as_posix()
    TITLE = APP_TITLE
    SUB_TITLE = APP_SUBTITLE
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DirListWidget(id="list-of-dirs")
        yield SnapshotListWidget()
        yield ContentWidget()
        yield Footer()

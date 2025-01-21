"""Application module for Directory Snapshot App."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Header,
    Markdown,
    OptionList,
    SelectionList,
    TabbedContent,
    TabPane,
)

from dir_snapshot import APP_TITLE, APP_SUBTITLE, TCSS_DIR
from dir_snapshot.ui import AddDirDialog, ConfirmDialog

MAX_SELECTED = 2


# TODO: Temporary content. Remove them once we got dynamic content.
COMPARISON_CONTENT = """
# Comparison Result for Snapshot 1 and Snapshot 2

## Added Directories
- Directory 1
- Directory 2

## Added Files
- File 1
- File 2

## Removed Directories
- Directory 3
- Directory 4

## Removed Files
- File 3
- File 4
"""

HELP_CONTENT = """
# Directory Snapshot Help

## Getting Started
The top area is for the list of directories.
The bottom area is for the list of snapshots.

## Adding a Directory
Click the 'Add Directory' button to add a directory to the list.

## Removing a Directory
Click the 'Remove Directory' button to remove a directory from the list.

## Comparing Snapshots
Click the 'Compare Snapshots' button to compare the selected snapshots.
"""


class DirSnapshotApp(App):
    """Main Directory Snapshot App class."""

    CSS_PATH = (TCSS_DIR / "app_styles.tcss").as_posix()
    TITLE = APP_TITLE
    SUB_TITLE = APP_SUBTITLE
    BINDINGS = [
        ("q", "request_quit", "Quit"),
        ("a", "add_dir", "Add Directory"),
        ("r", "remove_dir", "Remove Directory"),
        ("c", "compare_snapshots", "Compare Snapshots"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.selected_dir: str = ""

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(
            "C:/temp",
            "C:/Program Files/Python310/Scripts",
            "C:/Program Files (x86)/Common Files/Microsoft Shared/Office16",
            "C:/Program Files (x86)/Common Files/Microsoft Shared/Office16/COM",
            id="dirs",
        )
        yield SelectionList(
            ("Snapshot 1", 0, True),
            ("Snapshot 2", 1),
            ("Snapshot 3", 2),
            ("Snapshot 4", 3),
            ("Snapshot 5", 4),
            id="snapshots",
        )
        with TabbedContent(initial="snapshot-result", id="content"):
            with TabPane("Snapshot Results", id="snapshot-result"):
                yield Markdown(COMPARISON_CONTENT, id="result-content")
            with TabPane("Help", id="help"):
                yield Markdown(HELP_CONTENT, id="help-content")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#result-content").styles.height = "1fr"
        self.query_one("#help-content").styles.height = "1fr"
        self.query_one(OptionList).border_title = "Directories"
        self.query_one(SelectionList).border_title = "Snapshots"

    def action_request_quit(self) -> None:
        """Action to show quit dialog."""

        def check_quit(quit: bool) -> None:
            if quit:
                self.exit()

        self.push_screen(ConfirmDialog("Are you sure you want to quit?"), check_quit)

    def action_add_dir(self) -> None:
        """Action to show add directory dialog."""

        def check_input_dir(path: str | None) -> None:
            """Check path returned from input dialog."""
            if path:
                self.notify(path)
            else:
                self.notify("Cancelled")

        self.push_screen(AddDirDialog(), check_input_dir)

    def action_remove_dir(self) -> None:
        """Action to show remove directory dialog."""

        def check_confirm_remove(remove: bool) -> None:
            if remove:
                self.notify("Removed")
            else:
                self.notify("Cancelled")

        self.push_screen(
            ConfirmDialog("Are you sure you want to remove?"), check_confirm_remove
        )

    def action_compare_snapshots(self) -> None:
        """Action to show compare snapshots dialog."""
        snapshot_list = self.query_one(SelectionList)
        options = [
            str(snapshot_list.get_option_at_index(snapshot).prompt)
            for snapshot in snapshot_list.selected
        ]
        self.notify(f"{','.join(options)}")

    @on(SelectionList.SelectionToggled, "#snapshots")
    def update_selected_snapshots(self, event: SelectionList.SelectionToggled) -> None:
        """Update selected snapshots to limit selection to 2."""
        snapshot_list = self.query_one(SelectionList)
        if len(snapshot_list.selected) > MAX_SELECTED:
            snapshot_list.toggle(event.selection_index)

    @on(OptionList.OptionSelected, "#dirs")
    def update_selected_dirs(self, event: OptionList.OptionSelected) -> None:
        """Update selected directory."""
        self.selected_dir = event.option.prompt
        self.notify(f"{self.selected_dir}")

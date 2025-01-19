"""User interface module for custom widgets."""

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import (
    Button,
    Markdown,
    OptionList,
    Placeholder,
    SelectionList,
    Static,
    TabbedContent,
    TabPane,
)


class DirListWidget(Widget):
    """Directory list widget."""

    DEFAULT_CSS = """
    DirListWidget {
        width: 100%;
        height: 100%;
        layout: grid;
        grid-size: 2 2;
        grid-rows: 8% 92%;
        grid-columns: 2fr 1fr;
    }

    OptionList {
        height: 100%;
    }

    Button {
        margin: 1;
    }

    #title {
        column-span: 2;
        content-align: center middle;
        background: darkslategrey;
    }

    .button-container {
        align: center middle;
        background: rgb(30, 30, 30);
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("List of Directories", id="title")
        yield OptionList(
            "C:/temp",
            "C:/Program Files/Python310/Scripts",
            "C:/Program Files (x86)/Common Files/Microsoft Shared/Office16",
            "C:/Program Files (x86)/Common Files/Microsoft Shared/Office16/COM",
        )
        with Vertical(classes="button-container"):
            yield Button("Add Directory", variant="primary")
            yield Button("Remove Directory", variant="error")

    def on_mount(self) -> None:
        option_list = self.query_one(OptionList)
        option_list.styles.border = "none"
        option_list.styles.height = "1fr"


class SnapshotListWidget(Widget):
    """Snapshot list widget."""

    DEFAULT_CSS = """
    SnapshotListWidget {
        width: 100%;
        height: 100%;
    }

    #title {
        dock: top;
        height: 1;
        content-align: center middle;
        background: darkslategrey;
    }

    .button {
        content-align: center middle;
        dock: bottom;
        height: 3;
        text-align: center;
        color: goldenrod;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Snapshots", id="title")
        yield SelectionList(
            ("Snapshot 1", 0, True),
            ("Snapshot 2", 1),
            ("Snapshot 3", 2),
            ("Snapshot 4", 3),
            ("Snapshot 5", 4),
        )
        yield Button("Compare Snapshots", classes="button")

    def on_mount(self) -> None:
        selection_list = self.query_one(SelectionList)
        selection_list.styles.border = "none"
        selection_list.styles.height = "1fr"
        button = self.query_one(Button)
        button.styles.width = "100%"


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
The top area is for the list of directories. The bottom area is for the list of snapshots.

## Adding a Directory
Click the 'Add Directory' button to add a directory to the list.

## Removing a Directory
Click the 'Remove Directory' button to remove a directory from the list.

## Comparing Snapshots
Click the 'Compare Snapshots' button to compare the selected snapshots.
"""


class ContentWidget(Widget):
    """Content widget."""

    DEFAULT_CSS = """
    ContentWidget {
        width: 100%;
        height: 100%;
    }

    #title {
        dock: top;
        height: 1;
        content-align: center middle;
        background: purple;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Comparison & Help", id="title")
        with TabbedContent(initial="snapshot-result"):
            with TabPane("Snapshot Results", id="snapshot-result"):
                yield Markdown(COMPARISON_CONTENT, id="result-content")
            with TabPane("Help", id="help"):
                yield Markdown(HELP_CONTENT, id="help-content")

    def on_mount(self) -> None:
        self.query_one("#result-content").styles.height = "1fr"
        self.query_one("#help-content").styles.height = "1fr"

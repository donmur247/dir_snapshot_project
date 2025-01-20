"""User interface module for custom widgets."""

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Label


class ConfirmDialog(ModalScreen[bool]):
    """Quit dialog screen."""

    DEFAULT_CSS = """
    ConfirmDialog {
        align: center middle;
    }

    #dialog {
        grid-size: 2;
        grid-gutter: 1 2;
        grid-rows: 1fr 3;
        padding: 0 1;
        width: 60;
        height: 11;
        border: thick $background 80%;
        background: $surface;
    }

    #question {
        column-span: 2;
        height: 1fr;
        width: 1fr;
        content-align: center middle;
    }

    Button {
        width: 100%;
    }
    """

    def __init__(self, question: str):
        super().__init__()
        self.question = question

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.question, id="question"),
            Button("Yes", variant="primary", id="yes"),
            Button("No", variant="error", id="no"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)


class AddDirDialog(ModalScreen[str | None]):
    """Add directory dialog screen."""

    DEFAULT_CSS = """
    AddDirDialog {
        align: center middle;
    }

    #dialog {
        grid-size: 2 2;
        grid-gutter: 1 2;
        grid-rows: 1fr 1fr 3;
        width: 60;
        height: 11;
        border: thick $background 80%;
        background: $surface;
    }

    #dir-input {
        column-span: 2;
        width: 1fr;
        content-align: center middle;
    }

    Input {
        width: 100%;
    }

    Button {
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Grid(
            Input(placeholder="Paste directory here", id="dir-input"),
            Button("Add", variant="success", id="add"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add":
            if path := self.query_one(Input).value:
                self.dismiss(path)
        else:
            self.dismiss(None)

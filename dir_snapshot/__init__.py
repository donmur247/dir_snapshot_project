"""Top-level package for Directory Snapshot App."""

from pathlib import Path

__app_name__ = "dir_snapshot"
__version__ = "0.1.0"

# Constants for directory and files
APP_SETTINGS_DIR = ".dir_snapshot"
APP_SNAPSHOT_DIR = "snapshots"
APP_DB_FILE = "dir_snapshot.json"
APP_SNAPSHOT_EXT = ".snp"
TCSS_DIR = Path(__file__).parent / "styles"

# UI constants
APP_TITLE = "Directory Snapshot App"
APP_SUBTITLE = __version__

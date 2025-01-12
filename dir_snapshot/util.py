"""Utility module for Directory Snapshot App."""

import sys

from pathlib import Path
from typing import Optional

from dir_snapshot import (
    APP_SETTINGS_DIR,
    APP_SNAPSHOT_DIR,
    APP_DB_FILE,
)


def create_dir(path: Path) -> None:
    """Create directory safely.

    Args:
        path (Path): Path object of directory.
    """
    if not path.exists():
        try:
            path.mkdir(parents=True)
        except OSError as e:
            print(f"Failed to create directory: {e}")
            sys.exit(1)


def create_file(path: Path) -> None:
    """Create file safely.

    Args:
        path (Path): Path object of file.
    """
    if not path.exists():
        try:
            path.touch()
        except OSError as e:
            print(f"Failed to create file: {e}")
            sys.exit(1)


def get_user_home() -> Path:
    """Get user's home directory.

    Returns:
        Path: Path object of user's home directory.
    """
    return Path.home()


def get_settings_dir() -> Optional[Path]:
    """Get directory for settings.

    Returns:
        Optional[Path]: Path object of settings directory or None if there's an error.
    """
    settings_dir = get_user_home() / APP_SETTINGS_DIR
    create_dir(settings_dir)
    return settings_dir


def get_snapshot_dir() -> Optional[Path]:
    """Get snapshot directory.

    Returns:
        Optional[Path]: Path object of snapshot directory or None if there's an error.
    """
    snapshot_dir = get_settings_dir() / APP_SNAPSHOT_DIR
    create_dir(snapshot_dir)
    return snapshot_dir


def get_db_file() -> Optional[Path]:
    """Get database file.

    Returns:
        Optional[Path]: Path object of database file or None if there's an error.
    """
    db_file = get_settings_dir() / APP_DB_FILE
    create_file(db_file)
    return db_file

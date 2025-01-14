"""Conftest module for Directory Snapshot App."""

from pathlib import Path

import pytest

from dir_snapshot.db import SnapshotDB
from dir_snapshot.snapshot import SnapshotData


@pytest.fixture
def db_file_empty():
    """Fixture for empty database file."""

    def empty_json():
        return Path(__file__).parent / "data" / "empty.json"

    return empty_json


@pytest.fixture
def db_file_empty_dirs():
    """Fixture for empty dirs database file."""

    def empty_dirs_json():
        return Path(__file__).parent / "data" / "empty_dirs.json"

    return empty_dirs_json


@pytest.fixture
def empty_db(monkeypatch, db_file_empty):
    """Fixture for empty database from and empty JSON file."""
    monkeypatch.setattr("dir_snapshot.db.get_db_file", db_file_empty)
    return SnapshotDB()


@pytest.fixture
def empty_dirs_db(monkeypatch, db_file_empty_dirs):
    """Fixture for empty database from and empty dirs JSON file."""
    monkeypatch.setattr("dir_snapshot.db.get_db_file", db_file_empty_dirs)
    return SnapshotDB()


@pytest.fixture
def snapshot_db(empty_dirs_db):
    """Fixture for SnapshotDB with added snapshot directories."""
    db = empty_dirs_db
    db.add_snapshot_dir("C:/temp")
    db.add_snapshot_dir("C:/temp2")
    db.add_snapshot_dir("C:/temp3")
    return db


@pytest.fixture
def snapshots():
    """Fixture for list of snapshots."""
    snap1 = SnapshotData(
        dirs=["some_test"],
        files=[
            "test1 - Copy (2).txt",
            "test1 - Copy.txt",
            "test1.txt",
            "some_test/test1 - Copy.txt",
        ],
    )
    snap2 = SnapshotData(
        dirs=["some_test", "new_test"],
        files=[
            "test1 - Copy (2).txt",
            "some_test/test1 - Copy.txt",
            "new_test/test1.txt",
            "some_test/test2.txt",
        ],
    )
    return [snap1, snap2]

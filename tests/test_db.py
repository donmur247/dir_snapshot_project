"""Test db module."""

from dir_snapshot.db import SnapshotDB, SnapshotListData


def test_empty_db(monkeypatch, db_file_empty):
    """Test SnapshotDB with empty database file."""
    monkeypatch.setattr("dir_snapshot.db.get_db_file", db_file_empty)
    db = SnapshotDB()
    assert db.snapshot_data == SnapshotListData(dirs=[])
    assert db.snapshot_dirs == []


def test_empty_dirs_db(monkeypatch, db_file_empty_dirs):
    """Test SnapshotDB with empty dirs database file."""
    monkeypatch.setattr("dir_snapshot.db.get_db_file", db_file_empty_dirs)
    db = SnapshotDB()
    assert db.snapshot_data == SnapshotListData(dirs=[])
    assert db.snapshot_dirs == []

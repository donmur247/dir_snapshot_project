"""Test db module."""

import pytest

from dir_snapshot.db import SnapshotListData


def test_empty_db(empty_db):
    """Test SnapshotDB with empty database file."""
    db = empty_db
    assert db.snapshot_data == SnapshotListData(dirs=[])
    assert db.snapshot_dirs == []
    assert db.num_dirs == 0


def test_empty_dirs_db(empty_dirs_db):
    """Test SnapshotDB with empty dirs database file."""
    db = empty_dirs_db
    assert db.snapshot_data == SnapshotListData(dirs=[])
    assert db.snapshot_dirs == []
    assert db.num_dirs == 0


def test_add_snapshot_dir(empty_dirs_db):
    """Test add_snapshot_dir method."""
    test_dir = "C:/temp"
    db = empty_dirs_db
    assert db.add_snapshot_dir(test_dir)
    assert db.num_dirs == 1
    assert db.snapshot_dirs[0].id == 0
    assert db.snapshot_dirs[0].path == test_dir
    assert db.snapshot_dirs[0].snap_files == []
    assert not db.add_snapshot_dir(test_dir)


@pytest.mark.parametrize(
    "id, path",
    [
        (0, "C:/temp"),
        (1, "C:/temp2"),
        (2, "C:/temp3"),
    ],
)
def test_get_snapshot_dir(snapshot_db, id, path):
    """Test get_snapshot_dir method."""
    db = snapshot_db
    assert db.get_snapshot_dir(id).path == path

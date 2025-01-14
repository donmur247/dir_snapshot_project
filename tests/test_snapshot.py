"""Test snapshot module."""

from dir_snapshot.snapshot import compare_snapshot


def test_compare_snapshot(snapshots):
    """Test compare snapshot function."""
    snap1, snap2 = snapshots

    compare_data = compare_snapshot(snap1, snap2)
    assert compare_data.added_dirs == ["new_test"]
    assert compare_data.added_files == ["new_test/test1.txt", "some_test/test2.txt"]
    assert compare_data.removed_dirs == []
    assert compare_data.removed_files == ["test1 - Copy.txt", "test1.txt"]

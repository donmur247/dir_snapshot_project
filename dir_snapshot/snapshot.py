"""Snapshot module to handle actual directory snapshots."""

import datetime
import difflib
import pickle
from dataclasses import dataclass
from pathlib import Path

from dir_snapshot.util import get_snapshot_dir


@dataclass
class SnapshotData:
    dirs: list[str]
    files: list[str]


@dataclass
class SnapshotCompareData:
    added_dirs: list[str]
    added_files: list[str]
    removed_dirs: list[str]
    removed_files: list[str]


def create_snapshot(dir: str) -> SnapshotData:
    """Create snapshot of a directory.

    Args:
        dir (str): Directory to snapshot.

    Returns:
        SnapshotData: SnapshotData model.
    """
    snapshot_data = SnapshotData(dirs=[], files=[])

    for path in Path(dir).rglob("*"):
        if path.is_dir():
            snapshot_data.dirs.append(path.relative_to(dir).as_posix())
        else:
            snapshot_data.files.append(path.relative_to(dir).as_posix())

    return snapshot_data


def compare_snapshot(snap1: SnapshotData, snap2: SnapshotData) -> SnapshotCompareData:
    """Compare two snapshot data.

    Args:
        snap1 (SnapshotData): Snapshot data.
        snap2 (SnapshotData): Snapshot data to compare.

    Returns:
        SnapshotCompareData: SnapshotCompareData model.
    """
    result_dirs = list(difflib.unified_diff(snap1.dirs, snap2.dirs))
    result_files = list(difflib.unified_diff(snap1.files, snap2.files))

    snap_compare = SnapshotCompareData(
        added_dirs=[], added_files=[], removed_dirs=[], removed_files=[]
    )

    for result in result_dirs:
        if result.find("\n") == -1:
            if result.startswith("+"):
                snap_compare.added_dirs.append(result.strip("+"))
            elif result.startswith("-"):
                snap_compare.removed_dirs.append(result.strip("-"))

    for result in result_files:
        if result.find("\n") == -1:
            if result.startswith("+"):
                snap_compare.added_files.append(result.strip("+"))
            elif result.startswith("-"):
                snap_compare.removed_files.append(result.strip("-"))

    return snap_compare


def generate_snp_filename(id: int) -> str:
    """Generate snapshot filename.

    Args:
        id (int): Snapshot id.

    Returns:
        str: Generated filename.
    """
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return (get_snapshot_dir() / f"snapshot-{id}-{timestamp}.snp").as_posix()


def write_snp_data(snapshot_data: SnapshotData, file: str) -> bool:
    """Write snapshot data to file.

    Args:
        snapshot_data (SnapshotData): SnapshotData model.
        file (str): File output path.

    Returns:
        bool: True if file was written successfully.
    """
    try:
        with open(file, "wb") as f:
            pickle.dump(snapshot_data.dirs, f)
            pickle.dump(snapshot_data.files, f)
    except OSError:
        return False
    return True


def read_snp_data(file: str) -> SnapshotData:
    """Read snapshot data from file.

    Args:
        file (str): File input path.

    Returns:
        SnapshotData: SnapshotData model.
    """
    try:
        with open(file, "rb") as f:
            dir_data = pickle.load(f)
            file_data = pickle.load(f)
    except OSError:
        return [], []
    return SnapshotData(dirs=dir_data, files=file_data)

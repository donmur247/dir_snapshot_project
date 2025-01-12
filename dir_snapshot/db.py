"""Database module for Directory Snapshot App."""

import json
from dataclasses import dataclass, asdict

from dir_snapshot.util import get_db_file


@dataclass
class SnapshotDirData:
    id: int
    path: str
    snap_files: list[str]


@dataclass
class SnapshotListData:
    dirs: list[SnapshotDirData]


class SnapshotDB:
    """Snapshot database class."""

    def __init__(self):
        """Constructor method."""
        self._db_file = get_db_file()
        self._snapshot_data = self._load_data()

    @property
    def snapshot_data(self) -> SnapshotListData:
        """Get snapshot data.

        Returns:
            SnapshotListData: Snapshot List Data model.
        """
        return self._snapshot_data

    @property
    def snapshot_dirs(self) -> list[SnapshotDirData]:
        """Get snapshot directories.

        Returns:
            list[SnapshotDirData]: List of Snapshot Dir Data models.
        """
        return self._snapshot_data.dirs

    @property
    def db_file(self) -> str:
        """Get database file.

        Returns:
            str: Full path of database file.
        """
        return self._db_file.as_posix()

    def _load_data(self) -> SnapshotListData:
        """Load snapshot data from database file.

        Returns:
            SnapshotListData: Snapshot List Data model.
        """
        _snapshot_data = None
        try:
            with self._db_file.open("r") as f:
                _snapshot_data = SnapshotListData(**json.load(f))
        except json.JSONDecodeError:
            _snapshot_data = SnapshotListData(dirs=[])
        return _snapshot_data

    def save_data(self) -> bool:
        """Save snapshot data to database file.

        Returns:
            bool: True if save was successful.
        """
        try:
            with self._db_file.open("w") as f:
                json.dump(asdict(self._snapshot_data), f)
        except OSError:
            return False
        return True

"""Database module for Directory Snapshot App."""

import json
from dataclasses import dataclass, asdict
from typing import Optional

from dir_snapshot.util import delete_files, get_db_file


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

    @property
    def num_dirs(self) -> int:
        """Get number of snapshot directories.

        Returns:
            int: Number of snapshot directories.
        """
        return len(self.snapshot_dirs)

    @property
    def is_empty(self) -> bool:
        """Check if database is empty.

        Returns:
            bool: True if database is empty.
        """
        return self.num_dirs == 0

    def _load_data(self) -> SnapshotListData:
        """Load snapshot data from database file.

        Returns:
            SnapshotListData: Snapshot List Data model.
        """
        _snapshot_data = None
        try:
            with self._db_file.open("r") as f:
                _snapshot_data = SnapshotListData(dirs=[])
                rows = json.load(f).get("dirs")
                for row in rows:
                    _snapshot_data.dirs.append(SnapshotDirData(**row))
        except json.JSONDecodeError:
            _snapshot_data = SnapshotListData(dirs=[])
        return _snapshot_data

    def _is_dir_in_db(self, dir: str) -> bool:
        """Check if directory is in database.

        Args:
            dir (str): Directory to check.

        Returns:
            bool: True if directory is in database.
        """
        return dir in [d.path for d in self.snapshot_dirs]

    def _get_last_id(self) -> int:
        """Get last directory id.

        Returns:
            int: Last directory id.
        """
        if self.is_empty:
            return 0
        return max([d.id for d in self.snapshot_dirs]) + 1

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

    def get_snapshot_dir(self, id: int) -> Optional[SnapshotDirData]:
        """Get snapshot directory by id.

        Args:
            id (int): Directory id.

        Returns:
            Optional[SnapshotDirData]: Snapshot Dir Data model.
        """
        return next((d for d in self.snapshot_dirs if d.id == id), None)

    def get_snapshot_dir_by_path(self, path: str) -> Optional[SnapshotDirData]:
        """Get snapshot directory by path.

        Args:
            path (str): Full path of directory.

        Returns:
            Optional[SnapshotDirData]: Snapshot Dir Data model.
        """
        return next((d for d in self.snapshot_dirs if d.path == path), None)

    def add_snapshot_dir(self, dir: str) -> bool:
        """Add snapshot directory to database.

        Args:
            dir (str): Directory to add.

        Returns:
            bool: True if directory was added.
        """
        if not self._is_dir_in_db(dir):
            dir_data = SnapshotDirData(id=self._get_last_id(), path=dir, snap_files=[])
            self._snapshot_data.dirs.append(dir_data)
            return True
        return False

    def update_snapshot_dir(self, id: int, snap_file: str) -> None:
        """Update snapshot dir with new snapshot file.

        Args:
            id (int): Snapshot dir id.
            snap_file (str): Snapshot file.

        """
        for idx, d in enumerate(self.snapshot_dirs):
            if d.id == id:
                self._snapshot_data.dirs[idx].snap_files.append(snap_file)
                break

    def delete_snapshot_dir(self, id: int) -> bool:
        """Delete snapshot directory from database.

        Args:
            id (int): Snapshot dir id.

        Returns:
            bool: True if its deleted.
        """
        for idx, d in enumerate(self.snapshot_dirs):
            if d.id == id:
                self._snapshot_data.dirs.pop(idx)
                return delete_files(d.snap_files)

        return False

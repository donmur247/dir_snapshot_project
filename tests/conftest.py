"""Conftest module for Directory Snapshot App."""

from pathlib import Path

import pytest


@pytest.fixture
def db_file_empty():
    def empty_json():
        return Path(__file__).parent / "data" / "empty.json"

    return empty_json


@pytest.fixture
def db_file_empty_dirs():
    def empty_dirs_json():
        return Path(__file__).parent / "data" / "empty_dirs.json"

    return empty_dirs_json

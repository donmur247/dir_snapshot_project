from setuptools import setup, find_packages

setup(
    name="dir_snapshot",
    version="0.1.0",
    packages=find_packages(include=["dir_snapshot", "dir_snapshot.*"]),
)

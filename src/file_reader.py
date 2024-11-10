import os
import typing
from pathlib import Path


def read_file_contents(path: str | Path) -> list:
    files = os.listdir(path)
    return files
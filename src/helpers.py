import os
import typing
from pathlib import Path


def extract_extension_from_file_path(path: str) -> str:
    file_name = os.path.basename(path)
    if '.' not in file_name or file_name.startswith('.'):
        return ""
    return os.path.splitext(file_name)[1][1:]

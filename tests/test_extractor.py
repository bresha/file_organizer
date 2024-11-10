import pytest
import os
from pathlib import Path

from src import helpers


def test_extract_extension_from_file_path():
    file_path = "path/to/file.txt"
    extension = helpers.extract_extension_from_file_path(file_path)
    assert extension == "txt"

def test_extract_extension_from_file_path_no_extension():
    file_path = "path/to/file"
    extension = helpers.extract_extension_from_file_path(file_path)
    assert extension == ""

def test_extract_extension_from_file_path_multiple_dots():
    file_path = "path/to/file.tar.gz"
    extension = helpers.extract_extension_from_file_path(file_path)
    assert extension == "gz"

def test_extract_extension_from_file_path_starting_with_dot():
    file_path = ".gitignore"
    extension = helpers.extract_extension_from_file_path(file_path)
    assert extension == ""

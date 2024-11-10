import pytest
import os
from pathlib import Path

from src import extractor

@pytest.fixture
def sample_directory(tmp_path):
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    
    # Create some test files
    (test_dir / "file1.txt").touch()
    (test_dir / "file2.txt").touch()
    (test_dir / "file3.txt").touch()
    (test_dir / "file4.txt").touch()
    
    return test_dir


def test_read_folder_contents_return_correct_number_of_items(sample_directory):
    files = extractor.read_folder_contents(sample_directory)
    assert len(files) == 4

def test_read_folder_contents_handles_empty_directory(tmp_path):
    files = extractor.read_folder_contents(tmp_path)
    assert len(files) == 0

def test_extract_extension_from_file_path():
    file_path = "path/to/file.txt"
    extension = extractor.extract_extension_from_file_path(file_path)
    assert extension == "txt"

def test_extract_extension_from_file_path_no_extension():
    file_path = "path/to/file"
    extension = extractor.extract_extension_from_file_path(file_path)
    assert extension == ""

def test_extract_extension_from_file_path_multiple_dots():
    file_path = "path/to/file.tar.gz"
    extension = extractor.extract_extension_from_file_path(file_path)
    assert extension == "gz"

def test_extract_extension_from_file_path_starting_with_dot():
    file_path = ".gitignore"
    extension = extractor.extract_extension_from_file_path(file_path)
    assert extension == ""

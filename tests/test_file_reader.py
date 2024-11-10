import pytest
import os
from pathlib import Path

from src import file_reader

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
    files = file_reader.read_file_contents(sample_directory)
    assert len(files) == 4

def test_read_folder_contents_handles_empty_directory(tmp_path):
    files = file_reader.read_file_contents(tmp_path)
    assert len(files) == 0

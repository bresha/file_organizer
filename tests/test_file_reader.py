import pytest

from src import file_reader


def test_read_folder_contents():
    files = file_reader.read_file_contents("sample_files")
    assert len(files) == 4 
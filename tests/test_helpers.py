import os
from unittest.mock import patch
import pytest

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

def test_move_file_to_folder():
    file_path = "path/to/file.txt"
    folder_path = "path/to/folder"
    expected_path = os.path.join(folder_path, os.path.basename(file_path))
    
    # Using patch to mock the actual file moving operation
    with patch('shutil.move') as mock_move, \
         patch('os.path.exists') as mock_exists, \
         patch('os.makedirs') as mock_makedirs:
        
        # Configure the mocks
        mock_exists.return_value = True  # Pretend the directory exists
        mock_move.return_value = expected_path  # Set the return value for move
        
        new_file_path = helpers.move_file_to_folder(file_path, folder_path)
        
        # Assert the returned path is correct
        assert new_file_path == expected_path

def test_create_destination_folder_path():
    user_provided_path = "path/to/folder"
    extension = "txt"
    expected_path = os.path.join(user_provided_path, extension)
    actual_path = helpers.create_destination_folder_path(user_provided_path, extension)
    assert actual_path == expected_path

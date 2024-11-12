import pytest
from pathlib import Path

import main


@pytest.fixture
def test_items(tmp_path):
    # Create tmp dirs
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "destination"

    source_dir.mkdir()
    destination_dir.mkdir()

    # Create tmp files
    file_names = ["file1.txt", "file2.pdf", "file3.csv"]
    for file_name in file_names:
        file_path = source_dir / file_name
        file_path.touch()

    return source_dir, destination_dir, file_names

def test_move_files(test_items):
    source_dir, destination_dir, file_names = test_items

    main.move_files(source_dir, destination_dir)

    # Assert files were moved from source to destination
    for file_name in file_names:
        # Check file no longer exists in source
        assert not (source_dir / file_name).exists()
        
        # Check file exists in destination
        extension = file_name.split('.')[-1]
        expected_path = destination_dir / extension / file_name
        assert expected_path.exists()

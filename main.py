import os
import typing
from src import helpers


def move_files(source_dir: str, user_destination_dir: str) -> None:
    file_paths = os.listdir(source_dir)

    for file_path in file_paths:
        extension = helpers.extract_extension_from_file_path(file_path)
        destination_dir = helpers.create_destination_folder_path(user_destination_dir, extension)
        helpers.move_file_to_folder(os.path.join(source_dir, file_path), destination_dir)

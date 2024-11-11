import os
import typing
import shutil


def extract_extension_from_file_path(path: str) -> str:
    file_name = os.path.basename(path)
    if '.' not in file_name or file_name.startswith('.'):
        return ""
    return os.path.splitext(file_name)[1][1:]

def move_file_to_folder(file_path: str, destination_folder: str) -> None:
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    new_path = shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
    return new_path

import os
import stat
import typing
import shutil


def extract_extension_from_file_path(path: str) -> str:
    file_name = os.path.basename(path)
    if '.' not in file_name or file_name.startswith('.'):
        return ""
    return os.path.splitext(file_name)[1][1:]

def move_file_to_folder(file_path: str, destination_folder: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if we have write permission on the source file
    file_mode = os.stat(file_path).st_mode
    if not (file_mode & stat.S_IWUSR):
        raise PermissionError(f"Permission denied: Source file '{file_path}' is read-only")

    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    try:
        new_path = shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
        return new_path
    except Exception as e:
        raise e

def create_destination_folder_path(user_provided_path: str, extension: str) -> str:
    return os.path.join(user_provided_path, extension)

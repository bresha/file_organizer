import os
import typing


def read_file_contents(folder: str) -> list:
    files = os.listdir(folder)
    return files
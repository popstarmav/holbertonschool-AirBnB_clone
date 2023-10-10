#!/usr/bin/python3
"""
Initialize and reload 'storage' object using 'FileStorage' class.
"""

from models.engine.file_storage import FileStorage


def initialize_and_reload_storage():
    storage = FileStorage()
    storage.reload()


if __name__ == "__main__":
    initialize_and_reload_storage()

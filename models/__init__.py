#!/usr/bin/python3
"""
    init file define storage like import of filestorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

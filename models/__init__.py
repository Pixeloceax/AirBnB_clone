#!/usr/bin/python3
"""
    init file define storage like import of filestorage
"""
from models.engine.file_storage import FileStorage
import models

storage = FileStorage()
storage.reload()

#!/usr/bin/python3
""" Base Module """
import uuid
import models
import json
import datetime

class BaseModel:
    """
        base model class
    """
    def __init__(self, *args, **kwarg):
        if args is not None:
            pass
        if len(args) > 0:
            pass
        if kwarg
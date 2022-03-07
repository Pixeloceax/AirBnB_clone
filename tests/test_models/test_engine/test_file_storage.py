#!/usr/bin/python3
"""
  i hate test files
"""
import unittest
from time import sleep
import os
from models import base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_save(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        sleep(0.5)
        my_model.save()
        self.assertEqual(my_model.updated_at, old_updated_at)

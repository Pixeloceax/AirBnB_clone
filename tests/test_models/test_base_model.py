#!/usr/bin/python3
"""
  i hate test files
"""

import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel
import os
from time import sleep
import pycodestyle


class TestBaseModel(unittest.TestCase):

    def test_doc(self):
        """
        Test documentation
        """
        self.assertGreater(len(base_model.__doc__), 0)
        self.assertGreater(len(BaseModel.__doc__), 0)
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)
        self.assertGreater(len(BaseModel.save.__doc__), 0)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def test_style(self):
        """
        Test style
        """
        style = pycodestyle.StyleGuide(quiet=True).check_files(["models/base_model.py"])
        self.assertEqual(style.total_errors, 0, "style errors")

    def test_save(self):
        """
        Test save
        """
        my_model = BaseModel()
        old_update = my_model.updated_at
        sleep(0.01)
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_update)

    def test_to_dict(self):
        """
        Test dict
        """
        my_model = BaseModel()
        my_model.name = "User"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertIn("name", my_model_dict)
        self.assertIn("my_number", my_model_dict)

    def test_self_id(self):
        """
        Test id
        """
        my_model = BaseModel()
        sleep(0.1)
        other_model = BaseModel()
        self.assertNotEqual(my_model.id, other_model.id)

    def test_created(self):
        """
        Test created
        """
        my_model = BaseModel()
        sleep(0.1)
        my_model2 = BaseModel()
        self.assertEqual(my_model.created_at, my_model.updated_at)
        self.assertNotEqual(my_model.created_at, my_model2.created_at)
        self.assertNotEqual(my_model.updated_at, my_model2.updated_at)
        my_model2.save()
        self.assertNotEqual(my_model2.created_at, my_model2.updated_at)

    def test_str(self):
        my_model = BaseModel()
        self.assertIn(f"[BaseModel] ({my_model.id})", my_model.__str__())
        self.assertIn(my_model.id, my_model.__str__())
        self.assertIn(repr(my_model.created_at), my_model.__str__())
        self.assertIn(repr(my_model.updated_at), my_model.__str__())

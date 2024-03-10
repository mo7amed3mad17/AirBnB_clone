#!/usr/bin/python3
""" File for unittests of file_storage

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import models
import os
import json
import unittest


class TestFileStorage_instantiation(unittest.TestCase):
    """ Testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Testing methods of the FileStorage class."""

    @classmethod
    def init_enviroment(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def clean_enviroment(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base.id, save_text)
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

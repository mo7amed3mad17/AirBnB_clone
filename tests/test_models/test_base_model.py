#!/usr/bin/python3
""" File for Unittests of base_model

Unittest classes:
    TestBaseModel_objects
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import models
from models.base_model import BaseModel
from datetime import datetime
import os
import unittest
from time import sleep


class TestBaseModel_objects(unittest.TestCase):
    """Unittests for objects of the BaseModel class."""

    def test_simple_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_args_not_used(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        base = BaseModel(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base.id, "0000")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        base = BaseModel("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "00")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_will_ids_change(self):
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertNotEqual(base_1.id, base_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_different_creation_times(self):
        base_1 = BaseModel()
        sleep(1)
        base_2 = BaseModel()
        self.assertGreater(base_2.created_at, base_1.created_at)

    def test_diffierent_update_times(self):
        base_1 = BaseModel()
        sleep(1)
        base_2 = BaseModel()
        self.assertGreater(base_2.updated_at, base_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = date
        base_str = base.__str__()
        self.assertIn("[BaseModel] (123456)", base_str)
        self.assertIn("'id': '123456'", base_str)
        self.assertIn("'created_at': " + date_repr, base_str)
        self.assertIn("'updated_at': " + date_repr, base_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "BaseModel")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

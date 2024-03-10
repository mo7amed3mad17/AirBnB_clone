#!/usr/bin/python3
""" File for Unittests of user

Unittest classes:
    TestUser_objects
    TestSave
    TestToDict
    TestStr
"""
import models
from models.user import User
from datetime import datetime
import os
import unittest
from time import sleep

class TestUser_objects(unittest.TestCase):
    """Unittests for objects of the User class."""

    def test_simple_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_args_not_used(self):
        u = User(None)
        self.assertNotIn(None, u.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        u = User(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(u.id, "0000")
        self.assertEqual(u.created_at, date)
        self.assertEqual(u.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        u = User("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "00")
        self.assertEqual(u.created_at, date)
        self.assertEqual(u.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(User().id))

    def test_will_ids_change(self):
        u_1 = User()
        u_2 = User()
        self.assertNotEqual(u_1.id, u_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_different_creation_times(self):
        u_1 = User()
        sleep(1)
        u_2 = User()
        self.assertGreater(u_2.created_at, u_1.created_at)

    def test_diffierent_update_times(self):
        u_1 = User()
        sleep(1)
        u_2 = User()
        self.assertGreater(u_2.updated_at, u_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        u = User()
        u.id = "123456"
        u.created_at = u.updated_at = date
        base_str = u.__str__()
        self.assertIn("[User] (123456)", base_str)
        self.assertIn("'id': '123456'", base_str)
        self.assertIn("'created_at': " + date_repr, base_str)
        self.assertIn("'updated_at': " + date_repr, base_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = User()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = User()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "User")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = User()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

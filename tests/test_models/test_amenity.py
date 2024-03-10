#!/usr/bin/python3
""" File for Unittests of amenity

Unittest classes:
    TestAmenity_objects
    TestSave
    TestToDict
    TestStr
"""
import models
from models.amenity import Amenity
from datetime import datetime
import os
import unittest
from time import sleep

class TestCity_objects(unittest.TestCase):
    """Unittests for objects of the Amenity class."""

    def test_simple_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_args_not_used(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        amenity = Amenity(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity.id, "0000")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        amenity = Amenity("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "00")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_will_ids_change(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_different_creation_times(self):
        amenity_1 = Amenity()
        sleep(1)
        amenity_2 = Amenity()
        self.assertGreater(amenity_2.created_at, amenity_1.created_at)

    def test_diffierent_update_times(self):
        amenity_1 = Amenity()
        sleep(1)
        amenity_2 = Amenity()
        self.assertGreater(amenity_2.updated_at, amenity_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = date
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + date_repr, amenity_str)
        self.assertIn("'updated_at': " + date_repr, amenity_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = Amenity()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = Amenity()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "Amenity")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = Amenity()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

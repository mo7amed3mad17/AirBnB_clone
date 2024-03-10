#!/usr/bin/python3
""" File for Unittests of place

Unittest classes:
    TestPlace_objects
    TestSave
    TestToDict
    TestStr
"""
import models
from models.place import Place
from datetime import datetime
import os
import unittest
from time import sleep

class TestCity_objects(unittest.TestCase):
    """Unittests for objects of the Place class."""

    def test_simple_instantiation(self):
        self.assertEqual(Place, type(Place()))

    def test_args_not_used(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        place = Place(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place.id, "0000")
        self.assertEqual(place.created_at, date)
        self.assertEqual(place.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        place = Place("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(place.id, "00")
        self.assertEqual(place.created_at, date)
        self.assertEqual(place.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(Place().id))

    def test_will_ids_change(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_different_creation_times(self):
        place_1 = Place()
        sleep(1)
        place_2 = Place()
        self.assertGreater(place_2.created_at, place_1.created_at)

    def test_diffierent_update_times(self):
        place_1 = Place()
        sleep(1)
        place_2 = Place()
        self.assertGreater(place_2.updated_at, place_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = date
        place_str = place.__str__()
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str )
        self.assertIn("'created_at': " + date_repr, place_str)
        self.assertIn("'updated_at': " + date_repr, place_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = Place()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = Place()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "Place")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = Place()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

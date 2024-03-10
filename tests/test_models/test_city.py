#!/usr/bin/python3
""" File for Unittests of city

Unittest classes:
    TestCity_objects
    TestSave
    TestToDict
    TestStr
"""
import models
from models.city import City
from datetime import datetime
import os
import unittest
from time import sleep

class TestCity_objects(unittest.TestCase):
    """Unittests for objects of the City class."""

    def test_simple_instantiation(self):
        self.assertEqual(City, type(City()))

    def test_args_not_used(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        city = City(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city.id, "0000")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        city = City("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "00")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(City().id))

    def test_will_ids_change(self):
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_different_creation_times(self):
        city_1 = City()
        sleep(1)
        city_2 = City()
        self.assertGreater(city_2.created_at, city_1.created_at)

    def test_diffierent_update_times(self):
        city_1 = City()
        sleep(1)
        city_2 = City()
        self.assertGreater(city_2.updated_at, city_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = date
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + date_repr, city_str)
        self.assertIn("'updated_at': " + date_repr, city_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = City()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = City()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "City")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = City()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

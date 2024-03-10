#!/usr/bin/python3
""" File for Unittests of review

Unittest classes:
    TestReview_objects
    TestSave
    TestToDict
    TestStr
"""
import models
from models.review import Review
from datetime import datetime
import os
import unittest
from time import sleep

class TestCity_objects(unittest.TestCase):
    """Unittests for objects of the Review class."""

    def test_simple_instantiation(self):
        self.assertEqual(Review, type(Review()))

    def test_args_not_used(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        review = Review(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(review.id, "0000")
        self.assertEqual(review.created_at, date)
        self.assertEqual(review.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        review = Review("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "00")
        self.assertEqual(review.created_at, date)
        self.assertEqual(review.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(Review().id))

    def test_will_ids_change(self):
        rev_1 = Review()
        rev_2 = Review()
        self.assertNotEqual(rev_1.id, rev_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_different_creation_times(self):
        rev_1 = Review()
        sleep(1)
        rev_2 = Review()
        self.assertGreater(rev_2.created_at, rev_1.created_at)

    def test_diffierent_update_times(self):
        rev_1 = Review()
        sleep(1)
        rev_2 = Review()
        self.assertGreater(rev_2.updated_at, rev_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = date
        rev_str = review.__str__()
        self.assertIn("[Review] (123456)", rev_str)
        self.assertIn("'id': '123456'", rev_str)
        self.assertIn("'created_at': " + date_repr, rev_str)
        self.assertIn("'updated_at': " + date_repr, rev_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = Review()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = Review()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "Review")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = Review()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

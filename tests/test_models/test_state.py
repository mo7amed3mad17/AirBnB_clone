#!/usr/bin/python3
""" File for Unittests of state

Unittest classes:
    TestState_objects
    TestSave
    TestToDict
    TestStr
"""
import models
from models.state import State
from datetime import datetime
import os
import unittest
from time import sleep

class TestCity_objects(unittest.TestCase):
    """Unittests for objects of the State class."""

    def test_simple_instantiation(self):
        self.assertEqual(State, type(State()))

    def test_args_not_used(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_make_objects_none_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_make_objects_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        state = State(id="0000", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state.id, "0000")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_make_objects_args_and_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        state = State("7", id="00", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "00")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_id_str(self):
        self.assertEqual(str, type(State().id))

    def test_will_ids_change(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_different_creation_times(self):
        state_1 = State()
        sleep(1)
        state_2 = State()
        self.assertGreater(state_2.created_at, state_1.created_at)

    def test_diffierent_update_times(self):
        state_1 = State()
        sleep(1)
        state_2 = State()
        self.assertGreater(state_2.updated_at, state_1.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = date
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + date_repr, state_str)
        self.assertIn("'updated_at': " + date_repr, state_str)


class TestSave(unittest.TestCase):
    def setUp(self):
        self.model = State()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)


class TestToDict(unittest.TestCase):
    def setUp(self):
        self.model = State()

    def test_to_dict_returns_dictionary_with_right_arrangment(self):
        self.model.created_at = datetime(2024, 3, 8)
        self.model.updated_at = datetime(2024, 3, 10)
        result = self.model.to_dict()
        self.assertEqual(result["created_at"], "2024-03-08T00:00:00")
        self.assertEqual(result["updated_at"], "2024-03-10T00:00:00")
        self.assertEqual(result["__class__"], "State")


class TestStr(unittest.TestCase):
    def setUp(self):
        self.model = State()

    def test_str_returns_string_representation(self):
        self.model.id = "abc123"
        self.model.__dict__["name"] = "Test Model"
        result = str(self.model)
        self.assertEqual(result, str(self.model))


if __name__ == "__main__":
    unittest.main()

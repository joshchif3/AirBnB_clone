#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_instance(self):
        """Testing a new created instance"""
        instance = State()
        self.assertEqual(State, type(instance))

    def test_instance_id(self):
        "testing"
        instance = State()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = State()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = State()
        instance_2 = State()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = State()
        expected_str = f"[State] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = State()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = State()
        instance.name = "State"
        self.assertEqual(instance.name, "State")

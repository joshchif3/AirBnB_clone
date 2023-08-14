#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    TESTING CLASS
    """
    def test_instance(self):
        """Testing a new created instance"""
        instance = Place()
        self.assertEqual(Place, type(instance))

    def test_instance_id(self):
        "testing"
        instance = Place()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = Place()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = Place()
        instance_2 = Place()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = Place()
        expected_str = f"[Place] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = Place()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = Place()
        instance.name = "My First Model"
        self.assertEqual(instance.name, "My First Model")

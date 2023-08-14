#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_instance(self):
        """Testing a new created instance"""
        instance = City()
        self.assertEqual(City, type(instance))

    def test_instance_id(self):
        "testing"
        instance = City()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = City()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = City()
        instance_2 = City()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = City()
        expected_str = f"[City] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = City()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = City()
        instance.name = "Monaco"
        self.assertEqual(instance.name, "Monaco")

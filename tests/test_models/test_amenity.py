#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_instance(self):
        """Testing a new created instance"""
        instance = Amenity()
        self.assertEqual(Amenity, type(instance))

    def test_instance_id(self):
        "testing"
        instance = Amenity()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        "testing"
        instance = Amenity()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        "testing"
        instance_1 = Amenity()
        instance_2 = Amenity()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = Amenity()
        expected_str = f"[Amenity] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = Amenity()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = Amenity()
        instance.name = "Amenity"
        self.assertEqual(instance.name, "Amenity")

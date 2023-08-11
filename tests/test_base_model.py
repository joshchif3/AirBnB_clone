#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_instance(self):
        instance = BaseModel()
        self.assertEqual(BaseModel, type(instance))

    def test_instance_init_name_number(self):
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        self.assertEqual(instance.name, "My First Model")
        self.assertEqual(instance.my_number, 89)

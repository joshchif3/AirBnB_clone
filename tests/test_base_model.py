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
        """Testing a new created instance"""
        instance = BaseModel()
        self.assertEqual(BaseModel, type(instance))

    def test_object_to_dict(self):
        """Testing To_dict method"""
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        dictionary = instance.to_dict()
        dictionary_cmp = {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'BaseModel',
            'updated_at': instance.updated_at.isoformat(),
            'id': instance.id,
            'created_at': instance.created_at.isoformat()
        }
        self.assertEqual(dictionary_cmp, dictionary)

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        self.assertEqual(instance.name, "My First Model")
        self.assertEqual(instance.my_number, 89)

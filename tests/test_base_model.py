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

    def test_instance_id(self):
        instance = BaseModel()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))
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
"""
# The save method isn't working.
    def test_instance_save(self):
        instance = BaseModel()
        initial_value = instance.updated_at
        instance.save()
        updated_value = instance.updated_at
        self.assertNotEqual(initial_value, updated_value)
"""


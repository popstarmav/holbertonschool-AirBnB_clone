#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
import models
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_BaseModel_instantiation(self):
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_BaseModel_instantiation_with_id(self):
        self.assertEqual(type(BaseModel(id="123")), BaseModel)

    def test_BaseModel_unique_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_BaseModel_str_id(self):
        obj = BaseModel(id="1")
        self.assertEqual(obj.id, "1")

    def test_BaseModel_uuid_id(self):
        obj = BaseModel()
        self.assertEqual(type(obj.id) is str, True)

    def test_BaseModel_created_at(self):
        obj = BaseModel()
        self.assertEqual(type(obj.created_at), datetime)

    def test_BaseModel_updated_at(self):
        obj = BaseModel()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_BaseModel_created_updated_equal(self):
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_BaseModel_created_updated_not_equal(self):
        obj = BaseModel()
        obj.updated_at = datetime(2017, 2, 22, 12, 12, 12, 123456)
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_BaseModel_updated_at_after_change(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_BaseModel_str_return(self):
        obj = BaseModel()
        self.assertEqual(
                str(obj), "[BaseModel] ({}) {}".format
                (obj.id, obj.__dict__))

    def test_BaseModel_to_dict(self):
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_BaseModel_to_dict_contains_id(self):
        obj = BaseModel()
        self.assertIn("id", obj.to_dict())

    def test_BaseModel_to_dict_contains_created_at(self):
        obj = BaseModel()
        self.assertIn("created_at", obj.to_dict())

    def test_BaseModel_to_dict_contains_updated_at(self):
        obj = BaseModel()
        self.assertIn("updated_at", obj.to_dict())

    def test_BaseModel_to_dict_contains_updated_at_str(self):
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()["updated_at"]), str)

    def test_BaseModel_to_dict_contains_created_at_str(self):
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()["created_at"]), str)

    def test_BaseModel_to_dict_contains_class_key(self):
        obj = BaseModel()
        self.assertIn("__class__", obj.to_dict())

    def test_BaseModel_to_dict_updated_at(self):
        obj = BaseModel()
        obj.updated_at = datetime(2017, 2, 22, 12, 12, 12, 123456)
        self.assertEqual(
                obj.to_dict()["updated_at"], "2017-02-22T12:12:12.123456")

    def test_BaseModel_to_dict_created_at(self):
        obj = BaseModel()
        obj.created_at = datetime(2017, 2, 22, 12, 12, 12, 123456)
        self.assertEqual(
                obj.to_dict()["created_at"], "2017-02-22T12:12:12.123456")

    def test_BaseModel_to_dict_class(self):
        obj = BaseModel()
        self.assertEqual(obj.to_dict()["__class__"], "BaseModel")


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        try:
            os.remove("file.json")
        except Exception as e:
            pass

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except Exception as e:
            pass

    def test_BaseModel_save(self):
        obj = BaseModel()
        obj.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_BaseModel_save_updates(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_BaseModel_to_dict_output(self):
        obj = BaseModel()
        expected_dict = {
            'id': obj.id,
            '__class__': 'BaseModel',
            'created_at': obj.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'updated_at': obj.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        }
        self.assertDictEqual(obj.to_dict(), expected_dict)

    def test_BaseModel_to_dict_cls_attr(self):
        obj = BaseModel()
        self.assertTrue("__class__" in obj.to_dict())


if __name__ == "__main__":
    unittest.main()

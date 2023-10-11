#!/usr/bin/python3
"""Unit tests for the `city` module."""
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """Test cases for the `City` class."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        cls.c1 = City()
        cls.c2 = City(**cls.c1.to_dict())
        cls.c3 = City("hello", "wait", "in")

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        storage.delete(cls.c1)
        storage.delete(cls.c2)
        storage.delete(cls.c3)

    def tearDown(self):
        """Reset FileStorage data for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""
        self.assertIsInstance(self.c1.name, str)
        self.assertEqual(self.c3.name, "")
        self.c1.name = "Abuja"
        self.assertEqual(self.c1.name, "Abuja")

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(self.c1.id, str)
        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c1.updated_at, datetime)
        self.assertEqual(self.c1.updated_at, self.c2.updated_at)

    def test_save(self):
        """Test method for save"""
        old_update = self.c1.updated_at
        self.c1.save()
        self.assertNotEqual(self.c1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for dict"""
        city_dict = self.c2.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], type(self.c2).__name__)
        self.assertIn('created_at', city_dict.keys())
        self.assertIn('updated_at', city_dict.keys())
        self.assertNotEqual(self.c1, self.c2)


if __name__ == "__main__":
    unittest.main()

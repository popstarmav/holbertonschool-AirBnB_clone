#!/usr/bin/python3
"""Unit tests for the `place` module."""
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Test cases for the `Place` class."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        cls.p1 = Place()
        cls.p2 = Place(**cls.p1.to_dict())
        cls.p3 = Place("hello", "wait", "in")

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        storage.delete(cls.p1)
        storage.delete(cls.p2)
        storage.delete(cls.p3)

    def tearDown(self):
        """Reset FileStorage data for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""
        self.assertIsInstance(self.p1.name, str)
        self.assertIn(
                f"{type(self.p1).__name__}.{self.p1.id}", storage.all())
        self.assertEqual(self.p3.name, "")

        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(self.p1.id, str)
        self.assertIsInstance(self.p1.created_at, datetime)
        self.assertIsInstance(self.p1.updated_at, datetime)
        self.assertEqual(self.p1.updated_at, self.p2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        string = (
                f"[{type(self.p1).__name__}] ({self.p1.id})"
                f"{self.p1.__dict__}"
        )
        self.assertEqual(self.p1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        old_update = self.p1.updated_at
        self.p1.save()
        self.assertNotEqual(self.p1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for dict"""
        p2_dict = self.p2.to_dict()
        self.assertIsInstance(p2_dict, dict)
        self.assertEqual(p2_dict['__class__'], type(self.p2).__name__)
        self.assertIn('created_at', p2_dict.keys())
        self.assertIn('updated_at', p2_dict.keys())
        self.assertNotEqual(self.p1, self.p2)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit tests for the `review` module."""
import os
import unittest
from datetime import datetime
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        cls.r1 = Review()
        cls.r2 = Review(**cls.r1.to_dict())
        cls.r3 = Review("hello", "wait", "in")

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        storage.delete(cls.r1)
        storage.delete(cls.r2)
        storage.delete(cls.r3)

    def tearDown(self):
        """Reset FileStorage data for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""
        self.assertIsInstance(self.r1.text, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.place_id, str)
        self.assertEqual(self.r3.text, "")

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(self.r1.id, str)
        self.assertIsInstance(self.r1.created_at, datetime)
        self.assertIsInstance(self.r1.updated_at, datetime)
        self.assertEqual(self.r1.updated_at, self.r2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        string = (
                f"[{type(self.r1).__name__}] ({self.r1.id})"
                f"{self.r1.__dict__}"
        )
        self.assertEqual(self.r1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        old_update = self.r1.updated_at
        self.r1.save()
        self.assertNotEqual(self.r1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for dict"""
        r2_dict = self.r2.to_dict()
        self.assertIsInstance(r2_dict, dict)
        self.assertEqual(r2_dict['__class__'], type(self.r2).__name__)
        self.assertIn('created_at', r2_dict.keys())
        self.assertIn('updated_at', r2_dict.keys())
        self.assertNotEqual(self.r1, self.r2)


if __name__ == "__main__":
    unittest.main()

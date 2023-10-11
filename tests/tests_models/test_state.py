#!/usr/bin/python3
"""Unit tests for the `state` module."""
import os
import unittest
from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        cls.s1 = State()
        cls.s2 = State(**cls.s1.to_dict())
        cls.s3 = State("hello", "wait", "in")

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        storage.delete(cls.s1)
        storage.delete(cls.s2)
        storage.delete(cls.s3)

    def tearDown(self):
        """Reset FileStorage data for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        k = f"{type(self.s1).__name__}.{self.s1.id}"
        self.assertIsInstance(self.s1.name, str)
        self.assertEqual(self.s3.name, "")
        self.s1.name = "Chicago"
        self.assertEqual(self.s1.name, "Chicago")
        self.assertIn(k, storage.all())

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(self.s1.id, str)
        self.assertIsInstance(self.s1.created_at, datetime)
        self.assertIsInstance(self.s1.updated_at, datetime)
        self.assertEqual(self.s1.updated_at, self.s2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        string = (
                f"[{type(self.s1).__name__}] ({self.s1.id})"
                f"{self.s1.__dict__}"
        )
        self.assertEqual(self.s1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        old_update = self.s1.updated_at
        self.s1.save()
        self.assertNotEqual(self.s1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for dict"""
        s2_dict = self.s2.to_dict()
        self.assertIsInstance(s2_dict, dict)
        self.assertEqual(s2_dict['__class__'], type(self.s2).__name__)
        self.assertIn('created_at', s2_dict.keys())
        self.assertIn('updated_at', s2_dict.keys())
        self.assertNotEqual(self.s1, self.s2)


if __name__ == "__main__":
    unittest.main()

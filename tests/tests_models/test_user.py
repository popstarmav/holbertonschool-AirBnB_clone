#!/usr/bin/python3
"""Unit tests for the `user` module."""
import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the `User` class."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        cls.u1 = User()
        cls.u2 = User(**cls.u1.to_dict())

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        storage.delete(cls.u1)
        storage.delete(cls.u2)

    def tearDown(self):
        """Reset FileStorage data for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        k = f"{type(self.u1).__name__}.{self.u1.id}"
        self.assertIn(k, storage.all())
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(self.u1.id, str)
        self.assertIsInstance(self.u1.created_at, datetime)
        self.assertIsInstance(self.u1.updated_at, datetime)
        self.assertEqual(self.u1.updated_at, self.u2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        string = (
                f"[{type(self.u1).__name__}] ({self.u1.id})"
                f"{self.u1.__dict__}"
        )
        self.assertEqual(self.u1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        old_update = self.u1.updated_at
        self.u1.save()
        self.assertNotEqual(self.u1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for dict"""
        u2_dict = self.u2.to_dict()
        self.assertIsInstance(u2_dict, dict)
        self.assertEqual(u2_dict['__class__'], type(self.u2).__name__)
        self.assertIn('created_at', u2_dict.keys())
        self.assertIn('updated_at', u2_dict.keys())
        self.assertNotEqual(self.u1, self.u2)


if __name__ == "__main__":
    unittest.main()

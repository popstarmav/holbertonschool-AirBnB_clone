#!/usr/bin/python3
"""Unit tests for the `amenity` module."""
import os
import unittest
from models import storage
from models.amenity import Amenity
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        cls.amenity = Amenity()
        cls.amenity.name = "Sample Amenity"
        cls.amenity.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level resources."""
        storage.delete(cls.amenity)

    def tearDown(self):
        """Reset FileStorage data for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test class attributes."""
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "Sample Amenity")

    def test_init(self):
        """Test public instance attributes."""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str(self):
        """Test string representation."""
        string = str(self.amenity)
        expected_string = f"[{type(self.amenity).__name__}]
        ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(string, expected_string)

    def test_save(self):
        """Test save method."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(
                amenity_dict['__class__'], type(self.amenity).__name__)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertNotEqual(self.amenity, Amenity(**amenity_dict))


if __name__ == "__main__":
    unittest.main()

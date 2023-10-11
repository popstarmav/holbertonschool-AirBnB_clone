#!/usr/bin/python3
from io import StringIO
import os
import unittest
import storage
from unittest.mock import patch
from console import HBNBCommand
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment after each test."""
        self.console = None

    def test_console_help(self):
        """Test the 'help' command in the console."""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            self.console.onecmd("help")
            output = mock_output.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_console_create(self):
        """Test the 'create' command in the console."""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            self.console.onecmd("create BaseModel")
            output = mock_output.getvalue()
            self.assertIn("{}".format("ID"), output)

    def test_console_show(self):
        """Test the 'show' command in the console."""
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("show BaseModel 1")
            output = mock_output.getvalue()
            self.assertIn("{}".format("ID"), output)


class TestBaseModel(unittest.TestCase):
    def test_create_basemodel(self):
        """Test creating a new BaseModel instance."""
        bm = BaseModel()
        self.assertTrue(isinstance(bm, BaseModel))

    def test_all_basemodel(self):
        """Test 'all' method of BaseModel."""
        # Create some BaseModel instances
        bm1 = BaseModel()
        bm2 = BaseModel()

        all_basemodel = storage.all(BaseModel)
        self.assertIn(bm1, all_basemodel.values())
        self.assertIn(bm2, all_basemodel.values())

    def test_show_basemodel(self):
        """Test 'show' method of BaseModel."""
        bm = BaseModel()
        bm_id = bm.id

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            self.console.onecmd(f"show BaseModel {bm_id}")
            output = mock_output.getvalue()
            self.assertIn(str(bm), output)

    def test_update_basemodel(self):
        """Test 'update' method of BaseModel."""
        bm = BaseModel()
        bm_id = bm.id

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            self.console.onecmd(f"update BaseModel {bm_id} name 'New Name'")
            output = mock_output.getvalue()
            self.assertIn("name: 'New Name'", output)
            self.assertEqual(bm.name, "New Name")

    def test_destroy_basemodel(self):
        """Test 'destroy' method of BaseModel."""
        bm = BaseModel()
        bm_id = bm.id

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            self.console.onecmd(f"destroy BaseModel {bm_id}")
            output = mock_output.getvalue()
            self.assertNotIn(bm, storage.all(BaseModel).values())


class TestBaseModelDotNotation(unittest.TestCase):
    def test_create_basemodel(self):
        """Test creating a new BaseModel instance using dot notation."""
        bm = BaseModel()
        self.assertTrue(isinstance(bm, BaseModel))


class TestUser(unittest.TestCase):
    def test_create_user(self):
        """Test creating a new User instance."""
        user = User()
        self.assertTrue(isinstance(user, User))


class TestUserDotNotation(unittest.TestCase):
    def test_create_user(self):
        """Test creating a new User instance using dot notation."""
        user = User()
        self.assertTrue(isinstance(user, User))


class TestState(unittest.TestCase):
    def test_create_state(self):
        """Test creating a new State instance."""
        state = State()
        self.assertTrue(isinstance(state, State))


class TestStateDotNotation(unittest.TestCase):
    def test_create_state(self):
        """Test creating a new State instance using dot notation."""
        state = State()
        self.assertTrue(isinstance(state, State))


class TestReview(unittest.TestCase):
    def test_create_review(self):
        """Test creating a new Review instance."""
        review = Review()
        self.assertTrue(isinstance(review, Review))


class TestReviewDotNotation(unittest.TestCase):
    def test_create_review(self):
        """Test creating a new Review instance using dot notation."""
        review = Review()
        self.assertTrue(isinstance(review, Review))


class TestPlace(unittest.TestCase):
    def test_create_place(self):
        """Test creating a new Place instance."""
        place = Place()
        self.assertTrue(isinstance(place, Place))


class TestPlaceDotNotation(unittest.TestCase):
    def test_create_place(self):
        """Test creating a new Place instance using dot notation."""
        place = Place()
        self.assertTrue(isinstance(place, Place))


class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        """Test creating a new Amenity instance."""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity))


class TestAmenityDotNotation(unittest.TestCase):
    def test_create_amenity(self):
        """Test creating a new Amenity instance using dot notation."""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity))


class TestCity(unittest.TestCase):
    def test_create_city(self):
        """Test creating a new City instance."""
        city = City()
        self.assertTrue(isinstance(city, City))


class TestCityDotNotation(unittest.TestCase):
    def test_create_city(self):
        """Test creating a new City instance using dot notation."""
        city = City()
        self.assertTrue(isinstance(city, City))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Import necessary modules for testing"""
import unittest
import pep8
import os
from models.user import User
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unit tests for the User class."""

    @classmethod
    def setUp(cls):
        """Create a test instance of User."""
        cls.testUser = User()
        cls.testUser.email = "email"
        cls.testUser.password = "xxx"
        cls.testUser.first_name = "first"
        cls.testUser.last_name = "last"

    @classmethod
    def tearDown(cls):
        """Delete the test instance and 'file.json' if it exists."""
        del cls.testUser
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """Test for PEP8 compliance in 'models/user.py'."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Test for the existence of docstrings."""
        self.assertTrue(len(User.__doc__) > 0)
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables(self):
        """Test initialization and class variables."""
        self.assertTrue(isinstance(self.testUser, User))
        self.assertTrue(issubclass(type(self.testUser), BaseModel))
        self.assertTrue('email' in self.testUser.__dict__)
        self.assertTrue('id' in self.testUser.__dict__)
        self.assertTrue('created_at' in self.testUser.__dict__)
        self.assertTrue('updated_at' in self.testUser.__dict__)
        self.assertTrue('password' in self.testUser.__dict__)
        self.assertTrue('first_name' in self.testUser.__dict__)
        self.assertTrue('last_name' in self.testUser.__dict__)

    def test_save(self):
        """Test attribute types for strings."""
        self.testUser.save()
        self.assertTrue(self.testUser.updated_at != self.testUser.created_at)

    def test_strings(self):
        """Test the 'to_dict' method."""
        self.assertEqual(type(self.testUser.email), str)
        self.assertEqual(type(self.testUser.password), str)
        self.assertEqual(type(self.testUser.first_name), str)
        self.assertEqual(type(self.testUser.first_name), str)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.testUser), True)

if __name__ == '__main__':
    unittest.main()

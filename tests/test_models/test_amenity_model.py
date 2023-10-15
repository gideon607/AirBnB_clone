#!/usr/bin/python3

"""
    test unit for the amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """
        Testing the Amenity class
    """

    def test_Amenity_attributes(self):
        """
            Tests for Amenity class had name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_inheritence(self):
        """
            Tests for Amenity class Inherits from BaseModel
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attribute_type(self):
        """
            Tests for Amenity class for name attribute's type.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)


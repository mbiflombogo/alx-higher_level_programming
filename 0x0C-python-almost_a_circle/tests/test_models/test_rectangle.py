#!/usr/bin/python3

"""unit testing class
Rectangle ()"""


import unittest
import json
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleClass(unittest.TestCase):
    """Testing class Rectangle(Base)"""
    def test_init(self):
        """Testing __init__"""
        with self.assertRaises(TypeError) as cm:
            self.assertAlmostEqual(Rectangle(), cm)
            self.assertAlmostEqual(Rectangle(10), cm)

    def test_setters_type_err(self):
        """Testing @property.setter"""
        with self.assertRaises(TypeError) as cm:
            self.assertAlmostEqual(Rectangle("2", 10), cm)
            self.assertAlmostEqual(Rectangle(10, "2"), cm)
            self.assertAlmostEqual(Rectangle(20, 10, {}), cm)
            self.assertAlmostEqual(Rectangle(20, 10, 2, {}), cm)

    def test_setters_value_err(self):
        """Testing @property.setter"""
        with self.assertRaises(ValueError) as cm:
            self.assertAlmostEqual(Rectangle(-10, 10), cm)
            self.assertAlmostEqual(Rectangle(10, -10), cm)
            self.assertAlmostEqual(Rectangle(20, 10, -1), cm)
            self.assertAlmostEqual(Rectangle(20, 10, 2, -1), cm)

    def test_area(self):
        """...testing...area().. ..."""
        r1 = Rectangle(20, 10)
        r2 = Rectangle(50, 10, 2, 0)
        self.assertAlmostEqual(r1.area(), 200)
        self.assertAlmostEqual(r2.area(), 500)

    def test_to_dictionary(self):
        """testing to_dictionary()"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)

#!/usr/bin/python3

"""unit testing class
Square ()"""


import unittest
import json
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Testing class Square(Base)"""
    def test_init(self):
        """Testing __init__"""
        with self.assertRaises(TypeError) as cm:
            self.assertAlmostEqual(Square(), cm)

    def test_setters_type_err(self):
        """Testing @property.setter"""
        with self.assertRaises(TypeError) as cm:
            self.assertAlmostEqual(Square("2"), cm)

    def test_setters_value_err(self):
        """Testing @property.setter"""
        with self.assertRaises(ValueError) as cm:
            self.assertAlmostEqual(Square(-10), cm)

    def test_to_dictionary(self):
        """testing to_dictionary()"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(type(s1_dictionary), dict)

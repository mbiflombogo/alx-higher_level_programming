#!/usr/bin/python3
"""unit testing with the
unittest module"""


import unittest
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle
import json


class TestBaseClass(unittest.TestCase):
    """testing the base class"""

    def test_init(self):
        """test the initialize method"""
        b1 = Base(12)
        self.assertAlmostEqual(b1.id, 12)
        self.assertAlmostEqual(Base().id, 1)

    def test_to_json_string(self):
        """testing to_json_string()"""
        x = [1, 2, "b"]
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([]), "[]")
        self.assertAlmostEqual(Base.to_json_string(x), '[1, 2, "b"]')

    def test_save_to_file(self):
        """testing save_to_file()"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        self.assertAlmostEqual(Base.save_to_file(None), [].append([]))
        self.assertAlmostEqual(Rectangle.save_to_file([r1, r2]),
                               [{"y": 8, "x": 2, "id": 1,
                                 "width": 10, "height": 7},
                                {"y": 0, "x": 0, "id": 2,
                                 "width": 2, "height": 4}].append([]))

    def test_from_json_string(self):
        """testing from_json_string ()"""
        x = '[1, 2, "b"]'
        if type(x) in [str, bytes, bytearray]:
            self.assertAlmostEqual(Base.from_json_string(None), [])
            self.assertAlmostEqual(Base.from_json_string(x), [1, 2, "b"])
        else:
            self.assertRaises(TypeError, Base.from_json_string, x)

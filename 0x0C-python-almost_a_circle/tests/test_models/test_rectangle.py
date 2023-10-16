#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base

"""Test case for `rectangle` module"""


class testRectangle(unittest.TestCase):
    """Unit tests for `Rectangle` class"""


    def test_int_width(self):
        r = Rectangle(7, 3)
        self.assertEqual(r.width, 7)

    def test_not_int_width(self):
        with self.assertRaises(TypeError):
            Rectangle("not int", 7)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-3, 9)

    def test_int_height(self):
        r = Rectangle(12, 6)
        self.asserEqual(r.height, 6)

    def test_not_int_height(self):
        with self.assertRaises(TypeError):
            Rectangle(9, True)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -4)

    def test_int_x(self):
        r = Rectangle(6, 4, 3, 1)
        self.assertEqual(r.x, 3)

    def test_no_x(self):
        r = Rectangle(5, 9)
        self.assertEqual(r.x, 0)

    def test_not_int_x(self):
        with self.assertRaises(TypeError):
            Rectangle(9, 8, [1, 4, 2])

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 3, -1)

    def test_int_y(self):
        r = Rectangle(6, 4, 3, 1)
        self.assertEqual(r.y, 1)

    def test_no_y(self):
        r = Rectangle(5, 3)
        self.assertEqual(r.y, 0)

    def test_not_int_y(self):
        with self.assertRaises(TypeError):
            Rectangle(9, 8, 1, (7, 1))

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 3, 2, -3)

    def test_inheritence(self):
        self.asserIsInstance(Rectangle(8, 5), Base)

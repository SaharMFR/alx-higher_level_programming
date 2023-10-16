#!/usr/bin/python3
import unittest
from models.base import Base

"""Test cases for `base` module"""


class testBase(unittest.TestCase):
    """Unit tests for `Base` class"""


    def test_none_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_positive_id(self):
        b = Base(8)
        self.assertEqual(b.id, 8)

    def test_negative_id(self):
        b = Base(-12)
        self.assertEqual(b.id, -12)

    def test_zero_id(self):
        b = Base(0)
        self.asserEqual(b.id, 0)

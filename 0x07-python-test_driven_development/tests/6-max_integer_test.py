#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([..])."""

    def test_max_at_the_end(self):
        """Test max at the end of a list of integers."""
        max_at_the_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_the_end), 4)

    def test_max_in_the_middle(self):
        """Test max in the middle of a list of integers."""
        max_in_the_middle = [2, 4, 1, 3]
        self.assertEqual(max_integer(max_in_the_middle), 4)

    def test_max_at_the_begginning(self):
        """Test max at the begginning of a list of integers."""
        max_at_the_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_the_beginning), 4)

    def test_one_negative(self):
        """Test one negative number in the list."""
        one_negative = [2, 6, -8, 4, 3]
        self.asssertEqual(max_integer(one_negative), 6)

    def test_only_negative(self):
        """Test only negative numbers in the list."""
        only_negative = [-5, -2, -8, -1]
        self.assertEqual(max_integer(only_negative), -1)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [2]
        self.assertEqual(max_integer(one_element), 2)

    def test_floats(self):
        """Test a list of floats."""
        floats = [11.5, 5.21, 14.92, 7.45, -3.073]
        self.assertEqual(max_integer(floats), 14.92)

    def test_ints_and_floats(self):
        """Test a list of integerss and floats."""
        ints_and_floats = [6.93, 11.34, 5, 8.15, 17]
        self.assertEqual(max_integer(ints_and_floats), 17)

    def test_string(self):
        """Test a string."""
        string = "Sahar"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Hi", "hello", "yes", "No"]
        self.assertEqual(max_integer(strings), "yes")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(''), None)

if __name__ == '__main__':
    unittest.main()

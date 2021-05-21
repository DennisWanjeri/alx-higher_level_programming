#!/usr/bin/python3
"""unit tests for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit tests for max integer"""
    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ord_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ord_list), 4)

    def test_unordered_list(self):
        """testing an unordered list"""
        unord = [3, 1, 2, 4]
        self.assertEqual(max_integer(unord), 4)

    def test_empty_list(self):
        """testing an empty list occurrence"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_beginning(self):
        """tests when max is at the beginning"""
        beg = [3, 1, 2]
        self.assertEqual(max_integer(beg), 3)

    def test_one_element(self):
        """tests when list has only one element"""
        one = [3]
        self.assertEqual(max_integer(one), 3)

    def test_floats(self):
        """tests a list of floats"""
        fl = [1.1, 8.2, 18.9]
        self.assertEqual(max_integer(fl), 18.9)

    def test_string(self):
        """tests a string occurrence"""
        string = "Dennis"
        self.assertEqual(max_integer(string), 's')

    def test_list_strings(self):
        """tests a list of strings"""
        string = ["Dennis", "is", "my", "name"]
        self.assertEqual(max_integer(string), "name")

if __name__ == "__main__":
    unittest.main()

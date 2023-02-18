#!/usr/bin/python3
""" Unit test for max_integer in list function """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class contains unit tests for max_integer """

    def test_positive_list(self):
        """Test a list of positive numbers"""
        listy = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(listy), 5)

    def test_negative_list(self):
        """Test a list of negative numbers"""
        listy = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(listy), -1)

    def test_positive_negative_list(self):
        """Test a list of positive numbers"""
        listy = [-1, 2, -3, 4, 5]
        self.assertEqual(max_integer(listy), 5)

    def test_positive(self):
        """Test a list of positive numbers"""
        listy = [1, 2, 3, 4, 10]
        self.assertEqual(max_integer(listy), 10)

    def test_duplicate(self):
        """Test a list of positive numbers"""
        listy = [1, 2, 2, 4, 3]
        self.assertEqual(max_integer(listy), 4)

    def test_duplicate_result(self):
        """Test a list of positive numbers"""
        listy = [5, 2, 3, 5, 1]
        self.assertEqual(max_integer(listy), 5)

    def test_all_same_values(self):
        """Test a list of positive numbers"""
        listy = [1, 1, 1, 1, 1]
        self.assertEqual(max_integer(listy), 1)

    def test_all_same_values(self):
        """Test a list of positive numbers"""
        listy = [-1, -1, -1, -1, -1]
        self.assertEqual(max_integer(listy), -1)

    def test_all_same_values(self):
        """Test a list of positive numbers"""
        listy = [1, 1, 1, 1, 1]
        self.assertEqual(max_integer(listy), 1)

if __name__ == "__main__":
    unittest.main()

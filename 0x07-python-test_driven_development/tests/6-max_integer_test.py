#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """
        Test with empty list
        """
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """
        Test with negative numbers
        """
        self.assertEqual(max_integer([-4, -7, -8, -1]), -1)

    def test_positive_numbers(self):
        """
        Test using positive numbers
        """
        self.assertEqual(max_integer([7, 3, 8, 1]), 8)

    def test_single_element(self):
        """
        Test using single number
        """
        self.assertEqual(max_integer([8]), 8)

    def test_large_numbers(self):
        """
        Test with long numbers
        """
        self.assertEqual(max_integer([10000000000, 885888778]), 10000000000)

    def test_duplicate_numbers(self):
        """
        Test usnig same numbers
        """
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_mixed_numbers(self):
        """
        Test using mixed numbers float and inetegers
        """
        self.assertEqual(max_integer([2, -9, 9, -3]), 9)

    if __name__ == '__main__':
        unittest.main()

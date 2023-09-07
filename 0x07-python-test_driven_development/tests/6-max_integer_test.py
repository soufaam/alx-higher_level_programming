#!/bin/usr/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

""" This is a decription of this module .

This module contains a function called text_indentation
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over
multiple lines. Sections are created
with a section header and a colon followed
by a block of indented text.
"""

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_end(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns 
        """
        
        got = max_integer([1, 2, 4])
        self.assertEqual(got, 4)

    def test_max_integer_void(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns 
        """
        got = max_integer([])
        self.assertEqual(got, None)

    def test_max_negative(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns 
        """
        got = max_integer([-1, -2, -5, -4])
        self.assertEqual(got, -1)

    def test_max_bigining(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns 
        """
        got = max_integer([45, 2, 23, 4])
        self.assertEqual(got, 45)

    def test_max_midle(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns 
        """
        got = max_integer([34, 2, 70, 4])
        self.assertEqual(got, 70)

    def test_max_mix(self):
        """Class methods are similar to regular functions.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Returns:
            returns 
        """
        got = max_integer([34, -2, 70, 4])
        self.assertEqual(got, 70)

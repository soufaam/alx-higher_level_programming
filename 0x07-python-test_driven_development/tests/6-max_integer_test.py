#!/bin/usr/python3
import unittest

class TestStringMethods(unittest.TestCase):

  def test_max_integer(list=[]):
      self.assertEqual(', 'FOO')

  def test_max_integer(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_max_integer(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)
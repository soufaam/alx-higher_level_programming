import unittest
from models.base import Base

"""unitest model for base class"""


class TestBaseClass(unittest.TestCase):

    def test_constructor_none(self):
        """id == None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def ttest_constructor_not_none(self):
        """id != None"""
        b1 = Base(9)
        self.assertEqual(b1.id, 9)

    def ttest_constructor_not_none_inc(self):
        """increment nb_objects"""
        b1 = Base()
        self.assertEqual(b1.id, 2)

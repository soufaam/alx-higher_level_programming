import unittest
from models.rectangle import Rectangle

"""unitest model for base class"""


class TestBaseClass(unittest.TestCase):

    def test_calculate_area(self):
        """return area"""
        r = Rectangle(10, 2, id=12)
        self.assertEqual(r.area(), 20)

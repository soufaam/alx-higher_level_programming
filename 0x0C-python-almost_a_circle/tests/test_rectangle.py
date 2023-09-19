import unittest
from models.rectangle import Rectangle

"""unitest model for base class"""


class TestBaseClass(unittest.TestCase):

    def test_constructor_none(self):
        """id == None"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 5)

    def test_constructor_not_none(self):
        """id != None"""
        r = Rectangle(10, 2, id=23)
        self.assertEqual(r.id, 23)

    def test_constructor_not_none_inc(self):
        """increment nb_objects"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 6)

    def test_constructor_width(self):
        """get width attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

    def test_constructor_height(self):
        """get set width attribute"""
        r = Rectangle(10, 2)

        self.assertEqual(r.height, 2)

    def test_constructor_setter_height(self):
        """get set width attribute"""
        r = Rectangle(10, 2)
        r.height = 12

        self.assertEqual(r.height, 12)

    def test_constructor_setter_width(self):
        """get set width attribute"""
        r = Rectangle(10, 2)
        r.width = 12
        self.assertEqual(r.width, 12)

    def test_constructor_getter_x(self):
        """get set x attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)

    def test_constructor_getter_y(self):
        """get set width attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.y, 0)

    def test_constructor_setter_x(self):
        """get set x attribute"""
        r = Rectangle(10, 2)
        r.x = 2023
        self.assertEqual(r.x, 2023)

    def test_constructor_getter_y(self):
        """get set y attribute"""
        r = Rectangle(10, 2)
        r.y = 25
        self.assertEqual(r.y, 25)
import unittest
from models.rectangle import Rectangle

"""unitest model for base class"""


class TestRectangleClass(unittest.TestCase):

    def test_constructor_none(self):
        """id == None"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 7)

    def test_constructor_not_none(self):
        """id != None"""
        r = Rectangle(10, 2, id=23)
        self.assertEqual(r.id, 23)

    def test_constructor_not_none_inc(self):
        """increment nb_objects"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 8)

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

    def test_str__(self):
        """get set y attribute"""
        r = Rectangle(10, 2, 12, 13, id=10)
        st = r.__str__()
        self.assertEqual("[Rectangle] (10) 12/13 - 10/2", st)

    def test_display(self):
        """get set y attribute"""
        r = Rectangle(10, 2)
        st = r.display()
        self.assertEqual("##########\n##########", st)

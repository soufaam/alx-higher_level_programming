import unittest
from models.square import Square

"""unitest model for base class"""


class TestRectangleClass(unittest.TestCase):

    def test_constructor_none(self):
        """id == None"""
        r = Square(10, 2)
        self.assertEqual(r.id, 18)

    def test_constructor_not_none(self):
        """id != None"""
        r = Square(10, 2, id=23)
        self.assertEqual(r.id, 23)

    def test_constructor_not_none_inc(self):
        """increment nb_objects"""
        r = Square(10, 2)
        self.assertEqual(r.id, 19)

    def test_constructor_width(self):
        """get width attribute"""
        r = Square(10, 2)
        self.assertEqual(r.width, 10)

    def test_constructor_height(self):
        """get set width attribute"""
        r = Square(10, 2)

        self.assertEqual(r.height, 10)

    def test_constructor_setter_height(self):
        """get set width attribute"""
        r = Square(10, 2)
        r.size = 12

        self.assertEqual(r.height, 12)

    def test_constructor_setter_width(self):
        """get set width attribute"""
        r = Square(10, 2)
        r.size = 12
        self.assertEqual(r.width, 12)

    def test_constructor_getter_x(self):
        """get set x attribute"""
        r = Square(10, 2)
        self.assertEqual(r.x, 2)

    def test_constructor_getter_y(self):
        """get set width attribute"""
        r = Square(10, 2)
        self.assertEqual(r.y, 0)

    def test_constructor_setter_x(self):
        """get set x attribute"""
        r = Square(10, 2)
        r.x = 2023
        self.assertEqual(r.x, 2023)

    def test_constructor_getter_y(self):
        """get set y attribute"""
        r = Square(10, 2)
        r.y = 25
        self.assertEqual(r.y, 25)

    def test_str__(self):
        """get set y attribute"""
        r = Square(10, 2, 12, id=10)
        st = r.__str__()
        self.assertEqual("[Square] (10) 2/12 - 10", st)

    def test_display(self):
        """get set y attribute"""
        r = Square(2)
        st = r.display()
        self.assertEqual("##\n##", st)

    def test_update_val_x(self):
        """get set y attribute"""
        r = Square(10, 2, id=2)
        r.update(89, 1, 12, 98)
        st = r.to_dictionary()
        self.assertEqual({"size": 1,
                          "x": 12, "y": 98, "id": 89}, st)

    def test_update_val_y(self):
        """get set y attribute"""
        r = Square(10, 2, id=12)
        r.update(89, 98, 100)
        st = r.to_dictionary()
        self.assertEqual({"size": 98,
                          "x": 100, 'y': 0, "id": 89}, st)

    def test_update_val_create1(self):
        """get set y attribute"""
        r = Square.create(**{'id': 89, 'size': 1,
                             'x': 2, 'y': 3})
        st = r.to_dictionary()
        self.assertEqual({'id': 89, 'size': 1,
                          'x': 2, 'y': 3}, st)

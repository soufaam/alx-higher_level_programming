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

    def test_to_dict(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        st = r.to_dictionary()
        self.assertEqual({"width": 10, "height": 2,
                          "x": 0, "y": 0, "id": 12}, st)

    def test_update(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update()
        st = r.to_dictionary()
        self.assertEqual({"width": 10, "height": 2,
                          "x": 0, "y": 0, "id": 12}, st)

    def test_update_val(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(89)
        st = r.to_dictionary()
        self.assertEqual({"width": 10, "height": 2,
                          "x": 0, "y": 0, "id": 89}, st)

    def test_update_val_w(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(89, 1)
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 2,
                          "x": 0, "y": 0, "id": 89}, st)

    def test_update_val_h(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(89, 1, 12)
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 12,
                          "x": 0, "y": 0, "id": 89}, st)

    def test_update_val_x(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=2)
        r.update(89, 1, 12, 98)
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 12,
                          "x": 98, "y": 0, "id": 89}, st)

    def test_update_val_y(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(89, 1, 12, 98, 100)
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 12,
                          "x": 98, "y": 100, "id": 89}, st)

    def test_update_val_dict(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(**{'id': 89, 'width': 1})
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 2,
                          "x": 0, "y": 0, "id": 89}, st)

    def test_update_val_dict1(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(**{'id': 89, 'width': 1, 'height': 12})
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 12,
                          "x": 0, "y": 0, "id": 89}, st)

    def test_update_val_dict2(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(**{'id': 89, 'width': 1,
                    'height': 12, 'x': 3})
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 12,
                          "x": 3, "y": 0, "id": 89}, st)

    def test_update_val_dict2(self):
        """get set y attribute"""
        r = Rectangle(10, 2, id=12)
        r.update(**{'id': 89, 'width': 1, 'height': 12, 'x': 3, 'y': 4})
        st = r.to_dictionary()
        self.assertEqual({"width": 1, "height": 12,
                          "x": 3, "y": 4, "id": 89}, st)

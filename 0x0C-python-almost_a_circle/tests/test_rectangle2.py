import unittest
from models.rectangle import Rectangle

"""unitest model for base class"""


class TestBaseClass(unittest.TestCase):

    def test_w_attribute_not_in(self):
        """width not int"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle("12d", 2)
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_h_attribute_not_int(self):
        """height not int """

        with self.assertRaises(TypeError) as context:
            r = Rectangle(12, "2")
        self.assertTrue('height must be an integer' in str(context.exception))

    def test_x_attribute_not_int(self):
        """height not int """

        with self.assertRaises(TypeError) as context:
            r = Rectangle(12, 2, "23")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_y_attribute_not_int(self):
        """height not int """

        with self.assertRaises(TypeError) as context:
            r = Rectangle(12, 23, 23, "adsfdsa")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_w_attribute_ge0(self):
        """height not int """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 23, 23, )
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_h_attribute_ge0(self):
        """height not int """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(12, 0, 23)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_h_attribute_ge0(self):
        """height not int """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(12, 24, -1)
        self.assertTrue("x must be >= 0" in str(context.exception))

    def test_h_attribute_ge0(self):
        """height not int """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(12, 23, 13, y=-1, id=12)
        self.assertTrue("y must be >= 0" in str(context.exception))

    def test_no_args_not_int(self):
        """height not int """

        with self.assertRaises(Exception):
            r = Rectangle()

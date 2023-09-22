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

    def test_to_json_string_none(self):
        """Test of Base.to_json_string(None) exists"""

        b1 = Base()
        rt = b1.to_json_string(None)
        self.assertEqual(rt, '[]')

    def test_to_json_empty(self):
        """Test of Base.to_json_string(None) exists"""

        b1 = Base()
        rt = b1.to_json_string([])
        self.assertEqual(rt, '[]')

    def test_to_json_string_return_val(self):
        """Test of Base.to_json_string(None) exists"""

        self.assertEqual('[{"id": 12}]', Base.to_json_string([{'id': 12}]))

    def test_to_json_string_return_str(self):
        """Test of Base.to_json_string(None) exists"""

        df = Base.to_json_string([{'id': 12}])
        self.assertEqual('[{"id": 12}]', df)

    def test_from_json_string(self):
        """Test of Base.to_json_string(None) exists"""

        df = Base.from_json_string(None)
        self.assertEqual([], df)

    def test_from_json_string(self):
        """Test of Base.to_json_string(None) exists"""

        df = Base.from_json_string([])
        self.assertEqual([], df)

    def test_from_json_string(self):
        """Test of Base.to_json_string(None) exists"""

        df = Base.from_json_string(None)
        self.assertEqual([], df)

    def test_from_json_string_val(self):
        """Test of Base.to_json_string(None) exists"""

        df = Base.from_json_string('[{"id": 89}]')
        self.assertEqual([{"id": 89}], df)

    def test_from_json_string_(self):
        """Test of Base.to_json_string(None) exists"""

        df = Base.from_json_string('[{"id": 89}]')
        self.assertEqual([{"id": 89}], df)

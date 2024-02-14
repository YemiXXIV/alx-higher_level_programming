#!/usr/bin/python3

"""

Unittests for base.py

"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for Base class
    """

    def test_id_incrementation(self):
        """
        Test id incrementation
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b4.id - 3)

    def test_id_assign(self):
        """
        Test id assign
        """
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_if_instance_works(self):
        """
        Test if instance creation works perfectly
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_new_value(self):
        """
        Test new value
        """
        b = Base(10)
        b.id = 18
        self.assertEqual(b.id, 18)

    def test_nb_private_instance(self):
        """
        Test if private instance is accessible
        """
        with self.assertRaises(AttributeError):
            print(Base(14).__nb_instances)

    def test_str(self):
        self.assertEqual("hello", Base("hello").id)

    def test_instances_after_uniq_id(self):
        """
        Test instances id after unique aid was set
        """
        b_1 = Base()
        b_2 = Base(20)
        b_3 = Base()
        self.assertEqual(b_1.id, b_3.id - 1)

    def test_dict_id(self):
        """
        Test dictionary id
        """
        self.assertEqual({"a": 2, "b": 4}, Base({"a": 2, "b": 4}).id)

    def test_list_id(self):
        """
        Test list id
        """
        self.assertEqual([2, 4, 6], Base([2, 4, 6]).id)

    def test_boolean_id(self):
        self.assertEqual(True, Base(True).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(5, 6)

    def test_tuple_id(self):
        self.assertEqual((8, 12), Base((8, 12)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)


class Testbase_to_json_string(unittest.TestCase):
    """
    Unittest for json_string
    """
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(12, 5, 2, 7, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        sq = Square(5, 2, 3, 10)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

            
if __name__ == "__main__":
    unittest.main()

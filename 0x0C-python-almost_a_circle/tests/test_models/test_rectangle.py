#!/usr/bin/python3
""" identify the class TestRectangleMethods for the program """


from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """ example1:  identify the  tests for Rectangle class """

    @classmethod
    def setUp(self):
        """ example1: Runs each test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ example2:  Cleans up after individual test """
        pass

    def test_docstring(self):
        """ example3: the Test if docstring is present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_randos_id(self):
        """  example4: the test random arguments is passed """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)

    def test_class(self):
        """ example5: the  Test Rectangle class type """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_class_inheritance(self):
        """ example 6: make Test if Rectangle inherits from Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_arg_passed(self):
        """ example7: the Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle(20)
            Rectangle()

    def test_constructor_no_args(self):
        """ example8: the Test constructor that has no argument"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_one_arg(self):
        """ example9: the Test constructor has one argument """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_width_height_1(self):
        """example10: the Test for width and height types"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Chris", 9)
            Rectangle('c', 9)
            Rectangle(True, 8)
            self.assertEqual(str_out.getvalue(), result)

        r1.y = 2
        result = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_no_args(self):
        """ example18:the Test display method that has no arguments """
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_complex_display(self):
        """ example19 : the Test is  displayed """
        r1 = Rectangle(2, 2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.width = 6
        result = "######\n######\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """ example20 : the Test __str__ return will be the  value """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        result = "[Rectangle] (12) 2/1 - 4/6\n"
        result2 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(r2.__str__(), result2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_no_args(self):
        """ example21: the Test __str__ return value has no arguments """
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_update_args(self):
        """  example22: the Test that udpate method with *args """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """ example22: the Test  update method with **kwargs """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_to_dictonary_1(self):
        """example23 : the test to see if to_dictionary method is working"""
        r1 = Rectangle(10, 2, 1, 9)
        d1 = r1.to_dictionary()
        j1 = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        r2 = Rectangle(1, 1)
        d2 = r2.to_dictionary()
        j2 = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(d1, j1)
        self.assertEqual(d2, j2)
        self.assertEqual(type(d1), dict)
        self.assertEqual(type(d2), dict)

    def test_save_to_file_1(self):
        """ example24: the Test save_to_file_method with empty_file """
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_save_to_file_2(self):
        """ example25: the Test save_to_file method with None as file """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_save_to_file_3(self):
        """ example26: the Test save_to_file method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s2f = [r1, r2]
        Rectangle.save_to_file(s2f)
        rf = Rectangle.load_from_file()
        self.assertNotEqual(s2f, rf)

    def test_create(self):
        """example27: the Test create method """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (1) 1/0 - 3/5", str(r2))
        self.assertNotEqual(r1, r2)

    def test_load_from_file_1(self):
        """ example28: the Test load from file if file non-existent """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        Base._Base__nb_objects = 0
        lff = Rectangle.load_from_file()
        self.assertEqual(lff[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(lff[1].to_dictionary(), r2.to_dictionary())

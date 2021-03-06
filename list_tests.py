# Tests the list ADT.
# CSC 202, Lab 2
# Given tests, Summer '19

import unittest

# TODO: Leave one of these commented and one uncommented, depending on which
#       implementation you want to test.
#from array_list import *
from linked_list import *


class TestList(unittest.TestCase):
    def test00_shift(self):
        lst = List()
        add(lst, 0, 5)
        add(lst, 0, 4)
        add(lst, 0, 3)
        add(lst, 0, 2)
        add(lst, 0, 1)
        add(lst, 0, 0)
        remove(lst, 0)

        self.assertEqual(get(lst, 1), 1)
        self.assertEqual(get(lst, 3), 4)
    def test01_simple_list(self):
        lst = List()
        add(lst, 0, 0)
        add(lst, 1, 2)
        add(lst, 1, 0)
        set(lst, 1, 1)
        print(lst)

        self.assertEqual(size(lst), 3)
        self.assertEqual(get(lst, 1), 1)
        self.assertEqual(remove(lst, 1), 1)
        self.assertEqual(index(lst, 0), 0)
        self.assertEqual(remove(lst, 0), 0)


    def test_02_Equality(self):
        lst = List()
        lst2 = List()
        lst3 = List()
        lst4 = List()

        add(lst, 0, 2)
        add(lst, 1, 1)
        add(lst, 2, 2)
        remove(lst, 1)
        remove(lst, 1)
        add(lst2, 0, 2)
        add(lst2, 1, 1)
        add(lst2, 2, 2)
        remove(lst2, 1)
        remove(lst2, 1)
        add(lst2, 1, 1)
        add(lst2, 2, 2)
        remove(lst2, 1)
        remove(lst2, 1)
        add(lst4, 0, 1)
        add(lst4, 1, 1)
        add(lst4, 2, 2)
        remove(lst4, 1)
        remove(lst4, 1)

        print(lst == lst2)
        print(lst == lst3)
        print(lst == lst4)

    def test_03_Errors(self):
        lst = List()

        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        remove(lst, 2)

        self.assertRaises(ValueError, index, lst, 100)
        self.assertRaises(ValueError, index, lst, -5)
        self.assertRaises(IndexError, set, lst, 'z', 0)
        self.assertRaises(IndexError, set, lst, 200, 0)
        self.assertRaises(IndexError, set, lst, -1, 0)
        self.assertRaises(IndexError, remove, lst, 100)
        self.assertRaises(IndexError, remove, lst, -5)
        self.assertRaises(IndexError, add, lst, 2000, 5)
        self.assertRaises(IndexError, add, lst, -2, -2)
        self.assertRaises(IndexError, add, lst, 'z', 0)
        self.assertRaises(IndexError, get, lst, 'a')
        self.assertRaises(IndexError, get, lst, 20000)
        self.assertRaises(IndexError, get, lst, -2)




if __name__ == "__main__":
    unittest.main()

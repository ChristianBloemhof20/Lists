# Tests the list ADT.
# CSC 202, Lab 2
# Given tests, Summer '19

import unittest

# TODO: Leave one of these commented and one uncommented, depending on which
#       implementation you want to test.
from array_list import *
#from linked_list import *


class TestList(unittest.TestCase):
    def test01_simple_list(self):
        lst = List()

        add(lst, 0, 0)
        add(lst, 1, 2)
        add(lst, 1, 0)
        set(lst, 1, 1)

        self.assertEqual(size(lst), 3)
        self.assertEqual(get(lst, 1), 1)
        self.assertEqual(remove(lst, 1), 1)
        self.assertEqual(index(lst, 0), 0)
        print(lst)


    def test_02(self):
        lst = List()
        lst2 = List()
        lst3 = List()

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

        self.assertEqual(size(lst), 1)
        self.assertTrue(lst, lst2)
        self.assertNotEqual(lst, lst3)

    def test_03(self):
        lst = List()

        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)
        add(lst, 0, 0)

        self.assertRaises(ValueError, index, lst, 100)
        self.assertRaises(ValueError, index, lst, -5)
        self.assertRaises(ValueError, remove, lst, 100)
        self.assertRaises(ValueError, remove, lst, -5)
        self.assertRaises(IndexError, add, lst, 2000, 5)
        self.assertRaises(IndexError, add, lst, -2, -2)




if __name__ == "__main__":
    unittest.main()

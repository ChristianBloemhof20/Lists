# Tests the list ADT.
# CSC 202, Lab 2
# Given tests, Summer '19

import unittest

# TODO: Leave one of these commented and one uncommented, depending on which
#       implementation you want to test.
from array_list import *
# from linked_list import *


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


if __name__ == "__main__":
    unittest.main()

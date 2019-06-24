# Implements the list ADT using an array.
# CSC 202, Lab 2
# Given code, Summer '19


class List:
    """ An ordered collection of elements """

    def __init__(self, capacity = 16):
        # The backing array:
        self.array = [None] * capacity
        # The size of the backing array:
        self.capacity = capacity
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        # TODO: Implement this method.
        pass

    def __repr__(self):
        # TODO: Implement this method.
        pass


def size(lst):
    """
    Calculate the size of a list.
    TODO: Implement this function.

    :param lst: A List
    :return: The size of the list
    """
    pass


def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: An index into the list
    :return: The element in the list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    pass


def set(lst, idx, value):
    """
    Set the element at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: An index at which to place the value
    :param value: A value to place into the list
    :raise IndexError: If the index is out-of-bounds
    """
    pass


def index(lst, value):
    """
    Find the index of an element.
    TODO: Implement this function.

    :param lst: A List
    :param value: A value to find in the list
    :return: The index of the first occurrence of the value in the list
    :raise ValueError: If the value is not in the list
    """
    pass


def add(lst, idx, value):
    """
    Add a value to a list at an index. Double the capacity of the backing array
     first if necessary.
    TODO: Implement this function.

    :param lst: A List
    :param idx: The index at which to add the value -- note that the index may
                 be equal to the size of the list in this function.
    :param value: A value to add to the list
    :raise IndexError: If the index is out-of-bounds
    """
    pass


def remove(lst, idx):
    """
    Remove the value from a list at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: The index at which to remove a value
    :raise IndexError: If the index is out-of-bounds
    :return: The value that was removed
    """
    pass

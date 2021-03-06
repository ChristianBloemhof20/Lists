# Implements the list ADT using an array.
# CSC 202, Lab 2
# Given code, Summer '19


class List:
    """ An ordered collection of elements """

    def __init__(self, capacity = 4):
        # The backing array:
        self.array = [None] * capacity
        # The size of the backing array:
        self.capacity = capacity
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        # TODO: Implement this method.
        if type(self) == type(other) and self.size == other.size:
            for i in range(self.size):
                if self.array[i] != other.array[i]:
                    return False
            return True
        else:
            return False

    def __repr__(self):
        # TODO: Implement this method.
        return 'List(Size = {}, Capacity = {}, Array: {})'.format(self.size, self.capacity, self.array)


def size(lst):
    """
    Calculate the size of a list.
    TODO: Implement this function.

    :param lst: A List
    :return: The size of the list
    """
    size = lst.size
    return size


def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: An index into the list
    :return: The element in the list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if type(idx) == str:
        raise IndexError
    elif idx > lst.capacity or idx < 0:
        raise IndexError
    value = lst.array[idx]
    return value


def set(lst, idx, value):
    """
    Set the element at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: An index at which to place the value
    :param value: A value to place into the list
    :raise IndexError: If the index is out-of-bounds
    """
    if type(idx) == str:
        raise IndexError
    if idx > lst.capacity or idx < 0:
        raise IndexError
    lst.array[idx] = value
    return lst.array[idx]


def index(lst, value):
    """
    Find the index of an element.
    TODO: Implement this function.

    :param lst: A List
    :param value: A value to find in the list
    :return: The index of the first occurrence of the value in the list
    :raise ValueError: If the value is not in the list
    """
    for i in range(lst.size):
        if lst.array[i] == value:
            return i
    raise ValueError



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
    if lst.size >= lst.capacity:
        n_lst = List(2*lst.capacity)
        for i in range(lst.size):
            n_lst.array[i] = lst.array[i]
        lst.array = n_lst.array
        lst.capacity *= 2
    elif type(idx) == str:
        raise IndexError
    elif idx < 0:
        raise IndexError
    temp = lst.array[idx]
    for i in range(idx, lst.size):
        temp2 = lst.array[i + 1]
        lst.array[i + 1] = temp
        temp = temp2
    lst.array[idx] = value
    lst.size += 1
    return lst


def remove(lst, idx):
    """
    Remove the value from a list at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: The index at which to remove a value
    :raise IndexError: If the index is out-of-bounds
    :return: The value that was removed
    """

    if idx < 0 or idx > lst.capacity:
        raise IndexError
    value = lst.array[idx]
    for i in range(idx + 1, lst.size):
        lst.array[i - 1] = lst.array[i]
    lst.size -= 1
    return value

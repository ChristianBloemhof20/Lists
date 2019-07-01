# Implements the list ADT using a linked list.
# CSC 202, Lab 2
# Given code, Summer '19


class List:
    """ An ordered collection of elements """

    def __init__(self, head = None, size = 0):
        # The head of the backing linked list:
        self.head = head
        # The number of elements in this list:
        self.size = size

    def __eq__(self, other):
        # TODO: Implement this method.
        return type(self) == type(other) and \
               self.size == other.size and \
               self.head == other.head

    def __repr__(self):
        # TODO: Implement this method.
        return 'List(Head = {}, Size = {})'.format(self.head, self.size)


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next

    def __eq__(self, other):
        # TODO: Implement this method.
        return type(self) == type(other) and \
               self.value == other.value and \
               self.next == other.next

    def __repr__(self):
        # TODO: Implement this method.
        return 'Node(Value = {}, Next = {}'.format(self.value, self.next)


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
    cur = lst.head
    for i in range(idx - 1):
        cur = cur.next
    value = lst.next
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
    cur = lst.head
    for i in range(idx - 1):
        cur = cur.next
    cur = value
    return cur


def index(lst, value):
    """
    Find the index of an element.
    TODO: Implement this function.

    :param lst: A List
    :param value: A value to find in the list
    :return: The index of the first occurrence of the value in the list
    :raise ValueError: If the value is not in the list
    """
    try:
        for i in range(len(lst)):
            if lst.value[i] == value:
                return i
            else:
                raise ValueError
    except ValueError:
        return False


def add(lst, idx, value):
    """
    Add a value to a list at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: The index at which to add the value -- note that the index may
                 be equal to the size of the list in this function.
    :param value: A value to add to the list
    :raise IndexError: If the index is out-of-bounds
    """
    try:
        if idx == 0:
            lst.next = lst.head
            lst.head = value
        elif idx > lst.size or idx < 0:
            raise ValueError
        else:
            for i in range(idx - 1):
                lst.next[idx] = lst.next[idx - 1]
                lst.next[idx - 1] = lst.value[idx]
        lst.size += 1
        return lst
    except ValueError:
        return False


def remove(lst, idx):
    """
    Remove the value from a list at an index.
    TODO: Implement this function.

    :param lst: A List
    :param idx: The index at which to remove a value
    :raise IndexError: If the index is out-of-bounds
    :return: The value that was removed
    """
    try:
        if idx == 0:
            lst.head = lst.next
        elif idx > lst.size or idx < 0:
            raise ValueError
        else:
            for i in range(len(lst)):
                if i == (idx - 1):
                    lst.next[idx-1] = lst.next[idx]
        lst.size -= 1
        return lst.value[idx]
    except ValueError:
        print("The index is out-of-bounds")
        return lst


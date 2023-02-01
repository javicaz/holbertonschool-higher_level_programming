#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize data"""

    @property
    def size(self):
        """Pulls the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

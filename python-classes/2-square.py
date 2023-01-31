#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """starts data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

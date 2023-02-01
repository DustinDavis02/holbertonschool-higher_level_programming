#!/usr/bin/python3
"""
inherits the rectangle class to make a square class (equal sides)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle
    """
    def __init__(self, size):
        """
        initializes size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
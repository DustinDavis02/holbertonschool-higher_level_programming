#!/usr/bin/python3
"""
inherits from square to add area
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from retangle to get all equal sides
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method to calculate area of the square
        """

        return self.__size * self.__size

    def __str__(self):
        """
        print square description
        """

        return "[Square] {}/{}".format(self.__size, self.__size)

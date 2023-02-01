#!/usr/bin/python3
"""
inherits from BaseGeometry with width and height and area implemented
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
 inherits from BaseGeometry
"""

def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

def area(self):
        """Method that calculates area of rectangle
        """
        
        return self.__width * self.__height

def __str__(self):
        """
       return rectangle desc
        """
        
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
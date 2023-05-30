#!/usr/bin/python3
"""Imported from parent class BaseGeometry, and adds height and width"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """import from BaseGeometry"""
    def __init__(self, width, height):
        """
        checks to make sure height and width and correct
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

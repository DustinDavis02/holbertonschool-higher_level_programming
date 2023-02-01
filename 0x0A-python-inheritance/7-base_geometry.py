#!/usr/bin/python3
"""
Contains BaseGeometry
public instance method area and integer_validation
"""


class BaseGeometry:
    """
    empty class
    """
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        makes sure we are putting in correct data
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
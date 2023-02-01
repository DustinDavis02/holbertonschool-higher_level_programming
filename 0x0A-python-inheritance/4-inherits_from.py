#!/usr/bin/python3
"""
Checks direct or indirect class
"""


def inherits_from(obj, a_class):
    """
    Function that returns if the object is an part of class or subclass
    """

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
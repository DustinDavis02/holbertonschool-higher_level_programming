#!/usr/bin/python3
"""
Adding to integers (a + b)
"""


def add_integer(a, b=98):
    """
    Gives some of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
    
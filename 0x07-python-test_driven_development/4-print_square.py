#!/usr/bin/python3
"""
prints square according to input parameter
"""


def print_square(size):
    """
    Takes the user input and prints a square out of #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
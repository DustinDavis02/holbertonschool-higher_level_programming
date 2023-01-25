#!/usr/bin/python3
"""
Function that takes in 2 strings and prints first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints out First and last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
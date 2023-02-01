#!/usr/bin/python3
"""
Takes a readfile and displays it
"""


def read_file(filename=""):
    """
    Takes in filename to read it
    """

    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end='')
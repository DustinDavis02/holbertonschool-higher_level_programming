#!/usr/bin/python3
"""
Takes a readfile and displays it
"""

def read_file(filename=""):
    """Takes in filename to read and prints its content to the console."""
    with open(filename, encoding="utf-8") as read_file:
        print(read_file.read(), end='')
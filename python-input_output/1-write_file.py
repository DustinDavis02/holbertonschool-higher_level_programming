#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        write = f.write(text)

    return (write)

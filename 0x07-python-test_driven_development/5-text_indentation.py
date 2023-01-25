#!/usr/bin/python3
"""
Prints 2 newlines after '.,?,:'
"""


def text_indentation(text):
    """
    Prints input text with 2 new lines after our edgecases
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end='')
        if i in ".?:":
            print("\n" * 2)
    print("")
#!/usr/bin/python3
"""
Prints 2 newlines after '.,?,:'
"""


def text_indentation(text):
    """
    Prints input text with 2 new lines after our edgecases
    """
    if (type(text) is not str or text is None):
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if (c == '.' or c == '?' or c == ':'):
            print(c, end='')
            print('')
            print('')
            flag = 1
        else:
            if (flag == 0):
                print(c, end='')
            else:
                if (c == ' ' or c == '\t'):
                    pass
                else:
                    print(c, end="")
                    flag = 0
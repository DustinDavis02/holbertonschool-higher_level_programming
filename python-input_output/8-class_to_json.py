#!/usr/bin/python3
"""returns description of an object"""


def class_to_json(obj):
    """Returns description of JSON object."""
    return vars(obj)

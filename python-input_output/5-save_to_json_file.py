#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """save object to a file"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))

#!/usr/bin/python3

import sys
from typing import List
from os import path
from json import dump

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_arguments_to_list(args: List[str]) -> List[str]:
    filename = "add_item.json"
    my_list = []

    if path.exists(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(args)
    save_to_json_file(my_list, filename)

    return my_list

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)

#!/usr/bin/python3
"""Load, add and save date to a file"""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
from sys import argv 

args = argv[1:]
try:
    my_obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    objs = args
else:
    objs = my_obj + args
finally:
    save_to_json_file(objs, "add_item.json")
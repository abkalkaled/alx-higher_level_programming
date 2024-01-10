#!/usr/bin/python3
"""
    save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file in json representation
    """
    with open(filename, "w", encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)

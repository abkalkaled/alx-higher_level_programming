#!/usr/bin/python3
"""
    load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
        function that creates an object from JSON file
    """
    with open(filename, "r", encoding='utf-8') as json_source:
        return json.load(json_source)

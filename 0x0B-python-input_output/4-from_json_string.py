#!/usr/bin/python3
"""
    from_json_string
"""


import json


def from_json_string(my_str):
    """
        function that returns an objected represented by JSON
    """
    return json.loads(my_str)

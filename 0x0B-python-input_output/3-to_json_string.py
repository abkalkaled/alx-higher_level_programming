#!/usr/bin/python3
"""
    json_string(my_obj)
"""


import json



def to_json_string(my_obj):
    """
        function that returns JSON encryption of an object
    """
    return json.dumps(my_obj)

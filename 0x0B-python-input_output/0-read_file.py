#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


def read_file(filename=""):
    """
        function to read text file in UTF-8 and print to stdout
    """
    with open(filename, "r", encoding='utf-8') as my_text_file:
        print("{}".format(my_text_file.read()), end="")

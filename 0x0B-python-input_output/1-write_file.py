#!/usr/bin/python3
"""
    writes string to text file
"""


def write_file(filename="", text=""):
    """
        function that writes a string of textfile and returnd num of charcter
    """
    with open(filename, "w", encoding='utf-8') as text_file:
        return text_file.write(text)

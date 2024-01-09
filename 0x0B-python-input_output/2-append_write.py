#!/usr/bin/python3
"""
    2-append_write
"""


def append_write(filename="", text=""):
    """
        function to append string at end of text file & returns num of xter
    """
    with open(filename, "a", encoding='utf-8') as append_file:
        return append_file.write(text)

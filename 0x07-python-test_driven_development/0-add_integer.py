#!/usr/bin/python3
"""
    0-add_integer: add_integer()
"""


def add_integer(a, b=98):
    """
        add_integer returns the sum of two integers
        Args:
            a: first num.
            b: second num.
        Returns:
            the sum of the two numbers
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

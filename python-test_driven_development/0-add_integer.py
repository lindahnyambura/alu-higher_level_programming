#!/usr/bin/python3
"""
This module contains a function that adds two numbers.

The function ensures type checking and appropriate type conversions.
"""

def add_integer(a, b=98):
    """
    Returns the sum of a and b.
    If either of a or b is not an integer or float, a TypeError is raised.
    If a or b are floats, they're first casted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


#!/usr/bin/python3
"""
Defines a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list containing the names of attributes
    and methods available for an object.
    """
    return dir(obj)


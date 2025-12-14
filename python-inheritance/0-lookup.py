#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that returns the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of all attributes and methods of an object.

    The list includes both inherited attributes/methods and those
    defined directly on the object or its class.

    Args:
        obj: The object whose attributes and methods are to be inspected.

    Returns:
        list: A list object containing the names of the attributes and methods.
    """
    return dir(obj)

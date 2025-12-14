#!/usr/bin/python3
"""Module that provides a function to return attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods of the object.
    """
    return dir(obj)

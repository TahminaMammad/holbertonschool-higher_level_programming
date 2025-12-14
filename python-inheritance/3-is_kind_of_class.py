#!/usr/bin/python3
"""Check if an object is an instance or a subclass of a class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or subclass of a_class, else False."""
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object.

    The dictionary contains all serializable attributes of the object:
    lists, dictionaries, strings, integers, and booleans.
    """
    return obj.__dict__

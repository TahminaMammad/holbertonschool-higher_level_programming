#!/usr/bin/python3
"""Defines a Student class with JSON serialization and reloading."""
 

class Student:
    """Class that defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with names in this
        list are included. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for key in attrs:
                if hasattr(self, key):
                    filtered[key] = getattr(self, key)
            return filtered
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Keys must be public attribute names and values their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)

#!/usr/bin/python3
"""Defines a Student class with JSON serialization and filtering."""


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
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

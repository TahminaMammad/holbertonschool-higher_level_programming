#!/usr/bin/python3
"""
This module defines a BaseGeometry class used as a base
for geometry-related objects.
"""


class BaseGeometry:
    """
    This class provides basic geometric methods that
    can be extended by other geometry classes.
    """

    def area(self):
        """
        Raises an exception because the area method
        is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


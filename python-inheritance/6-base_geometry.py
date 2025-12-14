#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Class for geometry operations."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

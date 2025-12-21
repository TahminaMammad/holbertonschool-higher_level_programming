#!/usr/bin/env python3
"""
Pickling Custom Classes
This module defines a CustomObject class that can be serialized and deserialized
using the pickle module.
"""

import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serialize the current instance and save it to the provided filename.

        Args:
            filename (str): The file to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize an object from the provided filename.

        Args:
            filename (str): The file to load the serialized object from.

        Returns:
            CustomObject | None: The deserialized object or None if error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None

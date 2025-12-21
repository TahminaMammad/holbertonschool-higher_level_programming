#!/usr/bin/env python3
"""
XML Serialization Module
Provides functions to serialize a Python dictionary to XML
and deserialize XML back into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Write XML tree to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The filename to read the XML data from.

    Returns:
        dict: The deserialized dictionary, or None if error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct dictionary from XML elements
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except Exception:
        return None

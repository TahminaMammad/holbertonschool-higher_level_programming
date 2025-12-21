#!/usr/bin/env python3
"""
CSV to JSON Conversion Module
Reads data from a CSV file and converts it into JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data into JSON format and save to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # Read CSV file using DictReader
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Serialize to JSON and write to data.json
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False

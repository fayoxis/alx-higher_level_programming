#!/usr/bin/python3
"""Module for loading, adding, and saving arguments to a Python list"""
from sys import argv
import json


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def save_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

try:
    json_list = load_from_json_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_to_json_file(json_list, 'add_item.json')

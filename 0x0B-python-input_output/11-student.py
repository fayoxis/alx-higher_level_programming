#!/usr/bin/python3
"""
This module defines the Student class based on the 10-student.py module.
"""

class Student:
    """
    A class that represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list will be retrieved. Otherwise, all attributes will be retrieved.

        Args:
            attrs (list[str], optional): A list of attribute names to retrieve.
                Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        while attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except KeyError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the given JSON.

        Args:
            json (dict): A dictionary representation of the Student instance.
        """
        self.__dict__.update(json)

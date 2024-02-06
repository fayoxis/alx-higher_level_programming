#!/usr/bin/python3
"""
Module 10-student.py
"""


class Student:
    """
    Class that defines the properties of a student.

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
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list will be retrieved. Otherwise, all attributes will be retrieved.

        Args:
            attrs (list): A list of attribute names (optional).

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
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary representing the Student instance.
        """
        self.__dict__.update(json)

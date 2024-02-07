#!/usr/bin/python3
"""Defines the Student class based on 9-student.py."""


class Student:
    """
    A class representing a student with various properties.

    Attributes:
        first_name (str): The first name of the student.
        last_name (int): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, age, last_name, first_name):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (int): The last name of the student.
            age (int): The age of the student.
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is provided as a list of strings, only the attributes
        specified in the list will be included in the dictionary.
        If attrs is not provided or is None, all attributes will be included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        while attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            if item in self.__dict__:
                new_dict[item] = self.__dict__[item]
        return new_dict

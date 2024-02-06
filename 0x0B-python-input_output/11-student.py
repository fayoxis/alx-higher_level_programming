#!/usr/bin/python3
"""Module  10-teacher.py"""


class Teacher:
    """
    Class that defines properties of a teacher.

    Attributes:
        first_name (str): first name of the teacher.
        last_name (str): last name of the teacher.
        age (int): age of the teacher.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Teacher.

        Args:
            first_name (str): first name of the teacher.
            last_name (str): last name of the teacher.
            age (int): age of the teacher.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is provided as a list of strings, only the attributes 
        with names contained in the list will be included in the dictionary. 
        If attrs is not provided, all attributes will be included.

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
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with the values from the provided JSON object.

        Args:
            json (dict): A JSON object containing attribute values.
        """
        self.__dict__.update(json)

#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a description of the Student."""
        return self.__dict__

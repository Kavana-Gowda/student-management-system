"""
File: student.py
Description:
Defines the Student model class.

This class acts as a blueprint for creating student objects.
It stores student information and provides a method to convert
the object data into tuple format for database insertion.
"""


class Student:
    """
    Represents a student entity in the system.

    Attributes:
        name (str): Student's full name
        age (int): Student's age
        gender (str): Gender of the student
        parent_name (str): Name of the parent/guardian
        address (str): Residential address
        mobile (str): Contact number
        school_details (str): Previous school information
        year (int): Current academic year (1-4)
    """

    def __init__(self, name, age, gender, parent_name,
                 address, mobile, school_details, year):
        """
        Initializes a Student object with all required attributes.
        """

        self.name = name
        self.age = age
        self.gender = gender
        self.parent_name = parent_name
        self.address = address
        self.mobile = mobile
        self.school_details = school_details
        self.year = year

    def to_tuple(self):
        """
        Converts the Student object into tuple format.

        This is used for executing SQL INSERT queries.
        Order must match the database table column order.
        """

        return (
            self.name,
            self.age,
            self.gender,
            self.parent_name,
            self.address,
            self.mobile,
            self.school_details,
            self.year
        )
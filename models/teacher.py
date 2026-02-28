"""
File: teacher.py
Description:
Defines the Teacher model class.

This class represents a teacher entity and provides
a method to convert object data into tuple format
for database insertion.
"""


class Teacher:
    """
    Represents a teacher entity in the system.

    Attributes:
        name (str): Teacher's full name
        gender (str): Gender of the teacher
        address (str): Residential address
        mobile (str): Contact number
        joining_date (date): Date the teacher joined the institution
    """

    def __init__(self, name, gender, address, mobile, joining_date):
        """
        Initializes a Teacher object with required attributes.
        """

        self.name = name
        self.gender = gender
        self.address = address
        self.mobile = mobile
        self.joining_date = joining_date

    def to_tuple(self):
        """
        Converts the Teacher object into tuple format.

        This ensures the correct order of values for
        SQL INSERT operations.
        """

        return (
            self.name,
            self.gender,
            self.address,
            self.mobile,
            self.joining_date
        )
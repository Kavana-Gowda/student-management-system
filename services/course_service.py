"""
File: course_service.py
Description:
Handles all course-related operations such as:
- Adding a new course
- Viewing available courses

This module interacts directly with the database layer.
"""

from database import Database


class CourseService:
    """
    Service class responsible for managing course operations.
    """

    def __init__(self):
        # Initialize database connection
        self.db = Database()
        self.conn = self.db.get_connection()

    def add_course(self):
        """
        Adds a new course to the database.

        Takes input from user for:
        - Course name
        - Course duration (in years)
        """

        # Collect course details from user
        name = input("Course Name: ")
        duration = int(input("Duration (years): "))

        query = """
        INSERT INTO courses (course_name, duration)
        VALUES (%s, %s)
        """

        cursor = self.conn.cursor()

        # Insert new course into database
        cursor.execute(query, (name, duration))

        # Commit transaction to save changes
        self.conn.commit()

        print("Course added successfully!")

    def view_courses(self):
        """
        Retrieves and displays all courses available in the system.
        """

        cursor = self.conn.cursor()

        # Fetch all course records
        cursor.execute("SELECT * FROM courses")
        results = cursor.fetchall()

        if not results:
            print("No courses found.")
            return

        # Display each course record
        for row in results:
            print(row)
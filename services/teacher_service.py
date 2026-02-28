"""
File: teacher_service.py
Description:
Handles all teacher-related operations such as:
- Adding a teacher
- Viewing all active teachers
- Soft deleting a teacher

Business Rules Implemented:
- Teacher can only be deleted if they have worked for at least 30 days.
- Soft delete is used instead of permanent deletion.
"""

from database import Database
from models.teacher import Teacher
from datetime import datetime


class TeacherService:
    """
    Service class responsible for managing teacher operations.
    Interacts directly with the database.
    """

    def __init__(self):
        # Initialize database connection
        self.db = Database()
        self.conn = self.db.get_connection()

    def add_teacher(self, teacher: Teacher):
        """
        Adds a new teacher to the database.

        Parameters:
        teacher (Teacher): Teacher object containing teacher details.
        """

        query = """
        INSERT INTO teachers
        (name, gender, address, mobile, joining_date)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor = self.conn.cursor()

        # Insert teacher data using Teacher model's tuple format
        cursor.execute(query, teacher.to_tuple())

        # Commit transaction to save changes
        self.conn.commit()

        print("Teacher added successfully!")

    def view_all_teachers(self):
        """
        Displays all teachers who are not soft deleted.
        """

        query = """
        SELECT * FROM teachers
        WHERE is_deleted = FALSE
        """

        cursor = self.conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No teachers found.")
            return

        # Display each teacher record
        for row in results:
            print(row)

    def delete_teacher(self, teacher_id):
        """
        Performs soft delete on a teacher.

        Business Rule:
        - Teacher must have worked for at least 30 days
          before being eligible for deletion.
        """

        cursor = self.conn.cursor()

        # Check if teacher exists and is not already deleted
        cursor.execute(
            "SELECT joining_date FROM teachers WHERE id=%s AND is_deleted=FALSE",
            (teacher_id,)
        )

        result = cursor.fetchone()

        if not result:
            print("Teacher not found!")
            return

        joining_date = result[0]

        # Calculate number of days teacher has worked
        days_worked = (datetime.today().date() - joining_date).days

        # Enforce business rule: minimum 30 days work required
        if days_worked < 30:
            print("Teacher must work at least 1 month before deletion!")
            return

        # Perform soft delete
        cursor.execute(
            "UPDATE teachers SET is_deleted=TRUE WHERE id=%s",
            (teacher_id,)
        )

        # Commit changes
        self.conn.commit()

        print("Teacher deleted successfully (Soft Delete).")
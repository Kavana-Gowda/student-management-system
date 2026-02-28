"""
File: student_service.py
Description:
Handles all student-related database operations such as:
- Adding a new student
- Viewing student details
- Updating student information
- Soft deleting a student

Business Rules Implemented:
- Student name cannot be updated
- Soft delete is used instead of permanent delete
"""

from database import Database
from models.student import Student


class StudentService:
    """
    Service class responsible for managing student operations.
    Interacts directly with the database layer.
    """

    def __init__(self):
        # Initialize database connection
        self.db = Database()
        self.conn = self.db.get_connection()

    def add_student(self, student: Student):
        """
        Adds a new student to the database.

        Parameters:
        student (Student): Student object containing student details.
        """

        query = """
        INSERT INTO students
        (name, age, gender, parent_name, address, mobile, school_details, year)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor = self.conn.cursor()

        # Insert student data using tuple conversion from Student model
        cursor.execute(query, student.to_tuple())

        # Commit transaction to save changes
        self.conn.commit()

        print("Student added successfully!")

    def view_student(self, student_id):
        """
        Retrieves and displays student details based on student ID.
        Only displays students who are not soft deleted.
        """

        query = """
        SELECT * FROM students
        WHERE id = %s AND is_deleted = FALSE
        """

        cursor = self.conn.cursor()
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()

        if result:
            print("\n--- Student Details ---")
            print("ID:", result[0])
            print("Name:", result[1])
            print("Age:", result[2])
            print("Gender:", result[3])
            print("Parent Name:", result[4])
            print("Address:", result[5])
            print("Mobile:", result[6])
            print("School:", result[7])
            print("Year:", result[8])
        else:
            print("Student not found!")

    def update_student(self, student_id):
        """
        Updates student details except for the student's name.

        Business Rule:
        - Student name cannot be modified once created.
        - Only active (non-deleted) students can be updated.
        """

        # First verify that student exists and is not deleted
        check_query = """
        SELECT * FROM students
        WHERE id = %s AND is_deleted = FALSE
        """

        cursor = self.conn.cursor()
        cursor.execute(check_query, (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found!")
            return

        print("\n--- Enter New Details (Name cannot be changed) ---")

        # Collect updated values from user
        age = int(input("Age: "))
        gender = input("Gender: ")
        parent_name = input("Parent Name: ")
        address = input("Address: ")
        mobile = input("Mobile: ")
        school_details = input("School Details: ")
        year = int(input("Year (1-4): "))

        update_query = """
        UPDATE students
        SET age=%s, gender=%s, parent_name=%s,
            address=%s, mobile=%s, school_details=%s, year=%s
        WHERE id=%s
        """

        # Execute update query
        cursor.execute(update_query, (
            age, gender, parent_name,
            address, mobile, school_details, year, student_id
        ))

        # Commit changes to database
        self.conn.commit()

        print("Student updated successfully!")

    def delete_student(self, student_id):
        """
        Performs soft delete on a student.

        Instead of permanently deleting the record,
        the system sets is_deleted = TRUE.

        Business Rule:
        - Deleted students are hidden from normal queries.
        """

        check_query = """
        SELECT * FROM students
        WHERE id = %s AND is_deleted = FALSE
        """

        cursor = self.conn.cursor()
        cursor.execute(check_query, (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found or already deleted!")
            return

        delete_query = """
        UPDATE students
        SET is_deleted = TRUE
        WHERE id = %s
        """

        # Perform soft delete
        cursor.execute(delete_query, (student_id,))

        # Commit deletion
        self.conn.commit()

        print("Student deleted successfully (Soft Delete)!")
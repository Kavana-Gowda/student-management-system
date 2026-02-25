from database import Database
from models.student import Student


class StudentService:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def add_student(self, student: Student):
        query = """
        INSERT INTO students
        (name, age, gender, parent_name, address, mobile, school_details, year)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor = self.conn.cursor()
        cursor.execute(query, student.to_tuple())
        self.conn.commit()

        print("Student added successfully!")
    def view_student(self, student_id):
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
        # First check if student exists
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

        cursor.execute(update_query, (
            age, gender, parent_name,
            address, mobile, school_details, year, student_id
        ))

        self.conn.commit()
        print("Student updated successfully!")
    def delete_student(self, student_id):
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

        cursor.execute(delete_query, (student_id,))
        self.conn.commit()

        print("Student deleted successfully (Soft Delete)!")
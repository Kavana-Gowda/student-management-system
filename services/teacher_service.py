from database import Database
from models.teacher import Teacher
from datetime import datetime


class TeacherService:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def add_teacher(self, teacher: Teacher):
        query = """
        INSERT INTO teachers
        (name, gender, address, mobile, joining_date)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor = self.conn.cursor()
        cursor.execute(query, teacher.to_tuple())
        self.conn.commit()

        print("Teacher added successfully!")

    def view_all_teachers(self):
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

        for row in results:
            print(row)

    def delete_teacher(self, teacher_id):
        cursor = self.conn.cursor()

        cursor.execute("SELECT joining_date FROM teachers WHERE id=%s AND is_deleted=FALSE", (teacher_id,))
        result = cursor.fetchone()

        if not result:
            print("Teacher not found!")
            return

        joining_date = result[0]
        days_worked = (datetime.today().date() - joining_date).days

        if days_worked < 30:
            print("Teacher must work at least 1 month before deletion!")
            return

        cursor.execute("UPDATE teachers SET is_deleted=TRUE WHERE id=%s", (teacher_id,))
        self.conn.commit()

        print("Teacher deleted successfully (Soft Delete).")
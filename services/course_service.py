from database import Database


class CourseService:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def add_course(self):
        name = input("Course Name: ")
        duration = int(input("Duration (years): "))

        query = """
        INSERT INTO courses (course_name, duration)
        VALUES (%s, %s)
        """

        cursor = self.conn.cursor()
        cursor.execute(query, (name, duration))
        self.conn.commit()

        print("Course added successfully!")

    def view_courses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses")
        results = cursor.fetchall()

        if not results:
            print("No courses found.")
            return

        for row in results:
            print(row)


from services.student_service import StudentService
from models.student import Student


def add_student():
    print("\n--- Add Student ---")

    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    parent_name = input("Parent Name: ")
    address = input("Address: ")
    mobile = input("Mobile: ")
    school_details = input("School Details: ")
    year = int(input("Year (1-4): "))

    student = Student(
        name, age, gender, parent_name,
        address, mobile, school_details, year
    )

    service = StudentService()
    service.add_student(student)


def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Manage Teachers")
        print("6. Manage Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            service = StudentService()
            service.view_student(student_id)

        elif choice == "3":
            student_id = int(input("Enter Student ID to update: "))
            service = StudentService()
            service.update_student(student_id)

        elif choice == "4":
            student_id = int(input("Enter Student ID to delete: "))
            service = StudentService()
            service.delete_student(student_id)

        elif choice == "5":
            manage_teachers()

        elif choice == "6":
            manage_courses()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

from services.teacher_service import TeacherService
from models.teacher import Teacher


def manage_teachers():
    service = TeacherService()

    while True:
        print("\n--- Teacher Management ---")
        print("1. Add Teacher")
        print("2. View All Teachers")
        print("3. Delete Teacher")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            gender = input("Gender: ")
            address = input("Address: ")
            mobile = input("Mobile: ")
            joining_date = input("Joining Date (YYYY-MM-DD): ")

            teacher = Teacher(name, gender, address, mobile, joining_date)
            service.add_teacher(teacher)

        elif choice == "2":
            service.view_all_teachers()

        elif choice == "3":
            teacher_id = int(input("Enter Teacher ID to delete: "))
            service.delete_teacher(teacher_id)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

from services.course_service import CourseService


def manage_courses():
    service = CourseService()

    while True:
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            service.add_course()

        elif choice == "2":
            service.view_courses()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()

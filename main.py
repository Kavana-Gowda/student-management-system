"""
File: main.py
Description:
This is the entry point of the Student Management System.

It provides a CLI (Command Line Interface) menu that allows users to:
- Manage students
- Manage teachers
- Manage courses

This file connects service layers with user interaction.
"""

# Import Student-related services and models
from services.student_service import StudentService
from models.student import Student


def add_student():
    """
    Collects student details from user input
    and calls StudentService to insert into database.
    """

    print("\n--- Add Student ---")

    # Collect student details
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    parent_name = input("Parent Name: ")
    address = input("Address: ")
    mobile = input("Mobile: ")
    school_details = input("School Details: ")
    year = int(input("Year (1-4): "))

    # Create Student object
    student = Student(
        name, age, gender, parent_name,
        address, mobile, school_details, year
    )

    # Call service layer to insert into database
    service = StudentService()
    service.add_student(student)


def menu():
    """
    Main menu loop for the system.
    Displays available options and routes user
    to the appropriate functionality.
    """

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
            # View student details by ID
            student_id = int(input("Enter Student ID: "))
            service = StudentService()
            service.view_student(student_id)

        elif choice == "3":
            # Update student details (name cannot be changed)
            student_id = int(input("Enter Student ID to update: "))
            service = StudentService()
            service.update_student(student_id)

        elif choice == "4":
            # Soft delete student
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


# Import Teacher-related services and models
from services.teacher_service import TeacherService
from models.teacher import Teacher


def manage_teachers():
    """
    Provides submenu for managing teachers.
    Includes adding, viewing, and deleting teachers.
    """

    service = TeacherService()

    while True:
        print("\n--- Teacher Management ---")
        print("1. Add Teacher")
        print("2. View All Teachers")
        print("3. Delete Teacher")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            # Collect teacher details
            name = input("Name: ")
            gender = input("Gender: ")
            address = input("Address: ")
            mobile = input("Mobile: ")
            joining_date = input("Joining Date (YYYY-MM-DD): ")

            # Create Teacher object
            teacher = Teacher(name, gender, address, mobile, joining_date)

            # Call service layer
            service.add_teacher(teacher)

        elif choice == "2":
            # Display all active teachers
            service.view_all_teachers()

        elif choice == "3":
            # Soft delete teacher (only if worked 30+ days)
            teacher_id = int(input("Enter Teacher ID to delete: "))
            service.delete_teacher(teacher_id)

        elif choice == "4":
            # Return to main menu
            break

        else:
            print("Invalid choice!")


# Import Course service
from services.course_service import CourseService


def manage_courses():
    """
    Provides submenu for managing courses.
    Includes adding and viewing courses.
    """

    service = CourseService()

    while True:
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            # Add new course
            service.add_course()

        elif choice == "2":
            # Display all courses
            service.view_courses()

        elif choice == "3":
            # Return to main menu
            break

        else:
            print("Invalid choice!")


# Entry point of the application
if __name__ == "__main__":
    menu()
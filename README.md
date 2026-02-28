#  Student Management System

A CLI-based Student Management System built using **Python** and **MySQL**.

This project manages students, teachers, and courses with proper relational database design and business rule enforcement.

---

##  Features

###  Student Module
- Add new student
- View student details
- Update student information (Name cannot be updated)
- Soft delete student (is_deleted flag)
- Assign course to student
- View student's current course
- Maintain student course history

###  Teacher Module
- Add new teacher
- View all teachers
- Soft delete teacher (Only if worked more than 30 days)
- Assign teacher to course
- Maintain teacher course history

###  Course Module
- Add new course
- View all courses
- Assign course to student
- Assign teacher to course

---

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python
- OOP (Object Oriented Programming)
- CLI (Command Line Interface)

---

## Project Structure

```
student_management_system/
│
├── main.py
├── config.py
├── database.py
│
├── models/
│   ├── student.py
│   └── teacher.py
│
├── services/
│   ├── student_service.py
│   ├── teacher_service.py
│   └── course_service.py
│
├── sql/
│   └── schema.sql
│
└── README.md
```

---

## Database Tables

- students
- courses
- student_courses
- teachers
- teacher_courses

### Relationships

- One student → One current course
- Student course history maintained
- One teacher → Multiple courses
- Soft delete used for safety

---

## Setup Instructions

###  Clone Repository

```
git clone https://github.com/Kavana-Gowda/student-management-system.git
cd student-management-system
```

### Install Dependency

```
pip install mysql-connector-python
```

### Create Database

Login to MySQL:

```sql
CREATE DATABASE student_mgmt;
USE student_mgmt;
```

### Run Schema File

```
mysql -u root -p student_mgmt < sql/schema.sql
```

### Update Database Credentials

Edit `config.py` and update your MySQL username and password.

### Run Application

```
python main.py
```

---

## Business Rules Implemented

- Student name cannot be updated
- Soft delete for students and teachers
- Only one active course per student
- Previous course automatically closed when new one assigned
- Teacher can only be deleted after working 30+ days

---

## Future Improvements

- Role-based authentication
- CSV import/export
- Flask web interface
- Logging system
- Unit testing
- Pagination

---

##  Author

Kavana Gowda

---

If you like this project, give it a star!

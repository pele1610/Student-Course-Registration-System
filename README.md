# Student Course Registration System

## What the project does
A command-line application that helps a small training school manage students, courses, and student registrations.
The admin can add students, add courses, register students to courses, search for students, and save or load data from files.

## How to run the project
1. Make sure Python 3 is installed on your computer
2. Run the application:
   python3 main.py

## Features implemented
- Add a new student
- View all students
- Search for a student by ID or name
- Add a new course
- View all courses
- Register a student to a course
- View all students registered in a course
- View all courses a student has registered for
- Save data to JSON files
- Load data from JSON files
- Input validation on all fields
- Prevents duplicate students and courses
- Prevents a student from registering twice for the same course
- Prevents registration if a course is full

## Classes used
- Person — base class with name, email, and phone number
- Student — inherits from Person, adds student ID
- Course — manages course details and capacity
- SchoolSystem — handles all the main logic for students, courses, and registrations

## Folder structure
student-course-registration/
├── main.py
├── README.md
├── models/
│   ├── person.py
│   ├── student.py
│   └── course.py
├── services/
│   └── school_system.py
└── data/
    ├── students.json
    ├── courses.json
    └── registrations.json

## Challenges faced
- Validating user input without crashing the app
- Saving and loading objects to and from JSON files
- Limited time to complete the project

## What could be added to improve this application
- Delete a student or course
- Update student or course details
- Add an admin login system
- Show the number of available slots remaining in a course
- Export a student report to a text file
- Add the date and time when a student registers
- Sort students alphabetically by name
- Sort courses by available slots

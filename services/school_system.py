from models.student import Student
from models.course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

    def add_student(self , student_id, name, email, phone_number,):
        for student in self.students:
            if student.student_id == student_id:
                print(f"Student with ID {student_id} already exists.")
                return
            
        new_student = Student(student_id, name, email, phone_number)
        self.students.append(new_student)
        print(f"Student {name} added successfully.")


    
        

    def add_course(self, course_id, course_name, trainer_name, capacity):
        for course in self.courses:
            if course.course_id == course_id:
                print(f"Course with ID {course_id} already exists.")
                return

        new_course = Course(course_id, course_name, trainer_name, capacity)
        self.courses.append(new_course)
        print(f"Course {course_name} added successfully.")

    def view_courses_for_student(self, student_id):
        found_student = None
        for student in self.students:
            if student.student_id == student_id:
               found_student = student
               break


        if found_student is None:
            print(f"\nError: No student found with ID {student_id}.")
            return
        
        print(f"\nCOURSES FOR {found_student.name}")
        found = False
        for reg in self.registrations:
            if reg["student_id"] == student_id:
                for course in self.courses:
                    if course.course_id == reg["course_id"]:
                        print(course.get_details())
                        print()
                        found = True
        if not found:
            print("This student is not registered for any courses.")

    def register_student(self, student_id, course_id):
        found_student = None
        for student in self.students:
            if student.student_id == student_id:
                found_student = student
                break

        found_course = None
        for course in self.courses:
            if course.course_id == course_id:
                found_course = course
                break

        if found_student is None:
            print(f"\nError:No student found with ID {student_id}.")
            return
        
        if found_course is None:
            print(f"\nError: No course found with ID {course_id}.")
            return


        for reg in self.registrations:
            if reg["student_id"] == student_id and reg["course_id"] == course_id:
                print(f"\nError: Student {found_student.name} is already registered for course {found_course.course_name}.")
                return
            
        count = 0
        for reg in self.registrations:
            if reg["course_id"] == course_id:
                count += 1    
        
        if count >= found_course.capacity:
            print("\nRegistration failed: This course is already at full capacity.")
            return
        
        self.registrations.append({"student_id": student_id, "course_id": course_id})

        print(f"\nStudent {found_student.name} registered for course {found_course.course_name} successfully.")

    def view_students(self):
        if len(self.students) == 0:
            print("\nNo students found.")
            return
        
        print("\nALL STUDENTS")
        for student in self.students:
            print(student.get_details())
            print()

        print("\nALL COURSES")
        for course in self.courses:
            print(course.get_details())
            print()

    def search_student(self,search_term):
        found_students = []

        for student in self.students:
            if student.student_id == search_term or student.name.lower() == search_term.lower():
                found_students.append(student)

        if len(found_students) == 0:
            print(f"\nNo students found matching '{search_term}'.")
            return
        
        print("\nSEARCH RESULTS")
        for student in found_students:
            print(student.get_details())
            print()
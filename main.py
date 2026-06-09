from services.school_system import SchoolSystem

system = SchoolSystem()

def show_menu():
    print("\nStudent Course Registration System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View Students in a Course")
    print("8. View Courses for a Student")
    print("9. Save Data")
    print("10. Load Data")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nADD STUDENT")
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            system.add_student(student_id, name, email, phone)

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            print("\nSEARCH STUDENT")
            search_term = input("Enter Student ID or Name: ")
            system.search_student(search_term)

        elif choice == "4":
            print("\nADD COURSE")
            course_id = input("Enter Course ID: ")
            course_name = input("Enter Course Name: ")
            trainer_name = input("Enter Trainer Name: ")
            capacity = input("Enter Capacity: ")
            system.add_course(course_id, course_name, trainer_name, int(capacity))

        elif choice == "5":
            system.view_courses()

        elif choice == "6":
            print("\nREGISTER STUDENT TO COURSE")
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            system.register_student(student_id, course_id)

        elif choice == "7":
            print("\nVIEW STUDENTS IN A COURSE")
            course_id = input("Enter Course ID: ")
            system.view_students_in_course(course_id)

        elif choice == "8":
            print("\nVIEW COURSES FOR A STUDENT")
            student_id = input("Enter Student ID: ")
            system.view_courses_for_student(student_id)

        elif choice == "9":
            print("\nSave feature coming soon.")

        elif choice == "10":
            print("\nLoad feature coming soon.")

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number from the menu.")

main()
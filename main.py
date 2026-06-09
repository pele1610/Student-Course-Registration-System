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

def get_non_empty_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("This field cannot be empty.")
        else:
            return value.strip()


def get_valid_email():
    while True:
        email = input("Enter Email: ")
        if email.strip() == "":
            print("Email cannot be empty.")
        elif "@" not in email:
            print("Email must contain @.")
        else:
            return email.strip()


def get_valid_capacity():
    while True:
        capacity = input("Enter Capacity: ")
        if capacity.strip() == "":
            print("Capacity cannot be empty.")
        elif not capacity.isdigit():
            print("Capacity must be a number.")
        elif int(capacity) <= 0:
            print("Capacity must be greater than 0.")
        else:
            return int(capacity)


def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nADD STUDENT")
            student_id = get_non_empty_input("Enter Student ID: ")
            name = get_non_empty_input("Enter Name: ")
            email = get_valid_email()
            phone = get_non_empty_input("Enter Phone Number: ")
            system.add_student(student_id, name, email, phone)

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            print("\nSEARCH STUDENT")
            search_term = input("Enter Student ID or Name: ")
            system.search_student(search_term)

        elif choice == "4":
            print("\nADD COURSE")
            course_id = get_non_empty_input("Enter Course ID: ")
            course_name = get_non_empty_input("Enter Course Name: ")
            trainer_name = get_non_empty_input("Enter Trainer Name: ")
            capacity = get_valid_capacity()
            system.add_course(course_id, course_name, trainer_name, capacity)

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
            system.save_data()

        elif choice == "10":
            system.load_data()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number from the menu.")

main()
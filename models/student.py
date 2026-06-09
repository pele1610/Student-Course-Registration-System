from models.person import Person

class Student(Person):
    def __init__(self, name, email, phone_number, student_id):
        super().__init__(name, email, phone_number)
        self.student_id = student_id

    def get_details(self):
        return  (
            f"Student ID    : {self.student_id}\n"
            f"Name          : {self.name}\n"
            f"Email         : {self.email}\n"
            f"Phone Number  : {self.phone_number}"
        )   
    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }
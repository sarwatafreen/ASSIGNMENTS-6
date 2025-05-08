class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person): 
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher created with the subject: {self.subject}")

# Creating a Teacher object
t = Teacher("Sarwat", "GIAIC PYTHON COURSE")






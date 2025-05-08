# Using self
# Assignments:
# Create a class Student with attributes name and marks .  Use  the self Keyword to initialize these values 
# via a constructor . add a method display() that print student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

student = Student("Sarwat", 85)
student.display()




























# Class Student:
# def __init__(self,name,marks):
#        self.name = name
#        self.marks = marks

#        def display(self):
#            print(f" student Nmae: {self.name}")
#            print(f" student Marks: {self.marks}")

#            Student = Student("sarwat",85)
#            student .display()
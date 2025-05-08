# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a
#  reference to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Employee Name: {self.name}, Position: {self.position}"

    def __repr__(self):
        return f"Employee({self.name}, {self.position})"

class Department:
    def __init__(self, name, initial_employee=None):
        self.name = name
        self.employees = []
        if initial_employee:
            self.employees.append(initial_employee)

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"Department Name: {self.name}, Employees: {self.employees}"
e1 = Employee("Ali", "Manager")
e2 = Employee("Bobi", "Developer")

dept = Department("IT", e1)
dept.add_employee(e2)

print(dept)

# class Employee:
#     def __init__(self, name,position):
#         self: name = name
#         self : position = position
#         def __str__(self):
#             return f"Employee Name: {self.name} , position: {self.position}"
#         def __repr__(self):
#             return f"Employee({self.name}, {self.position})"
#         class Department:
#             def __init__(self, name, Department):
#                 self.name = name
#                 self.employees =[]
#                 self.employees.append(Department)
#                 def add_employee(self,employee):
#                     self.employees.append(employee)
#                     def __str__(self):
#                         return f"Department Name:{self.name}, Employees:{self.employees}"

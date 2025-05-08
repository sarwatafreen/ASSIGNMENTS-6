
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self.salary = salary
        self.__ssn = ssn  # private attribute

    def get_ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
        else:
            print("Salary must be a positive number")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self.salary}")
        print(f"Accessing SSN via getter method: {self.get_ssn()}")

# Create Manager object
m = Manager("Alice", 50000, "123-45-6789", "HR")

m.show_manager_info()
m.set_salary(660000)
print(f"Updated Salary: {m.salary}")

# Accessing private __ssn (not recommended, but possible using name mangling)
# print(m.__ssn)  # ❌ This will give AttributeError

# Correct way to access private variable (only for learning, not best practice)
print("Private SSN via mangled name:", m._Employee__ssn)






# class Employee:
#     def __init__(self):
#         self.name = name
#         self.salary = salary
#         self.__ssn = ssn

#         def get_ssn(self):
#             return self.__ssn
#         def set_ssn(self, new_salary):
#             if new_salary > 0:
#                 self.salary = new_salary
#             else:
#                 print("salary must be positive in number")
#                 def display(self):
#                     print(f"Name: {self.name}")
#                     print(f"salary:{self.salary}")
#                     print(f"SSN: {self.__ssn}")
#            class Manager(Employee):
#             def__init__(self,name, salary,ssn, department):
#              super().__init__(name, salary, ssn)
#              self.department = department
#             def show_manager_info(self):
#                 print(f"Manager:{self.name}")
#                print(f"Department:{self.department}")
#             print (f"Protected Salary :{self.__salary}")
#             print(f"Acessing SSN via getter command: { self.get_ssn()}")
#             m = Manager("Alice",50000,"123-45-6789","HR")
#             m.show_manager_info()
#             m.set_salary(660000)
#             print(f"Updated Salary:{m._salary}")
#             print(m.__ssn)
#             print("Privatw SSN via managed:", m._Emplyee__ssn)

          
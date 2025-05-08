# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def __str__(self):
        return "A's __str__ method"

    def show(self):
        print("A's show() method")

class B(A):
    def __str__(self):
        return "B's __str__ method"

    def show(self):
        print("B's show() method")

class C(A):
    def __str__(self):
        return "C's __str__ method"

    def show(self):
        print("C's show() method")

class D(B, C):  # Multiple inheritance
    def __str__(self):
        return "D's __str__ method"

    def show(self):
        print("D's show() method")

class E(D):
    def __str__(self):
        return "E's __str__ method"

    def show(self):
        print("E's show() method")

# Test
e = E()
print(e)      # Calls E's __str__
e.show()      # Calls E's show
 
# class A:
#     def__str__(self):
#      print("A's __init__method")
#     def show(self):
#        print("A's show() method")
#        class B(A):
#        def__str__(self):
#         print("B's __init__method")
#        def show(self):
    
#         print("B's show() method")
#         class C(A):
#           def__str__(self):
#           print("C;s__init_method")
#           def show(self):
#             print("C's show()method")
#             class D(B,C):
#               def__str__(self):
#               print("D's __init__method")
#               def show (self):
#                 print("D's show()method")
#                 class E(D)
# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning
# "Hello from Decorator!". Apply it to a class Person.
  # Decorator function
def greeting_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Hello from Decorator!")
        return func(self, *args, **kwargs)
    return wrapper

# Person class using the decorator
class Person:
    def __init__(self, name):
        self.name = name

    @greeting_decorator
    def greet(self):
        return f"Hello, {self.name}!"

# Usage
person = Person("Alina")
print(person.greet())

# 
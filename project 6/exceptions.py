# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception 
# if age < 18. Handle it with try...except.

# class InvalidAgeError(Exception):
#     """Custom exception for invalid age."""
#     pass
#  def check_age(age):
#     """ checks if the age is valid."""
#     if age < 18:
#         raise InvalidAgeError(f"Invaild age:{age}. Age must be 18 or older.")
#     return True
#  try:
#     age: int(input("Enter your age: "))
#     check = check_age(age)
#     print("Age is valid.")
#  except InvalidAgeError as e:
#     print(e)


class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    """Checks if the age is valid."""
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
    return True

try:
    age = int(input("Enter your age: "))
    check = check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)

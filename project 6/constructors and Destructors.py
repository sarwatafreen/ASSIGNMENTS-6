
# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Message Before: Logger object created.!")

    def __del__(self):
        print("Message After: Logger object destructor.")

# Creating a Logger object
log = Logger()

# Deleting the object manually (this will trigger the __del__ method)
del log










# class Logger:
#   def __init__(self):
#    print(f"Message Before: Logger object created.!")

#    def __del__(self):
#     print (f"Message After: Logger object destructor.")
#     log = logger()
#     del log
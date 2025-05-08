# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input 
# by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


# Example usage
multiplier = Multiplier(5)

# Check if object is callable
print(callable(multiplier))  # Output: True

# Call the object like a function
print(multiplier(10))  # Output: 50

# Another call
result = multiplier(5)
print(result)  # Output: 25


# class Multiplier:
#     def__init__(self,factor):
#        self.factor = factor
#       def __call__(self,x):
#         return x * self.factor
#      # Example usage
#      multiplier = Multiplier(5)
#      print (callable(multiplier)) # True
#        print(multiplier(10)) # 50
#     # Example usage
#     multiplier = Multiplier(5)
#     print(callable(multiplier)) # True
#     print (multiplier(10)) # 50
#     # Test with callable()
# print(callable(multiplier))  # Output: True

# # Call the object like a function
# result = multiplier(5)
# print(result)  # Output: 15
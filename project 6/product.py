#  18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete i# class Product:
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

# Example usage
product = Product("Laptop", 1000)

# Get price using property
print(product.price)  # Output: 1000

# Update price using setter
product.price = 1200
print(product.price)  # Output: 1200

# Attempt to set invalid price
try:
    product.price = -50
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Delete price using deleter
del product.price
try:
    print(product.price)  # Raises AttributeError: 'Product' object has no attribute '_price'
except AttributeError as e:
    print(e)  # Output: 'Product' object has no attribute '_price'






# def __init__(self, price):
#         self._price = None  # Avoid using setter until it's defined
#         self.price = price  # This will use the setter

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self._price = value

#     @price.deleter
#     def price(self):
#         del self._price


# # Example usage
# p = Product(100)
# print(p.price)  # 100

# p.price = 150
# print(p.price)  # 150

# del p.price
# try:
#     print(p.price)
# except AttributeError as e:
#     print("Caught error:", e)

# # Another instance
# laptop = Product(1000)
# print(laptop.price)  # 1000
# laptop.price = 1200
# print(laptop.price)  # 1200

# del laptop.price
# try:
#     print(laptop.price)
# except AttributeError as e:
#     print("Caught error:", e)

# class Product:
#     def__init__(self, Price):
#      self .price = Price
#     @property
#     def price(self):
#        return self._Price
#     @price.setter
#     def price(self,value):
#        if value < 0:
#           raise ValueError("price cannot be negative")
#        self.price =value
#        @price.deleter
#         def price(self):
#           del self._price
#           #Example useage
#           Product = Product(100)
#           print(Product.price)
#           Product.price = 150
#           print(Product.price)
#           del Product.price
#           try:
#             print(Product.price)
#           except AttributeError as e:
#             print(e)
#              Product =laptop(1000)
#             print(Product.price)
#             Product.price = 1200
#             print(Product.price)
#             del Product.price
#             try:
#                print(Product.price)
#             except AttributeError as e:
#               print(e)

        

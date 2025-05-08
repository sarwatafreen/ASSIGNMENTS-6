# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during
# initialization. Access a method of the Engine class via the Car class.
class Engine:
    def __init__(self, type, horsepower):
        self.type = type
        self.horsepower = horsepower

    def start(self):
        return f"{self.type} engine with {self.horsepower} HP is starting"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_engine(self):
        return self.engine.start()

# Create Engine and Car objects
engine = Engine("V8", 450)
car = Car("Toyota", engine)

# Start the car's engine
print(car.start_engine())






# class Engine:
#     def__init__(self, type,horsepower):
#      self.type = type

#     def start(self):
#         return f"{self.type} engine is starting"

# class Car:
#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine

#     def start_engine(self):
#         return self.engine.start()

# engine = Engine("V8")
# car = Car("Toyota", engine)
# print(car.start_engine())      
                
#        self.type =type
#         self.horesepower = horsepower
    
#     def start(self):
#        return f"{self.type} engine with {self.horsepower} "
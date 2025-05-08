# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f-32) * 5/9
   # Call static method outside the class
temp_f = TemperatureConverter.celsius_to_fahrenheit(25)
print(temp_f)

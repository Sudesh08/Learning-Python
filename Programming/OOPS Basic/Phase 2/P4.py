# 🔸 4. Temperature Converter
# Question:
# Create a class Temperature with a method:
#
# to_celsius(fahrenheit)
#
# to_fahrenheit(celsius)
#
# Use self correctly and demonstrate conversion for both.

class Temperature:
    def __init__(self,value):
        self.value=value

    def to_celsius(self):
        temperatureInCelcius =(float(self.value)-32)/1.8
        return temperatureInCelcius

    def to_fahrenheit(self):
        temperatureFahrenheit =(float(self.value)*9/5)+32
        return temperatureFahrenheit

temperature1=Temperature(5)
print(temperature1.to_celsius())
print(temperature1.to_fahrenheit())



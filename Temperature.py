class Temperature:

    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    @staticmethod
    def celcius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius, "C")

suhu = float(input("Enter temperature: "))
unit = input("Enter unit (C/F) : ").upper()

if unit == "C":
    temp = Temperature(suhu, unit)
    fahrenheit = temp.celcius_to_fahrenheit(suhu)
    print(f"{suhu}°C = {fahrenheit:.2f}°F")
elif unit == "F":
    temp = Temperature.from_fahrenheit(suhu)
    print(f"{suhu}°F = {temp.temperature:.2f}°C")
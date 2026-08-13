from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def riding(self):
        pass

class Engine:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle, Engine):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def riding(self):
        print(f"The Car is riding.")

car1 = Car("Toyota", 2020, 4)

print("=== Car Information ===")
print(f"Brand  : {car1.brand}")
print(f"Year   : {car1.year}")
print(f"Doors  : {car1.doors}")
car1.riding()
car1.start_engine()

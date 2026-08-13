class Car:
    def move(self):
        print("The car is moving.")

class Boat:
    def move(self):
        print("The boat is sailing.")

class Plane:
    def move(self):
        print("The plane is flying.")

class Person:
    def move(self):
        print("The person is walking.")

def start_transport(transport):
    transport.move()

car1 = Car()
boat1 = Boat()
plane1 = Plane()
person1 = Person()

start_transport(car1)
start_transport(boat1)
start_transport(plane1)
start_transport(person1)
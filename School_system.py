class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Whiteboard():
    def __init__(self, color):
        self.color = color

class Classroom():
    def __init__(self, room_name, student):
        self.room_name = room_name
        self.student = student
        self.whiteboard = Whiteboard("White")

student1 = Student("Andi", 16)
classroom1 = Classroom("RPL 1", student1)

print("=== CLASSROOM INFORMATION ===")
print(f"Room Name : {classroom1.room_name}")
print(f"Student Name : {classroom1.student.name}")  
print(f"Student Age  : {classroom1.student.age}")
print(f"Whiteboard Color : {classroom1.whiteboard.color}")



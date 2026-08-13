class Student:
    school = "SMK RPL"

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        print(f"Hello my name is {self.name}")

student1 = Student("Andi", 16, "RPL")
student2 = Student("Budi", 17, "TKJ")
student3 = Student("Dian", 16, "DKV")

print("=== STUDENT INFORMATION ===")
print(f"Name   : {student1.name}")
print(f"Age    : {student1.age}")
print(f"Major  : {student1.major}")
print(f"School : {student1.school}")
student1.introduce()
print(f"\nName   : {student2.name}")
print(f"Age    : {student2.age}")
print(f"Major  : {student2.major}")
print(f"School : {student2.school}")
student2.introduce()
print(f"\nName   : {student3.name}")
print(f"Age    : {student3.age}")
print(f"Major  : {student3.major}")
print(f"School : {student3.school}")
student3.introduce()

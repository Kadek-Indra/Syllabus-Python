from collections import Counter, namedtuple, defaultdict, deque, OrderedDict
import time

student_data = namedtuple("Student", ["name", "age", "major"])
students = []

for x in range(5):
    print("========= STUDENT REGISTRATION ==========")
    name = input(f"Enter student{x + 1} name  : ").capitalize()
    age = int(input(f"Enter student{x + 1} age   : "))
    major = input(f"Enter student{x + 1} major : ").upper()
    student = student_data(name, age, major)
    students.append(student)


print()
print()
for number, student in enumerate(students, start=1):
    print(f"====Student{number}====")
    print(f"Name   : {student.name}")
    print(f"Age    : {student.age}")
    print(f"Major  : {student.major}")


print()
print()
student_group = defaultdict(list)
for student in students:
    student_group[student.major].append(student.name)

print("=====Student Group=====")
for major, students_names in student_group.items():
    print(f"{major:5} : {students_names}")


print()
major_amount = Counter(student.major for student in students)

print("==== Major Statistic ====")
for major, amount in major_amount.items():
    print(f"{major:5} : {amount} students")


print()
student_queue = deque()

for student in students:
    student_queue.append(student)

print("====Student Queue====")
for student in student_queue:
    print(student.name)
print()
while student_queue:
    process = student_queue.popleft()
    print (f"Processing Queue : {process.name}")
    time.sleep(2)

print()
student_records = OrderedDict()

print("====Student Records====")

for student in students:
    student_records[student.name] = student

for number, (name, student) in enumerate(student_records.items(), start=1):
    print(f"{number}. {student.name} : {student.age} : {student.major}")
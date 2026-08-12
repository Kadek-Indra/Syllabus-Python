from collections import Counter, namedtuple, defaultdict, deque, OrderedDict
import time


# ==================================================
# 1. Counter
# ==================================================
print("\n========== WORD COUNTER ==========")
sentences = input("Enter the sentences : ").lower()

words = sentences.split()
count = Counter(words)

print()
print(f"Counting    : {count}")
print(f"Most common : {count.most_common(3)}")


# ==================================================
# 2. namedtuple
# ==================================================

Student = namedtuple("Student", ["name", "age", "major"])

print("\n========== STUDENT INFORMATION ==========")

name = input("Enter your name  : ").capitalize()
age = input("Enter your age   : ")
major = input("Enter your major : ").upper()

student = Student(name, age, major)

print()
print(f"Name  : {student.name}")
print(f"Age   : {student.age}")
print(f"Major : {student.major}")


# ==================================================
# 3. defaultdict
# ==================================================

student_group = defaultdict(list)

print("\n========== STUDENT GROUP ==========")

for x in range(5):
    student = input("Enter student name  : ").capitalize()
    major = input("Enter student major : ").upper()

    student_group[major].append(student)
    print()

for major, students in student_group.items():
    print(f"{'Name':8} : {str(students):20} Jurusan : {major}")



#=================================================
# 4. deque
#=================================================

queue = deque()

print("\n========== STUDENT QUEUE ==========")

for x in range(5):
    student = input("Enter student name : ").capitalize()
    queue.append(student)


print(f"Current queue : {list(queue)} ")
print()
print()

while queue:
    student = queue.popleft()
    print (f"Processing Queue : {student}")
    time.sleep(2)



#=================================================
# 5. OrderedDict
#=================================================

students = OrderedDict()

print("\n========== STUDENT RANKING ==========")

for x in range(5):
    name = input("Enter student name   : ").capitalize()
    score = float(input("Enter the the score  : "))
    students[name] = score

print()
for rank, (x, y) in enumerate(students.items(), start=1):
    print(f"{rank}. {x} : {y:.2f}")



print("\n========== PROGRAM FINISHED ==========")
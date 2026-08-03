# Logical operators & ternary
age = int(input("Enter your age : "))
result = "You are a man" if age >= 17 and age <= 40 else "You are not a man"
print (result)

height = float(input("Enter you heigh : "))
result1 = "You are a tall man" if height >= 170.0 or height >= 160.0 else "You are not a tall man"
print (result1)

Betul = True
if not Betul:
    print ("Betul")
else:
    print("Tidak Betul")

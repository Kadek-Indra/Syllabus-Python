# Modules and Scope

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    num1 = int(input("Enter the first number  :  "))
    num2 = int(input("Enter the second number : "))
    print (add(num1, num2))
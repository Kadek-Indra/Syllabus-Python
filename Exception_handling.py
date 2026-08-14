try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = str(input("Enter an operator (+, -, *, /): "))
except ValueError:
    print("Invalid input!")
else: 
    if op == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif op == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif op == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif op == "/":
        try:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator!")
finally:
    print("Program finished.")
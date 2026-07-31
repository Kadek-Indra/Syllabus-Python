print ("Python Calculator")
print ("")
number1 = float(input("Enter the first number  :  "))
number2 = float(input("Enter the second number : "))
operator = input("Choice the operator + , - ,* , / , % ,** : ")

if operator == "+":
    print (f"The result is : {number1 + number2}")
elif operator == "-":
    print (f"The result is : {number1 - number2}")    
elif operator == "*":
    print (f"The result is : {number1 * number2}")
elif operator == "/":
    print (f"The result is : {number1 / number2}")
elif operator == "%":
    print (f"The result is : {number1 % number2}")
elif operator == "**":
    print (f"The result is : {number1 ** number2}")
else:
    print("choice the right operator!")                                

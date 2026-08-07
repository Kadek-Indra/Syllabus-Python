import Module_simple_calculator2 as msc
running = True

while running:

    print("==== SIMPLE CALCULATOR ====")
    a = int(input("Enter the first number  : "))
    b = int(input("Enter the second number : "))
    print ()

    print("1. '+'")
    print("2. '-'")
    print("3. 'x'")
    print("4. '/'")
    operator = input("Enter the operator   : ")

    print ("The result is :",end=" ")
    match operator:
        case "1":
            print (msc.add(a, b))
        case "2":
            print (msc.subtract(a, b))
        case "3":
            print (msc.multiply(a, b))
        case "4":
            print (msc.divide(a, b))
        case _:
            print("The operator was not valid")

    print()

    choices = input("More calculation? (y / n) : ")
    if not choices == "y":
        print("The program ended, Thank you:)")
        break
    else:
        print()
# Validation The Credit_Card

running = True


while running:
    total = 0

    print ("=== Validation Card Number ===")
    number = input("Enter the card number : ")
    number = number.replace("-","")
    number = number.replace(" ","")
    number = number[::-1]
    

    for index, digit in enumerate(number):
        digit = int(digit)
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
                
    if total % 10 == 0:
        print("Valid")
    else:
        print("Invalid")

    
        

    

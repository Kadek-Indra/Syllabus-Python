# Validation The Credit_Card

running = True


while running:

    print ("=== Validation Card Number ===")
    number = input("Enter the card number : ")
    number = number.replace("-","")
    number = number.replace(" ","")
    number = number[::-1]
    

    for index, digit in enumerate(number):
        if index % 2 == 1:
            digit = int(digit)
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
                
    if total % 10 == 0:
        print("Valid")
    else:
        print("Invalid")

    
        

    

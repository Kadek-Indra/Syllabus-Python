#shopping cart program using 2D list

cart = [] 
total = 0

# Entering the
while True:
    product = input("Enter product : ")
    quantity = int(input("Enter the quantity : "))
    price = float(input("Enter price : "))

    cart.append([product, quantity, price]) # adding the value into the 2D list

    again = input("Add another item? (y/n) : ") # loop
    if again.lower() == "n":
        break


print("==== RECEIPT ====")
for item in cart:
    print(f"Product  : {item[0]}")  # print the value 
    print(f"Quantity  : {item[1]}")
    print(f"Price  : {item[2]}")
    subtotal = item[1] * item[2]
    print (f"Subtotal : {subtotal}") # counting the subtotal
    print()
    total += subtotal
    
print()
print (f"The total is : {total}") # counting the total

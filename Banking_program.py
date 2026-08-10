running = True
balance = 0

def deposit():
    global balance
    amount = float(input("Input the amount : "))
    if amount <= 0:
        print("Invalid Amount!")
    else:
        balance += amount
        
def withdraw():
    global balance
    amount = float(input("Input the amount : "))
    if amount <= 0:
        print("Invalid Amount!")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount

def show_balance():
    global balance
    print(f"Your Balance is : {balance:.2f}")


while running:

    print("==== BANKING PROGRAM ====")
    print ("1. Deposit")
    print ("2. Withdraw")
    print ("3. Balance")
    print ("4. Exit")
    choice = input("Enter the menu : ")

    if choice == '1':
        print("--------------------")
        deposit()
        print("--------------------")
    elif choice == '2':
        print("--------------------")
        withdraw()
        print("--------------------")
    elif choice == '3':
        print("--------------------")
        show_balance()
        print("--------------------")
    elif choice == '4':
        running = False
    else:
        print("--------------------")
        print("Invalid Menu!")
        print("--------------------")


print("--------------------")
print ("Good-bye, Thank You!")
print("--------------------")
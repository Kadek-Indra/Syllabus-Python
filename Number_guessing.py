import random

first_number = 100
last_number = 200
guesses = 0
number = random.randint(first_number, last_number)

while True:
    guess = int(input(f"Enter a number between ({first_number} - {last_number}) : "))
    guesses += 1

    if guess > (last_number) or guess < (first_number):
        print ("Your number is not valid") 
    elif guess == (number):
        print ("Your number is correct")
        print (f"Your guesses are {guesses}x")
        break
    elif guess > (number):
        print ("Your number is too high")
    else:
        print ("Your number is too low")


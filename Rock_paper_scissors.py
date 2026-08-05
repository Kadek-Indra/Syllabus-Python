import random

options = ("rock", "paper", "scissors")
playing = True
print ("WELCOME TO ROCK-PAPER-SCISSORS GAME")
round = 1
player = None

while playing: 

    while player not in options:
        print()

        print (f"ROUND {round}")
        player = str(input("Enter your choice (Rock-Paper-Scissors) : ")).lower()

        if player not in options:
            print("Your choice is not valid")
            continue
        print()
        computer  = random.choice(options)
        print (f"Yours    : {player}")
        print (f"computer : {computer}")

        if player == "rock" and computer == "scissors":
            print("You win!") 
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print ("You win!")
        elif player == computer:
            print("DRAW!")
        else:
            print ("You lose!")
        round += 1

        print()
        while True:
            play_again = input("More game? (y / n) : ").lower()

            if play_again == "y":
                player = None
                break
            elif play_again == "n":
                playing = False
                break
            else:
                print ("Your choice is not valid")
print("The Game Had Ended")
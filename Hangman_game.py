import random

hangman_art = {
    0: (
        "   ",
        "   ",
        "   "
    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}

words = ["banana", "apple", "orange", "grape", "mango", "pineapple"]
word = random.choice(words)
display = ["_"] * len(word)
lives = 6

while lives > 0:
    correct = False

    print("============")
    for line in hangman_art[6 - lives]:
        print(line)
    print("============")
    print()
    print(" ".join(display))
    
    guess = input("Guess a letter : ").lower()


    for index in range(len(word)):
        if word[index] == guess:
            display[index] = guess
            correct = True
    print()
    if not correct:
        lives -= 1
        print("Wrong Guess")

    print("=================")
    print(" ".join(display))
    print("=================")
    
    if "_" not in display:
        print("You win!")
        break

if lives == 0:
    for line in hangman_art[6]:
        print(line)
    print("You lose!")
    print(f"The word was: {word}")
# Multiple-choice quiz

questions = ("What is the most large country in the world? : ",
             "How country joining world cup 2026? : ",
             "Which one is the correct amount of the planets  in the solar system : ",
             "What is the hardware in computer that used to type? : ",
             "Where is spiderman actioning? : ")

options = (("A. Russian", "B. USA", "C. Chine", "D. Indonesia", "E. Japan"),
          ("A. 36", "B. 48", "C. 100", "D. 26", "E. 666"),
          ("A. 8", "B. 10", "C. 12", "D. 11", "E. 7"),
          ("A. Monitor", "B. Mouse", "C. HDMI", "D. Handphone", "E. Keyboard"),
          ("A. Denpasar", "B. Hiroshima", "C. New York", "D. Battleworlds", "E. Bangkok"),)

answers = ("A", "B", "A", "E", "C",)
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter your answer (A, B, C, D, E) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+= 1
        print("YOUR ASNWER IS CORRECT!")
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print(f"The right answer is {answers[question_num]}")
    question_num += 1

print ("==========================")
print ("       FINAL RESULT       ")
print ("==========================")

print("answers : ", end="")
for answer in answers:
    print(answer, end=" ")

print()

print("guesses : ", end="")
for guess in guesses:
    print(guess, end=" ")

print(" ")

score = int(score / len(questions) * 100)
print(f"Your final score is {score}% ")
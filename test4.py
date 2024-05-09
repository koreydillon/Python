score = 0
print("Hello, welcome to The Guessing Game?")

def check_questions(question, answer):
    global score 
    for attempt in range(3):
        guess = input(question)
        if guess == answer:
            print("That is the correct answer!")
            return 1
        else:
            print("That is not the correct answer.")

        if attempt == 2:
            print("The correct answer is " + str(answer) + ".")
            return 0


score += check_questions("What is H2O?\n", "water")
score += check_questions("What is the minimum age to be President of the United States?\n", "35")
score += check_questions("How many sides does a triangle have?\n", "3")
score += check_questions("What is Earths atmospheric pressure in psi?\n", "14.7 psi")
print("Thank you for playing! Your score is " + str(score) + "/4" ".")

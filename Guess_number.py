import random
# Game set up
print("Welcome to the guess game!")
number_of_guess = 3 # User has 3 guess befodre losing the game
user_won = False
# Computer guess a random number between 1 and 10
correct_answer = random.randint(1,10)
print(correct_answer)
while number_of_guess > 0 :


    # User guess the number
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)

    # Computer tells user whether guess was too high or too low
    if user_guess == correct_answer:
        print("Good guess")
        print("You are correct!")
        user_guess = True
        break
    elif user_guess > correct_answer:
        print("Sorry, you guessed high")
    elif user_guess < correct_answer:
        print("Sorry, you guessed low!")
    else:
        print("Incorrect")

    number_of_guess -= 1

if user_won == True:
    print("You won")
else:
    print("you loose")
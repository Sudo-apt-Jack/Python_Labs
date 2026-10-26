import random

print("Welcome to the Dice Guessing Game!")

score = 0

while True:
    guess = input("Guess a number on the dice (1-6) or type 'q' to quit: ")

    if guess.lower() == "q":
        print("Thanks for playing!")
        print("Your final score is:", score)
        break

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)

    if guess < 1 or guess > 6:
        print("Your guess must be between 1 and 6!")
        continue

    random_number = random.randint(1, 6)

    print("The dice rolled:", random_number)

    if guess == random_number:
        print("Congratulations! You guessed correctly!")
        score += 1
    else:
        print("Sorry! Better luck next time!")

    print("Current score:", score)
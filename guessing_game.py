# This program creates a number guessing game.

import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break

    except ValueError:
        print("Enter a valid number.")

else:
    print(f"Game Over! The number was {secret_number}")
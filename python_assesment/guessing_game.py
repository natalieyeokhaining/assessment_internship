# guessing_game.py
# Number Guessing Game
# Demonstrates use of random library, loops, conditionals, lists, input validation, and f-strings

import random  # Import random library


def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize attempts and guesses list
    attempts_remaining = 7
    guesses = []

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")

    # Game loop
    while attempts_remaining > 0:
        user_input = input(f"Enter your guess ({attempts_remaining} attempts left): ")

        # Input validation (non-numeric input)
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.\n")
            continue

        guess = int(user_input)
        guesses.append(guess)
        attempts_remaining -= 1

        # Game logic using conditionals
        if guess < secret_number:
            print("Too low!\n")
        elif guess > secret_number:
            print("Too high!\n")
        else:
            attempts_used = 7 - attempts_remaining
            print(f"Congratulations! You guessed the number in {attempts_used} attempts.")
            print(f"Your guesses: {guesses}")
            return

    # End game if attempts run out
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
    print(f"Your guesses: {guesses}")


def main():
    # Ask player if they want to play again
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break


# Run the program
main()
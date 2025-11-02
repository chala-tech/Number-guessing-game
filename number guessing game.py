import random

class Number_guessing:
    def __init__(self):
        print("WELCOME TO THE NUMBER GUESSING GAME!")
        print("I'm thinking of a number between 1 and 100.")
        start = input("Type 'yes' to begin: ").lower() # Handles "YES", "Yes", etc.
        if start == 'yes':
            self.num_game()
        else:
            print("Goodbye!")

    def num_game(self):
        # Set attempts based on level
        level = input("Choose a level: 'easy', 'medium', or 'hard': ").lower()
        if level == "easy":
            attempts = 10
            print(f"You have {attempts} attempts to guess the number.")
        elif level == "medium":
            attempts = 7
            print(f"You have {attempts} attempts to guess the number.")
        elif level == "hard":
            attempts = 5
            print(f"You have {attempts} attempts to guess the number.")
        else:
            print("Invalid choice. Defaulting to 'medium'.")
            attempts = 7
            print(f"You have {attempts} attempts to guess the number.")

        # Generate the random number
        secret_number = random.randint(1, 100)

        # Main game loop
        for attempt in range(attempts):
            guesses_left = attempts - attempt

            # Get user input with a single prompt
            try:
                guess = int(input(f"\nGuess the number (1-100). You have {guesses_left} attempt(s) left: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            # Check if the guess is out of range FIRST
            if guess < 1 or guess > 100:
                print("Your guess is out of range! Please enter a number between 1 and 100.")
                continue

            # Check the guess against the secret number
            if guess == secret_number:
                print(f" CONGRATULATIONS! You won! The number was {secret_number}.")
                break
            elif guess < secret_number:
                print("Your guess is LOWER than the number I'm thinking of.")
            else:
                print("Your guess is HIGHER than the number I'm thinking of.")

            # If this was the last attempt
            if guesses_left == 1:
                print(f"\n Game Over! You've run out of attempts. The number was {secret_number}.")

        # Ask to play again
        play_again = input("\nDo you want to play again? Type 'yes' to continue: ").lower()
        if play_again == "yes":
            self.num_game()
        else:
            print("Thanks for playing! Goodbye!")

# Start the game
my_game = Number_guessing()

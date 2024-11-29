import random

def main():
    print("Welcome to the python guessing game!")

    while True:
        play_game()
        if not play_again():
            print("Goodbye!")
            break


def play_game():
    random_number = random.randrange(1, 20)
    attempts = 0
    print("Guess what is the number between 1 and 20 I chose?")

    while True:
        guess = input("The number is: (type 'x' to exit, 'n' for a new game, 's' to show the number) ").strip().lower()

        if guess == "x":
            print("Goodbye!")
            exit(0)  
        elif guess == "n":
            print("Let's play again!")
            return 
        elif guess == "s":
            print(f"The number is: {random_number}")
            continue 

        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 20.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == random_number:
            print(f"Correct! You guessed in {attempts} attempts.")
            break
        elif guess > random_number:
            print("Try a smaller number.")
        else:
            print("Try a bigger number.")


def play_again():
    """Ask the user if they want to play again."""
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
import random

def main():
    print("Welcome to the python guessing game!")

    while True:
        play_game()
        if not play_again():
            print("Goodbye")
            break


def play_game():
    random_number = random.randrange(1, 20)
    attempts = 0
    print("Guess what is the number between 1 and 20 I chose?")

    while True:
        guess = int(input("The number is: (type 'x' to exit, 'n' for a new game, 's' to show the number)"))

        if guess == "x":
            print("Goodbye")
        elif guess == "n":
            print("Lets play again")
            return 
        elif guess == 's':
            print(f"The number is: {random_number_number}")
            continue

        attempts += 1

        if guess == random_number:
            print(f"Correct! Your number of attempts is: {attempts}")
            break
        elif guess > secret_number:
            print("Try a smaller number")
        else:
            print("Try a bigger number")

def play_again():
    while True:
        response = input("Do you want to play again?").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
  




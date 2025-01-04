import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Guessing Game")
        
        self.random_number = random.randint(1, 20)
        self.attempts = 0

        # Title 
        self.title_label = tk.Label(root, text="Welcome to the Python Guessing Game!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Instructions 
        self.instructions_label = tk.Label(root, text="Guess the number between 1 and 20", font=("Arial", 12))
        self.instructions_label.pack(pady=5)

        # User input
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        # Buttons
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_guess, font=("Arial", 12))
        self.submit_button.pack(pady=5)

        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game, font=("Arial", 12))
        self.new_game_button.pack(pady=5)

        self.show_number_button = tk.Button(root, text="Show Number", command=self.show_number, font=("Arial", 12))
        self.show_number_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
        self.exit_button.pack(pady=5)

    def submit_guess(self):
        guess = self.entry.get().strip()
        if not guess:
            messagebox.showerror("Error", "Please enter a guess!")
            return

        if guess.lower() == 'x':
            messagebox.showinfo("Goodbye", "Goodbye")
            self.root.after(100, self.root.quit)
            return
        elif guess.lower() == 'n':
            self.new_game()
            return
        elif guess.lower() == 's':
            self.show_number()
            return

        if not guess.isdigit():
            messagebox.showerror("Error", "Invalid input! Please enter a number between 1 and 20.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess == self.random_number:
            messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
            self.new_game()
        elif guess > self.random_number:
            messagebox.showinfo("Try Again", "Try a smaller number.")
        else:
            messagebox.showinfo("Try Again", "Try a bigger number.")

    def new_game(self):
        self.random_number = random.randint(1, 20)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        messagebox.showinfo("New Game", "A new game has started! Guess the number between 1 and 20.")

    def show_number(self):
        messagebox.showinfo("Hint", f"The number is: {self.random_number}")


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

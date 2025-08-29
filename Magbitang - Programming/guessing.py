import tkinter as tk
import random
import subprocess
import sys

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.guess_number)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Added Back to Dashboard button
        self.back_button = tk.Button(
            master,
            text="⬅ Back to Dashboard",
            bg="orange",
            font=("Arial", 12),
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=10)

    def guess_number(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"🎉 Correct in {self.attempts} attempts!")
                self.guess_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def back_to_dashboard(self):
        self.master.destroy()
        subprocess.Popen([sys.executable, "dashboard.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()


#Magbitang, Elisha Jhoyce M.

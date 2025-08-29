import tkinter as tk
import random
from tkinter import messagebox
import subprocess
import sys

class CardMatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Matching Game")
        self.root.geometry("600x800")
        self.root.resizable(False, False)

        self.symbols = ["1", "2", "3", "4", "5", "6", "7", "8"] * 2
        random.shuffle(self.symbols)

        self.buttons = []
        self.flipped = []
        self.matched = []
        self.attempts = 0
        self.matches = 0
        self.is_checking = False

        tk.Label(self.root, text="Memory Game", font=("Arial", 20, "bold")).pack(pady=10)

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(pady=20)

        self.create_board()

        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.pack(pady=10)

        self.attempts_label = tk.Label(self.stats_frame, text="Attempts: 0", font=("Arial", 14))
        self.attempts_label.pack(side=tk.LEFT, padx=20)

        self.matches_label = tk.Label(self.stats_frame, text="Matches: 0/8", font=("Arial", 14))
        self.matches_label.pack(side=tk.LEFT, padx=20)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.new_game_button = tk.Button(
            self.buttons_frame,
            text="New Game",
            font=("Arial", 14),
            width=12,
            bg="light blue",
            command=self.reset_game
        )
        self.new_game_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(
            self.buttons_frame,
            text="Reset",
            font=("Arial", 14),
            width=12,
            bg="light green",
            command=self.reset_game
        )
        self.reset_button.grid(row=0, column=1, padx=10)

        # Added Back to Dashboard button
        self.back_button = tk.Button(
            self.buttons_frame,
            text="⬅ Back to Dashboard",
            font=("Arial", 14),
            width=25,
            bg="orange",
            command=self.back_to_dashboard
        )
        self.back_button.grid(row=1, column=0, columnspan=2, pady=10)

    def create_board(self):
        for i in range(4):
            for j in range(4):
                idx = i * 4 + j
                btn = tk.Button(
                    self.game_frame,
                    text="?",
                    font=("Arial", 30, "bold"),
                    width=5,
                    height=2,
                    command=lambda index=idx: self.flip_card(index)
                )
                btn.grid(row=i, column=j, padx=8, pady=8)
                self.buttons.append(btn)

    def flip_card(self, index):
        if self.is_checking or index in self.flipped or index in self.matched:
            return

        self.buttons[index].config(text=self.symbols[index])
        self.flipped.append(index)

        if len(self.flipped) == 2:
            self.is_checking = True
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")
            self.root.after(800, self.check_match)

    def check_match(self):
        idx1, idx2 = self.flipped

        if self.symbols[idx1] == self.symbols[idx2]:
            self.matched.extend([idx1, idx2])
            self.buttons[idx1].config(bg="light green")
            self.buttons[idx2].config(bg="light green")
            self.matches += 1
            self.matches_label.config(text=f"Matches: {self.matches}/8")

            if self.matches == 8:
                messagebox.showinfo("Congratulations", f"You won in {self.attempts} attempts!")
        else:
            self.buttons[idx1].config(text="?")
            self.buttons[idx2].config(text="?")

        self.flipped = []
        self.is_checking = False

    def reset_game(self):
        random.shuffle(self.symbols)
        for button in self.buttons:
            button.config(text="?", bg="SystemButtonFace")
        self.flipped = []
        self.matched = []
        self.attempts = 0
        self.matches = 0
        self.is_checking = False
        self.attempts_label.config(text="Attempts: 0")
        self.matches_label.config(text="Matches: 0/8")

    def back_to_dashboard(self):
        self.root.destroy()
        subprocess.Popen([sys.executable, "dashboard.py"])


if __name__ == "__main__":
    root = tk.Tk()
    game = CardMatchGame(root)
    root.mainloop()



#Magbitang, Elisha Jhoyce M.
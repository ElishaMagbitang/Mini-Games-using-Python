import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# Dictionary of game titles and their corresponding Python files
games = {
    "Card Match": "cardmatch.py",
    "Guessing Game": "guessing.py",
    "Quiz Game": "quiz.py",
    "Snake Game": "snake.py",
    "Tic Tac Toe": "tictactoe.py"
}

def launch_game(game_file):
    if not os.path.exists(game_file):
        messagebox.showerror("Error", f"{game_file} not found.")
        return
    try:
        subprocess.Popen([sys.executable, game_file])
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch {game_file}\n{str(e)}")

def exit_program():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# Create dashboard window
root = tk.Tk()
root.title("Game Arcade")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="🎮 Choose a Game", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

# Create buttons for each game
for game_name, file_name in games.items():
    tk.Button(root, text=game_name, width=25, font=("Arial", 14),
              command=lambda f=file_name: launch_game(f)).pack(pady=5)

# Exit button
tk.Button(root, text="Exit", width=15, bg="red", fg="white", font=("Arial", 12),
          command=exit_program).pack(pady=20)

root.mainloop()

#Manimtim, Jasmine Aira D.
#BSIT 112 - A
#Finals Practical in Comp Prog

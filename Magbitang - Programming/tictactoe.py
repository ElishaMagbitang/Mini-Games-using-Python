import tkinter as tk
from tkinter import messagebox
import subprocess
import sys


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        
        self.status_label = tk.Label(
            root, 
            text=f"Player {self.current_player}'s turn", 
            font=('Arial', 12)
        )
        self.status_label.pack(pady=5)
        
        self.reset_button = tk.Button(
            root,
            text="New Game",
            font=('Arial', 10),
            command=self.reset_game
        )
        self.reset_button.pack(pady=5)

        # Added Back to Dashboard button
        self.back_button = tk.Button(
            root,
            text="⬅ Back to Dashboard",
            font=('Arial', 10),
            bg="orange",
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=5)
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.frame,
                    text="",
                    font=('Arial', 20, 'bold'),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)
    
    def make_move(self, row, col):
        if self.game_over:
            return
            
        index = row * 3 + col
        
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.game_over = True
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                self.status_label.config(text="It's a draw!")
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for pattern in win_patterns:
            if (self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != ""):
                for index in pattern:
                    self.buttons[index].config(bg="light green")
                return True
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")

    def back_to_dashboard(self):
        self.root.destroy()
        subprocess.Popen([sys.executable, "dashboard.py"])
        

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


#Magbitang, Elisha Jhoyce M.

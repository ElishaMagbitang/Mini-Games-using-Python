import tkinter as tk
import random
import subprocess
import sys


class SnakeGame:
    def __init__(self, master):
        self.master = master
        master.title("Snake Game")
        self.width = 600
        self.height = 400
        self.cell_size = 20

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        self.score_label = tk.Label(master, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack()

        self.restart_button = None
        self.back_button = None  # Added for back to dashboard button
        self.game_over_text = None

        self.bind_keys()
        self.running = True
        self.init_game()
        self.move_snake()

    def init_game(self):
        self.snake = [(10, 10)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.allow_direction_change = True

        self.canvas.delete("all")
        self.score_label.config(text="Score: 0")

        # Destroy buttons if they exist
        if self.restart_button:
            self.restart_button.destroy()
            self.restart_button = None
        if self.back_button:
            self.back_button.destroy()
            self.back_button = None
        if self.game_over_text:
            self.canvas.delete(self.game_over_text)
            self.game_over_text = None

        self.snake_objects = []
        for x, y in self.snake:
            self.snake_objects.append(self.create_square(x, y, "green"))
        self.food_object = self.create_square(self.food[0], self.food[1], "red")

    def create_square(self, x, y, color):
        return self.canvas.create_rectangle(
            x * self.cell_size, y * self.cell_size,
            (x + 1) * self.cell_size, (y + 1) * self.cell_size,
            fill=color
        )

    def bind_keys(self):
        self.master.bind("<Up>", lambda event: self.change_direction("Up"))
        self.master.bind("<Down>", lambda event: self.change_direction("Down"))
        self.master.bind("<Left>", lambda event: self.change_direction("Left"))
        self.master.bind("<Right>", lambda event: self.change_direction("Right"))

    def create_food(self):
        while True:
            x = random.randint(0, (self.width // self.cell_size) - 1)
            y = random.randint(0, (self.height // self.cell_size) - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, direction):
        if not self.allow_direction_change:
            return
        if direction == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif direction == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif direction == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif direction == "Right" and self.direction != "Left":
            self.direction = "Right"
        self.allow_direction_change = False

    def move_snake(self):
        if not self.running:
            return

        self.allow_direction_change = True
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)

        if (
            new_head[0] < 0 or new_head[0] >= (self.width // self.cell_size) or
            new_head[1] < 0 or new_head[1] >= (self.height // self.cell_size) or
            new_head in self.snake
        ):
            self.show_game_over()
            return

        self.snake.insert(0, new_head)
        self.snake_objects.insert(0, self.create_square(new_head[0], new_head[1], "green"))

        if new_head == self.food:
            self.score += 10
            self.score_label.config(text="Score: " + str(self.score))
            self.food = self.create_food()
            self.canvas.delete(self.food_object)
            self.food_object = self.create_square(self.food[0], self.food[1], "red")
        else:
            tail = self.snake.pop()
            tail_object = self.snake_objects.pop()
            self.canvas.delete(tail_object)

        self.master.after(100, self.move_snake)

    def show_game_over(self):
        self.running = False
        self.game_over_text = self.canvas.create_text(
            self.width / 2, self.height / 2 - 20,
            text=f"Game Over! Score: {self.score}",
            font=("Helvetica", 20),
            fill="white"
        )

        self.restart_button = tk.Button(
            self.master, text="Restart", font=("Helvetica", 14),
            command=self.restart_game
        )
        self.restart_button.pack(pady=10)

        self.back_button = tk.Button(
            self.master, text="⬅ Back to Dashboard", font=("Helvetica", 14),
            bg="orange",
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=5)

    def restart_game(self):
        self.running = True
        self.init_game()
        self.move_snake()

    def back_to_dashboard(self):
        self.master.destroy()
        subprocess.Popen([sys.executable, "dashboard.py"])


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


#Magbitang, Elisha Jhoyce M.

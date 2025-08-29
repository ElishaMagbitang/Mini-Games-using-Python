import tkinter as tk
from tkinter import messagebox
import subprocess
import sys


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.question_index = 0
        self.score = 0

        self.questions = [
            {"question": "What is the capital of France?",
             "options": ["Berlin", "Madrid", "Paris", "Rome"],
             "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?",
             "options": ["Earth", "Mars", "Jupiter", "Venus"],
             "answer": "Mars"},
            {"question": "What is the largest ocean on Earth?",
             "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
             "answer": "Pacific"}
        ]

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.option_radios = []

        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.check_answer)
            self.option_radios.append(radio)
            radio.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Back to Dashboard Button
        self.back_button = tk.Button(
            root,
            text="⬅ Back to Dashboard",
            font=("Arial", 12),
            width=20,
            bg="orange",
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_radios[i].config(text=option, value=option)

            self.radio_var.set(None)
        else:
            self.show_results()

    def check_answer(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            selected_answer = self.radio_var.get()

            if selected_answer == question_data["answer"]:
                self.score += 1

    def next_question(self):
        self.check_answer()
        self.question_index += 1
        self.show_question()

    def show_results(self):
        messagebox.showinfo("Quiz Results", f"You scored {self.score} out of {len(self.questions)}")
        self.root.destroy()

    def back_to_dashboard(self):
        self.root.destroy()
        subprocess.Popen([sys.executable, "dashboard.py"])


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

#Magbitang, Elisha Jhoyce M.
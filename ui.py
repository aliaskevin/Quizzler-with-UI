from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Ariel"


class QuizInterface:

    def __init__(self, quiz_data: QuizBrain):
        self.quiz = quiz_data
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score:", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="trail",
            font=(FONT, 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_click)
        self.wrong_button.grid(column=1, row=2, pady=20)
        right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right_click)
        self.right_button.grid(column=0, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text="You are reached the limit")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

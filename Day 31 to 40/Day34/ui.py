from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, pady=20)
        self.score.grid(row=0, column=1, sticky=E)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.display_question = self.canvas.create_text(150, 120)
        self.canvas.itemconfig(self.display_question,
                               width=280,
                               text="placeholder",
                               font=("Aerial", 20, "italic"),
                               fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file=".static/images/true.png")
        self.false_image = PhotoImage(file=".static/images/false.png")
        self.true_button = Button(image=self.true_image,
                                  width=100,
                                  height=97,
                                  highlightthickness=0,
                                  command=self.true_pressed)
        self.false_button = Button(image=self.false_image,
                                   width=100,
                                   height=97,
                                   highlightthickness=0,
                                   command=self.false_pressed)
        self.true_button.grid(row=2, column=0, pady=50)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.display_question, text=q_text)
        else:
            self.canvas.itemconfig(self.display_question, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

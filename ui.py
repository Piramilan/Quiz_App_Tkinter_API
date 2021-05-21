THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Milan Quiz App")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.label_1 = Label(text="Score : 0",fg="white",bg=THEME_COLOR)
        self.label_1.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",15,"italic")
        )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_btn.grid(column=0,row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image, highlightthickness=0,command=self.wrong_pressed)
        self.wrong_btn.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_1.config(text=f"score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've Reached The End of The Questions")
            self.true_btn.config(state="disable")
            self.wrong_btn.config(state="disable")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
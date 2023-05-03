import time
from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        img_true = PhotoImage(file='images/true.png')
        img_false = PhotoImage(file='images/false.png')

        self.l_score = Label(text=f'Score: {self.quiz_brain}', bg=THEME_COLOR, fg='white', font=('Arial', 10, 'bold'))
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.c_question_text = self.canvas.create_text(150, 125, text='', width=250,
                                                       fill=THEME_COLOR, font=('Arial', 15, 'italic'))
        self.b_true = Button(image=img_true, highlightthickness=0, borderwidth=0,
                             command=self.select_true)
        self.b_false = Button(image=img_false, highlightthickness=0, borderwidth=0,
                              command=self.select_false)

        self.get_next_question()
        self.window.after(10, self.main_loop)
        self.window.mainloop()

    def main_loop(self):
        print('M_loop')

        # Update widgets
        self.l_score.config(text=f'Score: {self.quiz_brain.score}')
        self.canvas.config(bg='white')

        # Grid
        self.l_score.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.b_false.grid(column=0, row=2, padx=20, pady=20)
        self.b_true.grid(column=1, row=2, padx=20, pady=20)

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(
                self.c_question_text,
                text=self.quiz_brain.next_question()
            )
        else:
            self.canvas.itemconfig(
                self.c_question_text,
                text='Finished\nSee you next time!'
            )
            self.b_true.config(command=NONE)
            self.b_false.config(command=NONE)

    def flash_screen(self, is_correct: bool):

        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.update()
        self.window.after(1000, self.get_next_question())

    def select_true(self):
        self.flash_screen(self.quiz_brain.check_answer('True'))
        self.main_loop()

    def select_false(self):

        self.flash_screen(self.quiz_brain.check_answer('False'))
        self.main_loop()

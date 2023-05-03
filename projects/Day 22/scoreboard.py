from turtle import Turtle
from pong_constants import *

class Scoreboard:

    def __init__(self):

        self.p1_score = 0
        self.p2_score = 0
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.pencolor('white')
        self.writer.goto(0,250)

    def write_score(self):
        self.writer.pendown()
        self.writer.write(f'{self.p1_score} {self.p2_score}', align='center', font=('courier', FONT_SIZE, 'normal') )

    def refresh(self):
        self.writer.clear()
        self.write_score()

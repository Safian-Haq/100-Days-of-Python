from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.color('blue')
        self.goto(randint(-280, 280), randint(-280, 280))
        self.showturtle()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))
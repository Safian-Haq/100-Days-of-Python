import math
from turtle import Turtle
from pong_constants import *
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.x_move = 1
        self.y_move = 2
        self.setposition(x=0, y=100)

    def move(self):

        new_x = self.xcor()
        new_y = self.ycor()

        if self.ycor() > HORIZONTAL_BORDER:
            self.y_move *= -1
        elif self.ycor() < -HORIZONTAL_BORDER:
            self.y_move *= -1

        self.goto(new_x + self.x_move, new_y + self.y_move)

    def center_ball(self):

        self.goto(0, randint(-200, 200))
        self.x_move = 1
        self.y_move = 1

    def bounce_on_paddle(self):

        self.x_move = (abs(self.x_move) + 0.2) * self.x_move/abs(self.x_move)
        self.x_move *= -1
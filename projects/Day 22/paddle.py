from turtle import Turtle
from pong_constants import *

class Paddle(Turtle):

    def __init__(self, player_number: int):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=4.0, stretch_len=1.0)
        self.color('white')
        self.penup()
        if player_number == 1:
            self.goto(-SCREEN_W/2 + (SCREEN_W * 0.05), 0)
        elif player_number == 2:
            self.goto(SCREEN_W/2 - (SCREEN_W * 0.05),0)
        else:
            raise ValueError ('player number can either be 1 or 2')

    def move_up(self):

        self.goto(self.xcor(),self.ycor() + PADDLE_MOVEMENT)

    def move_down(self):

        self.goto(self.xcor(), self.ycor() - PADDLE_MOVEMENT)

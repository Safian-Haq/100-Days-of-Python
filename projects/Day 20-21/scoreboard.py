from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'courier'
FONT_SIZE = 20

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.write(f'Score = {self.score}', False, ALIGNMENT, (FONT, FONT_SIZE, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score = {self.score}', False, ALIGNMENT, (FONT, FONT_SIZE, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over!', False, ALIGNMENT, (FONT, FONT_SIZE, 'normal'))

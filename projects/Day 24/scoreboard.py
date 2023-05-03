import os
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        if 'save_game.txt' in os.listdir():
            # Get score from file
            with open('save_game.txt', 'r') as fp:
                line = fp.readline()
                print(line)
                self.high_score = int(line)
        else:
            self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('save_game.txt', 'w+') as fp:
                fp.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
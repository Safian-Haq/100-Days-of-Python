from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.level = 1
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.goto(-200,260)

    def write_level(self):
        self.writer.clear()
        self.writer.write(f'Level : {self.level}', align='center', font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        temp = Turtle(visible=False)
        temp.write(f'Game Over!', align='center', font=FONT)


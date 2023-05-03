from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        # Initialize player
        self.draw_player()


    def draw_player(self):
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.showturtle()

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def is_level_done(self):
        if self.ycor() > FINISH_LINE_Y:
            self.back_to_start()
            return True
        return False

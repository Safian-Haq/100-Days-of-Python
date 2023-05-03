import time
from turtle import Turtle, Screen

MOVE_DISTANCE = 20

class Snake:

    def _seg_style(self, seg : Turtle):
        seg.color('white')
        seg.shape('square')
        seg.penup()
        seg.speed('fastest')

    def __init__(self, init_len_snake: int, screen: Screen):
        """Creates a snake with the specified length"""
        self.screen = screen
        self.turtles = []
        for i in range(init_len_snake):
            c_turtle = Turtle(visible=False)
            self._seg_style(c_turtle)
            c_turtle.goto(-MOVE_DISTANCE * i, 0)
            c_turtle.showturtle()
            self.turtles.append(c_turtle)

        self.screen.tracer(0)
        self.head = self.turtles[0]
        self.head_last_pos = (0,0)

    def move_forward(self):
        """Moves the snake forward"""

        # Move the head
        self.head_last_pos = self.head.pos()
        self.head.forward(MOVE_DISTANCE)

        # Snap segments to the head
        self.snap_segments()


    def turn_right(self):
        """Turns the snake right"""

        # Move the head
        self.head_last_pos = self.head.pos()
        self.head.right(90)
        self.head.forward(MOVE_DISTANCE)
        self.snap_segments()


    def turn_left(self):
        """Turns the snake right"""

        # Move the head
        self.head_last_pos = self.head.pos()
        self.head.left(90)
        self.head.forward(MOVE_DISTANCE)
        self.snap_segments()

    def snap_segments(self):

        last_pos = self.head_last_pos
        for i in range(1, len(self.turtles)):
            c_turtle = self.turtles[i]
            temp_pos = c_turtle.pos()
            c_turtle.goto(last_pos[0], last_pos[1])
            last_pos = temp_pos

    def move_up(self):

        if self.head.heading() == 0:
            self.turn_left()
        elif self.head.heading() == 180:
            self.turn_right()

    def move_down(self):

        if self.head.heading() == 0:
            self.turn_right()
        elif self.head.heading() == 180:
            self.turn_left()

    def move_left(self):

        if self.head.heading() == 90:
            self.turn_left()
        elif self.head.heading() == 270:
            self.turn_right()

    def move_right(self):

        if self.head.heading() == 90:
            self.turn_right()
        elif self.head.heading() == 270:
            self.turn_left()

    def extend(self):

        # Add a new segment
        new_turtle = Turtle()
        self._seg_style(new_turtle)
        last = self.turtles[len(self.turtles)-1]
        new_turtle.goto(last.xcor() - MOVE_DISTANCE, last.ycor() - MOVE_DISTANCE)
        new_turtle.showturtle()
        self.turtles.append(new_turtle)

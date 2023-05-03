import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from pong_constants import *
from ball import Ball

screen = Screen()
s_board = Scoreboard()

screen.setup(SCREEN_W, SCREEN_H)
screen.bgcolor('black')

# Dotted line in the middle
line_turtle = Turtle(visible=False)
line_turtle.pencolor('white')
line_turtle.penup()
line_turtle.goto(0, SCREEN_H / 2)
line_turtle.right(90)
screen.tracer(0)
dash = True
for i in range(int(SCREEN_H / 2), -int(SCREEN_H / 2), -10):
    if dash:
        line_turtle.pendown()
        line_turtle.forward(10)
        dash = False
    else:
        line_turtle.penup()
        line_turtle.forward(10)
        dash = True

s_board.write_score()
p1_paddle = Paddle(1)
p2_paddle = Paddle(2)
ball = Ball()

screen.update()

is_game = True
screen.listen()

# Player 1 Keys
screen.onkey(p1_paddle.move_up, 'w')
screen.onkey(p1_paddle.move_down, 's')

# Player 2 Keys
screen.onkey(p2_paddle.move_up, 'u')
screen.onkey(p2_paddle.move_down, 'j')

while is_game:
    ball.move()

    # Paddle collision
    if p1_paddle.distance(ball) < 50 and ball.xcor() < -390:
        ball.bounce_on_paddle()

    elif p2_paddle.distance(ball) < 50 and ball.xcor() > 390:
        ball.bounce_on_paddle()

    # Vertical wall collision
    if ball.xcor() > 450:
        s_board.p1_score += 1
        s_board.refresh()
        ball.center_ball()

    elif ball.xcor() < -450:
        s_board.p2_score += 1
        s_board.refresh()
        ball.center_ball()

    screen.update()
    time.sleep(0.01)

screen.exitonclick()

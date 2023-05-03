import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')

simon = Snake(3, screen)

is_game = True

screen.listen()
screen.onkey(simon.move_up, 'w')
screen.onkey(simon.move_down, 's')
screen.onkey(simon.move_left, 'a')
screen.onkey(simon.move_right, 'd')

food = Food()
s_board = Scoreboard()

while is_game:


    simon.move_forward()


    # Detect food collision
    if simon.head.distance(food) < 15:
        food.refresh()
        s_board.increase_score()
        simon.extend()

    # Detect wall collision
    if simon.head.xcor() > 280 or simon.head.xcor() < -280 or simon.head.ycor() > 280 or simon.head.ycor() < -280:
        is_game = False
        s_board.game_over()

    # Detect tail collision
    for segment in simon.turtles[1:]:
        if simon.head.distance(segment) < 10:
            is_game = False
            s_board.game_over()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
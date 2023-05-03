import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()

screen.listen()
screen.onkeypress(tim.move, 'space')

s_board = Scoreboard()
c_manager = CarManager(screen)

game_is_on = True
while game_is_on:

    s_board.write_level()
    c_manager.move_cars()

    # Reached the finish line
    if tim.is_level_done():
        s_board.level_up()
        tim.back_to_start()
        c_manager.speed_up()

    # Collision logic
    if c_manager.is_colliding(tim):
        game_is_on = False

    time.sleep(0.05)
    screen.update()

s_board.game_over()

screen.exitonclick()

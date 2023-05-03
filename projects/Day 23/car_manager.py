import random
from turtle import Turtle, Screen
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


def _reset_car(car: Turtle):
    car.color(random.choice(COLORS))
    car.goto(random.randint(310, 2000), random.randint(-250, 250))


class CarManager:

    def __init__(self, screen: Screen):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.gen_cars(50)
        self.screen = screen

    def move_cars(self):
        for car in self.cars:

            # Reuse existing cars that are out of bounds
            if car.xcor() < -300:
                _reset_car(car)

            # Simply move the car
            car.goto(car.xcor() - self.speed, car.ycor())

    def gen_cars(self, num_of_cars: int):
        """Generates cars depending on self.car_gen_timer"""
        for i in range(num_of_cars):
            c_turtle = Turtle(visible=False)
            c_turtle.shape('square')
            c_turtle.shapesize(stretch_len=2)
            c_turtle.penup()
            _reset_car(c_turtle)
            c_turtle.showturtle()
            self.cars.append(c_turtle)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def is_colliding(self, obj: Turtle):
        for car in self.cars:
            if obj.distance(car) < 20:
                return True

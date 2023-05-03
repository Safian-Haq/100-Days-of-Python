import random
import turtle
from turtle import Turtle, Screen
import colorgram

if __name__ == '__main__':

    ext_colors = colorgram.extract('hirst.jpg', 20)
    colours = []
    for colour in ext_colors:
        colours.append((colour.rgb.r, colour.rgb.g, colour.rgb.b))
    print(colours)

    DOT_SIZE = 20
    SPACE_FACTOR = 2.5

    screen = Screen()
    tim = Turtle()
    tim.hideturtle()
    turtle.colormode(255)
    tim.penup()
    tim.left(180)
    tim.forward(DOT_SIZE*SPACE_FACTOR*5)
    tim.left(90)
    tim.forward(DOT_SIZE*SPACE_FACTOR*5)
    tim.left(90)
    tim.speed(('fastest'))

    for i in range(10):
        for j in range(10):
            tim.dot(DOT_SIZE, random.choice(colours))
            tim.forward(int(DOT_SIZE * SPACE_FACTOR))
        tim.left(90)
        tim.forward(int(DOT_SIZE * SPACE_FACTOR))
        tim.left(90)
        tim.forward(DOT_SIZE*SPACE_FACTOR*10)
        tim.left(180)






    screen.exitonclick()

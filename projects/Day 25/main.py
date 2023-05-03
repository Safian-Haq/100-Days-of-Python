import csv
from turtle import Turtle, Screen
import pandas as pd

df = pd.read_csv('50_states.csv')

screen = Screen()
screen.tracer(0)
screen.setup(width=726,height=492)
screen.bgpic('blank_states_img.gif')

score = 0
correct_answer = []

writer = Turtle(visible=False)
writer.penup()

is_game = True
while is_game:

    user_input = screen.textinput(
        f'{score}/50 States Correct',
        "What's another state name?"
    ).title()

    if user_input in df.state.values:

        if user_input in correct_answer:
            continue
        else:
            correct_answer.append(user_input)
            score += 1

        d_row = df[df.state == user_input]
        writer.goto(int(d_row.x), int(d_row.y))
        writer.pendown()
        writer.write(d_row.state.iloc[0])
        writer.penup()
    elif user_input == 'Exit':
        is_game = False
        with open('missed_states.csv', 'w+') as fp:
            for val in df.state.values:
                if val not in correct_answer:
                    fp.write(f'{val}\n')

    screen.update()

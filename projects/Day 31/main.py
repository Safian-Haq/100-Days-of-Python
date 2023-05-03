import random
import time
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


def load_data():
    # Load card data
    with open('data/french_words.csv') as fp:
        card_data = pd.read_csv(fp, index_col=0)
    return card_data


def game_loop():
    global is_front
    global c_french

    print(card_data.describe())

    if is_front:

        c_french = random.choice(card_data.index)

        print(f'Card Front | {c_french}')

        render_front()
        is_front = False
        win.after(3000, game_loop)

    else:

        print(f"Card Back | {card_data.at[c_french, 'English']}")
        render_back()


def render_front():

    canvas.delete('all')
    b_wrong.grid_forget()
    b_right.grid_forget()

    # Widgets config
    canvas.create_image(400, 263, image=img_card_front)
    canvas.create_text(400, 160, text='French', fill='black', font=('Arial', 40, 'italic'))
    canvas.create_text(400, 280, text=c_french, fill='black', font=('Arial', 60, 'bold'))

    # Widgets grid
    canvas.grid(column=0, row=0, columnspan=2)


def render_back():

    canvas.delete('all')

    # Widgets config
    canvas.create_image(400, 263, image=img_card_back)
    canvas.create_text(400, 160, text='English', fill='white', font=('Arial', 40, 'italic'))
    canvas.create_text(400, 280, text=card_data.at[c_french, 'English'], fill='white', font=('Arial', 60, 'bold'))

    # Widgets grid
    canvas.grid(column=0, row=0, columnspan=2)
    b_wrong.grid(column=0, row=1)
    b_right.grid(column=1, row=1)


def wrong_func():

    global is_front

    print('Wrong')
    is_front = True
    game_loop()


def right_func():

    global is_front
    global card_data

    print('Right')
    is_front = True
    card_data = card_data.drop(index=c_french)
    game_loop()

# Global variables
card_data = load_data()
is_front = True
c_french = ''

# GUI Setup
#####################

win = Tk()
win.title('Flashy')
win.geometry("900x700")
win.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

img_card_back = PhotoImage(file='images/card_back.png')
img_card_front = PhotoImage(file='images/card_front.png')
img_right_icon = PhotoImage(file='images/right.png')
img_wrong_icon = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
b_wrong = Button(image=img_wrong_icon, command=wrong_func, borderwidth=0, highlightthickness=0)
b_right = Button(image=img_right_icon, command=right_func, borderwidth=0, highlightthickness=0)

win.after(10, game_loop)

win.mainloop()

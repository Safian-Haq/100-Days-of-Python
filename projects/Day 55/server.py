from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    home_content = "<body align=center>" \
                   "<h1>Guess a number between 0 and 9</h1>" \
                   "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif'>" \
                   "</body>"
    return home_content

@app.route('/<int:guessed_number>')
def check_guess(guessed_number):
    if guessed_number == target_number:
        return "<body align=center>" \
               "<h1 style='color: green'>" \
               "You won!</h1>" \
               "<img src='https://media.giphy.com/media/xT3i192KC1mB4Oro6A/giphy.gif'>" \
               "</body>"
    elif guessed_number > target_number:
        return "<body align=center>" \
               "<h1 style='color: teal'>" \
               "Go lower</h1>" \
               "<img src='https://media.giphy.com/media/3ohuPpBlFaKJMcSE0g/giphy.gif'>" \
               "</body>"
    else:
        return "<body align=center>" \
               "<h1 style='color: purple'>" \
               "Go higher</h1>" \
               "<img src='https://media.giphy.com/media/xTeV7L6PMPVrO4JkZi/giphy.gif'>" \
               "</body>"



if __name__ == '__main__':
    target_number = randint(1,9)
    app.run(debug=True)

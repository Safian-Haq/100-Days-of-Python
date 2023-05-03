from flask import Flask
import random

app = Flask(__name__)

# Home route for the webpage
@app.route('/')
def index():
    return '<body align="center">' \
           '<h1 ' \
           'style="text-align:center;color:red">' \
           'Guess a number between 0 and 9' \
           '</h1>' \
           '<p>The level of my flask skills as demonstrated by an animal</p>' \
           '<img src="https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif">' \
           '<body>'


# Different routes using url
@app.route('/bye')
def bye():
    return 'Bye'

# Path variables
@app.route('/username/<name>')
def greet(name):
    return f'Hello {name}'

@app.route('/username/<name>/<int:number>')
def greet_with_number(name, number):
    return f'Hello {name}, your number is {number}.'


if __name__ == '__main__':
    # Debug mode helps with auto-reload and access to debugger
    app.run(debug=True)

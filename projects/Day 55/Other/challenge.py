from flask import Flask

app = Flask(__name__)


def make_emphasis(function):
    def inner_function():
        return f'<em>{function()}</em>'

    return inner_function


def make_underline(function):
    def inner_function():
        return f'<u>{function()}</u>'

    return inner_function


def make_bold(function):
    """A decorator that adds a bold tag to function with html output."""

    def inner_function():
        return f'<b>{function()}</b>'

    return inner_function



@app.route('/')
def home(tag):
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)

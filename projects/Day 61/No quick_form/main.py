from flask import Flask, render_template
from login_form import LoginForm
from flask_bootstrap import Bootstrap
import os

VALID_CREDENTIALS = [('safian_haq@live.com', '12345678')]
SECRET_KEY = os.urandom(32)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    Bootstrap(app)
    return app


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():

        if (login_form.email.data, login_form.password.data) in VALID_CREDENTIALS:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

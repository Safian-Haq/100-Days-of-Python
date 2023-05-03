from flask import Flask, render_template, abort, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from is_safe_url import is_safe_url

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():

    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        # Check if email already exists
        if User.query.filter_by(email=request.form['email']).first() != None:
            flash('A user is already registered with the provided email.')
            return redirect(url_for('login'))
        else:
            password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)

            user = User(
                email = request.form['email'],
                password = password,
                name = request.form['name'],
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('secrets', username=user.name))

        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # Authentication
    if request.method == 'POST':

        # Get User by email
        user = User.query.filter_by(email=request.form['email']).first()

        # Check if email is correct
        if user is None:
            flash("The email does not exist, please try again.")

        # Valid email
        else:
            # Check if password is correct
            if check_password_hash(user.password, request.form['password']):

                # Login user
                login_user(user)

                # IS SAFE URL NOT IMPLEMENTED
                # next = request.args.get('next')
                # # is_safe_url should check if the url is safe for redirects.
                # # See http://flask.pocoo.org/snippets/62/ for an example.
                # if not is_safe_url(url=next, allowed_hosts={??}):
                #     return abort(400)
                # return redirect(next or url_for('home'))

                return redirect(url_for('secrets', username=user.name))

            # If invalid password
            else:
                flash("Incorrect password. Please try again.")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    username = current_user.name
    return render_template("secrets.html", username=username, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static/files',
                               path='cheat_sheet.pdf', as_attachment=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    app.run(debug=True)

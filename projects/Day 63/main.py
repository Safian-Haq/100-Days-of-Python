from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from book_form import BookForm


# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
#     " author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Books(
            title=request.form['name'], author=request.form['author'],
            rating=float(request.form['rating'])
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit_rating():

    # Only 1 if needed but using 2 for clarity
    if request.method == 'GET':
        book = Books.query.get(request.args['id'])
        return render_template('edit.html', book=book)
    elif request.method == 'POST':
        book = Books.query.get(request.args['id'])
        book.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/delete')
def delete_book():
    db.session.delete(Books.query.get(request.args['id']))
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

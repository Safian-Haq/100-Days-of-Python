from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = '8f8bd45db2070a1519211bbaec08caa7'
TMDB_SEARCH_MOVIES_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
TMDB_SEARCH_BY_ID_ENDPOINT = 'https://api.themoviedb.org/3/movie'


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Create table
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


class EditRatingForm(FlaskForm):
    rating = StringField('Your Rating [Out of 10 e.g. 7.5]')
    review = TextAreaField('Your Review', render_kw=dict(rows=5,cols=50))
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


with app.app_context():
    db.create_all()

# Add the first movie to the db
################################################
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()
# ###################################################

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.ranking.desc()).all()
    return render_template("index.html", all_movies=all_movies)

@app.route('/edit_rating', methods=['GET', 'POST'])
def edit_rating():

    form = EditRatingForm()
    # Update DB
    if form.validate_on_submit():
        target_movie = Movie.query.filter_by(title=request.args['movie_title']).first()
        # Only update if a value exists in form field
        if request.form['rating'] != '':
            target_movie.rating = request.form['rating']
        if request.form['review'] != '':
            target_movie.review = request.form['review']
        db.session.commit()
        update_ranks()
        return redirect(url_for('home'))

    movie_title = request.args['movie_title']
    return render_template('edit.html', form=form, movie_title=movie_title)

@app.route('/delete')
def delete_movie():
    print(f'DELETE MOVIE ID: {request.args["movie_id"]}')
    target_movie = Movie.query.get(request.args["movie_id"])
    db.session.delete(target_movie)
    db.session.commit()
    update_ranks()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():

        response = requests.get(TMDB_SEARCH_MOVIES_ENDPOINT,
                                params={'query':request.form['title'], 'api_key': TMDB_API_KEY})
        response.raise_for_status()
        movie_list = []
        for search_result in response.json()['results']:
            movie_list.append({
                'title': search_result['title'],
                'release_date' : search_result['release_date'],
                'id': search_result['id']
            })

        return render_template('select.html', s_movies=movie_list)

    return render_template('add.html', form=form)



@app.route('/add/<target_id>')
def add_movie_db(target_id):

    response = requests.get(f"{TMDB_SEARCH_BY_ID_ENDPOINT}/{target_id}",
                            params={'api_key': TMDB_API_KEY})
    response.raise_for_status()
    response = response.json()
    new_movie = Movie(
        title=response['title'], img_url=f"https://image.tmdb.org/t/p/w500/{response['poster_path']}",
        year=response['release_date'].split('-')[0], description=response['overview']
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit_rating', movie_title=response['title']))

def update_ranks():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    rank = 1
    for movie in movies:
        movie.ranking = rank
        rank += 1
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)

import datetime as dt

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

with app.app_context():
    posts = db.session.query(BlogPost).all()


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new-post", methods=['GET', 'POST'])
def new_post():

    form = CreatePostForm()

    if form.validate_on_submit():
        new_blog = BlogPost(
            title=request.form['title'],
            date=dt.datetime.now().date().strftime("%B %d,%Y"),
            body=request.form['body'],
            author=request.form['author'],
            img_url=request.form['img_url'],
            subtitle=request.form['subtitle']
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form, post_type='new')

@app.route('/edit_post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = CreatePostForm(
        id = post.id,
        title=post.title,
        date=post.date,
        body=post.body,
        author=post.author,
        img_url=post.img_url,
        subtitle=post.subtitle
    )

    if form.validate_on_submit():
        post.title=request.form['title']
        post.date=dt.datetime.now().date().strftime("%B %d,%Y")
        post.body=request.form['body']
        post.author=request.form['author']
        post.img_url=request.form['img_url']
        post.subtitle=request.form['subtitle']
        db.session.commit()
        return redirect(url_for('show_post', index=post.id))

    return render_template('make-post.html', form=form, post_type='edit')


@app.route('/delete_post/<index>')
def delete_post(index):

    db.session.delete(BlogPost.query.get(index))
    db.session.commit()

    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)

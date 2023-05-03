from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookForm():
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    add_book = SubmitField('Add Book')

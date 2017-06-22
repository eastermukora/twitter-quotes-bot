from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class AddQuoteForm(Form):
	quote = TextAreaField(
		'quote',
		validators=[DataRequired()]
	)
	author = StringField(
		'author',
		validators=[DataRequired()]
	)

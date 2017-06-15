from flask import Flask, render_template, redirect, url_for, flash

import models
import forms
import config


app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def add_quote():
	"""Single route in the Flask app. Shows a form that can be used to add quotes and their authors."""
	form = forms.AddQuoteForm()
	if form.validate_on_submit():
		flash("New quote added!")
		models.Quote.create_quote(form.quote.data, form.author.data)
	return render_template('add_quote.html', form=form)

if __name__ == '__main__':
	models.initialize()
	app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)

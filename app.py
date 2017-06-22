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
		render_template('add-quote.html')
	return render_template('add-quote.html', form=form)


@app.route('/quotes')
def view_quotes():
	"""Shows page listing all quotes."""
	try:
		quotes = models.Quote.select()
	except models.DoesNotExist:
		quotes = list()
	return render_template('quotes-list.html', quotes=quotes)


if __name__ == '__main__':
	models.initialize()
	app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)

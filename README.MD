# Quotes Twitter Bot

`twitter_bot.py` is the main file. Using `python twitter_bot.py` starts the twitter bot.

`add_quote.py` is a Flask app that allows you to add quotes to the database. Using `python add_quote.py` will create a single route with a form to submit quotes and their authors.

## Prereqs:

* Peewee
* Tweepy
* Flask
* flask_wtf

## Config File

You will also need to create a `config.py` file with the following constants:

- DATABASE - This is the peewee connection to your database
- CONSUMER_KEY - Consumer key for Twitter app
- CONSUMER_SECRET - Consumer secret for Twitter app
- ACCESS_TOKEN - Access token for Twitter app
- ACCESS_TOKEN_SECRET - Access token secret for Twitter app
- DEBUG - True/False if Flask is to run in Debug mode
- PORT - Port for Flask
- HOST - Host for Flask
- SECRET_KEY - Secret key for Flask

Since this is intended to only run locally for me, there is no authentication for the add_quote.py file. I only start flask when I want to add a quote and then kill the app when finished. If you upload this onto an actual server with the route exposed, you will want to add some authentication to that route.

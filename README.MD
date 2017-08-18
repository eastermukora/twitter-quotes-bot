# Quotes Bot

You can see this bot in action by checking out the [Motivation Quotes Twitter](https://twitter.com/myquotebot) and [Motivation Quotes Facebook Page](https://www.facebook.com/motivationalquotesbot/).

`quote-bot.py` is the main file. Using `python quote-bot.py` starts the twitter bot.

`app.py` is a Flask app that allows you to add quotes to the database. Using `python app.py` will run the app to use a form to submit quotes and their authors.

## Config File

You will also need to create a `config.py` file with the following constants:

- DATABASE - This is the peewee connection to your database
- CONSUMER_KEY - Consumer key for Twitter app
- CONSUMER_SECRET - Consumer secret for Twitter app
- ACCESS_TOKEN - Access token for Twitter app
- ACCESS_TOKEN_SECRET - Access token secret for Twitter app
- FB_ACCESS_TOKEN - Access token for Facebook app to post to your Facebook Page
- DEBUG - True/False if Flask is to run in Debug mode
- PORT - Port for Flask
- HOST - Host for Flask
- SECRET_KEY - Secret key for Flask
- UNSPLASH_ID - ID of Unsplash application
- UNSPLASH_SECRET - Secret key for Unsplash application
- UNSPLASH_CALLBACK - Callback for Unsplash application

Since this is intended to only run locally for me, there is no authentication for the app.py file. I only start flask when I want to add a quote and then kill the app when finished. If you upload this onto an actual server with the route exposed, you will want to add some authentication to that route.

In the very near future, I will probably be shifting this to a VPS. At that point, I will add in extra security to the flask app as well as more functions around adding, editing, and deleting quotes.

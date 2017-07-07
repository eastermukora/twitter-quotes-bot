# App: Quotes Twitter Bot
# Author: Frank Corso
# Date created: 06/14/2017
# Date last modified: 07/07/2017
# Python Version: 3.6.1


import os
import datetime
from time import sleep
import tweepy

import config
import models


auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def get_tweet():
	"""Returns a prepared tweet."""
	quote = models.Quote.random_quote()
	if quote:
		return prepare_tweet(quote.quote, quote.author)
	return None


def prepare_tweet(quote, author):
	"""Prepares the tweet to be sent."""
	tweet = '"{}" ~{}'.format(quote, author)
	tweet = add_hashtags(tweet)
	if len(tweet) > 135:
		tweet = None
	return tweet


def add_hashtags(tweet):
	"""Appends related hashtags if space available."""
	if datetime.datetime.now().weekday() == 0 and len(tweet) < 120:
		tweet += ' #motivationmonday'
	if datetime.datetime.now().weekday() == 2 and len(tweet) < 120:
		tweet += ' #wisdomwednesday'
	if len(tweet) < 130:
		tweet += ' #quote'
	if len(tweet) < 125:
		tweet += ' #motivation'
	return tweet


def bot_loop():
	"""Repeatedly pulls random quote and tweets it"""
	previous_tweets = list()
	tweet = get_tweet()
	print("*** Twitterbot running... ***")
	while True:

		# Creates new tweets and checks that we have not previously tweeted that quote
		while tweet in previous_tweets:
			tweet = get_tweet()

		# Tries to tweet the quote
		if tweet:
			print("*** Sharing tweet... ***")
			print(tweet)
			try:
				api.update_status(status=tweet)
			except tweepy.TweepError:
				continue

		# Adds new tweet to our previous tweets
		previous_tweets.insert(0, tweet)
		if len(previous_tweets) > 5:
			previous_tweets.pop()
		now = datetime.datetime.now().strftime('%I:%M %p')
		print("Last tweet time: " + now)
		sleep(14700) # Tweet every 4 hours and 5 minutes


if __name__ == '__main__':
	clear_screen()
	print("*** Starting database... ***")
	models.initialize()
	print("*** Starting twitterbot... ***")
	bot_loop()

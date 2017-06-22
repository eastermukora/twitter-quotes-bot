# App: Quotes Twitter Bot
# Author: Frank Corso
# Date created: 06/14/2017
# Date last modified: 06/21/2017
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


def prepare_tweet(quote, author):
	"""Prepares the tweet to be sent."""
	tweet = '"{}" ~{}'.format(quote, author)
	tweet = add_hashtags(tweet)
	if len(tweet) > 135:
		tweet = None
	return tweet


def add_hashtags(tweet):
	"""Appends related hashtags if space available."""
	if datetime.datetime.now().weekday == 0 and len(tweet) < 120:
		tweet += ' #motivationmonday'
	if datetime.datetime.now().weekday == 2 and len(tweet) < 120:
		tweet += ' #wisdomwednesday'
	if len(tweet) < 130:
		tweet += ' #quote'
	if len(tweet) < 125:
		tweet += ' #motivation'
	return tweet


def bot_loop():
	"""Repeatedly pulls random quote and tweets it"""
	previous_tweet = None
	tweet = None
	print("*** Twitterbot running... ***")
	while True:
		while previous_tweet == tweet:
			quote = models.Quote.random_quote()
			if quote:
				tweet = prepare_tweet(quote.quote, quote.author)
		if tweet:
			print("*** Sharing tweet... ***")
			print(tweet)
			api.update_status(status=tweet)
		previous_tweet = tweet
		sleep(10800)


if __name__ == '__main__':
	clear_screen()
	print("*** Starting database... ***")
	models.initialize()
	print("*** Starting twitterbot... ***")
	bot_loop()

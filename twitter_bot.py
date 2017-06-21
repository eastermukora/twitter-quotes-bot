# App: Quotes Twitter Bot
# Author: Frank Corso
# Date created: 06/14/2017
# Date last modified: 06/21/2017
# Python Version: 3.6.1


import os
import tweepy
from time import sleep

import config
import models


auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


def prepare_tweet(quote, author):
	"""Prepares the tweet to be sent."""
	tweet = "'{}' ~{}".format(quote, author)
	if len(tweet) > 135:
		tweet = None
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
			api.update_status(tweet)
		previous_tweet = tweet
		sleep(10800)


if __name__ == '__main__':
	clear_screen()
	print("*** Starting database... ***")
	models.initialize()
	print("*** Starting twitterbot... ***")
	bot_loop()

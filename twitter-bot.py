# App: Quotes Bot
# Author: Frank Corso
# Date created: 06/14/2017
# Date last modified: 08/16/2017
# Python Version: 3.6.1


import os
import datetime
import random
from time import sleep
import tweepy
import facebook

import config
import models
import photos


auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
graph = facebook.GraphAPI(config.FB_ACCESS_TOKEN)
pic_file = 'quote-image.jpg'


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
		tweet += ' #mondaymotivation'
	if datetime.datetime.now().weekday() == 2 and len(tweet) < 120:
		tweet += ' #wisdomwednesday'
	if len(tweet) < 130:
		tweet += ' #quote'
	if len(tweet) < 125:
		tweet += ' #motivation'
	return tweet


def add_photographer(tweet, photographer, user):
	"""Appends photographer's name and profile from UnSplash"""
	if len(tweet) + len(photographer) < 135:
		tweet += '<' + photographer + '>'
	if len(tweet) + 25 < 139:
		tweet += 'https://unsplash.com/@{}?utm_source=motivational_quotes_bot&utm_medium=referral&utm_campaign=api-credit'.format(user)
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

		# If tweet has content
		if tweet:
			# Creates random photo
			photo = photos.create_photo(pic_file)

			# If photo is not None, share with photo. If not, share just text
			if photo:
				tweet = add_photographer(tweet, photo["name"], photo["user"])
				try:
					api.update_with_media(filename=pic_file, status=tweet)
				except tweepy.TweepError:
					print("Error from Tweepy: {}".format(tweepy.TweepError.message[0]['code']))
				try:
					graph.put_photo(image=open(pic_file, 'rb'), message=tweet)
				except facebook.GraphAPIError:
					print("Error from Facebook: {}".format(facebook.GraphAPIError.message))
				os.remove(pic_file)
			else:
				try:
					api.update_status(status=tweet)
				except tweepy.TweepError:
					print("Error from Tweepy: {}".format(tweepy.TweepError.message[0]['code']))
				try:
					graph.put_object(parent_object='me', connection_name='feed', message=tweet)
				except facebook.GraphAPIError:
					print("Error from Facebook: {}".format(facebook.GraphAPIError.message))

		# Adds new tweet to our previous tweets
		print("*** Tweet Shared ***")
		print(tweet)
		previous_tweets.insert(0, tweet)
		if len(previous_tweets) > 5:
			previous_tweets.pop()
		now = datetime.datetime.now().strftime('%I:%M %p')
		print("*** Last tweet time: {}***".format(now))

		# Prepares time until next tweet
		hours = random.randint(1, 5)
		minutes = random.randint(1, 59)
		print("*** Sleeping for {} hours and {} minutes ***".format(hours, minutes))
		sleep((minutes + (hours * 60)) * 60)


if __name__ == '__main__':
	clear_screen()
	print("*** Starting database... ***")
	models.initialize()
	print("*** Starting twitterbot... ***")
	bot_loop()

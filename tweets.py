import tweepy
import datetime

import config

auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet(quote, author):
	"""Tweets status message of quote, author, and hashtags"""
	status = prepare_tweet(quote, author)
	if status:
		try:
			api.update_status(status=status)
		except tweepy.TweepError as error:
			print("Error from Tweepy: {}".format(error.reason))


def tweet_photo(quote, author, photo_file, photographer, user):
	"""Tweets photo with status message of quote, author, hashtags, photographer's name, and URL"""
	status = prepare_tweet(quote, author)
	# Check to make sure prepare_tweet did not return None
	if status:
		status = add_photographer(status, photographer, user)
		try:
			api.update_with_media(filename=photo_file, status=status)
		except tweepy.TweepError as error:
			print("Error from Tweepy: {}".format(error.reason))


def prepare_tweet(quote, author):
	"""Prepares the tweet to be sent."""
	status = '"{}" ~{}'.format(quote, author)
	status = add_hashtags(status)
	if len(status) > 270:
		status = None
	return status


def add_hashtags(status):
	"""Appends related hashtags if space available."""
	if datetime.datetime.now().weekday() == 0 and len(status) < 250:
		status += ' #mondaymotivation'
	if datetime.datetime.now().weekday() == 2 and len(status) < 250:
		status += ' #wisdomwednesday'
	if len(status) < 260:
		status += ' #quote'
	if len(status) < 255:
		status += ' #motivation'
	return status


def add_photographer(status, photographer, user):
	"""Appends photographer's name and profile from UnSplash"""
	if len(status) + len(photographer) < 270:
		status += '\n' + 'Photo: ' + photographer + ' '
	if len(status) + 25 < 275:
		status += 'https://unsplash.com/@{}?utm_source=motivational_quotes_bot&utm_medium=referral&utm_campaign=api-credit'.format(user)
	return status

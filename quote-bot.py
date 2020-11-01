# App: Quotes Bot
# Author: Frank Corso
# Date created: 06/14/2017
# Date last modified: 11/01/2020
# Python Version: 3.9.0


import datetime
import random
import os
from time import sleep

import photos
import quotes
import tweets
# import posts


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def bot_loop():
	"""Repeatedly pulls random quote and tweets it"""
	pic_file = 'quote-image.jpg'
	previous_quotes = list()
	print("*** Twitterbot running... ***")
	while True:

		# Creates new tweets and checks that we have not previously tweeted that quote
		quote, author = quotes.get_random_quote()
		while quote in previous_quotes:
			quote, author = quotes.get_random_quote()

		# If tweet has content
		if quote:
			# Creates random photo
			photo = photos.get_photo(quote, author, pic_file)

			# If photo is not None, share with photo. If not, share just text
			if photo:
				tweets.tweet_photo(quote, author, pic_file, photo["name"], photo["user"])
				# posts.share_photo(quote, author, pic_file, photo["name"], photo["user"])
				photos.delete_photo(pic_file)
			else:
				tweets.tweet(quote, author)
				# posts.share(quote, author)

		# Adds new tweet to our previous tweets
		previous_quotes.insert(0, quote)
		print("*** Quote shared: {}***".format(quote))
		if len(previous_quotes) > 5:
			previous_quotes.pop()
		now = datetime.datetime.now().strftime('%I:%M %p')
		print("*** Last tweet time: {}***".format(now))

		# Prepares time until next tweet
		hours = random.randint(3, 5)
		minutes = random.randint(1, 59)
		print("*** Sleeping for {} hours and {} minutes ***".format(hours, minutes))
		sleep((minutes + (hours * 60)) * 60)


if __name__ == '__main__':
	clear_screen()
	print("*** Starting twitterbot... ***")
	bot_loop()

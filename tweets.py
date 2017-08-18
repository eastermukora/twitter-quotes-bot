import tweepy

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet(quote, author):
	"""Tweets status message of quote, author, and hashtags"""
	status = prepare_tweet(quote, author)
	if status:
		try:
			api.update_status(status=status)
		except tweepy.TweepError:
			print("Error from Tweepy: {}".format(tweepy.TweepError.message[0]['code']))


def tweet_photo(quote, author, photo_file, photographer, user):
	"""Tweets photo with status message of quote, author, hashtags, photographer's name, and URL"""
	status = add_photographer(prepare_tweet(quote, author), photographer, user)
	try:
		api.update_with_media(filename=photo_file, status=status)
	except tweepy.TweepError:
		print("Error from Tweepy: {}".format(tweepy.TweepError.message[0]['code']))


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

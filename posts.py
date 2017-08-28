import facebook

import config

graph = facebook.GraphAPI(config.FB_ACCESS_TOKEN)


def share(quote, author):
	"""Shares the quote and author to Facebook Page"""
	post = prepare_post(quote, author)
	try:
		graph.put_object(parent_object='me', connection_name='feed', message=post)
	except facebook.GraphAPIError:
		#print("Error from Facebook: {}".format(facebook.GraphAPIError.message))
		pass


def share_photo(quote, author, photo_file, photographer, user):
	"""Shares a photo with message of quote, author, photographer, and URL to Facebook Page"""
	post = add_photographer(prepare_post(quote, author), photographer, user)
	try:
		graph.put_photo(image=open(photo_file, 'rb'), message=post)
	except facebook.GraphAPIError:
		#print("Error from Facebook: {}".format(facebook.GraphAPIError.message))
		pass


def add_photographer(post, name, user):
	"""Adds photographer's name and URL to post"""
	return post + '\n\n' + 'Photo By: {} (https://unsplash.com/@{}?utm_source=motivational_quotes_bot&utm_medium=referral&utm_campaign=api-credit)'.format(name, user)


def prepare_post(quote, author):
	"""Converts quote and author into template"""
	return '"{}" \n~{}'.format(quote, author)

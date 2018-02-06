from unsplash.api import Api
from unsplash.auth import Auth
import requests

import config

unsplash_auth = Auth(config.UNSPLASH_ID, config.UNSPLASH_SECRET, config.UNSPLASH_CALLBACK, code='')
unsplash_api = Api(unsplash_auth)

def get_random_photo():
	"""Gets a random photo URL from Unsplash"""
	photo = unsplash_api.photo.random(
		orientation='landscape',
		collections='1093525'
	)
	if photo:
		return {'url': photo[0].urls.regular, 'name': photo[0].user.name, 'user': photo[0].user.username}
	return None


def create_photo(filename):
	"""Creates a photo by downloading it from Unsplash URL"""
	photo = get_random_photo()
	if photo:
		f = open(filename, 'wb')
		f.write(
			requests.get(
				photo["url"]
			).content
		)
		f.close()
		return photo
	return None

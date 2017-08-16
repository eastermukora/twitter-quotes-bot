from unsplash_python.unsplash import Unsplash
import requests

import config


unsplash = Unsplash({
	'application_id': config.UNSPLASH_ID,
	'secret': config.UNSPLASH_SECRET,
	'callback_url': config.UNSPLASH_CALLBACK
})


def get_random_photo():
	"""Gets a random photo URL from Unsplash"""
	photo = unsplash.photos().get_random_photo(
		orientation='landscape',
		collections='1093525'
	)
	if photo:
		return {'url': photo[0]["urls"]["regular"], 'name': photo[0]["user"]["name"], 'user': photo[0]["user"]["username"]}
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

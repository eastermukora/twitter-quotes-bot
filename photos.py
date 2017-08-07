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
		orientation='landscape'
	)
	if photo:
		return photo[0]["urls"]["full"]
	return None


def create_photo(filename):
	"""Creates a photo by downloading it from Unsplash URL"""
	photo_url = get_random_photo()
	if photo_url:
		f = open(filename, 'wb')
		f.write(
			requests.get(
				photo_url
			).content
		)
		f.close()
		return filename
	return None

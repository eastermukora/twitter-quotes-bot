from unsplash.api import Api
from unsplash.auth import Auth
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import requests
import os

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


def create_photo(quote, filename):
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
		add_quote_to_photo(quote.quote, quote.author, filename)
		return photo
	return None

def delete_photo(filename):
	"""Deletes the photo"""
	os.remove(filename)

def add_quote_to_photo(quote, author, filename):
	"""Adds the quote to the photo"""

	# Opens image and makes it darker
	im = Image.open(filename)
	im = ImageEnhance.Brightness(im)
	im = im.enhance(0.30)

	# Add new lines to quote if too long for image
	new_quote = ''
	quote_line = ''
	for word in quote.split():
		test_line = quote_line
		test_line += word + ' '
		if len(test_line) > 30:
			new_quote += quote_line + '\n'
			quote_line = ''
		quote_line += word + ' '
	new_quote += quote_line

	# Draws quote and author on image
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("font/BreeSerif-Regular.ttf", 70)
	draw.multiline_text((30, im.size[1]/5), '{}\n~{}'.format(new_quote, author), font=font, spacing=10)
	im.save(filename, 'JPEG')

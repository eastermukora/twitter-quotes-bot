from peewee import *

import config


class Quote(Model):
	"""The model for our quotes table. Includes columns for quote and author."""
	quote = TextField(unique=True)
	author = TextField()

	@classmethod
	def create_quote(cls, quote, author):
		try:
			with config.DATABASE.transaction():
				cls.create(
					quote=quote,
					author=author
				)
		except IntegrityError:
			pass

	@staticmethod
	def random_quote():
		"""Returns a random quote from database"""
		try:
			return Quote.select().order_by(fn.Random()).get()
		except DoesNotExist:
			return None

	class Meta:
		database = config.DATABASE

def initialize():
	"""Creates the tables in not already created"""
	config.DATABASE.connect()
	config.DATABASE.create_tables([Quote], safe=True)
	config.DATABASE.close()

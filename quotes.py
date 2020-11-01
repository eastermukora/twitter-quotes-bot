import csv
import random


def load_quotes():
    """Loads all quotes from the CSV."""
    quotes = []
    with open('quotes.csv', newline='') as quotes_file:
        csv_reader = csv.reader(quotes_file)
        for row in csv_reader:
            if len(row) != 0:
                quotes.append({'quote': row[0], 'author': row[1]})
    return quotes


def get_random_quote():
    """Returns a random quote."""
    quotes = load_quotes()
    value = random.choice(quotes)
    return value['quote'], value['author']


def add_quote(quote, author):
    """Adds a quote to the CSV."""
    with open('quotes.csv', mode="a") as quotes_file:
        csv_writer = csv.writer(quotes_file)
        csv_writer.writerow([quote, author])

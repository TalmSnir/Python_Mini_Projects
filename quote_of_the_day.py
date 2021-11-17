
import csv
from bs4 import BeautifulSoup
import requests
from random import choice


URL = 'https://quotes.toscrape.com'


def check_if_first_run():
    with open('quotes_database.csv', 'r', encoding='utf-8-sig') as quotes_database:
        quotes_reader = csv.reader(quotes_database)
        if len(list(quotes_reader)) == 0:
            return True
        return False


def scrape_pages(quotes_writer):
    page_url = '/page/1'
    while page_url:
        data = requests.get(URL+page_url)
        parsed_data = BeautifulSoup(data.text, 'html.parser')

        quotes_data_unclean = parsed_data.find_all('div', class_='quote')
        for quote_data in quotes_data_unclean:
            quote_text = quote_data.find(class_='text').getText()
            quote_author = quote_data.find(
                class_='author').getText()
            quotes_writer.writerow(
                [quote_author, quote_text])
        next_page_btn = parsed_data.find('li', class_='next')
        page_url = next_page_btn.find('a')['href'] if next_page_btn else None


def build_quotes_database():
    if check_if_first_run():
        with open('quotes_database.csv', 'a', newline='', encoding='utf-8-sig') as quotes_database:
            quotes_writer = csv.writer(
                quotes_database)
            quotes_writer.writerow(['author', 'quote'])
            scrape_pages(quotes_writer)


def get_quote():
    build_quotes_database()
    quotes_database = open('quotes_database.csv', 'r', encoding='utf-8-sig')
    quotes_and_authors = csv.reader(quotes_database)

    last_used_quotes = open('last_used_quotes.csv', 'r+',
                            newline='', encoding='utf-8-sig')
    past_quotes = list(csv.reader(last_used_quotes))
    while True:

        chosen_quote = choice(list(quotes_and_authors))
        print(chosen_quote)
        print(past_quotes)
        if chosen_quote not in past_quotes:
            past_quotes = csv.writer(last_used_quotes)
            past_quotes.writerow(chosen_quote)
            break

    quotes_database.close()
    last_used_quotes.close()

    return chosen_quote


get_quote()

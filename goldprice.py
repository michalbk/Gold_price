import requests
import bs4
import datetime
import csv
import os

WORKING_DIR = '.'
FILENAME = 'gold_price.csv'
DATE_FORMAT = '%d.%m.%Y %H:%M UTC'
URL = 'https://markets.businessinsider.com/commodities/gold-price'


def get_price():
    webpage = requests.get(URL)
    parser = bs4.BeautifulSoup(webpage.text, 'html.parser')
    gold_tag = parser.find_all('span', class_='price-section__current-value')[0]
    gold_price = gold_tag.get_text()
    return gold_price


def get_datetime():
    return datetime.datetime.utcnow().strftime(DATE_FORMAT)


def write_to_csv(price, time):
    filepath = WORKING_DIR + os.sep + FILENAME
    row = [price] + [time]

    if not os.path.exists(filepath):
        header = ['Price'] + ['Time']
        with open(filepath, 'w', newline='') as f:
            fr = csv.writer(f)
            fr.writerow(header)
            fr.writerow(row)
    else:
        with open(filepath, 'a', newline='') as f:
            fr = csv.writer(f)
            fr.writerow(row)


def main():
    write_to_csv(get_price(), get_datetime())


main()

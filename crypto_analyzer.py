from bs4 import BeautifulSoup
from enum import Enum
import requests

COIN_MARKET_CAP_URL = 'https://coinmarketcap.com/currencies/'

HIGH_LOW_VALUE_SEARCH_QUERY = '52 Week Low / 52 Week High'


class Fetch(Enum):
    ALL = 0
    ONE = 1

class CryptoAnalyzer(BeautifulSoup):
    def __init__(self, coin_name):
        response = requests.get(f'{COIN_MARKET_CAP_URL}{coin_name}/')
        raw_html = response.text
        super().__init__(raw_html, 'html.parser')

    def __find_with_class__(self, class_name, fetch_type=Fetch.ALL, element='div'):
        if fetch_type == Fetch.ALL:
            return self.find_all(element, attrs={'class': class_name})
        return self.find(element, attrs={'class': class_name})

    def get_current_price(self):
        return self.__find_with_class__('priceValue', Fetch.ONE).text

    def get_market_cap(self):
        return self.__find_with_class__('statsValue')[0].text

    def get_highest_and_lowest_values(self):
        result = self.find('th', attrs={'scope': 'row'}, string=HIGH_LOW_VALUE_SEARCH_QUERY)
        result_children = result.parent.children
        [lowest_value_div, highest_value_div] = list(result_children)[1].find_all('div')
        return highest_value_div.text, lowest_value_div.text.strip(' /')

    def get_website_link(self):
        result = self.__find_with_class__('content', Fetch.ONE, 'ul')
        return list(result.children)[0].find("a").attrs.get("href")

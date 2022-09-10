from bs4 import BeautifulSoup
import requests
from enum import Enum


class Fetch(Enum):
    ALL = 0
    ONE = 1


class BaseAnalyzer(BeautifulSoup):
    def __init__(self, url):
        response = requests.get(url)
        raw_html = response.text
        super().__init__(raw_html, 'html.parser')

    def __find_with_class__(self, class_name, fetch_type=Fetch.ALL, element='div'):
        if fetch_type == Fetch.ALL:
            return self.find_all(element, attrs={'class': class_name})
        return self.find(element, attrs={'class': class_name})

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class CommunityAnalyzer:

    def find_twitter(self, link):
        name = link.split('/')
        name = '/' + name[len(name) - 1] + '/followers'
        driver = webdriver.Firefox(executable_path='C:\Program Files (x86)\selenium drivers\geckodriver.exe')
        driver.implicitly_wait(2)
        driver.get(link)
        number_of_followers = driver.find_element(By.XPATH, '//a[contains(@href,"followers")]').text
        number_of_followers = number_of_followers.split(' ')[0].replace(',', '')
        multiplier = number_of_followers[len(number_of_followers) - 1]  # k, m
        if multiplier in ('K', 'M'):
            number_of_followers = number_of_followers.replace(multiplier, '')
            multiplier = 1000 if multiplier == 'K' else 1000000
        else:
            multiplier = 1
        if '.' in number_of_followers:
            parts = number_of_followers.split('.')
            number_of_followers = multiplier * int(parts[0])
            if multiplier > 1:
                number_of_followers += multiplier // 10 * int(parts[1])
        else:
            number_of_followers = multiplier * int(number_of_followers)
        print('Number of twitter followers:', number_of_followers)
        driver.close()

    def find_discord(self, link):
        response = requests.get(link)
        raw_html = response.text
        soup = BeautifulSoup(raw_html, 'html.parser')
        number_of_users = soup.find_all('meta')[2].attrs['content'].split(' ')
        number_of_users = number_of_users[
            len(number_of_users) - len('other members and enjoy free voice and text chat.'.split(' ')) - 1]
        number_of_users = int(number_of_users.replace(',', ''))
        print('Number of discord followers:', number_of_users)

    def find_reddit(self, link):
        print(link)

    def find_telegram(self, link):
        response = requests.get(link)
        raw_html = response.text
        soup = BeautifulSoup(raw_html, 'html.parser')
        number_of_users = soup.find('div', attrs={'class': 'tgme_page_extra'}).text.split(' ')
        number_of_users = number_of_users[0] + number_of_users[1]
        print('Number of telegram followers:', number_of_users)

    def find_youtube(self, link):
        print(link)

    socials = {'twitter': find_twitter, 'discord': find_discord, 'reddit': find_reddit,
               'telegram': find_telegram, 't.me': find_telegram, 'youtube': find_youtube}

    def __init__(self, links: dict):
        for key in self.socials.keys():
            if key in links:
                self.socials[key](self, link=links[key])

from bs4 import BeautifulSoup
import requests

response = requests.get('https://coinmarketcap.com/currencies/shiba-inu/')
html_page = response.text
soup = BeautifulSoup(html_page, 'html.parser')
results = soup.find_all("div", attrs={'class': 'statsValue'})
print(f'Market Cap: {results[0].text}')
result = soup.find('th', attrs={'scope': 'row'}, string='52 Week Low / 52 Week High')
childs = result.parent.children
high_low = list(childs)[1].find_all('div')
high = high_low[1].text
low = high_low[0].text
print(f"Highest Value In Last Year: {high}")
print(f"Lowest Value In Last Year: {low.strip('/')}")
result = soup.find('ul', attrs={'class':'content'})
print(f'Website Link: {list(result.children)[0].find("a").attrs.get("href")}')
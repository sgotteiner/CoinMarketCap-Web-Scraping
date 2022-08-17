from bs4 import BeautifulSoup
import requests

def string_to_int(value: str) -> float:
    return float(value[1:].replace(',', ''))

# this function returns a grade between 0-100 how good this coin for long term investment
# it checks the coins stats from CoinMarketCap and the coins website
def get_coin_grade(coin: str) -> int:
    response = requests.get('https://coinmarketcap.com/currencies/' + coin + '/')
    html_page = response.text
    soup = BeautifulSoup(html_page, 'html.parser')
    results = soup.find_all("div", attrs={'class': 'statsValue'})
    current_price = soup.find('div', attrs={'class': 'priceValue'}).text
    print(f'Current Price: {current_price}')
    market_cap = results[0].text
    print(f'Market Cap: {market_cap}')
    result = soup.find('th', attrs={'scope': 'row'}, string='52 Week Low / 52 Week High')
    childs = result.parent.children
    high_low = list(childs)[1].find_all('div')
    highest_price = high_low[1].text
    lowest_price = high_low[0].text
    print(f"Highest Value In Last Year: {highest_price}")
    print(f"Lowest Value In Last Year: {lowest_price.strip('/')}")
    result = soup.find('ul', attrs={'class': 'content'})
    website_link = list(result.children)[0].find("a").attrs.get("href")
    print(f'Website Link: {website_link}')
    response = requests.get(website_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    footer = soup.find('footer')
    if not footer:
        footer = soup.find('div', attrs={'class': 'footer'})
    print('footer exists: ' + str(footer is not None))
    grade = 0
    market_cap = string_to_int(market_cap)
    current_price = string_to_int(current_price)
    highest_price = string_to_int(highest_price)
    if 500000000 > market_cap > 50000000:
        grade += 50
    if highest_price / current_price > 5:
        grade += 50
    return grade


if __name__ == '__main__':
    print(get_coin_grade('render-token'))

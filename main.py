from bs4 import BeautifulSoup
import requests

def string_to_int(value: str) -> float:
    return float(value[1:].replace(',', ''))

# this function returns a grade between 0-100 how good this coin for long tewm investment
# it checks the coins stats from CoinMarketCap and the coins website
def get_coin_grade(coin: str) -> int:
    response = requests.get('https://coinmarketcap.com/currencies/' + coin + '/')
    html_page = response.text
    soup = BeautifulSoup(html_page, 'html.parser')
    results = soup.find_all("div", attrs={'class': 'statsValue'})
    market_cap = results[0].text
    print(f'Market Cap: {market_cap}')
    result = soup.find('th', attrs={'scope': 'row'}, string='52 Week Low / 52 Week High')
    childs = result.parent.children
    high_low = list(childs)[1].find_all('div')
    high = high_low[1].text
    low = high_low[0].text
    print(f"Highest Value In Last Year: {high}")
    print(f"Lowest Value In Last Year: {low.strip('/')}")
    result = soup.find('ul', attrs={'class': 'content'})
    print(f'Website Link: {list(result.children)[0].find("a").attrs.get("href")}')
    grade = 0
    market_cap = string_to_int(market_cap)
    high = string_to_int(high)
    if market_cap < 500000000 and market_cap > 50000000:
        grade += 50
    if high / market_cap > 5:
        grade += 50
    return grade

if __name__ == '__main__':
    print(get_coin_grade('bitcoin'))

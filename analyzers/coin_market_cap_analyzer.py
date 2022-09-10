from base_analyzer import BaseAnalyzer, Fetch

COIN_MARKET_CAP_URL = 'https://coinmarketcap.com/currencies/'

HIGH_LOW_VALUE_SEARCH_QUERY = '52 Week Low / 52 Week High'

EXPLANATIONS_CLASS = 'sc-2qtjgt-0 eApVPN'


class CoinMarketCapAnalyzer(BaseAnalyzer):
    def __init__(self, coin_name):
        super().__init__(f'{COIN_MARKET_CAP_URL}{coin_name}/')

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

    def __find_explanation_topics__(self):
        results = self.__find_with_class__(class_name=EXPLANATIONS_CLASS)
        # usually results[0] is enough but sometimes there is another div before
        results = results[len(results) - 1].contents[0].contents
        # titles are in h[2,3,4...] items and the entire explanation is in p items
        explanation_topics = [r for r in results if 'h' in r.name]
        return explanation_topics

    def has_what_is_the_project(self) -> bool:
        explanation_topics = self.__find_explanation_topics__()
        for topic in explanation_topics:
            if 'what-is' in topic.attrs['id']:
                return True
        return False

    def has_who_are_the_founders(self) -> bool:
        explanation_topics = self.__find_explanation_topics__()
        for topic in explanation_topics:
            if 'who-are' in topic.attrs['id']:
                return True
        return False

    def number_of_explanation_topics(self):
        return len(self.__find_explanation_topics__())

    def like_bitcoin(self):
        chart = self.__find_with_class__(class_name='fullscreen')
        return self.prettify()

    def number_of_cmc_watchers(self):
        results = self.__find_with_class__(class_name='namePill')
        text = results[2].text
        num = text.split(' ')[1].replace(',', '')
        return num


print(CoinMarketCapAnalyzer('basic-attention-token').get_market_cap())

# TODO check if the coins graph grows similar to bitcoin graph
# TODO implement coin market cap API

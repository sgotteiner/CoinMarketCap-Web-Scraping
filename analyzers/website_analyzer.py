from base_analyzer import BaseAnalyzer, Fetch


class WebsiteAnalyzer(BaseAnalyzer):
    def __init__(self, website_url):
        super().__init__(website_url)
        self.footer = None
        self.tags = None
        self.texts = None
        self.links = None
        self.key_links = {}
        self.__find_footer__()
        self.__find_tags__()

    def __find_footer__(self):
        self.footer = self.find('footer')
        print('Footer exists: ' + str(self.footer is not None))

    def find_FAQ(self):
        print('faq' in self.texts)

    def find_blog(self):
        print('blog' in self.texts)

    def find_is_one_page(self):
        # todo
        pass

    def find_team(self):
        # todo find team
        print('team' in self.texts)

    def __find_community__(self):
        socials = ('twitter', 'discord', 'reddit', 'telegram', 'youtube')
        # self.community_links = [link for link in self.links if any(social in link for social in socials)]
        for social in socials:
            # if there are a couple of links for each social
            # d['social'] = list(dict.fromkeys([link for link in self.links if social in link]))
            # assuming there is one link per social
            self.__find_specific_link__(social)

        print(self.key_links)

    def find_github(self):
        self.__find_specific_link__('github')
        print('github' in self.texts or self.key_links['github'] is not None)

    def __find_specific_link__(self, key):
        for link in self.links:
            if key in link:
                self.key_links[key] = link
                break

    def find_roadmap(self):
        print('roadmap' in self.texts)

    def __find_tags__(self):
        self.tags = self.find_all('a')
        self.texts = [r.contents[0].text.lower() for r in self.tags]
        self.links = [r.attrs['href'] for r in self.tags]
        print(self.texts)
        print(self.links)
        self.__find_community__()

WebsiteAnalyzer('https://kadena.io/').find_github()
# WebsiteAnalyzer('https://www.telos.net/').find_FAQ()
# WebsiteAnalyzer('https://rendertoken.com/').find_FAQ()
# WebsiteAnalyzer('https://runonflux.io/').find_roadmap()

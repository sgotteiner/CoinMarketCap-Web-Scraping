from base_analyzer import BaseAnalyzer, Fetch


class WebsiteAnalyzer(BaseAnalyzer):
    def __init__(self, website_url):
        super().__init__(website_url)

    def find_footer(self):
        results = self.find('footer')
        print('Footer exists: ' + str(results is not None))


WebsiteAnalyzer('https://www.nervos.org/').find_footer()

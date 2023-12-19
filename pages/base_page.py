from abc import abstractmethod


class BasePage:
    def __init__(self, browser, url, open_page=False, check_url=False):
        self.browser = browser
        self.url = url

        if open_page:
            self.open()

        if check_url:
            self.check_url_contains()

    def open(self):
        self.browser.get(self.url)

    def check_url_contains(self):
        assert self.url in self.browser.current_url, f'Part {self.url} not contains in {self.browser.current_url}'

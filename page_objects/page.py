import urlparse

__author__ = 'Ivan'



class Page(object):
    BASE_URL = "http://127.0.0.1:8000/"
    PATH = ""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
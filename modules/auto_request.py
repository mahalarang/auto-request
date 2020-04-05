import requests
from .config import Config


class AutoRequest(Config):
    def __init__(self, method='', url='', data={}, headers={}, loop=0):
        super().__init__()
        if method:
            self.method = method

        if url:
            self.target = url

        if bool(headers):
            self.headers = headers

        if loop:
            self.request_times = loop

        if bool(data):
            self.data = data

    def run(self):
        pass

    def make_request():
        pass

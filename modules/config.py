class Config:
    DEFAULT_REQUEST_LOOP = 1
    DEFAULT_REQUEST_METHOD = 'GET'
    DEFAULT_REQUSET_HEADERS = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.162 Chrome/80.0.3987.162 Safari/537.36'
    }

    def __init__(self):
        self.__request_times = Config.DEFAULT_REQUEST_LOOP
        self.__request_method = Config.DEFAULT_REQUEST_METHOD
        self.__request_headers = Config.DEFAULT_REQUSET_HEADERS
        self.__target = ''
        self.__data = {}

    # HEADER
    @property
    def headers(self):
        pass

    @headers.getter
    def headers(self):
        return self.__request_headers

    @headers.setter
    def headers(self, header):
        self.__request_headers.update(header)

    # METHOD
    @property
    def method(self):
        pass

    @method.getter
    def method(self):
        return self.__request_method

    @method.setter
    def method(self, method):
        self.__request_method = method

    # REQUEST TIMES
    @property
    def request_times(self):
        pass

    @request_times.getter
    def request_times(self):
        return self.__request_times

    @request_times.setter
    def request_times(self, times):
        self.__request_times = times

    # TARGET
    @property
    def target(self):
        pass

    @target.getter
    def target(self):
        return self.__target

    @target.setter
    def target(self, target):
        self.__target = target

    # DATA
    @property
    def data(self):
        pass

    @data.getter
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


if __name__ == '__main__':
    print("This not executable file")

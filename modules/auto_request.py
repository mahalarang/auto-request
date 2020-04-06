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
        if self.target:
            if self.request_times > 0:
                print('')
                for i in range(self.request_times):
                    try:
                        result = self.__make_request(
                            self.method,
                            self.target,
                            self.data,
                            self.headers
                        )
                        self.__make_message(
                            request_order=i+1,
                            target=self.target,
                            status=result.status_code
                        )
                    except ValueError as e:
                        self.__make_message(
                            request_order=i+1,
                            error=e
                        )
                else:
                    print('')
            else:
                raise ValueError('Request Times Must Be Greater than 0')
        else:
            raise ValueError('request Target Was Invalid')

    def __make_request(self, method, url, data, headers):
        if method.upper() == 'GET':
            return requests.get(url=url, headers=headers)
        elif method.upper() == 'POST':
            return requests.post(url=url, data=data, headers=headers)
        else:
            raise ValueError('Unknown Request Method')

    def __make_message(self, request_order, target, status=0, error=''):
        if status == 0:
            print("[{}] [FAIL]\t{}".format(str(request_order), error))
        elif status >= 200 or status < 300:
            print("[{}] [PASS]\t{} => ({})".format(
                str(request_order), target, str(status)))
        elif status >= 300 or status < 400:
            print("[{}] [PASS?]\t{} => ({})".format(
                str(request_order), target, str(status)))
        else:
            print("[{}] [FAIL]\t{} => ({})".format(
                str(request_order), target, str(status)))


if __name__ == '__main__':
    print("This not executable file")

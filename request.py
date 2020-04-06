from modules import getOptions, AutoRequest


def parse_string_to_dict(str, default={}):
    updated_dict = {}
    splitted_str = str.split('&')
    for value in splitted_str:
        item = value.split('=')
        updated_dict[item[0]] = item[1]

    return updated_dict if bool(updated_dict) else default


def main():
    options = getOptions()
    request = AutoRequest(
        method=options.method,
        url=options.url,
        loop=options.repeat,
        data=parse_string_to_dict(options.data, default=None),
        headers=parse_string_to_dict(options.headers, default=None)
    )
    request.run()


if __name__ == '__main__':
    main()

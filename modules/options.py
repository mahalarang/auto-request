import argparse


def getOptions():
    parser = argparse.ArgumentParser(
        prog='python3 request.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('''
This program is intend to easy make request repeatly
so if you want to make much request, you have taken the right one

Before you run this program, make sure you have installed this pakages:
- argparse
- requests

or you can install all of them by running install.py
          '''),
        epilog='Build with love @sulhanjauhari'
    )
    parser.add_argument('-m', '--method', default='GET', help='Request Method')
    parser.add_argument('-u', '--url', required=True,
                        help='Request URL Target')
    parser.add_argument('-d', '--data', help='Request Data')
    parser.add_argument('-hd', '--headers', help='Request Header')
    parser.add_argument(
        '-r', '--repeat', help='How many request have you repeated', type=int)

    return parser.parse_args()

#!/usr/bin/python3
"""
Python script that takes in URL and an email
"""
import urllib.parse
import urllib.request
import sys


def main():
    """
    Python script that takes a URL and an email
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""
Python script that takes a URL and email adress as arguments using
the request package
"""
import requests
import sys


def main():
    """
    Python script that takes URL and email address as arguments
    using the requests package
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print("Response body:")
    print(response.text)


if __name__ == "__main__":
    main()

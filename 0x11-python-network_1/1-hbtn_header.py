#!/usr/bin/python3
"""
Python script that displays the value of the id variable in the
header of the response.
"""
import urllib.request
import sys


def main():
    """
    Python script that fetches an id variable
    """
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)


if __name__ == "__main__":
    main()

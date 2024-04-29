#!/usr/bin/python3
"""
Python script that takes in URL, sends request and displays
the value using the request package
"""
import sys
import requests


def main():
    """
    Python script to fect URL usin the requests package
    """
    req = requests.get(sys.argv[1])
    for key in req.headers:
        if key == 'X-Request-Id':
            val = req.headers['X-Request-Id']
            print(val)
            break


if __name__ == "__main__":
    main()

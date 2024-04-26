#!/usr/bin/python3
"""
Python script that takes URL, sends request to the URL and display
the body of response
"""
import requests
import sys


def main():
    """
    Python script that takes URL, sends request and display 
    body of response
    """
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print("Body response:")
        print(response.text)


if __name__ == "__main__":
    main()

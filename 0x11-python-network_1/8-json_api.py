#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request with
letter as a parameter
"""
import requests
import sys


def main():
    """
    Python script that takes in a letter and sends a POST request
    with letter as parameter
    """
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post(url, data={'q': q})

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
